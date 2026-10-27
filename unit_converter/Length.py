
def convert_length(value, from_unit, to_unit):
    """Convert a length between meters, kilometers, and miles."""
    conversion_to_meters = {
        "m": 1,
        "km": 1000,
        "mi": 1609.344,
    }

    if value < 0:
        raise ValueError("Length cannot be negative")

    if from_unit not in conversion_to_meters:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in conversion_to_meters:
        raise ValueError(f"Unknown unit: {to_unit}")

    meters = value * conversion_to_meters[from_unit]
    return meters / conversion_to_meters[to_unit]
