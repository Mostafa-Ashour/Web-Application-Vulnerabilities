# Generating a list of numbers from 0000 to 9999
num_list = []
for i in range(10000):
    num_list.append(f"{i:04d}")

# print(num_list)

# Write the list to a file
with open("numbers.txt", "w") as file:
    for num in num_list:
        file.write(num + "\n")
