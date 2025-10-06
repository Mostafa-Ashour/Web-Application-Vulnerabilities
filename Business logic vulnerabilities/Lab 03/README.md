# Lab: Inconsistent security controls

> Lab Objective: access the admin panel and delete the user carlos.

- When you try to access the admin interface `/admin`, you're not authorized to access it.
  ![1st screenshot](./attachments/1.png)

- Try to register an account you control, but in the email part add `@dontwannacry.com`.
  ![2nd screenshot](./attachments/2.png)

- But I have to check my email, and it's not actually mine (and it doesn't exist).
  ![3rd screenshot](./attachments/3.png)

- But when using a real email (provided by portswigger), it actually worked.
  ![4th screenshot](./attachments/4.png)
  ![5th screenshot](./attachments/5.png)

- Just click the link sent to you via your email, and the registration process will be completed.
  ![6th screenshot](./attachments/6.png)

- Login using registered credentials `Hacker:123456`.

- You'll notice that there is an Update Email functionality.
  ![7th screenshot](./attachments/7.png)

- Try to update your email to `attacker@dontwannacry.com`
  ![8th screenshot](./attachments/8.png)

- You'll notice that the email is changed successfully, and the admin panel is shown in your account page.
  ![9th screenshot](./attachments/9.png)

- Access the Admin Panel.
  ![10th screenshot](./attachments/10.png)

- Delete the user carlos, and the lab is solved.
  ![11th screenshot](./attachments/11.png)

---
