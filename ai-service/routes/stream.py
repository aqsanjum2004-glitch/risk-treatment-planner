from flask import Blueprint, request, jsonify, Response
from datetime import datetime
import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

stream_bp = Blueprint('stream', __name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@stream_bp.route('/generate-report/stream', methods=['POST'])
def stream_report():
    data = request.get_json()

    if not data or 'risks' not in data or not data['risks']:
        return jsonify({
            "error": "Missing required field: risks"
        }), 400

    risks = data['risks']

    risks_text = ""
    for i, risk in enumerate(risks):
        risks_text += f"""
Risk {i+1}:
- Title: {risk.get('risk_title', 'N/A')}
- Category: {risk.get('risk_category', 'N/A')}
- Likelihood: {risk.get('likelihood', 'N/A')}
- Impact: {risk.get('impact', 'N/A')}
"""

    prompt = f"""You are a professional risk management consultant.

Generate a comprehensive risk treatment report for the following risks:

{risks_text}

Write a detailed professional report with these sections:
1. Executive Summary
2. Risk Overview
3. Key Findings
4. Recommendations
5. Conclusion

Be detailed and professional."""

    def generate():
        try:
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1500,
                stream=True
            )

            for chunk in stream:
                if chunk.choices[0].delta.content:
                    token = chunk.choices[0].delta.content
                    yield f"data: {json.dumps({'token': token})}\n\n"

            yield f"data: {json.dumps({'done': True, 'generated_at': datetime.utcnow().isoformat() + 'Z'})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'error': str(e), 'is_fallback': True})}\n\n"

    return Response(
        generate(),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )