from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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

def load_and_split_pdf(folder_path):
    documents = []

    for path in folder_path:
        loader = PyPDFLoader(path)
        docs = loader.load()
        documents.extend(docs)

    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""],
        length_function=len,
        )
    chunks = text_splitter.split_documents(documents=documents)

    print(type(chunks[0]))
    # print(chunks[0])

    return chunks

# load_and_split_pdf()