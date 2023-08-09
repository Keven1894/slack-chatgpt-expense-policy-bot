from llama_index import GPTVectorStoreIndex, download_loader

SimpleWebPageReader = download_loader("SimpleWebPageReader")

loader = SimpleWebPageReader()
documents = loader.load_data(urls=['https://esriaustraliatechblog.wordpress.com/2021/02/18/authorising-arcgis-desktop-arcmap-single-use/'])
index = GPTVectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is the topic of the site?")
print(response)
#index.query('What is the topic of the site?')

index.storage_context.persist()