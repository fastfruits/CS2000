from typing import Optional

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

# Contamination follows the mathematical order of operations
print("I am so excited" + "!" * 3)

cats: int = 4
print(f"There are {cats} cats in this room")

name: str = input("What is your name: ")
age: int = int(input("How old are you: "))
year: int = 100 - age + 2026
print(f"You will turn 100 in year {year}")


def get_number(num: str) -> Optional[int]:
    """Returns None if string is not able to be turned into an int"""
    try:
        return int(num)
    except ValueError:
        return None

"""
    Mutation testing
    Want to make sure tests fail on incorrect code
    but work on correct code
"""
def test_negative_area() -> None:
    """Make sure it raises a ValueError for negative values"""
    with pytest.raises(ValueError):
        get_rectangle(-1, 4)