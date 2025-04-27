from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain_ollama import OllamaEmbeddings
from graph import *
embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

def retrieval():
 neo4j_graph_vectorbase = Neo4jVector.from_existing_graph(
    embedding=embeddings,
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="Game",
    node_label="Game",
    text_node_properties=[
        'Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales',
       'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Description'
       ],
    embedding_node_property="embedding",  
  )
 return neo4j_graph_vectorbase


vector_base = retrieval()
