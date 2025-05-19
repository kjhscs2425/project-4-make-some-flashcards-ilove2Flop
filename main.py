import random

class Roulette:
    def __init__(self, chance_of_winning=0%):
        # Default chance of winning is 50%, but you can adjust it
        self.chance_of_winning = chance_of_winning

    def spin(self):
        # Simulate a spin based on the chance of winning
        return random.random() < self.chance_of_winning

    def play(self, bet_amount, bet_on="Red"):
        # Simulate a bet and return the result (win or lose)
        if self.spin():
            print(f"You won the bet on {bet_on}!")
            return bet_amount  # Return the winnings (same as the bet for simplicity)
        else:
            print(f"You lost the bet on {bet_on}.")
            return -bet_amount  # Losing the bet amount

# Main game loop
if __name__ == "__main__":
    # Set the chance of winning (can be adjusted)
    chance_of_winning = float(input("Enter the chance of winning (0-1): "))
    roulette = Roulette(chance_of_winning)
    
    balance = 100  # Starting balance
    print(f"Your starting balance is {balance}.")
    
    while balance > 0:
        print(f"\nCurrent balance: {balance}")
        
        bet_amount = int(input("Enter your bet amount: "))
        if bet_amount > balance:
            print("You can't bet more than your current balance!")
            continue
        
        bet_on = input("Bet on (Red/Black): ").capitalize()
        if bet_on not in ["Red", "Black"]:
            print("Invalid bet choice! Please bet on 'Red' or 'Black'.")
            continue
        
        # Play the round
        result = roulette.play(bet_amount, bet_on)
        balance += result
        
        # Check if player still has money
        if balance <= 0:
            print("You ran out of money. Game over!")
            break
