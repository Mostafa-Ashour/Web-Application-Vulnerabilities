# Lab: JWT authentication bypass via flawed signature verification

> Lab Objective: modify your session token to gain access to the admin panel at `/admin`, then delete the user carlos.

- Login using provided credentials `wiener:peter`, then inspect the login requests.

- Login POST request.
  ![1st screenshot](./attachments/1.png)

- Login to `/my-account?id=wiener` to retrieve wiener's account page.
  ![2nd screenshot](./attachments/2.png)

- Notice that if you changed the username from `wiener` to `administrator` in the payload part, you'll be redirected to `/login` endpoint, indicating that the server validates the user sending the request.
  ![3rd screenshot](./attachments/3.png)

- But in the header part of the JWT, if you changed the value of `alg` parameter to `none` and removed the signature part (while keeping the trailing `.`), you'll notice that the request to wiener's account page is accepted.
  ![4th screenshot](./attachments/4.png)

- Therefore, in addition to the changes that you've made:

  - Replace the accessed endpoint to `/admin`.
  - The `sub` value from `wiener` to `administrator`.

- You'll notice that the request is accepted and you've accessed the admin panel.
  ![5th screenshot](./attachments/5.png)

- Delete the user carlos via this endpoint `/admin/delete?username=carlos`.
  ![6th screenshot](./attachments/6.png)

- Send that request, and follow redirection to `/admin` endpoint.
  ![7th screenshot](./attachments/7.png)

- You'll notice that the user carlos is deleted and the lab is solved successfully.
  ![8th screenshot](./attachments/8.png)

---
