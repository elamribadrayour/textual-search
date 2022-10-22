"""Embeddings and similarity api."""

from typing import List

from fastapi import FastAPI

import nlp.embedding
import nlp.preprocessing

app = FastAPI()


@app.get("/clean/{text}")
async def get_cleaned(text: str) -> dict:
    """Clean Text."""
    return {"clean": nlp.preprocessing.get_cleaned(text)}


@app.get("/lemmatize/{text}")
async def get_lemmas(text: str) -> dict:
    """Transform text words to lemmas."""
    return {"lemmas": nlp.preprocessing.get_lemmas(text)}


@app.get("/embeddings/")
async def get_embeddings(texts: List[str]) -> dict:
    """Get texts embeddings."""
    embedding = nlp.embedding.get_embeddings(texts, type_="list")
    return {"embedding": embedding}


@app.get("/similarities/")
async def get_similarities(texts: List[str]) -> dict:
    """Get texts similarities."""
    return {"similarity": nlp.embedding.get_cosine_similarities(texts=texts)}
