"""Conditional lesson/practice"""

guess: int = 0
answer: int = 21

if guess == answer:
    print("You guessed the answer correctly!")
elif guess - 1 == answer or guess + 1 == answer:
    print("Very close!")
else:
    print("Wrong")


while True:
    number: int = int(input("Pick a random number: "))
    if number % 2 == 0:
        print("This number is even")
        break
    else:
        print("Rhis number is odd")
        break

n: int = 3

match n:
    case 1:
        print("n is 1")

i_love_cats: str = "Cats suck"


for char in i_love_cats:
    print(char)

# Hard coded literal consts are good for codebase-wide usage and are a single point of control
SECONDS_PER_MINUTE: int = 60
MINUTES_PER_HOUR: int = 60

def main() -> None:
    """Main function for the file"""
    print(None)

if __name__ == '__main__':
    main()
