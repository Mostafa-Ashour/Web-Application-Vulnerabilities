# Lab: JWT authentication bypass via kid header path traversal

> Lab Objective: forge a JWT that gives you access to the admin panel at `/admin`, then delete the user carlos.

- Login using provided credentials `wiener:peter`, then inspect the login requests.

- Login POST Request.
  ![1st screenshot](./attachments/1.png)

- Accessing Wiener's Account Page via `/my-account?id=wiener` endpoint.
  ![2nd screenshot](./attachments/2.png)

- By setting the `alg` parameter in the header part to `none` and removing the signature part, and changing the value of `sub` parameter from your username to `administrator` and the endpoint to `/admin`, results of both of them indicates a failed attempt.
  ![3rd screenshot](./attachments/3.png)
  ![4th screenshot](./attachments/4.png)

- By generating a symmetric key, and setting the `k` parameter to `AA==` which is the Base64 Encoding for Null Byte, it has the same impact as signing the tokens with an empty string.
  ![5th screenshot](./attachments/5.png)

- In the Request where you access Wiener's Account Page, replace the `kid` parameter to `../../../../dev/null` which points to an empty file, then sign the token with the newly created symmetric Key.
  ![6th screenshot](./attachments/6.png)

- Then send the request, and you'll notice that the request is accepted without any problems.
  ![7th screenshot](./attachments/7.png)

- Do the same steps, but replace the `sub` value from your username to `administrator`, and the endpoint to `/admin`, then send the request, and you'll notice that you've access to the admin panel.
  ![8th screenshot](./attachments/8.png)
  ![9th screenshot](./attachments/9.png)

- Delete the user carlos via `/admin/delete?username=carlos` endpoint.
  ![10th screenshot](./attachments/10.png)

- Follow the redirection to `/admin` endpoint, and you'll notice that the user carlos is deleted and the lab is solved.
  ![11th screenshot](./attachments/11.png)
  ![12th screenshot](./attachments/12.png)

---
