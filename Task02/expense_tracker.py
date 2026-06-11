# Project 2: Expense Tracker
# DecodeLabs Industrial Training Kit | Batch 2026

def main():
    print("=== Welcome to Expense Tracker ===")
    print("Keep entering your expenses one by one.")
    print("Type 'quit' at any time to see the total spent and exit.")
    print("----------------------------------\n")
    
    total = 0
    
    while True:
        user_input = input("Enter expense: ")
        
        if user_input.lower() == 'quit':
            break
            
        try:
            expense = int(user_input)
            total += expense
        except ValueError:
            print("Invalid Data")
            
    print(f"Total Spent: {total}")

if __name__ == "__main__":
    main()
