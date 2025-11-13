# Lab: Accidental exposure of private GraphQL fields

> Lab Objective: sign in as the administrator and delete the username carlos.

- Visit ay Product page, then inspect the request.

- You'll notice that it's a GraphQL Endpoint.
  ![1st screenshot](./attachments/1.png)

- Right CLick > GraphQL > Set Introspection Request, then traverse available mutations, and you'll find `getUser` mutation, with `id` as an argument.
  ![2nd screenshot](./attachments/2.png)

- Therefore, use the `getUser` mutation to retrieve the user with `id:1`, which is revealed to be the user.
  ![3rd screenshot](./attachments/3.png)

- Obtain the username & password, and login using those credentials
  ![4th screenshot](./attachments/4.png)

- And you're logged in as an administrator.
  ![5th screenshot](./attachments/5.png)

- Access the admin panel.
  ![6th screenshot](./attachments/6.png)

- Then delete the user carlos, and the lab is solved.
  ![7th screenshot](./attachments/7.png)

---
