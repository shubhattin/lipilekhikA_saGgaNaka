# Both the Typing language database and Display Language Databses are store in "resources/others". Thier names are in base64


def antaH_parivartan(js):
    ret = {}
    for k in js:
        ret[js[k]] = k
    return ret


lang_code = [
    {
        "हिन्दी": "Hindi",
        "বাংলা": "Bengali",
        "తెలుగు": "Telugu",
        "தமிழ்": "Tamil",
        "मराठी": "Marathi",
        "ગુજરાતી": "Gujarati",
        "മലയാളം": "Malayalam",
        "ಕನ್ನಡ": "Kannada",
        "ଓଡ଼ିଆ": "Oriya",
        "कोंकणी": "Konkani",
        "অসমীয়া": "Assamese",
        "संस्कृतम्": "Sanskrit",
        "नेपाली": "Nepali",
        "ਪੰਜਾਬੀ": "Punjabi",
        "اُردُو‎": "Urdu",
        "كٲشُر": "Kashmiri",
        "Romanized": "Romanized",
        "සිංහල": "Sinhala",
        "தமிழ்-Extended": "Tamil-Extended",
        "शारदा": "Sharada",
        "मोडी": "Modi",
        "सिद्धम्": "Siddham",
        "கிரந்த (தமிழ்)": "Granth",
        "ब्राह्मी": "Brahmi",
    },
    [],
    [],
]
lang_code[1] = antaH_parivartan(lang_code[0])
main = False
for x in lang_code[1]:
    lang_code[2].append(x)

display_lang_lists = (
    "English",
    "हिन्दी",
    "संस्कृतम्",
    "తెలుగు",
    "বাংলা",
    "தமிழ்",
    "ಕನ್ನಡ",
    "मराठी",
    "ગુજરાતી",
    "മലയാളം",
    "ଓଡ଼ିଆ",    
    "ਪੰਜਾਬੀ",
    "اُردُو"
)
bhAShAH = []
for x in lang_code[0]:
    bhAShAH.append(x)
bhAShAH_img = []
for x in bhAShAH:
    bhAShAH_img.append(x)
bhAShAH_img.append("Vedic")

AJAY = {
    "Hindi": "अजय्",
    "Sanskrit": "अजय्",
    "Brahmi": "अजय्",
    "Nepali": "अजय्",
    "Siddham": "अजय्",
    "Marathi": "अजय्",
    "Konkani": "अजय्",
    "Tamil": "அஜய்",
    "Sinhala": "අජය්",
    "Tamil-Extended": "அஜய்",
    "Granth": "அஜய்",
    "Telugu": "అజయ్",
    "Malayalam": "അജയ്",
    "Kannada": "ಅಜಯ್",
    "Bengali": "অজয্",
    "Oriya": "ଅଜଯ୍",
    "Assamese": "অজয্",
    "Gujarati": "અજય્",
    "Punjabi": "ਅਜਯ੍",
    "Urdu": "اجَے ",
    "Kashmiri": "اجَے ",
    "Romanized": "ajay ",
    "Sharada": "अजय्",
    "Modi": "अजय्",
}
