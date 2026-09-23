"""Lecture notes for class"""
import pytest


class Animal:
    """Creates an animal class which contains a name, owner, and species"""
    def __init__(self, name: str, owner: str, species: str) -> None:
        self.name: str = name
        self.owner: str = owner
        self.species: str = species

        if species == 'cat':
            self.sound: str = 'meow'
        elif species == 'dog':
            self.sound = 'woof'
        else:
            self.sound = 'hello'

    def make_sound(self) -> str:
        """Returns the pet's sound"""
        return self.sound

mini: Animal = Animal("fred", "jack", "cat")

print(mini.make_sound())

class Rectangle:
    """Creates a rectangle object"""
    def __init__(self, length: int, width: int):
        self.length: int = length
        self.width: int = width

    def get_area(self) -> int:
        """Gets the area of the rectangle"""
        return self.width * self.length

rectangle: Rectangle = Rectangle(3, 4)

@pytest.fixture(name="rectangle")
def rectangle_fixture() -> Rectangle:
    """Define a rectangle for testing"""
    return Rectangle(3, 4)

class TestRectangle:
    """Test for the rectangle test"""

    def test_area(self, rectangle: Rectangle) -> None:
        """Test the area of a 3 by 4 rectangle"""
        assert rectangle.get_area() == 12
