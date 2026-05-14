from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def print_image(self):
        pass

class Latte(Coffee):
    def print_image(self):
        print("Latte:")
        print("  #####  ")
        print(" #     # ")
        print("#  ###  #")
        print("#       #")
        print(" #     # ")
        print("  #####  ")
        print()

class Matcha(Coffee):
    def print_image(self):
        print("Matcha:")
        print("  #####  ")
        print(" #     # ")
        print("#  $$$  #")
        print("#       #")
        print(" #     # ")
        print("  #####  ")
        print()

class Americano(Coffee):
    def print_image(self):
        print("Americano:")
        print("  #####  ")
        print(" #     # ")
        print("#       #")
        print("#       #")
        print(" #     # ")
        print("  #####  ")
        print()

class Espresso(Coffee):
    def print_image(self):
        print("Espresso:")
        print("   ###   ")
        print("  #   #  ")
        print(" #     # ")
        print(" #     # ")
        print("  #   #  ")
        print("   ###   ")
        print()

def main():
    coffees = {
        'latte': Latte(),
        'matcha': Matcha(),
        'americano': Americano(),
        'espresso': Espresso()
    }

    print("Welcome to the Coffee Machine!")
    print("Available coffees: latte, matcha, americano, espresso")
    print("Type 'quit' to exit.")

    while True:
        choice = input("Choose your coffee: ").lower().strip()
        if choice == 'quit':
            print("Goodbye!")
            break
        elif choice in coffees:
            coffees[choice].print_image()
        else:
            print("Invalid choice. Please choose from: latte, matcha, americano, espresso")

if __name__ == "__main__":
    main()