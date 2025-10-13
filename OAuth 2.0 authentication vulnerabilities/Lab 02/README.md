# Lab: SSRF via OpenID dynamic client registration

> Lab Objective: craft an SSRF attack to access `http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/` and steal the secret access key for the OAuth provider's cloud environment.

- Login using provided credentials `wiener:peter`, then inspect the login process.

- The Login Process:

  - You send a GET request to `/my-account`.
    ![1st screenshot](./attachments/1.png)
  - Then you're redirected to `/social-login`, that indicates that you'll be redirected to login with your social media account.
    ![2nd screenshot](./attachments/2.png)
  - then the Authorization Request is sent including `response_type=code` indicating that Authorization Code grant type is used.
    ![3rd screenshot](./attachments/3.png)
  - Then you're prompted to enter your credentials `wiener:peter`.
    ![4th screenshot](./attachments/4.png)
  - Then a POST request is sent with your submitted credentials.
    ![5th screenshot](./attachments/5.png)
  - Then you're prompted to provide your consent that your Profile and email data will be used by the client application (which is WeLikeToBlog).
    ![6th screenshot](./attachments/6.png)
  - If you agree, a confirmation request will be sent.
    ![7th screenshot](./attachments/7.png)
  - You'll be redirected to the callback URL specified in the authorization request and the authorization code is granted.
    ![8th screenshot](./attachments/8.png)
  - A GET Request is sent with the authorization code indicating a successful login.
    ![9th screenshot](./attachments/9.png)
  - Click continue and you'll be redirected to the root `/` page.
    ![10th screenshot](./attachments/10.png)
    ![11th screenshot](./attachments/11.png)

- Inspect the request where you retrieve the logo.
  ![12th screenshot](./attachments/12.png)

- Extract the OAuth server from the Host header and add `/.well-known/openid-configuration` to the url to access the configuration file.
  ![13th screenshot](./attachments/13.png)

- Access the `registration_endpoint` to register your client application.
  ![14th screenshot](./attachments/14.png)

- But firstly you need to customize a suitable POST request.
  ![15th screenshot](./attachments/15.png)

- And you'll notice that you've registered a Client Application without any kind of authentication.

- Therefore, you can use `logo_uri` with Burp Collaborator URL.
  ![16th screenshot](./attachments/16.png)

- Send the request where you retrieve the logo to Burp Repeater then replace the client ID with your client ID and send the request.
  ![17th screenshot](./attachments/17.png)

- Visit Burp Collaborator Tab, and you'll notice that there's an HTTP request sent to your Burp Collaborator
  ![18th screenshot](./attachments/18.png)

- Therefore, a Second-Order SSRF Vulnerability Exist.

- Therefore, instead of placing Burp Collaborator URL in `logo_uri`, place the internal admin panel `http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/`, and repeat this process again.
  ![19th screenshot](./attachments/19.png)
  ![20th screenshot](./attachments/20.png)

- Obtain the Secret Access Key, and submit it.
  ![21th screenshot](./attachments/21.png)

- And the lab is solved.
  ![22th screenshot](./attachments/22.png)

---
