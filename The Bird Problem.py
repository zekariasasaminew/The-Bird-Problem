total_budget = 100  # constant total budget in dollars

# Define the prices for different birds
duck_price = 2
pigeon_price = 0.5
wood_pigeon_price = 1 / 3
lark_price = 0.25
chicken_price = 1
count = 0
bitanya = 0

# Iterate through different quantities of each bird
for ducks in range(1, total_budget // duck_price + 1):
    for pigeons in range(1, int((total_budget - ducks * duck_price) // pigeon_price) + 1):
        for wood_pigeons in range(1, int((total_budget - ducks * duck_price - pigeons * pigeon_price) // wood_pigeon_price) + 1):
            for larks in range(1, int((total_budget - ducks * duck_price - pigeons * pigeon_price - wood_pigeons * wood_pigeon_price) // lark_price) + 1):
                for chickens in range(1, int((total_budget - ducks * duck_price - pigeons * pigeon_price - wood_pigeons * wood_pigeon_price - larks * lark_price) // chicken_price) + 1):
                    count += 1
                    if (
                        ducks * duck_price +
                        pigeons * pigeon_price +
                        wood_pigeons * wood_pigeon_price +
                        larks * lark_price +
                        chickens * chicken_price == total_budget
                    ) and (ducks + pigeons + wood_pigeons + larks + chickens == 100):
                        # Output the valid combination
                        print(f"Ducks: {ducks}, Pigeons: {pigeons}, Wood Pigeons: {wood_pigeons}, Larks: {larks}, Chickens: {chickens}, Count: {count}")
