# Lab: JWT authentication bypass via unverified signature

> Lab Objective: modify your session token to gain access to the admin panel at `/admin`, then delete the user carlos.

- Login using provided credentials, then inspect the login requests.

- POST request sent to `/login`.
  ![1st screenshot](./attachments/1.png)

- A GET request is sent to `/my-account?id=wiener` endpoint to retrieve wiener account page.
  ![2nd screenshot](./attachments/2.png)

- Select the payload part from the JWT token in the `session` parameter.
  ![3rd screenshot](./attachments/3.png)

- You'll notice that you username is set as the value for `sub` parameter.

- Send a request to `/admin` endpoint and inspect the response.

- You'll notice that you're blocked because you're not logged in as an administrator.
  ![4th screenshot](./attachments/4.png)

- Therefore, change the value of the `sub` parameter from `wiener` to `administrator` then apply changes, and change the endpoint to `/admin`, and send the request.

- You'll notice that you've access to the admin panel.
  ![5th screenshot](./attachments/5.png)

- Delete the user carlos via this endpoint `/admin/delete?username=carlos`.
  ![6th screenshot](./attachments/6.png)

- You'll notice that the user carlos is deleted.
  ![7th screenshot](./attachments/7.png)
  ![8th screenshot](./attachments/8.png)

- And the lab is solved.
  ![9th screenshot](./attachments/9.png)

---
