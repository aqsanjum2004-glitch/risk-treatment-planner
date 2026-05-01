# ChromaDB mock for local development
# Real ChromaDB will work on demo machine

def add_document(doc_id, text, metadata={}):
    print(f"Document added: {doc_id}")
    return True

def query_documents(query_text, n_results=3):
    return {
        "documents": [[
            "Risk management best practices include implementing strong controls and regular audits.",
            "Cybersecurity risks should be mitigated through encryption and access controls.",
            "Compliance risks require regular monitoring and staff training."
        ]],
        "ids": [["doc_001", "doc_002", "doc_003"]]
    }

collection = type('obj', (object,), {'count': lambda self: 10})()