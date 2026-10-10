# Route uncertainty to human review: isolated pure document service.
def service_review(s: dict) -> dict:
    # A failed validation must result in manual inspection, never auto-approval.
    s["review_required"] = not s["record_valid"]
    s["review_status"] = "queued" if s["review_required"] else "not_required"
    return s
