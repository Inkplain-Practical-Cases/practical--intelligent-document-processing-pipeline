# Input contract: Pydantic validates fields at the external boundary.
from pydantic import BaseModel, Field
class DocumentRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
    document_id: str = Field(min_length=1)
