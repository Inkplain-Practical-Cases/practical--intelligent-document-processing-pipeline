# Emit traceable processing audit: isolated pure document service.
def service_audit(s: dict) -> dict:
    # Record a minimal privacy-aware trail without full document text.
    s["audit"] = {"document_id": s["document_id"], "valid": s["record_valid"], "review": s["review_status"]}
    return s
