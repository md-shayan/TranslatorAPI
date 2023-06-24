import requests
import os # This is to import the API key hidden in the environment variables.

'''A dictionary that contains the supporting languages and their language code for reference. '''
LANGUAGE_CODES = {
    "Auto-detection": 'auto',
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chichewa": "ny",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Kurdish (Kurmanji)": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Odia (Oriya)": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu",
    "Hebrew": "he",
    "Chinese (Simplified)": "zh"
}

API_KEY = os.environ["RAPID_API_KEY"] # Your API key goes here.

URL = "https://text-translator2.p.rapidapi.com/translate"

while True:
    help = input("To generate the supporting languages and their codes type 'y' or 'exit' to end the program):")
    if help == "y":
        for key, value in LANGUAGE_CODES.items():
            print("Language:", key, "\nCode:", value)
    elif help == 'exit':
        break
    else:
        pass

    source_lang = input("Enter the text's language code (auto for auto detection): ")
    target_lang = input("Enter the language code of the language you want to translate the text to: ")

    if source_lang not in LANGUAGE_CODES.values() or target_lang not in LANGUAGE_CODES.values():
        print("Invalid/Unsupported language code\n")    
    else:
        text = input("Enter the text you want to translate: ")
        payload = {
	        "source_language": source_lang,
	        "target_language": target_lang,
	        "text": text
        }
        headers = {
	        "content-type": "application/x-www-form-urlencoded",
	        "X-RapidAPI-Key": API_KEY,
	        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
        }
        response = requests.post(URL, data=payload, headers=headers)
        data = response.json()['data']
        print("Here's the translated text...")
        print(data['translatedText'])
        print("\n")
