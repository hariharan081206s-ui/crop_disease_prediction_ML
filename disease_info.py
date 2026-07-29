# =============================================================================
# disease_info.py — Crop Disease Information Module
# Developer: Hariharan S
# =============================================================================

DISEASE_INFO = {
    "Apple - Apple Scab": {
        "description": "Apple Scab is a common fungal disease caused by Venturia inaequalis. It affects the leaves, fruit, and sometimes the twigs of apple trees, causing significant yield losses if left untreated.",
        "symptoms": "Olive-green to brown velvety spots on leaves and fruit. Infected leaves may curl, yellow, and drop prematurely. Fruit shows dark, scabby lesions that crack as the fruit grows.",
        "cause": "Fungus: Venturia inaequalis. Spreads via windborne ascospores released from infected leaf litter during wet spring weather.",
        "organic_treatment": "Apply sulfur or copper-based sprays. Remove and destroy fallen leaves. Use neem oil as a preventive spray every 7-10 days during wet weather.",
        "chemical_treatment": "Apply captan, myclobutanil, or thiophanate-methyl fungicides at 7-10 day intervals starting at green tip growth stage.",
        "prevention": "Plant scab-resistant apple varieties. Prune trees for good air circulation. Rake and destroy fallen leaves in autumn. Avoid overhead irrigation."
    },
    "Apple - Black Rot": {
        "description": "Black Rot is a fungal disease caused by Botryosphaeria obtusa. It attacks the fruit, leaves, and bark of apple trees, causing mummified fruit and cankers.",
        "symptoms": "Circular, brown-purple spots (frog-eye lesions) on leaves. Fruit rot beginning at the blossom end, turning black. Dark, sunken cankers on branches.",
        "cause": "Fungus: Botryosphaeria obtusa. Overwinters in mummified fruit and dead wood, spreading via rain splash.",
        "organic_treatment": "Remove mummified fruit and dead wood. Apply copper-based fungicides. Prune infected branches 8-10 inches below visible infection.",
        "chemical_treatment": "Apply captan or thiophanate-methyl during bloom and petal fall. Repeat every 10-14 days during wet weather.",
        "prevention": "Remove all mummified fruit from trees and ground. Prune dead wood annually. Maintain orchard sanitation."
    },
    "Apple - Cedar Apple Rust": {
        "description": "Cedar Apple Rust is a fungal disease requiring two hosts: apple/crabapple and eastern red cedar (juniper). It causes significant defoliation in susceptible apple varieties.",
        "symptoms": "Bright orange-yellow spots on upper leaf surfaces in spring/early summer. Tube-like structures (aecia) on lower leaf surfaces. Premature defoliation.",
        "cause": "Fungus: Gymnosporangium juniperi-virginianae. Alternates between juniper/cedar and apple trees.",
        "organic_treatment": "Apply sulfur or copper-based fungicides during wet spring weather. Remove nearby cedar/juniper trees if possible.",
        "chemical_treatment": "Apply myclobutanil, trifloxystrobin, or propiconazole fungicides starting at pink stage, continuing for 3-4 sprays at 7-10 day intervals.",
        "prevention": "Plant rust-resistant apple varieties. Remove eastern red cedar trees within 300 meters. Monitor and apply protectant sprays in spring."
    },
    "Apple - Healthy": {
        "description": "The apple leaf is healthy with no signs of disease, pest damage, or nutrient deficiency.",
        "symptoms": "No symptoms. Leaf appears vibrant green with uniform color and intact surface.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment required. Maintain regular organic fertilization and proper irrigation.",
        "chemical_treatment": "No chemical treatment needed. Continue routine preventive maintenance.",
        "prevention": "Maintain good orchard hygiene. Prune for airflow. Monitor regularly for early disease signs. Use balanced fertilization."
    },
    "Bell Pepper - Bacterial Spot": {
        "description": "Bacterial Spot of bell pepper is caused by Xanthomonas campestris pv. vesicatoria. It is one of the most devastating diseases of peppers in warm, wet climates.",
        "symptoms": "Small, water-soaked spots on leaves that enlarge and turn brown with yellow halos. Lesions on fruit appear water-soaked, then raised and scabby. Premature defoliation.",
        "cause": "Bacteria: Xanthomonas campestris pv. vesicatoria. Spreads by rain splash, wind, infected seed, and handling.",
        "organic_treatment": "Copper-based bactericides applied at first sign of disease. Remove and destroy infected plant debris. Avoid overhead irrigation.",
        "chemical_treatment": "Apply copper hydroxide or copper sulfate combined with mancozeb. Follow a 7-10 day spray schedule during wet weather.",
        "prevention": "Use certified disease-free seed. Practice 2-3 year crop rotation. Avoid working in wet fields. Use drip irrigation."
    },
    "Bell Pepper - Healthy": {
        "description": "The bell pepper leaf is healthy with no signs of bacterial, fungal, or viral infection.",
        "symptoms": "No symptoms. Leaf displays deep green color and smooth, undamaged surface.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment required. Apply compost and balanced organic nutrients.",
        "chemical_treatment": "No chemical treatment needed.",
        "prevention": "Practice crop rotation. Use drip irrigation to keep foliage dry. Monitor regularly for early pest and disease signs."
    },
    "Cherry - Healthy": {
        "description": "The cherry leaf is healthy with no signs of fungal, bacterial, or viral infection.",
        "symptoms": "No symptoms. Leaf is vibrant green with smooth margins and uniform color.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment required. Regular composting and mulching recommended.",
        "chemical_treatment": "No chemical treatment needed.",
        "prevention": "Prune for air circulation. Remove fallen leaf debris. Monitor for powdery mildew during humid conditions."
    },
    "Cherry - Powdery Mildew": {
        "description": "Powdery Mildew on cherry is caused by Podosphaera clandestina. It primarily attacks young leaves and shoots, reducing fruit quality and tree vigor.",
        "symptoms": "White powdery fungal growth on upper leaf surfaces. Infected leaves curl upward. Young shoots become stunted and distorted. Fruit may show russeting.",
        "cause": "Fungus: Podosphaera clandestina. Spreads through airborne conidia. Favored by warm days, cool nights, and high humidity without rainfall.",
        "organic_treatment": "Apply potassium bicarbonate or sodium bicarbonate spray. Neem oil applications every 7-14 days. Improve air circulation by pruning.",
        "chemical_treatment": "Apply myclobutanil, trifloxystrobin, or propiconazole at first sign of infection. Rotate fungicide classes to prevent resistance.",
        "prevention": "Avoid excessive nitrogen fertilization. Prune to improve canopy airflow. Plant resistant varieties. Remove infected tissue immediately."
    },
    "Corn (Maize) - Cercospora Leaf Spot": {
        "description": "Gray Leaf Spot (Cercospora Leaf Spot) is caused by Cercospora zeae-maydis and is one of the most yield-limiting diseases of maize worldwide.",
        "symptoms": "Rectangular, pale-brown to gray lesions parallel to leaf veins. Lesions have distinct parallel edges bounded by leaf veins. Severe infections cause complete leaf blighting.",
        "cause": "Fungus: Cercospora zeae-maydis. Overwinters in infected crop residue. Favored by warm, humid conditions and poor air circulation.",
        "organic_treatment": "Rotate crops. Incorporate crop residue deeply. Select resistant hybrids. Improve plant spacing for airflow.",
        "chemical_treatment": "Apply strobilurin (azoxystrobin, pyraclostrobin) or triazole fungicides at VT-R1 growth stages. Repeat at 14-21 day intervals.",
        "prevention": "Plant resistant or tolerant corn hybrids. Rotate with non-host crops (soybeans, wheat). Minimize plant stress. Manage crop residue."
    },
    "Corn (Maize) - Common Rust": {
        "description": "Common Rust of corn is caused by Puccinia sorghi. While rarely causing severe yield loss in most seasons, it can be significant on susceptible hybrids under favorable conditions.",
        "symptoms": "Small, circular to elongated, powdery, brick-red to brown pustules on both leaf surfaces. Pustules rupture and release rust-colored spores. Heavy infection causes leaf yellowing.",
        "cause": "Fungus: Puccinia sorghi. Spreads by windborne urediniospores. Favored by cool temperatures (16-23°C) and high humidity.",
        "organic_treatment": "Plant resistant varieties. Avoid late planting in high-risk areas. Crop rotation with non-grass species.",
        "chemical_treatment": "Apply triazole or strobilurin fungicides early in infection cycle. Economic thresholds: treat when pustules appear before tasseling on susceptible hybrids.",
        "prevention": "Use rust-resistant hybrid varieties. Plant early to avoid peak spore periods. Monitor fields regularly from V6 stage onward."
    },
    "Corn (Maize) - Healthy": {
        "description": "The corn leaf is healthy with no signs of fungal, bacterial, or viral disease.",
        "symptoms": "No symptoms. Leaf shows vibrant green color with no spots, lesions, or discoloration.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment needed. Maintain proper soil fertility and irrigation.",
        "chemical_treatment": "No treatment needed.",
        "prevention": "Use certified disease-free seed. Practice crop rotation. Monitor fields regularly during growing season."
    },
    "Corn (Maize) - Northern Leaf Blight": {
        "description": "Northern Leaf Blight (NLB) is caused by Setosphaeria turcica (anamorph: Exserohilum turcicum). It is a major foliar disease of maize causing significant yield losses.",
        "symptoms": "Long (2.5-15 cm), elliptical, cigar-shaped lesions on leaves that are initially gray-green then turn tan or light brown. Lesions may coalesce causing complete blighting.",
        "cause": "Fungus: Setosphaeria turcica. Overwinters in infected debris. Conidia spread by wind and rain. Favored by moderate temperatures and humid conditions.",
        "organic_treatment": "Crop rotation with non-host crops. Bury crop residue. Select resistant hybrids. Improve air circulation.",
        "chemical_treatment": "Apply propiconazole, pyraclostrobin, or azoxystrobin at V8-V10 stage or when disease is first observed.",
        "prevention": "Plant resistant hybrid varieties. Practice 2-year crop rotation. Manage irrigation to minimize leaf wetness. Eliminate volunteer corn plants."
    },
    "Grape - Black Rot": {
        "description": "Black Rot of grapes is caused by Guignardia bidwellii. It is one of the most destructive diseases of grapes in humid regions, potentially causing 100% crop loss.",
        "symptoms": "Small, yellowish-green leaf spots that enlarge and turn brown with black margins. Circular, light-brown fruit spots that rapidly expand to cause complete fruit mummification.",
        "cause": "Fungus: Guignardia bidwellii. Overwinters in mummified fruit and infected cane tissue. Spreads during wet weather from bud break through veraison.",
        "organic_treatment": "Remove and destroy all mummified fruit and infected canes. Apply copper-based fungicides. Open canopy for air circulation.",
        "chemical_treatment": "Apply mancozeb, captan, or myclobutanil on a 7-14 day schedule from pre-bloom through 4 weeks post-bloom.",
        "prevention": "Remove mummified berries during pruning. Maintain open canopy. Time critical spray periods from bud break through berry set."
    },
    "Grape - Esca (Black Measles)": {
        "description": "Esca (Black Measles) is a complex trunk disease of grapevines caused by multiple wood-decay fungi including Phaeomoniella chlamydospora and Phaeoacremonium species.",
        "symptoms": "Interveinal chlorosis and necrosis creating tiger-stripe pattern on leaves. Berries show dark purple spots (measles). Vine may show chronic wilting or sudden death.",
        "cause": "Fungi: Complex of Phaeomoniella chlamydospora, Phaeoacremonium spp., and Botryosphaeria spp. Enter through pruning wounds.",
        "organic_treatment": "Apply wound protectant paste to pruning cuts. Remove severely infected vines. Avoid pruning in wet weather.",
        "chemical_treatment": "No fully effective chemical cure exists. Thiophanate-methyl or flusilazole applied to pruning wounds may slow progression.",
        "prevention": "Make pruning cuts in dry weather. Apply fungicidal wound sealants immediately after pruning. Remove and destroy infected wood."
    },
    "Grape - Healthy": {
        "description": "The grape leaf is healthy with no signs of fungal, bacterial, or viral infection.",
        "symptoms": "No symptoms. Leaf shows deep green color, clear venation, and undamaged margins.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment needed. Apply compost and balanced nutrition.",
        "chemical_treatment": "No treatment needed.",
        "prevention": "Maintain open canopy. Practice good sanitation. Remove leaf litter. Monitor for disease throughout the growing season."
    },
    "Grape - Leaf Blight": {
        "description": "Grape Leaf Blight (Isariopsis Leaf Spot) is caused by Pseudocercospora vitis. It is common in warm, humid grape-growing regions and can cause premature defoliation.",
        "symptoms": "Irregular, dark brown spots on upper leaf surfaces with yellowish halos. Lower surfaces show dark olivaceous fungal sporulation. Severely infected leaves drop prematurely.",
        "cause": "Fungus: Pseudocercospora vitis. Favored by warm, wet weather. Spreads through airborne and water-splash spores.",
        "organic_treatment": "Remove and destroy infected leaves. Apply copper-based fungicides. Improve air circulation through canopy management.",
        "chemical_treatment": "Apply mancozeb, captan, or copper fungicides at 10-14 day intervals during warm, wet periods.",
        "prevention": "Ensure good vine spacing and trellising for airflow. Remove fallen leaf debris. Avoid overhead irrigation."
    },
    "Peach - Bacterial Spot": {
        "description": "Bacterial Spot of peach is caused by Xanthomonas arboricola pv. pruni. It is one of the most serious diseases of peach, affecting leaves, fruit, and twigs.",
        "symptoms": "Small, water-soaked leaf spots that turn purple-brown with yellow halos. Centers drop out giving a shot-hole appearance. Fruit shows sunken, dark lesions. Twig cankers develop.",
        "cause": "Bacteria: Xanthomonas arboricola pv. pruni. Spreads by rain splash, wind-driven rain, and insects. Overwinters in infected twigs.",
        "organic_treatment": "Apply copper-based bactericides during dormancy. Remove infected twigs. Avoid overhead irrigation.",
        "chemical_treatment": "Apply oxytetracycline during bloom and shoot growth. Use copper + mancozeb mix post-bloom at 5-7 day intervals in wet weather.",
        "prevention": "Select resistant varieties. Prune for air circulation. Avoid planting in low, frost-prone areas. Never apply nitrogen late in season."
    },
    "Peach - Healthy": {
        "description": "The peach leaf is healthy with no signs of bacterial, fungal, or viral infection.",
        "symptoms": "No symptoms. Leaf shows bright green color with smooth, glossy surface.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment needed. Maintain balanced nutrition and adequate irrigation.",
        "chemical_treatment": "No treatment needed.",
        "prevention": "Monitor regularly. Prune for air circulation. Practice good orchard sanitation."
    },
    "Potato - Early Blight": {
        "description": "Early Blight of potato is caused by Alternaria solani. It is one of the most common diseases of potato worldwide, reducing yield and tuber quality.",
        "symptoms": "Dark brown to black, circular to angular lesions with concentric rings (target-board pattern) on lower leaves. Lesions have yellow halo. Severe infection causes complete defoliation.",
        "cause": "Fungus: Alternaria solani. Overwinters in infected plant debris. Spreads by wind and rain-splash. Favored by alternating wet and dry conditions.",
        "organic_treatment": "Apply copper-based fungicides or Bacillus subtilis biofungicides. Remove infected leaves. Ensure adequate potassium nutrition.",
        "chemical_treatment": "Apply chlorothalonil, mancozeb, azoxystrobin, or boscalid fungicides at 7-14 day intervals starting at first sign of infection.",
        "prevention": "Plant certified disease-free seed tubers. Practice 3-year crop rotation. Maintain plant vigor with proper nutrition. Avoid unnecessary plant stress."
    },
    "Potato - Healthy": {
        "description": "The potato leaf is healthy with no signs of fungal, bacterial, or viral disease.",
        "symptoms": "No symptoms. Leaf shows fresh green color with no spots or lesions.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment needed. Apply compost and maintain soil health.",
        "chemical_treatment": "No treatment needed.",
        "prevention": "Use certified disease-free seed. Practice crop rotation. Hill potato rows to prevent tuber greening. Monitor regularly."
    },
    "Potato - Late Blight": {
        "description": "Late Blight is caused by Phytophthora infestans, the most destructive disease of potato worldwide. It caused the Irish Famine of 1845-1849 and remains a major threat to global food security.",
        "symptoms": "Water-soaked, pale-green to brown lesions on leaf margins and tips. White fluffy sporulation on leaf undersides in humid conditions. Entire plant can collapse within days. Brown rot in tubers.",
        "cause": "Oomycete (water mold): Phytophthora infestans. Spreads rapidly by windborne sporangia in cool, wet weather. Can destroy a crop within 7-10 days.",
        "organic_treatment": "Copper-based fungicides (copper hydroxide) applied preventively. Immediately remove and destroy infected plants. Hill soil around stems.",
        "chemical_treatment": "Apply metalaxyl + mancozeb, dimethomorph, or fluopicolide at 5-7 day intervals. Begin before disease onset in high-risk conditions.",
        "prevention": "Plant resistant varieties. Use certified seed. Destroy volunteer potato plants. Apply preventive fungicides during cool, wet weather. Avoid overhead irrigation."
    },
    "Strawberry - Healthy": {
        "description": "The strawberry leaf is healthy with no signs of fungal, bacterial, or viral disease.",
        "symptoms": "No symptoms. Leaf displays bright green color with serrated margins and no discoloration.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment needed. Maintain proper soil pH (5.5-6.5) and drainage.",
        "chemical_treatment": "No treatment needed.",
        "prevention": "Use certified disease-free transplants. Renovate beds annually. Maintain proper spacing for airflow."
    },
    "Strawberry - Leaf Scorch": {
        "description": "Leaf Scorch of strawberry is caused by Diplocarpon earlianum. It is a common and serious fungal disease in humid strawberry-growing regions.",
        "symptoms": "Numerous small, dark purple to red-brown irregular spots on upper leaf surfaces. Spots may coalesce causing large scorched areas. Severely infected leaves turn brown and die.",
        "cause": "Fungus: Diplocarpon earlianum. Spreads by rain-splash and water movement. Overwinters in infected plant debris.",
        "organic_treatment": "Apply sulfur-based fungicides. Remove infected leaves. Mulch beds to reduce soil splash. Improve air circulation.",
        "chemical_treatment": "Apply captan, thiram, or myclobutanil fungicides. Begin applications in early spring and repeat at 7-14 day intervals.",
        "prevention": "Use certified disease-free plants. Avoid overhead irrigation. Renovate plantings after harvest. Remove infected debris."
    },
    "Tomato - Bacterial Spot": {
        "description": "Bacterial Spot of tomato is caused by Xanthomonas campestris pv. vesicatoria. It is one of the most damaging diseases of tomato in warm, wet climates.",
        "symptoms": "Small, water-soaked, irregular spots on leaves, stems, and fruit. Leaf spots turn brown-black with yellow halos. Fruit lesions are raised, brown, and scabby.",
        "cause": "Bacteria: Xanthomonas campestris pv. vesicatoria. Spreads by rain, wind, infected seed, and transplants. Favored by temperatures of 25-30°C with frequent rain.",
        "organic_treatment": "Apply copper-based bactericides preventively. Remove and destroy infected plant material. Avoid working in wet conditions.",
        "chemical_treatment": "Apply copper hydroxide + mancozeb mixture. Begin at transplanting and repeat every 7-10 days in wet weather.",
        "prevention": "Use disease-free certified seed. Hot-water treat seed at 50°C for 25 minutes. Practice 2-3 year rotation. Use drip irrigation."
    },
    "Tomato - Early Blight": {
        "description": "Early Blight of tomato is caused by Alternaria solani. It is one of the most common and widespread diseases of tomato affecting leaves, stems, and fruit.",
        "symptoms": "Dark brown, target-like concentric ring lesions on lower leaves first. Yellow halo surrounds lesions. Severe infection causes defoliation from the bottom up. Stem lesions cause collar rot in seedlings.",
        "cause": "Fungus: Alternaria solani. Persists in soil and plant debris. Spreads by wind, rain splash, and contaminated tools.",
        "organic_treatment": "Apply copper-based fungicides or Bacillus subtilis. Remove infected lower leaves. Mulch to prevent soil splash.",
        "chemical_treatment": "Apply chlorothalonil, mancozeb, azoxystrobin, or difenoconazole at 7-day intervals starting when disease appears.",
        "prevention": "Use resistant varieties. Practice 3-year crop rotation. Mulch soil surface. Stake and train plants for airflow. Avoid wetting foliage."
    },
    "Tomato - Healthy": {
        "description": "The tomato leaf is healthy with no signs of fungal, bacterial, or viral disease.",
        "symptoms": "No symptoms. Leaf shows vibrant dark green color with no spots, lesions, or yellowing.",
        "cause": "No disease detected.",
        "organic_treatment": "No treatment needed. Apply balanced organic fertilizer and compost.",
        "chemical_treatment": "No treatment needed.",
        "prevention": "Practice crop rotation. Stake plants for airflow. Use drip irrigation. Monitor regularly for early symptoms."
    },
    "Tomato - Late Blight": {
        "description": "Late Blight of tomato, caused by Phytophthora infestans, is one of the most devastating diseases of tomato. The same pathogen caused the Irish Potato Famine.",
        "symptoms": "Large, dark brown, greasy-looking lesions on leaves. White cottony sporulation on leaf undersides in humid weather. Dark brown lesions on stems. Fruit shows large, firm, brown rot.",
        "cause": "Oomycete: Phytophthora infestans. Spreads rapidly by windborne sporangia in cool (10-25°C), wet conditions. Can destroy entire crops within 1-2 weeks.",
        "organic_treatment": "Apply copper-based fungicides preventively. Immediately remove all infected plant material. Destroy do not compost infected plants.",
        "chemical_treatment": "Apply metalaxyl + mancozeb, dimethomorph, or mandipropamid at 5-7 day intervals. Apply preventively when conditions favor disease.",
        "prevention": "Use resistant varieties. Avoid overhead irrigation. Space plants for good airflow. Destroy infected plant debris. Apply preventive sprays during cool, wet weather."
    },
    "Tomato - Septoria Leaf Spot": {
        "description": "Septoria Leaf Spot is caused by Septoria lycopersici. It is one of the most destructive diseases of tomato foliage in the eastern United States and other humid regions.",
        "symptoms": "Numerous small, circular spots (3-6mm) on lower leaves with dark brown borders and gray-white centers containing tiny black dots (pycnidia). Affected leaves turn yellow and drop.",
        "cause": "Fungus: Septoria lycopersici. Overwinters in infected crop debris and weed hosts. Spreads by water splash. Favored by warm (20-25°C), wet, humid weather.",
        "organic_treatment": "Apply copper-based fungicides. Remove infected lower leaves immediately. Mulch soil surface to prevent splash dispersal.",
        "chemical_treatment": "Apply chlorothalonil, mancozeb, or azoxystrobin on a 7-10 day schedule from transplanting through harvest.",
        "prevention": "Use disease-free seed and transplants. Practice 3-year rotation. Stake and train for airflow. Mulch to prevent soil splash."
    },
    "Tomato - Yellow Leaf Curl Virus": {
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is a devastating viral disease transmitted exclusively by the silverleaf whitefly (Bemisia tabaci). It causes severe yield losses worldwide.",
        "symptoms": "Upward and inward curling of leaf margins. Interveinal chlorosis giving leaves a yellowed appearance. Stunted plant growth. Flowers may drop. Fruit production severely reduced or eliminated.",
        "cause": "Virus: Tomato Yellow Leaf Curl Virus (TYLCV), transmitted persistently by Bemisia tabaci (silverleaf whitefly). No plant-to-plant transmission without the insect vector.",
        "organic_treatment": "There is no cure for infected plants. Remove and destroy infected plants immediately to prevent whitefly spread. Use yellow sticky traps to monitor whitefly populations. Apply insecticidal soap or neem oil to manage whitefly populations.",
        "chemical_treatment": "Apply systemic insecticides (imidacloprid, thiamethoxam) to control whitefly vector. Soil drench at transplanting for long-term protection. Reflective mulches repel whiteflies.",
        "prevention": "Plant TYLCV-resistant varieties. Use insect-proof nets on seedbeds. Monitor and control whitefly populations early. Remove and destroy infected plants. Avoid planting near other infected crops."
    },
}


def get_disease_info(disease_name: str) -> dict:
    """Return disease information dict for the given disease name."""
    return DISEASE_INFO.get(disease_name, {
        "description": f"Information for '{disease_name}' is not available in the database.",
        "symptoms": "Please consult a local agricultural extension officer for detailed symptom information.",
        "cause": "Unknown — consult an agricultural expert.",
        "organic_treatment": "Consult your local agricultural extension officer for organic treatment options.",
        "chemical_treatment": "Consult your local agricultural extension officer for recommended chemical treatments.",
        "prevention": "Practice good field hygiene, crop rotation, and regular monitoring."
    })


def is_healthy(disease_name: str) -> bool:
    """Return True if the predicted class represents a healthy plant."""
    return "healthy" in disease_name.lower() or "Healthy" in disease_name
