from googletrans import Translator
def translate(phrase, target_language="en"):
    translator = Translator()

    try:
        translation = translator.translate(phrase, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return phrase

user_phrase = input("Enter a phrase: ")
user_language = input("Enter the target language code (e.g., en for English, es for Spanish, fr for French): ")

translated_phrase = translate(user_phrase, user_language)
print("Translated phrase:", translated_phrase)
