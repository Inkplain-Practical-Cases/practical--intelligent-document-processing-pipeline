# Validate business record: isolated pure document service.
def service_validate_fields(s: dict) -> dict:
    # Reject incomplete records before downstream use.
    f = s["fields"]
    s["record_valid"] = bool(f["reference"] and f["total"] > 0 and f["currency"] == "USD")
    return s
