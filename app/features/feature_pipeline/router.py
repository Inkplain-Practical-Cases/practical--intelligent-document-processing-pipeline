# Thin HTTP door: delegates the request to the injected handler.
from fastapi import APIRouter
from app.features.feature_pipeline.handlers.handle_request import handle_request
from app.features.feature_pipeline.schemas.request import DocumentRequest
router = APIRouter()
@router.post("/documents")
def submit(body: DocumentRequest):
    return handle_request(body)
