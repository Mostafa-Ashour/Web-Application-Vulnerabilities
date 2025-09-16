# Lab: User ID controlled by request parameter with password disclosure

> Lab Objective: User ID controlled by request parameter with password disclosure.

- Login using the provide credentials `wiener:peter`, then inspect the requests.

- You'll notice that there is a request made to retrieve the account page related to the user with `id=wiener` (my account page).
  ![3rd screenshot](./attachments/3.png)

- When viewing my account page, you'll notice that there is a functionality to change your password with the old password stated in the input field.
  ![1st screenshot](./attachments/1.png)
  ![2nd screenshot](./attachments/2.png)

- When changing the value of the `id` parameter to `carlos`, I'll be able to access the account page for that user.
  ![4th screenshot](./attachments/4.png)

- Therefore, I'll be able to retrieve his password.
  ![5th screenshot](./attachments/5.png)

- In order to delete the user carlos, therefore I must retrieve the Administrator password and login as the administrator.

- Therefore, change the value of the `id` parameter to `administrator`.
  ![6th screenshot](./attachments/6.png)

- Then get his password.
  ![7th screenshot](./attachments/7.png)

- Then login using the administrator's credentials `administrator:i7s666ue05d93j8gh6o2`, and access the admin panel.
  ![8th screenshot](./attachments/8.png)
  ![9th screenshot](./attachments/9.png)

- Then delete the user carlos, and the lab is solved.
  ![10th screenshot](./attachments/10.png)

---
