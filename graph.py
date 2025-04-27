from langchain.graphs import Neo4jGraph
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
load_dotenv()
import os
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
# Initialize components
graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USER, password=NEO4J_PASSWORD)
llm = OllamaLLM(model="llama3.1:latest")