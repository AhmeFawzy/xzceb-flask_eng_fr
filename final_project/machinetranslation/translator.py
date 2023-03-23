"""
Module for language translation using IBM Watson Language Translator.
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

# Create an authenticator object with your API key
AUTHENTICATOR = IAMAuthenticator(API_KEY)

# Create a Language Translator instance using the authenticator and service URL
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=AUTHENTICATOR
)
LANGUAGE_TRANSLATOR.set_service_url(URL)


def english_to_french(english_text):
    """
    Translate English text to French.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source="en",
        target="fr"
    ).get_result()

    # Extract the translated text and return it
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translate French text to English.
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source="fr",
        target="en"
    ).get_result()

    # Extract the translated text and return it
    english_text = translation['translations'][0]['translation']
    return english_text
