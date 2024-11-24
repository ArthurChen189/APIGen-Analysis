from z3 import *

# Variables
product_id = Int("product_id")
quantity = Int("quantity")
user_id = Int("user_id")
user_balance = Int("user_balance")
product_price = Int("product_price")

# Create two solvers: one for valid cases and one for invalid cases
valid_solver = Solver()
invalid_solver = Solver()

# Define edge cases and invalid scenarios
def test_valid_edge_cases():
    valid_solver.push()  # Save the current state
    
    # Edge cases (at boundaries but still valid)
    valid_solver.add(Or(
        And(product_id == 1),      # Minimum product_id
        And(product_id == 1000),   # Maximum product_id
        And(quantity == 1),        # Minimum quantity
        And(quantity == 100),      # Maximum quantity
        And(user_balance == product_price * quantity),  # Exact balance needed
        And(product_price == 1),   # Minimum price
        And(product_price == 10000) # Maximum price
    ))
    
    print("\n=== Valid Edge Cases ===")
    get_solutions(valid_solver, 3)
    valid_solver.pop()  # Restore the state

def test_invalid_cases():
    invalid_solver.push()
    
    # Invalid scenarios - at least one of these conditions must be true
    invalid_solver.add(Or(
        product_id <= 0,           # Invalid product ID
        product_id > 1000,         # Invalid product ID
        quantity <= 0,             # Invalid quantity
        quantity > 100,            # Exceeds quantity limit
        user_balance < quantity * product_price,  # Insufficient balance
        user_balance < 0,          # Negative balance
        user_balance > 1000000,    # Exceeds balance limit
        product_price <= 0,        # Invalid price
        product_price > 10000,     # Exceeds price limit
        user_id <= 0,             # Invalid user ID
        user_id > 1000            # Invalid user ID
    ))
    
    print("\n=== Invalid Cases ===")
    get_solutions(invalid_solver, 3)
    invalid_solver.pop()

def get_solutions(solver, num_solutions):
    for i in range(num_solutions):
        if solver.check() == sat:
            model = solver.model()
            print(f"\nSolution {i+1}:")
            print(f"product_id: {model[product_id]}")
            print(f"quantity: {model[quantity]}")
            print(f"user_id: {model[user_id]}")
            print(f"user_balance: {model[user_balance]}")
            print(f"product_price: {model[product_price]}")
            
            # Add constraint to exclude this solution
            solver.add(Or(
                product_id != model[product_id],
                quantity != model[quantity],
                user_id != model[user_id],
                user_balance != model[user_balance],
                product_price != model[product_price]
            ))
        else:
            print(f"\nNo more solutions found after {i} solutions")
            break

# Run the tests
test_valid_edge_cases()
test_invalid_cases()
