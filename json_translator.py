# Credits: Leonardo Rignanese (twitter.com/leorigna)

import openai
import json
import os
import concurrent.futures
from config import API_KEY

# Set up OpenAI API credentials (https://beta.openai.com/docs/developer-quickstart/your-api-keys)
openai.api_key = API_KEY

# Set up target languages for translation
languages = ["it-IT", "en-US", "fr-FR", "es-ES", "de-DE", "pt-PT", "nl-NL", "ru-RU",    "pl-PL", "tr-TR", "zh-CN", "ja-JP", "ko-KR", "ar-AR", "hi-IN", "sv-SE",    "no-NO", "fi-FI", "da-DK", "cs-CZ",
             "sk-SK", "hu-HU", "ro-RO", "uk-UA",    "bg-BG", "hr-HR", "sr-SP", "sl-SI", "et-EE", "lv-LV", "lt-LT",    "he-IL", "fa-IR", "ur-PK", "bn-IN", "ta-IN", "te-IN", "mr-IN", "ml-IN",    "th-TH", "vi-VN"]


# Prompt user to enter the path to the input JSON file
input_path = input("Enter the path to the source JSON file: ")
print(f"Reading input file from {input_path}")

# Load JSON file with language translations as a single string
with open(input_path, "r") as f:
    json = f.read()

# Define function to translate text for a given target language
def translate(target_language):
    print(f"Translating to {target_language}...")
    # Call OpenAI API to translate text
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are TranslatorGpt, a powerful language model designed for seamless translation of text across multiple languages. You have been trained on a vast corpus of linguistic data and possess a deep understanding of grammar, syntax, and vocabulary. You excel at generating structured data in JSON format, adhering to best practices such as escaping special characters to avoid breaking the JSON, and using double quotes only. Additionally, you never include an extra comma at the end of the last row in the JSON.",
            },
            {
                "role": "user",
                "content": f"Translate the following JSON to {target_language}:\n\n{json}\n",
            },
        ],
    )

    translated_json = completion["choices"][0]["message"]["content"]
    print(f"Translation to {target_language} complete.")
    return target_language, translated_json


# Translate the JSON string into target languages
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit translation tasks to the executor
    future_to_language = {
        executor.submit(translate, target_language): target_language
        for target_language in languages
    }
    # Process completed translation tasks and write output files
    for future in concurrent.futures.as_completed(future_to_language):
        target_language = future_to_language[future]
        filename = f"{target_language}.json"
        try:
            res = future.result()
            output_path = os.path.join(os.path.dirname(input_path), filename)
            with open(output_path, "w") as f:
                f.write(res[1])
            print(f"Output file saved as {output_path}")
        except Exception as e:
            print(
                f"Error occurred while translating to {target_language}: {e}")

print("Translation complete.")

# Credits: Leonardo Rignanese (twitter.com/leorigna)
