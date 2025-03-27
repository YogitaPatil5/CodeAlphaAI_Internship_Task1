import requests
from googletrans import Translator
from transformers import MarianMTModel, MarianTokenizer


# Google Translate API Function
def google_translate(text, src_lang='en', dest_lang='fr'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Google Translate Error: {e}"


# Microsoft Translator API Function
def microsoft_translate(text, src_lang='en', dest_lang='fr', api_key='', region=''):
    url = "https://api.cognitive.microsofttranslator.com/translate"
    headers = {
        'Ocp-Apim-Subscription-Key': api_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-Type': 'application/json'
    }
    params = {
        'api-version': '3.0',
        'from': src_lang,
        'to': dest_lang
    }
    body = [{'text': text}]
    try:
        response = requests.post(url, headers=headers, params=params, json=body)
        response.raise_for_status()
        result = response.json()
        return result[0]['translations'][0]['text']
    except Exception as e:
        return f"Microsoft Translate Error: {e}"


# Hugging Face MarianMT Model Translation
def huggingface_translate(text, src_lang='en', dest_lang='fr'):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{dest_lang}'
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**inputs)
        return tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception as e:
        return f"Hugging Face Translation Error: {e}"


# Main Translation Interface
def translate_text(text, src_lang='en', dest_lang='fr', method='google', api_key='', region=''):
    if method == 'google':
        return google_translate(text, src_lang, dest_lang)
    elif method == 'microsoft':
        return microsoft_translate(text, src_lang, dest_lang, api_key, region)
    elif method == 'huggingface':
        return huggingface_translate(text, src_lang, dest_lang)
    else:
        return "Invalid translation method selected."


# Example Usage
if __name__ == "__main__":
    text_to_translate = "Hello, how are you?"
    method = 'google'  # Options: google, microsoft, huggingface
    src_lang = 'en'
    dest_lang = 'fr'

    # API Key and Region for Microsoft Translator
    ms_api_key = "YOUR_MICROSOFT_API_KEY"
    ms_region = "YOUR_REGION"

    result = translate_text(text_to_translate, src_lang, dest_lang, method, ms_api_key, ms_region)
    print(f"Translated Text: {result}")
