from fastapi import FastAPI
from translation.main import load_all_translation_packages
from translation.languages import Languages
import argostranslate.translate

print("Loading translation packages")
translateService = load_all_translation_packages()

app = FastAPI()


@app.post("/translate")
async def translate(from_code: Languages, text: str):
    to_code = "en"

    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang = list(filter(lambda x: x.code == from_code, installed_languages))[0]
    to_lang = list(filter(lambda x: x.code == to_code, installed_languages))[0]
    translatedText = from_lang.get_translation(to_lang).translate(text)
    return {"translatedText": translatedText}
