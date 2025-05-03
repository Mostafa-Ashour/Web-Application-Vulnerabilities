# Lab: Blind SQL injection with time delays

> Lab Objective: exploit the SQL injection vulnerability to cause a 10 second delay.

- Firstly, run the Burp with interception off (we'll look the history in a while), then filter products based on category.

- Look at that request in the burp, send to repeater, you'll see that there is a tracking id in the cookie
  ![1st Screenshot](./Photos/1.png)

- Then try to concat time delays payloads of different DBMSs, this is the only one that will work

  - The Payload: `'||pg_sleep(10)--+-`
    ![2nd Screenshot](./Photos/2.png)

- Therefore the lab is solved.
  ![3rd Screenshot](./Photos/3.png)
