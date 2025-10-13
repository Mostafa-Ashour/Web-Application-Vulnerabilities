# Lab: Authentication bypass via OAuth implicit flow

> Lab Objective: exploit the flawed validation by the client application, then log in to Carlos's account

- Login using provided credentials `wiener:peter`, then inspect the login process.

- The Login Process:

  - You access `/my-account` endpoint, then You're redirected to `/social-login`
    ![1st screenshot](./attachments/1.png)
  - A GET request is sent to `/social-login`, indicating that you'll be redirected to login using your social media account.
    ![2nd screenshot](./attachments/2.png)
  - Then the Authorization Request for Implicit Grant Type is sent.
    ![3rd screenshot](./attachments/3.png)
  - Then You're prompted to enter your login credentials `wiener:peter`.
    ![4th screenshot](./attachments/4.png)
  - You send a POST request with your login credentials.
    ![5th screenshot](./attachments/5.png)
  - Then you're prompted again but for your consent on provisioning access for your profile and email.
    ![6th screenshot](./attachments/6.png)
  - If you agree, a confirm request will be sent.
    ![7th screenshot](./attachments/7.png)
  - Then you're redirected to the callback specified in the Authorization request, and the access token is sent to the Client Application.
    ![8th screenshot](./attachments/8.png)
    ![9th screenshot](./attachments/9.png)
  - Then an API call is made to retrieve your data via a GET request to `/me` endpoint.
    ![10th screenshot](./attachments/10.png)
  - Then a POST request sent to `/authenticate`, with your data retrieved from the previous request.
    ![11th screenshot](./attachments/11.png)
  - Then you're redirected to `/`, and you're authenticated successfully.
    ![12th screenshot](./attachments/12.png)

- In the `/authenticate` POST request, replace your email with `carlos@carlos-montoya.net` and your username with `carlos`, then send the request.
  ![13th screenshot](./attachments/13.png)

- Right Click on the request, "Request in Browser" > "In Original Session", then copy the URL and paste it in your Browser, then access my Account, and you're logged in as carlos and the lab is solved.
  ![14th screenshot](./attachments/14.png)

- Or after sending the `/authenticate` request, copy the issued cookie paste it in your burp request, then send a request to `/`, then `/my-account?id=carlos`, and you'll achieve the same result.
  ![15th screenshot](./attachments/15.png)
  ![16th screenshot](./attachments/16.png)

---
