# Application entry point: builds the FastAPI app and mounts the feature router.
from fastapi import FastAPI
from app.features.feature_pipeline.router import router
app = FastAPI(title="Guarded document intake")
app.include_router(router)

# Independent SQLite audit of HTTP operations; no document bodies are stored.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
