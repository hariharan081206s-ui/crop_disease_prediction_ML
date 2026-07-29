# ============================================================
# Crop Disease Prediction - MobileNetV2 Transfer Learning
# Run this script in Google Colab
# Developer: Hariharan S
# ============================================================
# After training, download crop_disease_model.keras and
# replace the file in your Crop_Disease_Prediction_Project folder.
# ============================================================

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

print("TensorFlow version:", tf.__version__)

# ── Step 1: Mount Google Drive ───────────────────────────────
from google.colab import drive
drive.mount("/content/drive")

# ── Step 2: Set dataset path ─────────────────────────────────
# CHANGE THIS to the path of your PlantVillage folder in Google Drive.
# It must contain 29 subfolders named after each disease class.
DATASET_DIR = "/content/drive/MyDrive/PlantVillage"   # <-- UPDATE THIS

IMG_SIZE   = 224
BATCH_SIZE = 32
AUTOTUNE   = tf.data.AUTOTUNE

# ── Step 3: Load datasets using the modern API ───────────────
# tf.keras.utils.image_dataset_from_directory replaces the deprecated
# ImageDataGenerator.flow_from_directory approach.

train_ds_raw = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=True,
)

val_ds_raw = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=False,
)

# Capture class names BEFORE prefetch/map transforms the dataset object
class_names_ordered = train_ds_raw.class_names
NUM_CLASSES = len(class_names_ordered)
print(f"\nNum classes detected: {NUM_CLASSES}")
print("Class order:", class_names_ordered)

# ── Step 4: Preprocessing & augmentation pipeline ────────────
# Normalize to [0, 1]
normalization = tf.keras.layers.Rescaling(1.0 / 255)

# Data augmentation (applied only during training)
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),           # ~30 degrees
    tf.keras.layers.RandomTranslation(0.15, 0.15),
    tf.keras.layers.RandomZoom(0.2),
    tf.keras.layers.RandomBrightness(0.2),
], name="augmentation")

def preprocess_train(images, labels):
    images = normalization(images)
    images = data_augmentation(images, training=True)
    return images, labels

def preprocess_val(images, labels):
    images = normalization(images)
    return images, labels

train_ds = (
    train_ds_raw
    .map(preprocess_train, num_parallel_calls=AUTOTUNE)
    .prefetch(AUTOTUNE)
)

val_ds = (
    val_ds_raw
    .map(preprocess_val, num_parallel_calls=AUTOTUNE)
    .prefetch(AUTOTUNE)
)

# ── Step 5: Build MobileNetV2 transfer learning model ────────
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights="imagenet"
)
base_model.trainable = False

inputs  = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
x       = base_model(inputs, training=False)
x       = layers.GlobalAveragePooling2D()(x)
x       = layers.Dense(256, activation="relu")(x)
x       = layers.Dropout(0.4)(x)
outputs = layers.Dense(NUM_CLASSES, activation="softmax")(x)
model   = models.Model(inputs, outputs)
model.summary()

# ── Step 6: Phase 1 – train new head ─────────────────────────
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history1 = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10,
    callbacks=[
        EarlyStopping(monitor="val_accuracy", patience=4, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2, verbose=1),
        ModelCheckpoint("/content/best_phase1.keras", monitor="val_accuracy", save_best_only=True, verbose=1),
    ]
)

# ── Step 7: Phase 2 – fine-tune last 30 layers ───────────────
base_model.trainable = True
for layer in base_model.layers[:-30]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history2 = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=15,
    callbacks=[
        EarlyStopping(monitor="val_accuracy", patience=5, restore_best_weights=True, verbose=1),
        ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2, verbose=1),
        ModelCheckpoint("/content/best_phase2.keras", monitor="val_accuracy", save_best_only=True, verbose=1),
    ]
)

# ── Step 8: Evaluate and save ─────────────────────────────────
val_loss, val_acc = model.evaluate(val_ds)
print(f"\nFinal Validation Accuracy: {val_acc*100:.2f}%")

SAVE_PATH = "/content/crop_disease_model.keras"
model.save(SAVE_PATH)
print(f"Model saved: {SAVE_PATH}")

# ── Step 9: Download model ────────────────────────────────────
from google.colab import files
files.download(SAVE_PATH)
print("Download started! Replace crop_disease_model.keras in your project folder.")

# ── Step 10: Print CLASS_NAMES to copy into app.py ───────────
print("\n=== COPY THIS INTO app.py as CLASS_NAMES ===")
print("CLASS_NAMES = [")
for name in class_names_ordered:
    print(f'    "{name}",')
print("]")
