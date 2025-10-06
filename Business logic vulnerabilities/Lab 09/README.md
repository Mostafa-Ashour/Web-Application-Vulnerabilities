# Lab: Authentication bypass via flawed state machine

> Lab Objective: exploit login process flaw to bypass the lab's authentication, access the admin interface, and delete the user carlos.

- Login using provided credentials `wiener:peter`, then inspect the login process.

- Normal Login Process:

  - Login using username & password, if valid you'll be redirected to `/role-selector`:
    ![1st screenshot](./attachments/1.png)
  - In `/role-selector` endpoint, you'll choose your role either a user or Content Author.
    ![2nd screenshot](./attachments/2.png)
  - Your choice will be sent in a POST request to the same endpoint via POST data.
    ![3rd screenshot](./attachments/3.png)
  - Finally, you'll be redirected to home page `/`.

- Intercept the request when you enter your credentials `username:password`, then intercept the response to that request.

- When the response to the login request is intercepted, replace the redirection from `/role-selector` to `/admin`, and forward the response.
  ![4th screenshot](./attachments/4.png)

- You'll notice that there's a GET request made to `/admin`, and the response to that request is the admin panel.
  ![5th screenshot](./attachments/5.png)
  ![6th screenshot](./attachments/6.png)

- Delete the user carlos.
  ![7th screenshot](./attachments/7.png)

- You'll notice that the user carlos is deleted and the lab is solved.
  ![8th screenshot](./attachments/8.png)
  ![9th screenshot](./attachments/9.png)

---
