from langchain_core.tools import tool


@tool
def calculator(a: float, b: float, operation: str) -> float:
    """Perform a mathematical calculation."""
    operation = operation.lower()

    if operation in ["add", "addition", "plus"]:
        return a + b

    if operation in ["sub", "subtract", "minus"]:
        return a - b

    if operation in ["mul", "multiply", "multiplication", "times"]:
        return a * b

    if operation in ["divide", "division"]:
        return a / b

    raise ValueError(f"Invalid operation: {operation}")

@tool
def get_user_data(key: str) -> str:
    """Retrieve user information."""
    data = {
        "name": "Shivam Kumar",
        "company": "RoboSiddhi",
        "age": 22
    }

    return str(data.get(key, "Value not found"))


@tool
def calculat_currency(num: float, currency: str) -> float:
    """Convert rupees to dollars or euros."""
    currency = currency.lower()

    if currency in ["dollar", "usd"]:
        return num / 100

    if currency in ["euro", "eur"]:
        return num / 106

    raise ValueError(f"Invalid currency: {currency}")