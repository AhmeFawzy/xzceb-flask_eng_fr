import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an authenticator object with your API key
authenticator = IAMAuthenticator(apikey)

# Create a Language Translator instance using the authenticator and service URL
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    if not englishText:
        return None
    translation = language_translator.translate(
        text=englishText,
        source="en",
        target="fr"
    ).get_result()

    # Extract the translated text and return it
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    if not frenchText:
        return None
    translation = language_translator.translate(
        text=frenchText,
        source="fr",
        target="en"
    ).get_result()

    # Extract the translated text and return it
    englishText = translation['translations'][0]['translation']
    return englishText
