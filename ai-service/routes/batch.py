from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_client import call_groq
import json
import time

batch_bp = Blueprint('batch', __name__)

@batch_bp.route('/batch-process', methods=['POST'])
def batch_process():
    data = request.get_json()

    # Validate input
    if not data or 'items' not in data or not data['items']:
        return jsonify({
            "error": "Missing required field: items"
        }), 400

    items = data['items']

    # Limit to 20 items
    if len(items) > 20:
        return jsonify({
            "error": "Maximum 20 items allowed per batch"
        }), 400

    results = []

    for i, item in enumerate(items):
        try:
            # 100ms delay between each item
            if i > 0:
                time.sleep(0.1)

            prompt = f"""You are a professional risk management analyst.

Analyse this risk and provide a brief assessment.

Risk Title: {item.get('risk_title', 'N/A')}
Risk Category: {item.get('risk_category', 'N/A')}
Likelihood: {item.get('likelihood', 'N/A')}
Impact: {item.get('impact', 'N/A')}

Return a JSON object with these fields:
{{
    "risk_title": "title",
    "severity": "Critical | High | Medium | Low",
    "summary": "1-2 sentence assessment",
    "action_required": true or false
}}

Return valid JSON only."""

            result_text = call_groq(prompt, temperature=0.3, max_tokens=300)
            result = json.loads(result_text)
            result['status'] = 'processed'
            results.append(result)

        except Exception as e:
            results.append({
                "risk_title": item.get('risk_title', 'Unknown'),
                "status": "failed",
                "error": str(e)
            })

    return jsonify({
        "total": len(items),
        "processed": len([r for r in results if r.get('status') == 'processed']),
        "failed": len([r for r in results if r.get('status') == 'failed']),
        "results": results,
        "generated_at": datetime.utcnow().isoformat() + 'Z'
    }), 200