# Lab: Blind OS command injection with out-of-band interaction

> Lab Objective: exploit the blind OS command injection vulnerability to issue a DNS lookup to Burp Collaborator.

- Submit a feedback then inspect the request.
  ![1st screenshot](./attachments/1.png)

- Inject this command `& echo Ashour &` within any parameter, you'll notice no change in the response.
  ![2nd screenshot](./attachments/2.png)

- Therefore, I'll try to trigger the application to make a DNS Lookup to a Domain I control (I'm using Burp Collaborator, you can use anything to achieve the same goal).

- Try inject this command `& nslookup Burp-Collaborator-Domain &` within email parameter.
  ![3rd screenshot](./attachments/3.png)

- View Burp Collaborator tab and Poll Now, you'll notice that the DNS Lookup has been made.
  ![4th screenshot](./attachments/4.png)

- And the lab is solved.
  ![5th screenshot](./attachments/5.png)

---
