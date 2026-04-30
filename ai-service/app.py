from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)

# Track startup time
START_TIME = time.time()

# Register blueprints
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.query import query_bp
from routes.report import report_bp
from routes.analyse import analyse_bp
from routes.batch import batch_bp
from routes.stream import stream_bp
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(query_bp)
app.register_blueprint(report_bp)
app.register_blueprint(analyse_bp)
app.register_blueprint(batch_bp)
app.register_blueprint(stream_bp)

@app.route('/health', methods=['GET'])
def health():
    uptime_seconds = int(time.time() - START_TIME)
    uptime_minutes = uptime_seconds // 60

    try:
        from services.chroma_client import collection
        doc_count = collection.count()
    except:
        doc_count = 0

    return jsonify({
        "status": "ok",
        "service": "ai-service",
        "model": "llama-3.3-70b-versatile",
        "uptime_seconds": uptime_seconds,
        "uptime_minutes": uptime_minutes,
        "chromadb_doc_count": doc_count,
        "endpoints": [
            "/health",
            "/describe",
            "/recommend",
            "/generate-report",
            "/generate-report/stream",
            "/query",
            "/ingest",
            "/analyse-document",
            "/batch-process"
        ]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)