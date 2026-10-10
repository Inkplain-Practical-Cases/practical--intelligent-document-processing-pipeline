# Pipeline orchestration: each service accepts and returns validated state.
from app.features.feature_pipeline.schemas.request import DocumentRequest
from app.features.feature_pipeline.services.service_validate import service_validate
from app.features.feature_pipeline.services.service_extract_text import service_extract_text
def handle_request(body: DocumentRequest) -> dict:
    state = service_validate(body.model_dump())
    state = service_extract_text(state)
    return state
