from strands import Agent
from strands.memory import MemoryManager
from strands.vended_memory_stores.bedrock_knowledge_base import BedrockKnowledgeBaseStore

KNOWLEDGE_BASE_ID = "<Enter your Knowledge Base ID here>"

# 1. Initialize the correct store path and provide configuration details via a dict
kb_store = BedrockKnowledgeBaseStore(
    config={
        "knowledge_base_id": KNOWLEDGE_BASE_ID,
    },
    name="knowledge_base",
    writable=False
)

# 2. Assign the store inside the MemoryManager
memory_manager = MemoryManager(stores=[kb_store])

# 3. Correct parameter name: Use `memory_manager` instead of `memory`
agent = Agent(
    system_prompt="""You are a document-based Q&A assistant.
    When answering user questions, you must search for relevant information from the Knowledge Base before answering.
    Answer accurately based on the retrieved document content, and say you don't know if the information is not in the documents.""",
    memory_manager=memory_manager 
)

if __name__ == "__main__":
    response = agent("Please summarize the main content of the uploaded document.")
    print(response)
