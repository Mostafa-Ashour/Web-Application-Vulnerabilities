passwords = []
with open("./passwords.txt", "r") as file:
    for line in file:
        passwords.append(line.strip())

# print(passwords)

with open("./data.txt", "w") as file:
    file.write('{\n"username":"carlos",\n"password":[\n')
    for password in passwords:
        file.write(f'"{password}",\n')
    file.write("]\n}\n")
