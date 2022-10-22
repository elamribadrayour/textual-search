"""Embedding with sentence transformers"""

import torch
import torch.nn
from sentence_transformers import SentenceTransformer

file_path = "sentence-transformers/msmarco-distilroberta-base-v2"
model = SentenceTransformer(file_path)


def get_embeddings(texts: list, type_="list") -> list | torch.Tensor:

    if isinstance(texts, list) == False:
        return

    query_embeddings = model.encode(texts, convert_to_tensor=True)

    if type_ == "list":
        return query_embeddings.tolist()
    elif type_ == "tensor":
        return torch.unsqueeze(query_embeddings, 0)


def get_cosine_similarities(texts: list):
    embeddings = get_embeddings(texts, type_="tensor")
    
    cosine_similarities : list = list()

    length = embeddings.shape[1]
    for i in range(length):
        query = embeddings[:, i, :]
        queries = embeddings
        cosine_similarity = torch.nn.CosineSimilarity(dim=-1)(
            query,
            queries
        )
        cosine_similarity = torch.round(input=cosine_similarity, decimals=2)
        cosine_similarities.append(cosine_similarity.tolist())

    return cosine_similarities

