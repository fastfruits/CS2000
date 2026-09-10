x1: int = 3
y1: int = 4

def get_rectangle(width: int, height: int) -> int:
    """
    Documentation statement for all functions
    Includes parameters, output, error raises
    """
    if width < 0 or height < 0:
        raise ValueError("Dimension values cannot be negative")

    return width * height

result1: int = get_rectangle(x1, y1)

print(result1)