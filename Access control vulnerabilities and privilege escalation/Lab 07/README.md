# Lab: User ID controlled by request parameter with data leakage in redirect

> Lab Objective: obtain the API key for the user carlos and submit it as the solution.

- Login using the provided credentials `wiener:peter`, then inspect the requests made.

- You'll notice that there's a request made to retrieve the account page for the user with id=wiener (my account) through this path `/my-account?id=wiener`.
  ![1st screenshot](./attachments/1.png)

- When changing the value of the id parameter to carlos, you'll be redirected to the login page.
  ![2nd screenshot](./attachments/2.png)

- But when viewing the source code before following the redirection, you'll notice that you have the API Key of carlos.
  ![3rd screenshot](./attachments/3.png)

- Therefore, submit the api key of the user carlos and the lab is solved.
  ![4th screenshot](./attachments/4.png)

---
