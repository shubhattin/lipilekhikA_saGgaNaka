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
    "తెలుగు",
    "বাংলা",
    "தமிழ்",
    "ಕನ್ನಡ",
    "संस्कृतम्",
)
bhAShAH = []
for x in lang_code[0]:
    bhAShAH.append(x)
bhAShAH_img = []
for x in bhAShAH:
    bhAShAH_img.append(x)
bhAShAH_img.append("Vedic")
#lang_db_here
DISPLAY_DATA = {
    "English": {
        "app_title": "Lipi Lekhika",
        "about_title": "About Lipi Lekhika",
        "licence_title": "Lipi Lekhika Licence",
        "values": {
            "sahayika": "Lekhan Sahayika",
            "app_description": "This is an Application to type Indian Langugaes with Full Speed and Accuracy.\nFor More Related Information visit lipilekhika.com.",
            "version": "Version : {0}",
            "pin_top": "Pin On Top",
            "licence": "Show Licence",
            "background_run": "Run in Background",
            "typing_lang_main": "Language",
            "instructions": "• Windows+Ctrl :-To turn On/Off\n• .(dot) :- To type numbers, vowels or special symbols \n• Alt for 1 second :- To see current selected options.\n• Lekhan Sahayika will be at cursor(of mouse) position.",
            "vishisht_label": "This is the Advanced Version of Lipi Lekhika.\nIt may contain Edited Data.",
            "vishisht_button": "Use Main Application",
            "sUchI_msg": "There are more alternatives for typing the aksharas below.\nMake sure to Turn On the Lekhan Sahayika to learn more.",
            "nirdesh": "• Shift+F2 :-To Start Lipi Lekhika Directly  &  • Windows+Esc :- To Close Appliaction\n• Lekhan Sahayika will be displed at current mouse cursor position.\n• You can set Default Option for Application in menu, for eg- default typing language.\n• Windows+F5 : To Decrease Volume & Windows+F6 : To Increase Volume"
        },
        "menu_values": {
            "sahayika": "Lekhan Sahayika",
            "about": "Parichaya",
            "encoding_table": "View Encoding Table",
            "normal_version": "Open Normal Version (Lipi Parivartak)",
            "typing_lang": "Typing Language",
            "default": "Set Default Options",
            "startup": "Open This Window on App Startup",
            "extra": "Other Information"
        },
        "on": "On",
        "off": "Off",
        "yes": "Yes",
        "no": "No",
        "turned_on": "Turned On",
        "turned_off": "Turned Off",
        "sahayika_on": "Lekhan Sahayika Turned On",
        "sahayika_off": "Lekhan Sahayika Turned off",
        "startup_msg": "Lipi Lekhika Started\nApp : {0}\nLekhan Sahayika : {1}\nTyping Script : {2}\n{3}\nPress Shift+F2 to start App Directly",
        "hide2": "Lipi Lekhika running in background.\nCan be Controlled through Taskbar Icon",
        "typ_lang_change": "Typing Language Changed to {0}",
        "lang": "Language",
        "anuprayog": "App",
        "exit_msg": "Lipi Lekhika Closed",
        "time_exceed": "Lipi Lekhika Turned off\nAs It was Left idle for 10 minutes.",
        "sahAyikA_msg": {
            "first_sahayika": "Press Characters in black for their corresponding akshara.\nPress ; or q to reset or to remove continuations.",
            "second_sahayika": " Shift can also be used in place of CapsLock.For eg: Shift+a➠A"
        },
        "scripts": {
            "Hindi": "Hindi",
            "Bengali": "Bengali",
            "Telugu": "Telugu",
            "Tamil": "Tamil",
            "Tamil-Extended": "Tamil Extended",
            "Marathi": "Marathi",
            "Gujarati": "Gujarati",
            "Sinhala": "Sinhala",
            "Sanskrit": "Sanskrit",
            "Malayalam": "Malayalam",
            "Kannada": "Kannada",
            "Oriya": "Odia",
            "Konkani": "Konkani",
            "Assamese": "Assamese",
            "Nepali": "Nepali",
            "Punjabi": "Punjabi",
            "Urdu": "Urdu",
            "Kashmiri": "Kashmiri",
            "Romanized": "Romanized",
            "Sharada": "Sharada",
            "Modi": "Moḍi",
            "Brahmi": "Brahmi",
            "Siddham": "Siddham",
            "Granth": "Granth"
        },
        "download_msg": "New Version Of Lipi Lekhika Available !\nDo you want to update to newer version?",
        "tray": {
            "show": "Show App Window",
            "exit": "Exit Application",
            "title": "Lipi Lekhika is {0}\nTyping Language : {1}\nLekhan Sahayika : {2}",
            "restart": "Resatrt Lipi Lekhika",
            "restarted": "Lipi Lekhika Resatrted"
        },
        "title": {
            "usage": "View Usage Table and Other Instructions",
            "app_lang_img": "Set User Interface Language",
            "app_lang_option": "Set User Interface Language",
            "typ_lang": "Set Typing Language",
            "background": "Use in background through Taskbar and keyboard shortcuts",
            "main0": "Turn On Lipi Lekhika",
            "main1": "Turn Off Lipi Lekhika",
            "sahayika0": "Turn On Lekhan Sahayika",
            "sahayika1": "Turn Off Lekhan Sahayika",
            "menu": "Set Default Options and More"
        }
    },
    "हिन्दी": {
        "app_title": "लिपि लेखिका",
        "about_title": "परिचय",
        "licence_title": "प्रत्यादेश",
        "values": {
            "sahayika": "लेखन सहायिका",
            "app_description": "यह अनुप्रयोग भारतीय भाषाओं को पूर्ण गति एवं सूक्ष्मता के साथ लिखने के लिए है।\nअधिक संबन्धित जानकारी के lipilekhika.com पर जाएं।",
            "typing_lang_main": "लेखन भाषा",
            "background_run": "परोक्षता मे चलाएं",
            "version": "संस्करण संख्या : {0}",
            "licence": "प्रत्यादेश दिखाएं",
            "pin_top": "सर्वोच्च स्थापित करें",
            "instructions": "• Windows+Ctrl :- चालू/बन्द करने के लिए \n• .(डॉट) :- संख्याएं, मात्रा एवं अन्य विशेष चिह्नों के लिए \n• Alt 1 सेकेंड :- वर्तमान विकल्पों को देखने के लिए\n • लेखन सहायिका को मौषकस्थान पर दिखाया जाएगा",
            "vishisht_label": "यह लिपि लेखिका का विशिष्ट संस्करण है।\n हो सकता है ये मूल से भिन्न हो।.",
            "vishisht_button": "मूल अनुप्रयोग खोलें",
            "sUchI_msg": "नीचे लिखे अक्षरों को और भी तरीकों से लिख जा सकत है।\nअधिक जानने के लिए लेखन सहायिका अवश्य चालू रखें।",
            "nirdesh": "• Shift+F2 :- लिपि लेखिका को सीधा खोलने के लिए  &  • Windows+Esc :- अनुप्रयोग को बन्द करने के लिए\n• लेखन सहायिका को वर्तमान मौषकस्थान पर दिखाया जाएगा।\n• विकल्पपट्टी से पूर्वनिश्चित विकल्पों को निर्धारित किया जा सकता है। उदाहरण - पूर्वनिश्चित लेखन भाषा।\n• Windows+F5 : ध्वनि कम करने के लिए & Windows+F6 : ध्वनि बढ़ाने के लिए"
        },
        "menu_values": {
            "sahayika": "लेखन सहायिका",
            "about": "परिचय",
            "encoding_table": "परिवर्तन सूची देखें",
            "normal_version": "सामान्य संस्करण खोलें (लिपि परिवर्तक)",
            "typing_lang": "लेखन भाषा",
            "default": "पूर्वनिश्चित विकल्प निर्धारण",
            "startup": "इस कोष्ठ को अनुप्रयोग के प्रारंभ मे खोलें",
            "extra": "अन्य विशिष्ट जानकारी"
        },
        "on": "चालू",
        "off": "बन्द",
        "yes": "हाँ",
        "no": "नहीं",
        "turned_on": "चालू किया गया",
        "turned_off": "बन्द किया गया",
        "sahayika_on": "लेखन सहायिका चालू किया गया",
        "sahayika_off": "लेखन सहायिका बन्द किया गया",
        "startup_msg": "लिपि लेखिका चालू\nअनुप्रयोग : {0}\nलेखन सहायिका : {1}\nलेखन लिपि : {2}\n{3}\nअनुप्रयोग खोलने हेतु Shift+F2 दबाएं।",
        "hide2": "लिपि लेखिका परोक्ष मे अभी भी कार्यशील है।\nकार्यपट्टी चित्रक से नियंत्रित किया जा सकता है",
        "typ_lang_change": "लेखन भाषा को {0} मे बदला गया",
        "lang": "भाषा",
        "anuprayog": "अनुप्रयोग",
        "exit_msg": "लिपि लेखिका बन्द",
        "time_exceed": "लिपि लेखिका को बन्द किया गया\nक्यों कि यह 10 मिनट से अनुपयुक्त था।",
        "sahAyikA_msg": {
            "first_sahayika": "काले अक्षरों को दबाएं उनके नीचे लिके अक्षरों को लिखने के लिए।\n   q या ; को दबाएं पुनर्प्रर्वतन करने के लिए।",
            "second_sahayika": " Shift भी दबाया जा सकता है CapsLock की जगह। उदाहरण: Shift+a➠A"
        },
        "scripts": {
            "Hindi": "हिन्दी",
            "Bengali": "बंगाली",
            "Telugu": "तेलुगु",
            "Tamil": "तमिल",
            "Tamil-Extended": "विस्तारित-तमिल",
            "Marathi": "मराठी",
            "Gujarati": "गुजराती",
            "Sinhala": "सिंहल",
            "Sanskrit": "संस्कृत",
            "Malayalam": "मलयालम",
            "Kannada": "कन्नड़",
            "Oriya": "ओड़िया",
            "Konkani": "कोंकणी",
            "Assamese": "असमिया",
            "Nepali": "नेपाली",
            "Punjabi": "पंजाबी",
            "Urdu": "उर्दू",
            "Kashmiri": "कश्मीरी",
            "Romanized": "रोमनीकृत",
            "Sharada": "शारदा",
            "Modi": "मोडी",
            "Brahmi": "ब्राह्मी",
            "Siddham": "सिद्धम्",
            "Granth": "ग्रन्थ"
        },
        "download_msg": "लिपि लेखिका का नया संस्करण उपलब्ध !\nक्या आप नए संस्करण मे अद्यतित करना चाहेंगे?",
        "tray": {
            "show": "अनुप्रयोग का कोष्ठ दिखाएं",
            "exit": "अनुप्रयोग बन्द करें",
            "title": "लिपि लेखिका {0} है\nलेखन भाषा : {1}\nलेखन सहायिका : {2}",
            "restart": "लिपिलेखिका पुनरारंभ करें",
            "restarted": "लिपिलेखिका चालू किया गया"
        },
        "title": {
            "usage": "परिवर्तन सूची एवं अन्य निर्देशों को देखें",
            "app_lang_img": "अनुप्रयोग की भाषा निर्धारित करें",
            "app_lang_option": "अनुप्रयोग की भाषा निर्धारित करें",
            "typ_lang": "लेखन भाषा निर्धारित करें",
            "background": "परोक्ष मे कार्यपट्टी चित्रक एवं लघुतोदनों के द्वारा प्रयोग करें",
            "main0": "लिपि लेखिका चालू करें",
            "main1": "लिपि लेखिका बन्द करें",
            "sahayika0": "लेखन सहायिका चालू करें",
            "sahayika1": "लेखन सहायिका बन्द करें",
            "menu": "पूर्वनिश्चित विकल्पों को निर्धारित करें एवं अधिक"
        }
    },
    "संस्कृतम्": {
        "app_title": "लिपिलेखिका",
        "about_title": "लिपिलेखिकापरिचयः",
        "licence_title": "लिपिलेखिकाप्रत्यादेशम्",
        "values": {
            "sahayika": "लेखनसहायिका",
            "app_description": "इदम् अनुप्रयोगः भारतीयभाषाः पूर्णगत्या पूर्णसूक्ष्मतया सह लेखितुमस्ति।\n अधिकसंबन्धितसूचनायै lipilekhika.comजालस्थाने यातु।",
            "typing_lang_main": "लेखनभाषा",
            "version": "संस्करणं सङ्ख्या : {0}",
            "background_run": "परोक्षतायां चल्यते",
            "licence": "प्रत्यादेशं दर्शतु",
            "pin_top": "सर्वोच्चे स्थापयतु",
            "instructions": "• Windows+Ctrl :- अनुप्रयोगं चलितुं विचलितुं वा \n• .(डौट) :- संख्यामात्राभ्याम् अन्यविशेषचिह्नाय च\n• Alt एकक्षणाय :- वर्तमानविकल्पानि द्रष्टुम्\n • लेखनसहायिकां वर्तमानमौषकस्थाने दृष्टः",
            "vishisht_label": "इदं लिपिलेखिकायाः विशिष्ट अस्ति।\n एतच् छक्नोति भवति मूलरूपाद् भिन्नः अस्तु।",
            "vishisht_button": "मूलसंस्करम् उद्घाटयतु",
            "sUchI_msg": "निच्चैः लिखिताक्षरान् लेखितुम् अधिकविकल्पानि अपि वर्तते।\nअधिकः आज्ञातुं लेखनसहायिकां अवश्यः चलनं कुरु।",
            "nirdesh": "• Shift+F2 :- लिपिलेखिकां प्रत्यक्षतः उद्घाट्यतुम्  &  • Windows+Esc :- अनुप्रयोगं विचलितुम्\n• लेखनसहायिकां वर्तमानमौषकस्थाने अनुप्रयोगेन दृष्टः।\n• विकल्पपट्ट्या पूर्वनिश्चितविकल्पान् निर्धारिष्यति शक्नोष्यति। उदाहरणार्थम् - लेखनभाषा।\n• Windows+F5 : ध्वनिं अपदस्यतुं & Windows+F6 : ध्वनिं व्रद्धुम्"
        },
        "menu_values": {
            "sahayika": "लेखनसहायिका",
            "about": "परिचयः",
            "encoding_table": "परिवर्तनसूचीं दर्शतु",
            "normal_version": "सामान्यसंस्करणमुद्घाटयतु (लिपिपरिवर्तकम्)",
            "typing_lang": "लेखनभाषा",
            "default": "पूर्वनिश्चितविकल्प-निर्धारणम्",
            "startup": "इदं कोष्ठं अनुप्रयोगस्य प्रारम्भे उद्घाटयतु",
            "extra": "विशिष्टान्याः"
        },
        "on": "चलितः",
        "off": "विचलितः",
        "yes": "अस्तु",
        "no": "नास्तु",
        "turned_on": "चलितं क्रियते",
        "turned_off": "विचलितं क्रियते",
        "sahayika_on": "लेखनसहायिकां चाल्यते",
        "sahayika_off": "लेखनसहायिकां विचल्यते",
        "startup_msg": "लिपिलेखिका चल्यते\nअनुप्रयोगः : {0}\nलेखनसहायिका : {1}\nलेखनलिपिः : {2}\n{3}\nअनुप्रयोगं उद्घाटयतुं Shift+F2 तुदतु।",
        "hide2": "लिपिलेखिका परोक्षे अधुनापि कार्यशीलम् अस्ति।\nकार्यपट्टीचित्रकेन नियन्त्र्यते शक्यते",
        "typ_lang_change": "लेखनभाषां {0} परिवर्त्यते",
        "lang": "भाषाः",
        "anuprayog": "अनुप्रयोगः",
        "exit_msg": "लिपिलेखिकां विघाटयते",
        "time_exceed": "लिपि लेखिकां विचल्यते\nयतः इदं 10निमेषात् अनुपयुक्तम् अभवत्।",
        "sahAyikA_msg": {
            "first_sahayika": "कृष्णान् अक्षरान् तुदतु तेषां निच्चैः लिखितान् अक्षराणि अधिलेखितुम्।\n qकुञ्जिकां ;कुञ्जिकां वा तुदतु पुनर्प्रवर्तितुं दूरीकर्तुं वा।",
            "second_sahayika": " Shiftकुञ्जिकाम् अपि तुदेत् CapsLockकुञ्जिकां तत्स्थाने।यथोदाहरणम्: Shift+a➠A"
        },
        "scripts": {
            "Hindi": "हिन्द्यां",
            "Bengali": "बङ्गाल्यां",
            "Telugu": "तेलुग्वां",
            "Tamil": "तमिले",
            "Tamil-Extended": "विस्तारिततमिले",
            "Khudabadi": "खुदाबाद्यां",
            "Marathi": "मराठ्यां",
            "Gujarati": "गुजरात्यां",
            "Sanskrit": "संस्कृते",
            "Malayalam": "मलयाळमे",
            "Kannada": "कन्नडे",
            "Sinhala": "सिंहले",
            "Oriya": "ओडियायां",
            "Konkani": "कोङ्कण्यां",
            "Assamese": "असमीयायां",
            "Nepali": "नेपाल्यां",
            "Punjabi": "पञ्जाब्यां",
            "Urdu": "उर्द्वां",
            "Kashmiri": "कश्मीर्यां",
            "Romanized": "रोमनीकृते",
            "Sharada": "शारदायां",
            "Modi": "मोड्यां",
            "Brahmi": "ब्राह्म्यां",
            "Siddham": "सिद्धे",
            "Granth": "ग्रन्थे"
        },
        "download_msg": "लिपिलेखिकायाः  नवसंस्करणम् उपलब्धः !\nकिं भवान् अनुप्रयोगम् अद्यतितव्यम्?",
        "tray": {
            "show": "अनुप्रयोगस्य कोष्ठं दर्शतु",
            "exit": "अनुप्रयोगं विचलयतु",
            "title": "लिपिलेखिका {0}\nलेखनभाषा : {1}\nलेखनसहायिका : {2}",
            "restart": "लिपिलेखिकां पुनरारम्भयतु",
            "restarted": "लिपिलेखिकां पुनरारम्भितम्"
        },
        "title": {
            "usage": "परिवर्तनसूचीम् अन्यनिर्देशानि च दर्शतु",
            "app_lang_img": "अनुप्रयोगस्य भाषां निर्धारयतु",
            "app_lang_option": "अनुप्रयोगस्य भाषां निर्धारयतु",
            "typ_lang": "लेखनभाषां निर्धारयतु",
            "background": "परोक्षतायां कार्यपट्टीचित्रकेन लघुतोदनेभ्यश्च प्रयोगं कुरु",
            "main0": "लिपिलेखिकां चलितं क्रियते",
            "main1": "लिपिलेखिकां विचलितं क्रियते",
            "sahayika0": "लेखनसहायिकां चलितं क्रियते",
            "sahayika1": "लेखनसहायिकां विचलितं क्रियते",
            "menu": "पूर्वनिश्चितविकल्पानि निर्धारयतु अधिकाः च"
        }
    },
    "தமிழ்": {
        "app_title": "ஸ்கிரிப்ட் எழுத்தாளர்",
        "about_title": "அறிமுகம்",
        "licence_title": "ஆணை",
        "values": {
            "sahayika": "எழுத்து உதவியாளர்",
            "app_description": "இந்த பயன்பாடு முழு வேகத்துடனும் துல்லியத்துடனும் இந்திய மொழிகளை எழுதுவதற்கானது.\nமேலும் தொடர்புடைய தகவல்களுக்கு lipilekhika.com ஐப் பார்வையிடவும்.",
            "typing_lang_main": "மொழி எழுதுதல்",
            "background_run": "மறைமுகமாக இயக்கவும்",
            "version": "பதிப்பு எண்: {0}",
            "licence": "கட்டளையைக் காட்டு",
            "pin_top": "மேல் நிறுவவும்",
            "instructions": "• Windows + Ctrl: - இயக்க / அணைக்க\n(. (புள்ளி): - எண்கள், அளவுகள் மற்றும் பிற சிறப்பு சின்னங்களுக்கு\nT Alt 1 நொடி: - தற்போதைய விருப்பங்களைக் காண\nAssistant எழுத்து உதவியாளர் இருப்பிடத்தில் காண்பிக்கப்படுவார்",
            "vishisht_label": "இந்த ஸ்கிரிப்ட் ஆசிரியரின் குறிப்பிட்ட பதிப்பாகும்.\nஇது அசலில் இருந்து வேறுபட்டிருக்கலாம்.",
            "vishisht_button": "சொந்த பயன்பாட்டைத் திறக்கவும்",
            "sUchI_msg": "கீழே கொடுக்கப்பட்டுள்ள கடிதங்களை வேறு வழிகளில் எழுதலாம்.\nமேலும் அறிய எழுத்து உதவியாளரை தொடர்ந்து வைத்திருங்கள்.",
            "nirdesh": "• Shift + F2: - ஸ்கிரிப்ட் எழுத்தாளரை நேரடியாகத் திறக்க &amp; • Windows + Esc: - பயன்பாட்டை மூட\nAssistant எழுத்து உதவியாளர் தற்போதைய இடத்தில் காண்பிக்கப்படுவார்.\nRed விருப்பத்தேர் பட்டியில் இருந்து முன் வரையறுக்கப்பட்ட விருப்பங்களை அமைக்கலாம். எடுத்துக்காட்டு - முன் வரையறுக்கப்பட்ட எழுத்து மொழி.\n• விண்டோஸ் + எஃப் 5: ஒலியைக் குறைக்கவும் &amp; விண்டோஸ் + எஃப் 6: அளவை அதிகரிக்கவும்"
        },
        "menu_values": {
            "sahayika": "எழுத்து உதவியாளர்",
            "about": "அறிமுகம்",
            "encoding_table": "மாற்றம் பட்டியலைக் காண்க",
            "normal_version": "இயல்பான பதிப்பைத் திறக்கவும் (ஸ்கிரிப்ட் சேஞ்சர்)",
            "typing_lang": "மொழி எழுதுதல்",
            "default": "முன்னரே தீர்மானிக்கப்பட்ட விருப்ப அமைப்பு",
            "startup": "பயன்பாட்டின் தொடக்கத்தில் இந்த கலத்தைத் திறக்கவும்",
            "extra": "பிற குறிப்பிட்ட தகவல்கள்"
        },
        "on": "ஆன்",
        "off": "மூடப்பட்டது",
        "yes": "ஆம்",
        "no": "இல்லை",
        "turned_on": "இயக்கப்பட்டது",
        "turned_off": "மூடப்பட்டது",
        "sahayika_on": "எழுத்து உதவியாளர் இயக்கப்பட்டது",
        "sahayika_off": "எழுத்து உதவியாளர் அணைக்கப்பட்டார்",
        "startup_msg": "ஸ்கிரிப்ட் எழுத்தாளர்\nவிண்ணப்பம்: {0}\nஎழுத்து உதவியாளர்: {1}\nஎழுதும் ஸ்கிரிப்ட்: {2}\n{3}\nபயன்பாட்டைத் திறக்க Shift + F2 ஐ அழுத்தவும்.",
        "hide2": "ஸ்கிரிப்ட் எழுத்தாளர் இன்னும் மறைமுகமாக வேலை செய்கிறார்.\nபெயிண்டரிலிருந்து பணிப்பட்டியைக் கட்டுப்படுத்தலாம்",
        "typ_lang_change": "எழுதும் மொழி {0 to ஆக மாற்றப்பட்டது",
        "lang": "மொழி",
        "anuprayog": "விண்ணப்பம்",
        "exit_msg": "ஸ்கிரிப்ட் எழுத்தாளர் மூடப்பட்டார்",
        "time_exceed": "ஸ்கிரிப்ட் எழுத்தாளர் நீக்கப்பட்டார்\nஏனெனில் இது 10 நிமிடங்களுக்கு பொருந்தாது.",
        "sahAyikA_msg": {
            "first_sahayika": "கீழே உள்ள எழுத்துக்களை எழுத கருப்பு எழுத்துக்களை அழுத்தவும்.\nq அல்லது; புத்துயிர் பெற அழுத்தவும்.",
            "second_sahayika": "கேப்ஸ்லாக் என்பதற்கு பதிலாக ஷிப்டையும் அழுத்தலாம். எடுத்துக்காட்டு: Shift + a➠A"
        },
        "scripts": {
            "Hindi": "இந்தி",
            "Bengali": "பெங்காலி",
            "Telugu": "தெலுங்கு",
            "Tamil": "தமிழ்",
            "Tamil-Extended": "விரிவாக்கப்பட்ட-தமிழ்",
            "Marathi": "கொடி",
            "Gujarati": "குஜராத்தி",
            "Sinhala": "சிங்களம்",
            "Sanskrit": "சமஸ்கிருதம்",
            "Malayalam": "மலையாளம்",
            "Kannada": "கன்னடம்",
            "Oriya": "ஒரியா",
            "Konkani": "கொங்கனி",
            "Assamese": "அசாமி",
            "Nepali": "நேபாளி",
            "Punjabi": "பஞ்சாபி",
            "Urdu": "உருது",
            "Kashmiri": "காஷ்மீர்",
            "Romanized": "ரோமானிய",
            "Sharada": "ஷர்தா",
            "Modi": "மோடி",
            "Brahmi": "பிராமி",
            "Siddham": "சித்தம்",
            "Granth": "மானியம்"
        },
        "download_msg": "திரைக்கதை எழுத்தாளரின் புதிய பதிப்பு கிடைக்கிறது!\nபுதிய பதிப்பிற்கு புதுப்பிக்க விரும்புகிறீர்களா?",
        "tray": {
            "show": "பயன்பாட்டு கலத்தைக் காட்டு",
            "exit": "பயன்பாட்டை மூடுக",
            "title": "ஸ்கிரிப்ட் எழுத்தாளர் {0}\nஎழுதும் மொழி: {1}\nஎழுத்து உதவியாளர்: {2}",
            "restart": "ஸ்கிரிப்டை மறுதொடக்கம் செய்யுங்கள்",
            "restarted": "ஸ்கிரிப்ட் இயக்கப்பட்டது"
        },
        "title": {
            "usage": "மாற்றம் பட்டியல் மற்றும் பிற வழிமுறைகளைக் காண்க",
            "app_lang_img": "பயன்பாட்டின் மொழியை அமைக்கவும்",
            "app_lang_option": "பயன்பாட்டின் மொழியை அமைக்கவும்",
            "typ_lang": "எழுதும் மொழியை அமைக்கவும்",
            "background": "பணிப்பட்டி ஓவியர் மற்றும் சிறிய செதில்கள் மூலம் மறைமுகமாகப் பயன்படுத்தவும்",
            "main0": "ஸ்கிரிப்ட் எழுத்தாளரைத் தொடங்குங்கள்",
            "main1": "நெருங்கிய ஸ்கிரிப்ட் எழுத்தாளர்",
            "sahayika0": "எழுத்து உதவியாளரை இயக்கவும்",
            "sahayika1": "நெருங்கிய எழுத்து உதவியாளர்",
            "menu": "முன் விருப்பங்கள் மற்றும் பலவற்றை அமைக்கவும்"
        }
    },
    "తెలుగు": {
        "app_title": "స్క్రిప్ట్ రచయిత",
        "about_title": "పరిచయం",
        "licence_title": "ఆదేశం",
        "values": {
            "sahayika": "రైటింగ్ అసిస్టెంట్",
            "app_description": "ఈ అనువర్తనం పూర్తి వేగంతో మరియు ఖచ్చితత్వంతో భారతీయ భాషలను వ్రాయడానికి.\nమరింత సంబంధిత సమాచారం కోసం lipilekhika.com ని సందర్శించండి.",
            "typing_lang_main": "భాష రాయడం",
            "background_run": "పరోక్షంగా అమలు చేయండి",
            "version": "సంస్కరణ సంఖ్య: {0}",
            "licence": "ఆదేశాన్ని చూపించు",
            "pin_top": "టాప్ ఇన్‌స్టాల్ చేయండి",
            "instructions": "• Windows + Ctrl: - ఆన్ / ఆఫ్ చేయడానికి\n(. (డాట్): - సంఖ్యలు, పరిమాణాలు మరియు ఇతర ప్రత్యేక చిహ్నాల కోసం\n• ఆల్ట్ 1 సెకను: - ప్రస్తుత ఎంపికలను చూడటానికి\nAssistant స్థానంలో రైటింగ్ అసిస్టెంట్ చూపబడతారు",
            "vishisht_label": "ఈ స్క్రిప్ట్ రచయిత యొక్క నిర్దిష్ట వెర్షన్.\nఇది అసలు నుండి భిన్నంగా ఉండవచ్చు.",
            "vishisht_button": "స్థానిక అనువర్తనాన్ని తెరవండి",
            "sUchI_msg": "క్రింద ఇచ్చిన అక్షరాలను ఇతర మార్గాల్లో వ్రాయవచ్చు.\nమరింత తెలుసుకోవడానికి రైటింగ్ అసిస్టెంట్‌ను ఉంచాలని నిర్ధారించుకోండి.",
            "nirdesh": "• Shift + F2: - స్క్రిప్ట్ రైటర్‌ను నేరుగా తెరవడానికి &amp; • Windows + Esc: - అప్లికేషన్‌ను మూసివేయడానికి\nAssistant ప్రస్తుత స్థానంలో రైటింగ్ అసిస్టెంట్ చూపబడతారు.\nRed ఆప్షన్ బార్ నుండి ముందే నిర్వచించిన ఎంపికలను సెట్ చేయవచ్చు. ఉదాహరణ - ముందే నిర్వచించిన రచనా భాష.\n• విండోస్ + ఎఫ్ 5: ధ్వనిని తగ్గించండి &amp; విండోస్ + ఎఫ్ 6: వాల్యూమ్ పెంచండి"
        },
        "menu_values": {
            "sahayika": "రైటింగ్ అసిస్టెంట్",
            "about": "పరిచయం",
            "encoding_table": "మార్పు జాబితాను చూడండి",
            "normal_version": "సాధారణ సంస్కరణను తెరవండి (స్క్రిప్ట్ ఛేంజర్)",
            "typing_lang": "భాష రాయడం",
            "default": "ముందుగా నిర్ణయించిన ఎంపిక సెట్టింగ్",
            "startup": "అప్లికేషన్ ప్రారంభంలో ఈ సెల్‌ను తెరవండి",
            "extra": "ఇతర నిర్దిష్ట సమాచారం"
        },
        "on": "పై",
        "off": "మూసివేయబడింది",
        "yes": "అవును",
        "no": "లేదు",
        "turned_on": "ఆన్ చేయబడింది",
        "turned_off": "మూసివేయబడింది",
        "sahayika_on": "రైటింగ్ అసిస్టెంట్ ఆన్ చేశారు",
        "sahayika_off": "రైటింగ్ అసిస్టెంట్ ఆపివేయబడింది",
        "startup_msg": "స్క్రిప్ట్ రచయిత\nఅప్లికేషన్: {0}\nరైటింగ్ అసిస్టెంట్: {1}\nస్క్రిప్ట్ రాయడం: {2}\n{3}\nఅప్లికేషన్ తెరవడానికి Shift + F2 నొక్కండి.",
        "hide2": "స్క్రిప్ట్ రచయిత ఇప్పటికీ పరోక్షంగా పనిచేస్తున్నారు.\nటాస్క్‌బార్‌ను పెయింటర్ నుండి నియంత్రించవచ్చు",
        "typ_lang_change": "వ్రాసే భాష {0 to కు మార్చబడింది",
        "lang": "భాష",
        "anuprayog": "అప్లికేషన్",
        "exit_msg": "స్క్రిప్ట్ రచయిత మూసివేయబడింది",
        "time_exceed": "స్క్రిప్ట్ రైటర్ తొలగించారు\nఎందుకంటే ఇది 10 నిమిషాలు అనుచితంగా ఉంది.",
        "sahAyikA_msg": {
            "first_sahayika": "వాటి క్రింద ఉన్న అక్షరాలను వ్రాయడానికి నల్ల అక్షరాలను నొక్కండి.\nq లేదా; పునరుద్ధరించడానికి నొక్కండి.",
            "second_sahayika": "క్యాప్స్‌లాక్‌కు బదులుగా షిఫ్ట్ కూడా నొక్కవచ్చు. ఉదాహరణ: Shift + a➠A"
        },
        "scripts": {
            "Hindi": "హిందీ",
            "Bengali": "బెంగాలీ",
            "Telugu": "తెలుగు",
            "Tamil": "తమిళం",
            "Tamil-Extended": "విస్తరించిన-తమిళం",
            "Marathi": "జెండా",
            "Gujarati": "గుజరాతీ",
            "Sinhala": "సింహళ",
            "Sanskrit": "సంస్కృతం",
            "Malayalam": "మలయాళం",
            "Kannada": "కన్నడ",
            "Oriya": "ఒరియా",
            "Konkani": "కొంకణి",
            "Assamese": "అస్సామీ",
            "Nepali": "నేపాలీ",
            "Punjabi": "పంజాబీ",
            "Urdu": "ఉర్దూ",
            "Kashmiri": "కష్మెరె",
            "Romanized": "రోమనైజ్ చేయబడింది",
            "Sharada": "శారద",
            "Modi": "మోడీ",
            "Brahmi": "బ్రహ్మి",
            "Siddham": "సిద్ధం",
            "Granth": "మంజూరు"
        },
        "download_msg": "స్క్రిప్ట్‌రైటర్ యొక్క క్రొత్త సంస్కరణ అందుబాటులో ఉంది!\nమీరు క్రొత్త సంస్కరణకు నవీకరించాలనుకుంటున్నారా?",
        "tray": {
            "show": "అప్లికేషన్ సెల్ చూపించు",
            "exit": "అప్లికేషన్ మూసివేయండి",
            "title": "స్క్రిప్ట్ రచయిత {0}\nరచనా భాష: {1}\nరైటింగ్ అసిస్టెంట్: {2}",
            "restart": "స్క్రిప్ట్‌ను పున art ప్రారంభించండి",
            "restarted": "స్క్రిప్ట్ ప్రారంభించబడింది"
        },
        "title": {
            "usage": "మార్పు జాబితా మరియు ఇతర సూచనలను చూడండి",
            "app_lang_img": "అప్లికేషన్ యొక్క భాషను సెట్ చేయండి",
            "app_lang_option": "అప్లికేషన్ యొక్క భాషను సెట్ చేయండి",
            "typ_lang": "సెట్టింగ్ రైటింగ్ లాంగ్వేజ్",
            "background": "టాస్క్‌బార్ చిత్రకారుడు మరియు చిన్న ప్రమాణాల ద్వారా పరోక్షంగా ఉపయోగించండి",
            "main0": "స్క్రిప్ట్ రచయిత ప్రారంభించండి",
            "main1": "దగ్గరి స్క్రిప్ట్ రచయిత",
            "sahayika0": "రాయడం సహాయకుడిని ప్రారంభించండి",
            "sahayika1": "క్లోజ్ రైటింగ్ అసిస్టెంట్",
            "menu": "ముందే నిర్వచించిన ఎంపికలు మరియు మరిన్ని సెట్ చేయండి"
        }
    },
    "ಕನ್ನಡ": {
        "app_title": "ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರ",
        "about_title": "ಪರಿಚಯ",
        "licence_title": "ಆದೇಶ",
        "values": {
            "sahayika": "ಬರವಣಿಗೆ ಸಹಾಯಕ",
            "app_description": "ಈ ಅಪ್ಲಿಕೇಶನ್ ಭಾರತೀಯ ಭಾಷೆಗಳನ್ನು ಪೂರ್ಣ ವೇಗ ಮತ್ತು ನಿಖರತೆಯಿಂದ ಬರೆಯುವುದಕ್ಕಾಗಿ ಆಗಿದೆ.\nಹೆಚ್ಚಿನ ಸಂಬಂಧಿತ ಮಾಹಿತಿಗಾಗಿ lipilekhika.com ಗೆ ಭೇಟಿ ನೀಡಿ.",
            "typing_lang_main": "ಭಾಷೆ ಬರೆಯುವುದು",
            "background_run": "ಪರೋಕ್ಷವಾಗಿ ಚಲಾಯಿಸಿ",
            "version": "ಆವೃತ್ತಿ ಸಂಖ್ಯೆ: {0}",
            "licence": "ಆಜ್ಞೆಯನ್ನು ತೋರಿಸಿ",
            "pin_top": "ಮೇಲ್ಭಾಗವನ್ನು ಸ್ಥಾಪಿಸಿ",
            "instructions": "• Windows + Ctrl: - ಆನ್ / ಆಫ್ ಮಾಡಲು\n(. (ಡಾಟ್): - ಸಂಖ್ಯೆಗಳು, ಪ್ರಮಾಣಗಳು ಮತ್ತು ಇತರ ವಿಶೇಷ ಚಿಹ್ನೆಗಳಿಗಾಗಿ\n• ಆಲ್ಟ್ 1 ಸೆಕೆಂಡ್: - ಪ್ರಸ್ತುತ ಆಯ್ಕೆಗಳನ್ನು ವೀಕ್ಷಿಸಲು\nAssistant ಸ್ಥಳದಲ್ಲಿ ಬರವಣಿಗೆ ಸಹಾಯಕನನ್ನು ತೋರಿಸಲಾಗುತ್ತದೆ",
            "vishisht_label": "ಈ ಸ್ಕ್ರಿಪ್ಟ್ ಲೇಖಕರ ನಿರ್ದಿಷ್ಟ ಆವೃತ್ತಿಯಾಗಿದೆ.\nಇದು ಮೂಲಕ್ಕಿಂತ ಭಿನ್ನವಾಗಿರಬಹುದು.",
            "vishisht_button": "ಸ್ಥಳೀಯ ಅಪ್ಲಿಕೇಶನ್ ತೆರೆಯಿರಿ",
            "sUchI_msg": "ಕೆಳಗೆ ನೀಡಲಾದ ಅಕ್ಷರಗಳನ್ನು ಬೇರೆ ರೀತಿಯಲ್ಲಿ ಬರೆಯಬಹುದು.\nಇನ್ನಷ್ಟು ತಿಳಿಯಲು ಬರವಣಿಗೆ ಸಹಾಯಕರನ್ನು ಇರಿಸಿಕೊಳ್ಳಲು ಮರೆಯದಿರಿ.",
            "nirdesh": "• ಶಿಫ್ಟ್ + ಎಫ್ 2: - ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರನನ್ನು ನೇರವಾಗಿ ತೆರೆಯಲು &amp; • ವಿಂಡೋಸ್ + ಎಸ್ಸಿ: - ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಮುಚ್ಚಲು\nAssistant ಪ್ರಸ್ತುತ ಸ್ಥಳದಲ್ಲಿ ಬರವಣಿಗೆ ಸಹಾಯಕವನ್ನು ತೋರಿಸಲಾಗುತ್ತದೆ.\nRed ಆಯ್ಕೆಯ ಪಟ್ಟಿಯಿಂದ ಪೂರ್ವನಿರ್ಧರಿತ ಆಯ್ಕೆಗಳನ್ನು ಹೊಂದಿಸಬಹುದು. ಉದಾಹರಣೆ - ಪೂರ್ವನಿರ್ಧರಿತ ಬರವಣಿಗೆ ಭಾಷೆ.\n• ವಿಂಡೋಸ್ + ಎಫ್ 5: ಧ್ವನಿ ಮತ್ತು ವಿಂಡೋಸ್ + ಎಫ್ 6 ಅನ್ನು ಕಡಿಮೆ ಮಾಡಿ: ಪರಿಮಾಣವನ್ನು ಹೆಚ್ಚಿಸಿ"
        },
        "menu_values": {
            "sahayika": "ಬರವಣಿಗೆ ಸಹಾಯಕ",
            "about": "ಪರಿಚಯ",
            "encoding_table": "ಬದಲಾವಣೆ ಪಟ್ಟಿಯನ್ನು ವೀಕ್ಷಿಸಿ",
            "normal_version": "ಸಾಮಾನ್ಯ ಆವೃತ್ತಿಯನ್ನು ತೆರೆಯಿರಿ (ಸ್ಕ್ರಿಪ್ಟ್ ಚೇಂಜರ್)",
            "typing_lang": "ಭಾಷೆ ಬರೆಯುವುದು",
            "default": "ಪೂರ್ವನಿರ್ಧರಿತ ಆಯ್ಕೆ ಸೆಟ್ಟಿಂಗ್",
            "startup": "ಅಪ್ಲಿಕೇಶನ್‌ನ ಪ್ರಾರಂಭದಲ್ಲಿ ಈ ಕೋಶವನ್ನು ತೆರೆಯಿರಿ",
            "extra": "ಇತರ ನಿರ್ದಿಷ್ಟ ಮಾಹಿತಿ"
        },
        "on": "ಆನ್",
        "off": "ಮುಚ್ಚಲಾಗಿದೆ",
        "yes": "ಹೌದು",
        "no": "ಇಲ್ಲ",
        "turned_on": "ಆನ್ ಮಾಡಲಾಗಿದೆ",
        "turned_off": "ಮುಚ್ಚಿತು",
        "sahayika_on": "ಬರವಣಿಗೆ ಸಹಾಯಕ ಆನ್ ಮಾಡಲಾಗಿದೆ",
        "sahayika_off": "ಬರವಣಿಗೆ ಸಹಾಯಕ ಆಫ್ ಮಾಡಲಾಗಿದೆ",
        "startup_msg": "ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರ\nಅಪ್ಲಿಕೇಶನ್: {0}\nಬರವಣಿಗೆ ಸಹಾಯಕ: {1}\nಸ್ಕ್ರಿಪ್ಟ್ ಬರೆಯುವುದು: {2}\n{3}\nಅಪ್ಲಿಕೇಶನ್ ತೆರೆಯಲು Shift + F2 ಒತ್ತಿರಿ.",
        "hide2": "ಚಿತ್ರಕಥೆ ಬರೆಯುವವರು ಇನ್ನೂ ಪರೋಕ್ಷವಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತಿದ್ದಾರೆ.\nಟಾಸ್ಕ್ ಬಾರ್ ಅನ್ನು ಪೇಂಟರ್ ನಿಂದ ನಿಯಂತ್ರಿಸಬಹುದು",
        "typ_lang_change": "ಬರೆಯುವ ಭಾಷೆಯನ್ನು {0 to ಗೆ ಬದಲಾಯಿಸಲಾಗಿದೆ",
        "lang": "ಭಾಷೆ",
        "anuprayog": "ಅಪ್ಲಿಕೇಶನ್",
        "exit_msg": "ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರ ಮುಚ್ಚಲಾಗಿದೆ",
        "time_exceed": "ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರನನ್ನು ವಜಾ ಮಾಡಲಾಯಿತು\nಏಕೆಂದರೆ ಇದು 10 ನಿಮಿಷಗಳ ಕಾಲ ಸೂಕ್ತವಲ್ಲ.",
        "sahAyikA_msg": {
            "first_sahayika": "ಕೆಳಗಿನ ಅಕ್ಷರಗಳನ್ನು ಬರೆಯಲು ಕಪ್ಪು ಅಕ್ಷರಗಳನ್ನು ಒತ್ತಿರಿ.\nq ಅಥವಾ; ಪುನರುಜ್ಜೀವನಗೊಳಿಸಲು ಒತ್ತಿರಿ.",
            "second_sahayika": "ಕ್ಯಾಪ್ಸ್‌ಲಾಕ್ ಬದಲಿಗೆ ಶಿಫ್ಟ್ ಅನ್ನು ಸಹ ಒತ್ತಬಹುದು. ಉದಾಹರಣೆ: ಶಿಫ್ಟ್ + a➠A"
        },
        "scripts": {
            "Hindi": "ಹಿಂದಿ",
            "Bengali": "ಬಂಗಾಳಿ",
            "Telugu": "ತೆಲುಗು",
            "Tamil": "ತಮಿಳು",
            "Tamil-Extended": "ವಿಸ್ತರಿತ-ತಮಿಳು",
            "Marathi": "ಧ್ವಜ",
            "Gujarati": "ಗುಜರಾತಿ",
            "Sinhala": "ಸಿಂಹಳ",
            "Sanskrit": "ಸಂಸ್ಕೃತ",
            "Malayalam": "ಮಲಯಾಳಂ",
            "Kannada": "ಕನ್ನಡ",
            "Oriya": "ಒರಿಯಾ",
            "Konkani": "ಕೊಂಕಣಿ",
            "Assamese": "ಅಸ್ಸಾಮೀಸ್",
            "Nepali": "ನೇಪಾಳಿ",
            "Punjabi": "ಪಂಜಾಬಿ",
            "Urdu": "ಉರ್ದು",
            "Kashmiri": "ಕ್ಯಾಶ್ಮೀರ್",
            "Romanized": "ರೋಮಾನೈಸ್ಡ್",
            "Sharada": "ಶಾರದಾ",
            "Modi": "ಮೋದಿ",
            "Brahmi": "ಬ್ರಾಹ್ಮಿ",
            "Siddham": "ಸಿದ್ಧಮ್",
            "Granth": "ಅನುದಾನ"
        },
        "download_msg": "ಸ್ಕ್ರಿಪ್ಟ್‌ರೈಟರ್‌ನ ಹೊಸ ಆವೃತ್ತಿ ಲಭ್ಯವಿದೆ!\nಹೊಸ ಆವೃತ್ತಿಗೆ ನವೀಕರಿಸಲು ನೀವು ಬಯಸುವಿರಾ?",
        "tray": {
            "show": "ಅಪ್ಲಿಕೇಶನ್ ಸೆಲ್ ತೋರಿಸಿ",
            "exit": "ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಮುಚ್ಚಿ",
            "title": "ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರ {0}\nಬರವಣಿಗೆ ಭಾಷೆ: {1}\nಬರವಣಿಗೆ ಸಹಾಯಕ: {2}",
            "restart": "ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ",
            "restarted": "ಸ್ಕ್ರಿಪ್ಟ್ ಸಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ"
        },
        "title": {
            "usage": "ಬದಲಾವಣೆ ಪಟ್ಟಿ ಮತ್ತು ಇತರ ಸೂಚನೆಗಳನ್ನು ವೀಕ್ಷಿಸಿ",
            "app_lang_img": "ಅಪ್ಲಿಕೇಶನ್‌ನ ಭಾಷೆಯನ್ನು ಹೊಂದಿಸಿ",
            "app_lang_option": "ಅಪ್ಲಿಕೇಶನ್‌ನ ಭಾಷೆಯನ್ನು ಹೊಂದಿಸಿ",
            "typ_lang": "ಬರವಣಿಗೆಯ ಭಾಷೆಯನ್ನು ಹೊಂದಿಸಿ",
            "background": "ಟಾಸ್ಕ್ ಬಾರ್ ವರ್ಣಚಿತ್ರಕಾರ ಮತ್ತು ಸಣ್ಣ ಮಾಪಕಗಳ ಮೂಲಕ ಪರೋಕ್ಷವಾಗಿ ಬಳಸಿ",
            "main0": "ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರನನ್ನು ಪ್ರಾರಂಭಿಸಿ",
            "main1": "ನಿಕಟ ಸ್ಕ್ರಿಪ್ಟ್ ಬರಹಗಾರ",
            "sahayika0": "ಬರವಣಿಗೆ ಸಹಾಯಕನನ್ನು ಆನ್ ಮಾಡಿ",
            "sahayika1": "ನಿಕಟ ಬರವಣಿಗೆ ಸಹಾಯಕ",
            "menu": "ಪೂರ್ವನಿರ್ಧರಿತ ಆಯ್ಕೆಗಳು ಮತ್ತು ಹೆಚ್ಚಿನದನ್ನು ಹೊಂದಿಸಿ"
        }
    },
    "বাংলা": {
        "app_title": "স্ক্রিপ্ট লেখক",
        "about_title": "ভূমিকা",
        "licence_title": "ম্যান্ডেট",
        "values": {
            "sahayika": "রাইটিং সহায়ক",
            "app_description": "এই অ্যাপ্লিকেশনটি সম্পূর্ণ গতি এবং নির্ভুলতার সাথে ভারতীয় ভাষাগুলি লেখার জন্য।\nআরও সম্পর্কিত তথ্যের জন্য ভিজিট করুন lipilekhika.com।",
            "typing_lang_main": "লেখার ভাষা",
            "background_run": "পরোক্ষভাবে চালান",
            "version": "সংস্করণ সংখ্যা: {0}",
            "licence": "কমান্ড প্রদর্শন",
            "pin_top": "শীর্ষ ইনস্টল করুন",
            "instructions": "• উইন্ডোজ + সিটিআরএল: - চালু / বন্ধ করতে\n• (বিন্দু): - সংখ্যা, পরিমাণ এবং অন্যান্য বিশেষ চিহ্নগুলির জন্য\n• Alt 1 সেকেন্ড: - বর্তমান বিকল্পগুলি দেখতে\n• লিখিত সহকারী লোকেশন প্রদর্শিত হবে",
            "vishisht_label": "এই স্ক্রিপ্টটি লেখকের নির্দিষ্ট সংস্করণ।\nএটি মূল থেকে আলাদা হতে পারে।",
            "vishisht_button": "নেটিভ অ্যাপ্লিকেশন খুলুন",
            "sUchI_msg": "নীচে দেওয়া অক্ষরগুলি অন্য উপায়ে লেখা যেতে পারে।\nআরও শিখতে লেখার সহায়ককে নিশ্চিত রাখুন।",
            "nirdesh": "Ift শিফট + এফ 2: - স্ক্রিপ্ট লেখক সরাসরি খুলতে &amp; • উইন্ডোজ + এস্কি: - অ্যাপ্লিকেশনটি বন্ধ করতে\nWriting লেখক সহকারী বর্তমান অবস্থানে প্রদর্শিত হবে।\nOption অপশন বার থেকে পূর্বনির্ধারিত বিকল্পগুলি সেট করা যেতে পারে। উদাহরণ - পূর্বনির্ধারিত লেখার ভাষা।\n• উইন্ডোজ + এফ 5: শব্দ এবং উইন্ডোজ + এফ 6 হ্রাস করুন: ভলিউম বৃদ্ধি করুন"
        },
        "menu_values": {
            "sahayika": "রাইটিং সহায়ক",
            "about": "ভূমিকা",
            "encoding_table": "পরিবর্তন তালিকা দেখুন",
            "normal_version": "সাধারণ সংস্করণ খুলুন (স্ক্রিপ্ট চেঞ্জার)",
            "typing_lang": "লেখার ভাষা",
            "default": "পূর্বনির্ধারিত বিকল্প সেটিংস",
            "startup": "অ্যাপ্লিকেশন শুরুতে এই ঘরটি খুলুন",
            "extra": "অন্যান্য নির্দিষ্ট তথ্য"
        },
        "on": "চালু",
        "off": "বন্ধ",
        "yes": "হ্যাঁ",
        "no": "না",
        "turned_on": "চালু",
        "turned_off": "বন্ধ আছে",
        "sahayika_on": "লেখা সহকারী চালু",
        "sahayika_off": "লেখা সহকারী বন্ধ",
        "startup_msg": "স্ক্রিপ্ট লেখক চালু\nঅ্যাপ্লিকেশন: {0}\nরাইটিং অ্যাসিস্ট্যান্ট: {1}\nলিখন লিখন: {2}\n{3\nঅ্যাপ্লিকেশনটি খুলতে শিফট + এফ 2 টিপুন।",
        "hide2": "স্ক্রিপ্ট লেখক এখনও অপ্রত্যক্ষভাবে কাজ করছেন।\nটাস্কবারকে পেইন্টার থেকে নিয়ন্ত্রণ করা যায়",
        "typ_lang_change": "লেখার ভাষা {0 to এ পরিবর্তিত হয়েছে",
        "lang": "ভাষা",
        "anuprayog": "প্রয়োগ",
        "exit_msg": "স্ক্রিপ্ট লেখক বন্ধ",
        "time_exceed": "স্ক্রিপ্ট লেখক বরখাস্ত করা হয়েছিল\nকারণ এটি 10 ​​মিনিটের জন্য অনুপযুক্ত ছিল।",
        "sahAyikA_msg": {
            "first_sahayika": "তাদের নীচে বর্ণগুলি লিখতে কালো বর্ণগুলি টিপুন।\nq বা; পুনরুদ্ধার করতে টিপুন।",
            "second_sahayika": "ক্যাপসলকের পরিবর্তে শিফটটিও চাপ দেওয়া যায়। উদাহরণ: শিফট + এ.এ.এ."
        },
        "scripts": {
            "Hindi": "হিন্দি",
            "Bengali": "বাংলা",
            "Telugu": "তেলেগু",
            "Tamil": "তামিল",
            "Tamil-Extended": "প্রসারিত-তামিল",
            "Marathi": "পতাকা",
            "Gujarati": "গুজরাটি",
            "Sinhala": "সিংহলা",
            "Sanskrit": "সংস্কৃত",
            "Malayalam": "মালায়ালাম",
            "Kannada": "কান্নাডা",
            "Oriya": "ওড়িয়া",
            "Konkani": "কোঙ্কানি",
            "Assamese": "অসমীয়া",
            "Nepali": "নেপালি",
            "Punjabi": "পাঞ্জাবি",
            "Urdu": "উর্দু",
            "Kashmiri": "কাশ্মির",
            "Romanized": "রোমানাইজড",
            "Sharada": "শারদা",
            "Modi": "মোডি",
            "Brahmi": "ব্রাহ্মী",
            "Siddham": "সিদ্ধাম",
            "Granth": "প্রদান"
        },
        "download_msg": "স্ক্রিপ্ট রাইটারের নতুন সংস্করণ উপলব্ধ!\nআপনি কি নতুন সংস্করণে আপডেট করতে চান?",
        "tray": {
            "show": "অ্যাপ্লিকেশন সেল প্রদর্শন করুন",
            "exit": "অ্যাপ্লিকেশন বন্ধ করুন",
            "title": "স্ক্রিপ্ট লেখক {0}\nলেখার ভাষা: {1}\nরাইটিং সহকারী: {2",
            "restart": "স্ক্রিপ্ট পুনরায় আরম্ভ করুন",
            "restarted": "স্ক্রিপ্ট সক্ষম"
        },
        "title": {
            "usage": "পরিবর্তন তালিকা এবং অন্যান্য নির্দেশাবলী দেখুন",
            "app_lang_img": "অ্যাপ্লিকেশনটির ভাষা নির্ধারণ করুন",
            "app_lang_option": "অ্যাপ্লিকেশনটির ভাষা নির্ধারণ করুন",
            "typ_lang": "লেখার ভাষা সেট করুন",
            "background": "টাস্কবার পেইন্টার এবং ছোট স্কেলগুলির মাধ্যমে অপ্রত্যক্ষভাবে ব্যবহার করুন",
            "main0": "স্ক্রিপ্ট লেখক শুরু করুন",
            "main1": "বন্ধ স্ক্রিপ্ট লেখক",
            "sahayika0": "লেখক সহকারী চালু করুন",
            "sahayika1": "বন্ধ লেখার সহায়ক",
            "menu": "পূর্বনির্ধারিত বিকল্পগুলি এবং আরও অনেক কিছু সেট করুন"
        }
    }
}
#lang_db_here
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
