from flask import Flask, request, jsonify
import os
from langchain.retrievers.tavily_search_api import TavilySearchAPIRetriever
# Initialize Flask app
app = Flask(__name__)

# Set Tavily API key
os.environ["TAVILY_API_KEY"] = "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"

# Initialize Tavily retriever
retriever = TavilySearchAPIRetriever(k=3)

@app.route("/", methods=["GET"])
def index():
    return "Server is running"


@app.route("/query", methods=["POST"])
def query():
    # Get question from request
    question = request.json["question"]
    print(question)
    # Invoke Tavily retriever
    results = retriever.invoke(question)

    # Convert results to a list of dictionaries
    results_list = [result.dict() for result in results]

    # Return results as JSON response
    return jsonify(results=results_list)

if __name__ == "__main__":
    # Run Flask app
    app.run(host="0.0.0.0",debug=True)
import requests

url = "http://127.0.0.1:5000/query"
question = {"question": "where is next fifa world cup going to be"}
response = requests.post(url, json=question)

if response.ok:
    results = response.json()["results"]
    for result in results:
        print(result)
else:
    print("Error:", response.text)
