# Lab: Remote code execution via web shell upload

> Lab Objective: upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

- Login using provided credentials `wiener:peter`, then inspect the file upload functionality.

- The file upload functionality, you just browse to and select the wanted picture to upload, and a POST request is sent.
  ![1st screenshot](./attachments/1.png)

- And the uploaded file is accessed via this endpoint `/files/avatars/449750.jpg`.

```url
view-source:https://0a2900f0049cd64280ad7b19002c0035.web-security-academy.net/files/avatars/449750.jpg
```

![2nd screenshot](./attachments/2.png)

- Create a php file including this payload:
  ![7th screenshot](./attachments/7.png)

- Upload that shell, and you'll notice that it's uploaded without any problem.
  ![3rd screenshot](./attachments/3.png)

- Visit this endpoint `/avatars/shell.php?id=cat+/home/carlos/secret`.
  ![4th screenshot](./attachments/4.png)

- Copy and submit carlos' secret value.
  ![5th screenshot](./attachments/5.png)

- And te lab is solved successfully.
  ![6th screenshot](./attachments/6.png)

---
