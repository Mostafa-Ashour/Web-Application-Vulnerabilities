# Lab: Exploiting an API endpoint using documentation

> Lab Objective: find the exposed API documentation and delete carlos.

- Login using provided credentials `wiener:peter`, while letting Burp Suite Crawl the lab in order to construct a sitemap

- After Burp constructed the sitemap, you'll that there's two API related endpoints.
  ![1st screenshot](./attachments/1.png)
  ![2nd screenshot](./attachments/2.png)
  ![3rd screenshot](./attachments/3.png)

- Try changing the endpoint to `/api`.
  ![4th screenshot](./attachments/4.png)

- Then follow redirection to `/api/`, you'll notice that you've access to the API documentation.
  ![5th screenshot](./attachments/5.png)

- When observing User Documentation endpoint `/api/doc/User` from API Documentation, you'll notice that the User object has two parameters: Username & Email.
  ![6th screenshot](./attachments/6.png)
  ![7th screenshot](./attachments/7.png)

- You'll notice that when trying to GET the user object of Wiener (which is my account), I;m not authorized to do so.
  ![8th screenshot](./attachments/8.png)

- Change your email.
  ![9th screenshot](./attachments/9.png)

- If you changed the HTTP request verb to DELETE, and removed the request body, you'll notice that you're able to delete users (you've deleted your account).
  ![10th screenshot](./attachments/10.png)

- Therefore, restart the lab and repeat the same steps, but don't delete your account and replace your username with `carlos`, you'll notice that the user carlos is deleted.
  ![11th screenshot](./attachments/11.png)

- The lab is solved.
  ![12th screenshot](./attachments/12.png)

---
