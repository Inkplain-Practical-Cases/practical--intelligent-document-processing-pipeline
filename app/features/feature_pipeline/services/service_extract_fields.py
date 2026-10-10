# Extract typed document fields: isolated pure document service.
def service_extract_fields(s: dict) -> dict:
    # Deterministic offline extraction illustrates structured LLM output.
    tokens = s["text"].split()
    s["fields"] = {"document_type": tokens[0], "reference": tokens[1], "total": float(tokens[3]), "currency": tokens[4]}
    return s
