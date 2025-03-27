import googletrans
from googletrans import Translator

def translate_text(text, target_language):
    """Translates text to the specified target language."""
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

def main():
    print("🌍 Language Translation Tool 🌍")
    print("Available languages:", list(googletrans.LANGUAGES.values()))

    text = input("Enter text to translate: ")
    target_language = input("Enter target language (e.g., 'fr' for French, 'es' for Spanish): ").lower()

    if target_language not in googletrans.LANGUAGES:
        print("❌ Invalid language code! Please enter a valid code.")
        return

    translated_text = translate_text(text, target_language)
    print(f"✅ Translated Text: {translated_text}")

if __name__ == "__main__":
    main()
