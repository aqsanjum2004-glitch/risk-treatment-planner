import pytest
import json
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test 1 — Health endpoint
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ok'

# Test 2 — Describe missing fields
def test_describe_missing_fields(client):
    response = client.post('/describe',
        json={},
        content_type='application/json')
    assert response.status_code == 400

# Test 3 — Describe with valid input
@patch('routes.describe.client')
def test_describe_valid(mock_client, client):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({
        "description": "Test risk description",
        "severity": "High",
        "key_factors": ["factor1", "factor2", "factor3"]
    })
    mock_client.chat.completions.create.return_value = mock_response

    response = client.post('/describe',
        json={
            "risk_title": "Data Breach",
            "risk_category": "Cybersecurity",
            "likelihood": "High",
            "impact": "Critical"
        },
        content_type='application/json')
    assert response.status_code == 200

# Test 4 — Recommend missing fields
def test_recommend_missing_fields(client):
    response = client.post('/recommend',
        json={},
        content_type='application/json')
    assert response.status_code == 400

# Test 5 — Recommend with valid input
@patch('routes.recommend.client')
def test_recommend_valid(mock_client, client):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = json.dumps({
        "recommendations": [
            {"action_type": "Preventive", "description": "Test", "priority": "High"},
            {"action_type": "Detective", "description": "Test", "priority": "Medium"},
            {"action_type": "Corrective", "description": "Test", "priority": "Low"}
        ]
    })
    mock_client.chat.completions.create.return_value = mock_response

    response = client.post('/recommend',
        json={
            "risk_title": "Data Breach",
            "risk_category": "Cybersecurity",
            "likelihood": "High",
            "impact": "Critical"
        },
        content_type='application/json')
    assert response.status_code == 200

# Test 6 — Query missing fields
def test_query_missing_fields(client):
    response = client.post('/query',
        json={},
        content_type='application/json')
    assert response.status_code == 400

# Test 7 — Analyse document missing fields
def test_analyse_missing_fields(client):
    response = client.post('/analyse-document',
        json={},
        content_type='application/json')
    assert response.status_code == 400

# Test 8 — Generate report missing fields
def test_generate_report_missing_fields(client):
    response = client.post('/generate-report',
        json={},
        content_type='application/json')
    assert response.status_code == 400

# Test 9 — Ingest missing fields
def test_ingest_missing_fields(client):
    response = client.post('/ingest',
        json={},
        content_type='application/json')
    assert response.status_code == 400

# Test 10 — Health endpoint model name
def test_health_model(client):
    response = client.get('/health')
    data = json.loads(response.data)
    assert data['model'] == 'llama-3.3-70b-versatile'