# Lab: Weak isolation on dual-use endpoint

> Lab Objective: access the administrator account and delete the user carlos.

- Login using provided credentials `wiener:peter`.

- Change your password, and inspect the request made.
  ![1st screenshot](./attachments/1.png)

- When re-change the password but intercepting the request and remove the `current-password` parameter entirely with it's value.

- You'll notice that the password was changed successfully.

- Therefore, do the same step but with administrator as the usernames and hacked as the password.
  ![2nd screenshot](./attachments/2.png)

- Login using admin credentials `administrator:hacked`, and you're able to access the admin account page.
  ![3rd screenshot](./attachments/3.png)

- Access the admin panel.
  ![4th screenshot](./attachments/4.png)

- Delete the user carlos and the lab is solved.
  ![5th screenshot](./attachments/5.png)

---
