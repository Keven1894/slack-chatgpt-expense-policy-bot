#Libary Modules needed for this script: slack_bolt, os, json, llama_index, openai
import os
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from llama_index import VectorStoreIndex
from llama_index import StorageContext, load_index_from_storage

# Initialize Slack App with the provided bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Load the GPT index from disk
#index = GPTSimpleVectorIndex.load_from_disk('expense-policy-index')
# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="storage")

# load index
index = load_index_from_storage(storage_context)

# Test the index with a query and print the result
query_engine = index.as_query_engine()
response = query_engine.query("Who are the main approvers for contractor expenses?")
print(response)
#print(index.query('Who are the main approvers for contractor expenses?'))

# Listens to any incoming messages
@app.message("")
def message_all(message, say):
    # Print the incoming message text
    print(message['text'])
    
    # Query the index with the message text and get a response
    text = message['text']
    query_engine = index.as_query_engine()
    response = query_engine.query(text)
    #response = index.query(text)
    
    # Extract the desired message and sources from the response object
    message = str(response)  # Convert the 'Response' object to a string
    sources = json.dumps(response.get_formatted_sources(length=100))
    
    # Print the message and sources and send them as a message back to the user
    print(message)
    print(sources)
    say(message + '\n\n' + sources)

# Start the Socket Mode handler
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
