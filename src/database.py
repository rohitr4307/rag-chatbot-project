from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings

import warnings

warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module="langchain"
)

# Tokenizer / model warnings (Nemotron)
warnings.filterwarnings(
    "ignore",
    message=".*get_num_tokens_from_messages.*"
)

def create_or_load_index(chunks, index_path="faiss_index"):
    embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
    try:
        vectordb = FAISS.load_local(index_path, embeddings=embedding, allow_dangerous_deserialization=True)
        print("Loaded existing index.")
    except Exception as e:
        print("Creating new FAISS index...", e)
        for doc in chunks:
            if not isinstance(doc.page_content, str):
                doc.page_content = str(doc.page_content)
        vectordb = FAISS.from_documents(documents=chunks, embedding=embedding)
        vectordb.save_local(index_path)
        print("Created and saved new index.")
    return vectordb