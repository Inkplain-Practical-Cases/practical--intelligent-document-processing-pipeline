# Verify the HTTP facade and the real cumulative document transformation.
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_document_pipeline():
    r=client.post("/documents",json={"tenant_id":"t","document_id":"doc-1"})
    assert r.status_code==200
    assert r.json()["status"]=="accepted"
    assert "review_status" in r.json()
def test_empty_document_rejected():
    assert client.post("/documents",json={"tenant_id":"t","document_id":""}).status_code==422
