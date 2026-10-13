"""Test source-derived relational document API metadata and event integrity."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_document_audit_relations(tmp_path):
    db = str(tmp_path / "document.sqlite3")
    id = provider_record_request_audit("POST", "/documents", 202, 6.5, db)
    with sqlite3.connect(db) as conn:
        assert conn.execute("SELECT COUNT(*) FROM document_api_requests WHERE id=?", (id,)).fetchone()[0] == 1
        assert conn.execute("SELECT COUNT(*) FROM document_api_events WHERE request_id=?", (id,)).fetchone()[0] == 1
        assert conn.execute("PRAGMA foreign_key_check").fetchall() == []
