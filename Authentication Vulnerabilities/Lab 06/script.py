# Reading Passwords from `/passwords.txt` file.
with open(
    r"D:\Courses\Web Application Penetration Testing\Web Application Vulnerabilities\Authentication Vulnerabilities\Lab 06\passwords.txt",
    "r",
) as file:
    passwords = []
    for line in file:
        passwords.append(line.strip())

# Embedding valid password after each 2 passwords.
valid_password = "wiener"
new_list = []
for i in range(2, len(passwords), 3):
    passwords.insert(i, "peter")


# Writing the modified passwords back to the file.
with open(
    r"D:\Courses\Web Application Penetration Testing\Web Application Vulnerabilities\Authentication Vulnerabilities\Lab 06\passwords.txt",
    "w",
) as file:
    for password in passwords:
        file.write(password + "\n")
