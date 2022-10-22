"""Preprocessing with spacy."""

from functools import partial

import textacy
import textacy.extract.basics
import textacy.preprocessing
import textacy.preprocessing.replace
import textacy.spacier.core

textacy.load_spacy_lang("en_core_web_sm")

clean_pipeline = textacy.preprocessing.make_pipeline(
    partial(textacy.preprocessing.replace.user_handles, repl=""),
    partial(textacy.preprocessing.replace.currency_symbols, repl="_CUR_"),
    partial(textacy.preprocessing.replace.emails, repl=""),
    partial(textacy.preprocessing.replace.emojis, repl=""),
    partial(textacy.preprocessing.replace.hashtags, repl=""),
    partial(textacy.preprocessing.replace.numbers, repl=""),
    partial(textacy.preprocessing.replace.phone_numbers, repl=""),
    partial(textacy.preprocessing.replace.urls, repl=""),
    partial(textacy.preprocessing.replace.user_handles, repl=""),
)

remove_pipeline = textacy.preprocessing.make_pipeline(
    textacy.preprocessing.remove.brackets,
    textacy.preprocessing.remove.html_tags,
    textacy.preprocessing.remove.punctuation,
)

normalize_pipeline = textacy.preprocessing.make_pipeline(
    textacy.preprocessing.normalize.hyphenated_words,
    textacy.preprocessing.normalize.unicode,
    textacy.preprocessing.normalize.whitespace,
)

preprocessing_pipeline = textacy.preprocessing.make_pipeline(
    clean_pipeline,
    remove_pipeline,
    normalize_pipeline,
)


def get_cleaned(raw_text: str) -> str:
    """Clean text."""
    if isinstance(raw_text, str) is False:
        return []

    clean_text = preprocessing_pipeline(raw_text)
    clean_text = clean_text.lower()

    return clean_text


def get_lemmas(raw_text: str) -> list:
    """Get Lemmas."""
    if isinstance(raw_text, str) is False:
        return []

    clean_text = get_cleaned(raw_text=raw_text)
    document = textacy.spacier.core.make_spacy_doc(
        data=clean_text,
        lang=textacy.load_spacy_lang("en_core_web_sm"),
    )
    words = textacy.extract.basics.words(
        doclike=document,
        filter_stops=False,
        min_freq=1,
    )

    lemmas = list()
    for word in words:
        print(type(word))
        lemmas.append(word.text)

    return lemmas
