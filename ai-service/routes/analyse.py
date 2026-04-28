from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_client import call_groq
import json

analyse_bp = Blueprint('analyse', __name__)

@analyse_bp.route('/analyse-document', methods=['POST'])
def analyse_document():
    data = request.get_json()

    # Validate input
    if not data or 'text' not in data or not data['text']:
        return jsonify({
            "error": "Missing required field: text"
        }), 400

    text = str(data['text'])[:3000]

    prompt = f"""You are a professional risk management analyst.

Analyse the following document and identify key insights and risks.

Document:
{text}

Return a JSON object with exactly these fields:
{{
    "key_insights": [
        {{
            "insight": "key finding from document",
            "significance": "High | Medium | Low"
        }}
    ],
    "identified_risks": [
        {{
            "risk_title": "risk name",
            "risk_category": "category",
            "likelihood": "High | Medium | Low",
            "impact": "High | Medium | Low",
            "description": "brief description"
        }}
    ],
    "summary": "2-3 sentence overall summary",
    "generated_at": "timestamp"
}}

Rules:
- Identify at least 3 key insights
- Identify at least 3 risks
- Always return valid JSON only
- Never include extra text outside the JSON"""

    try:
        result_text = call_groq(prompt, temperature=0.3, max_tokens=1200)
        result = json.loads(result_text)
        result['generated_at'] = datetime.utcnow().isoformat() + 'Z'

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "Document analysis error",
            "details": str(e),
            "is_fallback": True
        }), 500