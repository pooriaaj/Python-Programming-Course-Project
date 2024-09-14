import random

def roll_dice(num_dice=1):
    """Roll a given number of dice and return the results."""
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice < 1:
                print("Please enter a number greater than 0.")
                continue
            results = roll_dice(num_dice)
            print("You rolled:", results)
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
