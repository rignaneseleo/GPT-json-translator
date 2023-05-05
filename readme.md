# GPT JSON Translator

This script is a Python program that uses the OpenAI API to translate a JSON file into multiple target languages. The script prompts the user to enter the path to the source JSON file, which is then loaded as a single string. The user can then specify the target languages for translation from a list of supported languages.

## Dependencies
This script requires the following dependencies to be installed:
- openai (installation instructions can be found [here](https://github.com/openai/openai-python#installation))
- concurrent.futures (should be included in Python standard library)

## Usage
To use the script, you will need to have an OpenAI API key. You can follow the instructions [here](https://beta.openai.com/docs/developer-quickstart/your-api-keys) to obtain an API key.

Once you have obtained an API key, you can set it in the script by replacing the value of `openai.api_key` with your own API key.

To run the script, save it as `json_translator.py` and run the following command in the terminal:

```
python json_translator.py
```

Follow the prompts to enter the path to the input JSON file and select the target languages for translation.

The translated JSON files will be saved in the same directory as the input file with the language code as the filename extension (e.g. `it-IT.json`, `en-US.json`, etc.).

Note: This script uses OpenAI's GPT-3.5-Turbo model for translation, which may incur costs if you exceed the monthly free tier limit. Please refer to [OpenAI's pricing page](https://openai.com/pricing/) for more information on pricing.

## License
This script is released under the MIT License. See the LICENSE file for more information.