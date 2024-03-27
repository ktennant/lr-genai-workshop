# RAG pipeline with Ollama and Llama Index

## Install Prerequisites

```shell
pip install --upgrade pip
pip install --upgrade pipx
pipx install virtualenv
```

## Setup Environment

```shell
mkdir workshop1 && cd workshop1
virtualenv .venv
source .venv/bin/activate
```

## Create the App

```shell
ollama run gemma:2b
pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface
touch qa.py
```

In editor:

```python
import os.path
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
    Settings,
)

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="gemma:2b", request_timeout=60.0)


# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data(show_progress=True)
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

query = input("?: ")

query_engine = index.as_query_engine()
response = query_engine.query(query)
print(response)

```

```shell
python qa.py
```
