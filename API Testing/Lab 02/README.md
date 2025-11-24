# Lab: Exploiting server-side parameter pollution in a query string

> lab objective: log in as the administrator and delete carlos.

- Capture the forget password request, you'll notice that `wiener` is not a valid username.
  ![1st screenshot](./attachments/1.png)

- But `administrator` is a valid username, and something is sent via administrator's email in order to complete the forget password process.
  ![2nd screenshot](./attachments/2.png)
  ![3rd screenshot](./attachments/3.png)

- If you repeated this request while monitoring requests made through network tab, you'll notice a request made to `forgotPassword.js`.

- While investigating this JS file, you'll notice that there's a potential parameter for `/forgot-password` endpoint which is `reset-token`.
  ![4th screenshot](./attachments/4.png)

- Send a GET request to `/forgot-password` while specifying a test reset token.
  ![5th screenshot](./attachments/5.png)

- Therefore, I can conclude that the reset token is used to reset the password.

- Back to forget password request again, If I tried to add an additional parameter, you'll receive the response normally.
  ![6th screenshot](./attachments/6.png)

- But if you url-encoded the `&` sign, You'll receive a `Parameter is not supported.` response.
  ![7th screenshot](./attachments/7.png)

- If you changed the `&` to `#` then url-encoded it, you'll receive a `Field not specified.` indicating the there's a `field` parameter that can be specified in the forget password POST request.
  ![8th screenshot](./attachments/8.png)

- If you added the field parameter after the `#` sign you'll receive an error.
  ![9th screenshot](./attachments/9.png)

- But if you place it before the has sign, you'll notice that it's accepted, but you concluded that the field parameter controls what is returned in the response body.
  ![10th screenshot](./attachments/10.png)

- If you changed the field parameter to email, the email value is returned in the response.
  ![11th screenshot](./attachments/11.png)

- The same happens if you stated the `username` as the value for `field` parameter.
  ![12th screenshot](./attachments/12.png)

- Same for `reset_token` specified in the `forgotPassword.js` file.
  ![13th screenshot](./attachments/13.png)

- But since that I want to reset the administrator's password, I'll change the username to `administrator`, and retrieve his `reset_token`.
  ![14th screenshot](./attachments/14.png)

- Place the retrieved reset token as the parameter for `/forgot-password` endpoint, and you're prompted to enter the new password.
  ![15th screenshot](./attachments/15.png)

- The request was accepted.
  ![16th screenshot](./attachments/16.png)

- If you logged in as administrator using those credentials `administrator:hacked`, you'll notice that you've logged in as administrator successfully.
  ![17th screenshot](./attachments/17.png)

- Access the admin panel.
  ![18th screenshot](./attachments/18.png)

- Then delete the user `carlos`, and the lab is solved.
  ![19th screenshot](./attachments/19.png)

---
