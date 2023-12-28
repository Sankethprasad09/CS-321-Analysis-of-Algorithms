def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()
    satisfied_dogs = 0

    hunger_index = 0
    biscuit_index = 0

    while hunger_index < len(hunger_level) and biscuit_index < len(biscuit_size):
        if biscuit_size[biscuit_index] >= hunger_level[hunger_index]:
            satisfied_dogs += 1
            hunger_index += 1
            biscuit_index += 1
        else:
            biscuit_index += 1

    return satisfied_dogs

# User input
num_dogs = int(input("Enter the number of dogs: "))
hunger_level = []
for i in range(num_dogs):
    hunger = int(input(f"Enter the hunger level of dog {i+1}: "))
    hunger_level.append(hunger)

num_biscuits = int(input("Enter the number of biscuits: "))
biscuit_size = []
for i in range(num_biscuits):
    size = int(input(f"Enter the size of biscuit {i+1}: "))
    biscuit_size.append(size)

# Call the function and display the result
result = feedDog(hunger_level, biscuit_size)
print(f"Number of satisfied dogs: {result}")

