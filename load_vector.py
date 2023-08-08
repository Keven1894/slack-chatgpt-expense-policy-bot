#Library Modules Needed: llama_index, pathlib, pypdf2
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)
from pathlib import Path
from llama_index import download_loader

PDFReader = download_loader("PDFReader")
loader = PDFReader()
documents = loader.load_data(file=Path("expense-policy.pdf"))
index = VectorStoreIndex.from_documents(documents)
#index.save_to_disk("expense-policy-index")
# by default, save to ./storage, 
# it also can be saved to assigned location by index.storage_context.persist(persist_dir="<persist_dir>")
index.storage_context.persist()