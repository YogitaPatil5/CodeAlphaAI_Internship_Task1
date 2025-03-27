from googletrans import Translator, LANGUAGES

def translate_text(text: str, src_lang: str, dest_lang: str) -> str:
    """
    Translates text from source language to target language.
    
    :param text: Input text to translate
    :param src_lang: Source language code (e.g., 'en' for English)
    :param dest_lang: Destination language code (e.g., 'fr' for French)
    :return: Translated text
    """
    try:
        translator = Translator()
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

def get_language_codes():
    """Returns a dictionary of available language names and their codes."""
    return {name.capitalize(): code for code, name in LANGUAGES.items()}

# Test
if __name__ == "__main__":
    print(translate_text("Hello, world!", "en", "es"))  # English to Spanish
