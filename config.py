# ++++ CONFIG ++++

# Set up OpenAI API credentials (https://beta.openai.com/docs/developer-quickstart/your-api-keys)
API_KEY = ""

# path of the english json file to translate
SOURCE_PATH = "/path/en.json"

# target languages for translation in the format "xx-XX" where "xx" is the language code and "XX" is the country code
TRANSLATE_TO = ["de-DE"]
# "it-IT", "en-US","fr-FR", "es-ES", "de-DE", "pt-PT", "pt-BR", "nl-NL", "ru-RU",    "pl-PL", "tr-TR", "zh-CN", "ja-JP", "ko-KR", "ar-AR", "hi-IN", "sv-SE", "no-NO", "fi-FI", "da-DK", "cs-CZ","sk-SK", "hu-HU", "ro-RO", "uk-UA",    "bg-BG", "hr-HR", "sr-SP", "sl-SI", "et-EE", "lv-LV", "lt-LT",    "he-IL", "fa-IR", "ur-PK", "bn-IN", "ta-IN", "te-IN", "mr-IN", "ml-IN", "th-TH", "vi-VN"


# ++++ ADVANCED SETTINGS ++++

# GPT model to use for translation
GPT_MODEL = "gpt-4-1106-preview"

# number of threads to use for parallel translation (1 = no parallelization)
MAX_THREADS = 1