def clean_dict(value: dict) -> dict:
    return {key: value for key, value in value.items() if value is not None} if value else {}