# Credits: Leonardo Rignanese (twitter.com/leorigna)

import openai
import json
import os
import concurrent.futures
from config import API_KEY, SOURCE_PATH

# Set up OpenAI API credentials (https://beta.openai.com/docs/developer-quickstart/your-api-keys)
openai.api_key = API_KEY

# Set up target languages for translation
languages = ["zh", "es", "en", "hi", "ar", "pt", "bn", "ru",
             "ja", "pa", "de", "jv", "fr", "te", "vi", "ko",
             "mr", "ta", "ur", "tr", "it", "th", "gu", "pl",
             "uk", "ro", "az", "id", "nl", "sw", "el", "cs",
             "hu", "he", "sv", "bg", "da", "no", "fi", "sk"]

# Prompt user to enter the path to the input JSON file
if (SOURCE_PATH):
    input_path = SOURCE_PATH
else:
    input_path = input("Enter the path to the source JSON file: ")
print(f"Reading input file from {input_path}")

# Load JSON file with language translations as a single string
with open(input_path, "r") as f:
    source_json = json.load(f)


# Define function to translate text for a given target language
def translate(target_language, rows_to_translate):
    print(f"Translating to {target_language}...")
    # Call OpenAI API to translate text
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are TranslatorGpt, a powerful language model designed for seamless translation of text across multiple languages. You have been trained on a vast corpus of linguistic data and possess a deep understanding of grammar, syntax, and vocabulary of every language in the world. You excel at generating structured data in JSON format and follow this rules: you never translate the key, you always use the double quotes to surround key and valye, you always escape single quotes and backslashes contained in the value, you never write a comma at the end of the last row in the file.",
            },
            {
                "role": "user",
                "content": f"Translate the following JSON to {target_language}:\n\n{rows_to_translate}\n",
            },
        ],
    )

    translated_json_str = completion["choices"][0]["message"]["content"]
    # only double quotes are allowed in JSON, so replace single quotes with double quotes
    translated_json_str = translated_json_str.replace("'", '"')
    print(f"Translation to {target_language} complete.")
    # print(f"Translated JSON:\n{translated_json}\n")
    # convert the string into a json object
    translated_json = json.loads(translated_json_str)
    return translated_json


# Translate the JSON string into target languages
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit translation tasks to the executor
    future_to_language = {}
    for target_language in languages:
        filename = f"{target_language}.json"
        output_path = os.path.join(os.path.dirname(input_path), filename)
        if os.path.exists(output_path):
            with open(output_path, "r") as f:
                try:
                    existing_json = json.load(f)
                except json.decoder.JSONDecodeError:
                    existing_json = {}
            existing_keys = "\n".join(existing_json.keys())
            missing_keys = set(source_json.keys()) - set(existing_json.keys())
            
            if missing_keys:
                print(
                f"Found {len(missing_keys)} missing keys for {target_language}")
                filtered_json = {
                    key: value for key, value in source_json.items() if key in missing_keys}
                # print(f"Filtered JSON:\n{filtered_json}\n")
                future_to_language[executor.submit(
                    translate, target_language, filtered_json)] = target_language, existing_json
        else:
            print(
                f"Output file not found for {target_language}. Generating a new one...")
            future_to_language[executor.submit(
                translate, target_language, source_json)] = target_language, {}

    # Process completed translation tasks and write output files
    for future in concurrent.futures.as_completed(future_to_language):
        target_language, existing_json = future_to_language[future]
        filename = f"{target_language}.json"
        translated_json=""
        try:
            translated_json = future.result()
            if existing_json:
                output_json = {**existing_json, **translated_json}
            else:
                output_json = json.loads(translated_json)
            output_path = os.path.join(os.path.dirname(input_path), filename)
            with open(output_path, "w") as f:
                json.dump(output_json, f, indent=2)
            print(f"Output file saved as {output_path}")
        except Exception as e:
            print(
                f"Error occurred while translating to {target_language}: {e}\n{translated_json}\n")

print("Translation complete.")

# Credits: Leonardo Rignanese (twitter.com/leorigna)
