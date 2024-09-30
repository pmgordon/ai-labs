from langchain_core.tools import tool
from langchain_nomic.embeddings import NomicEmbeddings
from langchain_community.vectorstores import OpenSearchVectorSearch

import urllib3
urllib3.disable_warnings()


EMBEDDINGS = NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local")

VECTORSTORE = OpenSearchVectorSearch(
    "https://localhost:9200",
    "opensearch-self-query-demo",
    EMBEDDINGS,
    verify_certs=False,
    http_auth=('admin', 'bigStrongPassword124315'),
)


def get_opensearch_reteriver() -> OpenSearchVectorSearch:
    return VECTORSTORE
