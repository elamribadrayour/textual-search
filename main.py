"""Countries, Cities and States Api."""

from typing import List

from fastapi import FastAPI, Query

import nlp.preprocessing
import nlp.embedding

app = FastAPI()

@app.get("/clean/{text}")
async def get_cleaned(text: str) -> dict:
    return {"clean": nlp.preprocessing.get_cleaned(text)}


@app.get("/lemmatize/{text}")
async def get_lemmas(text: str) -> dict:
    return {"lemmas": nlp.preprocessing.get_lemmas(text)}


@app.get("/embeddings/")
async def get_embeddings(texts: List[str] = Query(None)) -> dict:
    embedding = nlp.embedding.get_embeddings(texts, type_="list")
    return {"embedding": embedding}



@app.get("/similarities/")
async def get_similarities(texts: List[str] = Query(None)) -> dict:
    return {"similarity": nlp.embedding.get_cosine_similarities(texts=texts)}
