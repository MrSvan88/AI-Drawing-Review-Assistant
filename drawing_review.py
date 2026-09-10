"""
AI Drawing Review Assistant
Prototype v0.2

A simple prototype for demonstrating automated checks
of information found in technical engineering drawings.

The current version uses structured drawing data from the
fictional example drawing included in this repository.
"""

# Expected information for the drawing
REQUIRED_BASIC_FIELDS = [
    "drawing_number",
    "revision",
    "date",
    "title",
]

REQUIRED_ENGINEERING_FIELDS = [
    "design_pressure",
    "design_temperature",
    "material",
    "nozzle_schedule",
]


def check_required_fields(drawing, required_fields):
    """Check that required information exists and has a value."""
    results = {}

    for field in required_fields:
        results[field] = field in drawing and bool(drawing[field])

    return results


def check_nozzles(drawing, expected_nozzles):
    """Check that all expected nozzle IDs are present."""
    actual_nozzles = drawing.get("nozzles", [])

    results = {}

    for nozzle in expected_nozzles:
        results[nozzle] = nozzle in actual_nozzles

    return results


def print_section(title, results):
    """Print one section of the review report."""
    print(f"\n{title}")
    print("-" * len(title))

    issues = 0

    for item, passed in results.items():
        symbol = "✓" if passed else "✗"
        status = "OK" if passed else "MISSING"

        readable_name = item.replace("_", " ").title()

        print(f"{symbol} {readable_name}: {status}")

        if not passed:
            issues += 1

    return issues


def review_drawing(drawing):
    """Run all currently available drawing checks."""

    print("\nAI DRAWING REVIEW ASSISTANT")
    print("=" * 35)

    print(f"Drawing:  {drawing.get('drawing_number', 'Unknown')}")
    print(f"Revision: {drawing.get('revision', 'Unknown')}")

    basic_results = check_required_fields(
        drawing,
        REQUIRED_BASIC_FIELDS
    )

    engineering_results = check_required_fields(
        drawing,
        REQUIRED_ENGINEERING_FIELDS
    )

    expected_nozzles = [
        "N1", "N2", "N3", "N4",
        "N5", "N6", "N7", "N8"
    ]

    nozzle_results = check_nozzles(
        drawing,
        expected_nozzles
    )

    issues = 0

    issues += print_section(
        "BASIC DRAWING CHECKS",
        basic_results
    )

    issues += print_section(
        "ENGINEERING CHECKS",
        engineering_results
    )

    issues += print_section(
        "NOZZLE CHECK",
        nozzle_results
    )

    print("\nREVIEW RESULT")
    print("-" * 13)

    if issues == 0:
        print("✓ No issues found by the automated checks.")
    else:
        print(f"⚠ {issues} potential issue(s) found.")

    print("\nFinal review must be performed by a qualified engineer.")


# ---------------------------------------------------------
# Fictional test data based on example_drawing.png
# ---------------------------------------------------------

example_drawing = {
    "drawing_number": "EX-1000-001",
    "revision": "A",
    "date": "2025-09-01",
    "title": "Vertical Pressure Vessel - General Arrangement",

    "design_pressure": "10 bar(g)",
    "design_temperature": "150 °C",
    "material": "S355",
    "nozzle_schedule": True,

    "nozzles": [
        "N1", "N2", "N3", "N4",
        "N5", "N6", "N7", "N8"
    ],
}


if __name__ == "__main__":
    review_drawing(example_drawing)
