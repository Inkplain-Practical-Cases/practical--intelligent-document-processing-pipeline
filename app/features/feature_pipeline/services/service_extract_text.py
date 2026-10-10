# Extract safe document text: isolated pure document service.
def service_extract_text(s: dict) -> dict:
    # Synthetic document fixture; production extraction remains an adapter.
    s["text"] = "Invoice INV-42 Total 125.50 USD"
    return s
