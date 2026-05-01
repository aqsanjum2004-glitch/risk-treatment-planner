from services.chroma_client import add_document

# 10 domain knowledge documents for Risk Treatment Planner
documents = [
    {
        "id": "doc_001",
        "text": "Data breach risk management involves implementing strong encryption, access controls, and regular security audits. Organizations should have an incident response plan ready to minimize damage when breaches occur.",
        "source": "Cybersecurity Risk Management Guide"
    },
    {
        "id": "doc_002",
        "text": "Operational risk includes risks from inadequate internal processes, people, systems, or external events. Key mitigation strategies include process documentation, staff training, and business continuity planning.",
        "source": "Operational Risk Framework"
    },
    {
        "id": "doc_003",
        "text": "Regulatory compliance risk arises when organizations fail to comply with laws and regulations. Regular compliance audits, legal reviews, and staff training are essential mitigation measures.",
        "source": "Compliance Risk Management"
    },
    {
        "id": "doc_004",
        "text": "Financial risk management involves identifying and managing risks that could impact an organization's financial health. Key strategies include diversification, hedging, and maintaining adequate cash reserves.",
        "source": "Financial Risk Management Guide"
    },
    {
        "id": "doc_005",
        "text": "Third party vendor risk management requires thorough due diligence before engaging vendors, regular performance monitoring, and having backup vendors for critical services.",
        "source": "Vendor Risk Management"
    },
    {
        "id": "doc_006",
        "text": "Business continuity planning ensures organizations can continue operating during and after a disaster. Key components include risk assessment, recovery strategies, and regular testing of the plan.",
        "source": "Business Continuity Planning Guide"
    },
    {
        "id": "doc_007",
        "text": "Cybersecurity risk treatment involves implementing technical controls like firewalls and intrusion detection systems, administrative controls like security policies, and physical controls like access restrictions.",
        "source": "Cybersecurity Controls Framework"
    },
    {
        "id": "doc_008",
        "text": "Risk appetite defines the amount of risk an organization is willing to accept in pursuit of its objectives. It should be clearly defined by senior management and communicated throughout the organization.",
        "source": "Risk Appetite Framework"
    },
    {
        "id": "doc_009",
        "text": "Risk assessment is the process of identifying, analyzing, and evaluating risks. It involves determining the likelihood and impact of each risk and prioritizing them for treatment.",
        "source": "Risk Assessment Methodology"
    },
    {
        "id": "doc_010",
        "text": "Risk treatment options include risk avoidance, risk reduction, risk sharing, and risk acceptance. The choice of treatment depends on the risk appetite, cost of treatment, and potential impact.",
        "source": "Risk Treatment Options Guide"
    }
]

def seed():
    print("Seeding ChromaDB with 10 domain knowledge documents...")
    for doc in documents:
        try:
            add_document(
                doc_id=doc["id"],
                text=doc["text"],
                metadata={"source": doc["source"]}
            )
            print(f"✅ Added: {doc['source']}")
        except Exception as e:
            print(f"❌ Error adding {doc['source']}: {e}")
    print("\nSeeding complete! ChromaDB now has 10 documents.")

if __name__ == "__main__":
    seed()