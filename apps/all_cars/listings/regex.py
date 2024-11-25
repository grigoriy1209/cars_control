from enum import Enum


class CarRegex(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\s\-]{1,49}$',
        "Brand must start with an uppercase letter and can contain only letters, spaces, and dashes.",
    )
    MODEL = (
        r'^[A-Z][a-zA-Z0-9\s\-]{1,49}$',
        "Model must start with an uppercase letter and can contain letters, numbers, spaces, and dashes.",
    )

    REGION = (
        r'^[A-Za-z\s\-]{1,23}$',
        "Region must consist of up to 23 characters and can include only letters, spaces, and dashes.",
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
