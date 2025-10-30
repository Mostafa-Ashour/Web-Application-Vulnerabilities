# Lab: JWT authentication bypass via weak signing key

> Lab Objective: first brute-force the website's secret key. Once you've obtained this, use it to sign a modified session token that gives you access to the admin panel at `/admin`, then delete the user carlos.

- Login using provided credentials `wiener:peter`, then inspect the login requests.

- Login POST Request.
  ![1st screenshot](./attachments/1.png)

- Wiener's account page.
  ![2nd screenshot](./attachments/2.png)

- If you changed the `alg` in the header part to `none`, and removed the signature, you'll notice that you're redirected to `/login` endpoint, indicating that this method is not working.
  ![3rd screenshot](./attachments/3.png)

- The same happened when changing the username to `administrator`.
  ![4th screenshot](./attachments/4.png)

- Therefore, I'll try to brute force the secret key used for signing the JWT (the JWT signature).

- Obtain a valid JWT token from accessing Wiener's Account page `/my-account?id=wiener`, and a wordlist of well-known secrets, and run the following command:

```
hashcat -a 0 -m 16500 <jwt> <wordlist>
```

- Retrieve the secret from hashcat output.
  ![5th screenshot](./attachments/5.png)

- Base64 decode it, then generate a new key from JWT Editor Key tab, and replace the value of `k` parameter with the encoded secret.
  ![6th screenshot](./attachments/6.png)

- In Repeater Json Web Token Tab, replace `sub` value to `administrator`, then `sign` and select the previously created key.
  ![7th screenshot](./attachments/7.png)

- Then change the endpoint to `/admin`, and send the request.

- You'll notice that the request is accepted and you have access to the admin panel.
  ![8th screenshot](./attachments/8.png)

- Delete the user carlos via this endpoint `/admin/delete?username=carlos`.
  ![9th screenshot](./attachments/9.png)

- Send the request, then follow the redirection to `/admin`.
  ![10th screenshot](./attachments/10.png)

- You'll notice that the user is deleted successfully, and the lab is solved.
  ![11th screenshot](./attachments/11.png)
  ![12th screenshot](./attachments/12.png)

---
