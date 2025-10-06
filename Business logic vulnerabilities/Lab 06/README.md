# Lab: Inconsistent handling of exceptional input

> Lab Objective: access the admin panel and delete the user carlos.

- When you try to access the admin panel, you'll notice that only DontWannaCry users are allowed to access the admin panel.
  ![1st screenshot](./attachments/1.png)

- When accessing email client in the lab banner, you'll notice that:
  - Portswigger provided you with an email (which is `attacker@YOUR-EMAIL-ID.web-security-academy.net`).
  - It also states that it will display all emails for `@YOUR-EMAIL-ID.web-security-academy.net` and all included subdomains.

![2nd screenshot](./attachments/2.png)

- Register a new account:

  - Provide Credentials.
    ![3rd screenshot](./attachments/3.png)
  - Check your email client, and click on the sent link, therefore the account registration is successful.
    ![4th screenshot](./attachments/4.png)

- When using a very email, for instance:

```
attackerattackerattacackerattackerattackerattackerattackerattackerattackerattackerattackerattacktackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattacackerattackerattackerattackerattackerattackerattacker@exploit-0ab900e004ece9a680b4a72701a20000.exploit-server.net
```

- Then registering normally, you'll receive the verification email in your email client, but when logging in, you'll notice that your email is truncated into exactly 255 characters:
  ![5th screenshot](./attachments/5.png)

- Therefore, register again but in the email field make `your-string@dontwannacry.com` is exactly 255 characters followed by `.YOUR-EMAIL-ID.web-security-academy.net`.

- The email will be:

```
attackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattackerattack@dontwannacry.com.exploit-0ab900e004ece9a680b4a72701a20000.exploit-server.net
```

- When registering with the new email.
  ![6th screenshot](./attachments/6.png)

- Then logging in, and you'll notice that email is suitable, and admin panel is accessible.
  ![7th screenshot](./attachments/7.png)

- Access the admin panel.
  ![8th screenshot](./attachments/8.png)

- Then delete the user carlos, and the lab is solved.
  ![8th screenshot](./attachments/8.png)

---
