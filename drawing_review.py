"""
AI Drawing Review Assistant
Prototype v0.1

A simple first prototype for checking whether common drawing
information is present in extracted drawing text.

This version does not yet read PDF files automatically.
Instead, paste or load text from a technical drawing and run
the checks below.
"""

REQUIRED_FIELDS = {
    "Drawing number": ["drawing no", "drawing number", "dwg no", "dwg"],
    "Revision": ["revision", "rev"],
    "Date": ["date"],
    "Drawing title": ["title", "drawing title"],
}


def check_drawing_text(text):
    """Check whether expected drawing information appears in the text."""
    text_lower = text.lower()
    results = {}

    for field, keywords in REQUIRED_FIELDS.items():
        results[field] = any(keyword in text_lower for keyword in keywords)

    return results


def print_report(results):
    """Print a simple drawing review report."""
    print("\nAI Drawing Review Assistant")
    print("-" * 30)

    missing = []

    for field, found in results.items():
        symbol = "✓" if found else "✗"
        status = "Found" if found else "Missing"
        print(f"{field:<16}: {symbol} {status}")

        if not found:
            missing.append(field)

    print("\nReview result:")

    if not missing:
        print("✓ All basic drawing information was identified.")
    else:
        for field in missing:
            print(f"⚠ {field} information could not be identified.")


if __name__ == "__main__":
    # Example drawing text.
    # Replace this later with text extracted from a real drawing.
    drawing_text = """
    DRAWING NUMBER: P-101
    REV: A
    TITLE: Process Piping Layout
    """

    results = check_drawing_text(drawing_text)
    print_report(results)
