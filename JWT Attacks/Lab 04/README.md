# Lab: JWT authentication bypass via jwk header injection

> Lab Objective: modify and sign a JWT that gives you access to the admin panel at `/admin`, then delete the user carlos.

- Login using provided credentials `wiener:peter`, then inspect the login requests.

- Login Request:
  ![1st screenshot](./attachments/1.png)

- Redirection to wiener's account page `/my-account?id=wiener`.
  ![2nd screenshot](./attachments/2.png)

- Replacing your username with `administrator` within the `sub` parameter in the payload part, results in redirection to `/login`, indicating a failed attempt.
  ![3rd screenshot](./attachments/3.png)

- Making the value of `alg` in header part `none` and removing the signature part, also results in redirection to `/login`, indicating a failed attempt.
  ![4th screenshot](./attachments/4.png)

- Create a new RSA key using JWT Editor extension in Burp.
  ![5th screenshot](./attachments/5.png)

- Modify the payload part in the JWT token as desired, then use the created RSA key to sign it, and send the request.

- Replace your usernames with `administrator`, and the endpoint with `/admin`, and you'll notice that the server has accepted the RSA key, and you've accessed the Admin Panel.
  ![6th screenshot](./attachments/6.png)

- Delete the user carlos via this endpoint `/admin/delete?username=carlos`.
  ![7th screenshot](./attachments/7.png)

- The request of deleting the user carlos is accepted.
  ![8th screenshot](./attachments/8.png)

- Follow the redirection to the `/admin` endpoint.
  ![9th screenshot](./attachments/9.png)

- You'll notice that the user carlos is deleted and the lab is solved.
  ![10th screenshot](./attachments/10.png)

---
