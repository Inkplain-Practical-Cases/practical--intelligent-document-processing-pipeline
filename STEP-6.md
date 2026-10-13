# STEP-6 — Emit traceable processing audit

Learn the source-level component, execute `pytest -q`, and examine STEP-6.crd. This branch inherits every prior capability.

## Database (Entity) Relations
SQLite audit stores metadata only in document_api_requests and document_api_events; raw documents remain outside this store. See STEP-6.erd and STEP-6-ERD tab.
