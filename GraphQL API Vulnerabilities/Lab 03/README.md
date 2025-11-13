# Lab: Finding a hidden GraphQL endpoint

> Lab Objective: find the hidden endpoint and delete carlos.

- Traverse through the Lab while monitoring the Burp History, and you'll notice that there's no GraphQL endpoints.

- Therefore, run a simple Burp Scan in order to retrieve Graphql API Endpoints.
  ![1st screenshot](./attachments/1.png)

- When trying to set introspection query, you'll notice that it's not allowed.
  ![2nd screenshot](./attachments/2.png)

- But when adding Url Encoding of `\n` which is `\0a` after `__schema`, you'll be able to set introspection query, right click on the response then Graphql > Save GraphQ: Queries to sitemap.
  ![3rd screenshot](./attachments/3.png)

- When inspecting the available mutations, there's a mutation for deleting a user, but it needs the user's id, therefore I need to know carlos's id in order to use this mutation to delete him.

- there's another mutation `getUser` which takes `id` as an argument, I'll use it to enumerate users until I know carlos's id.
  ![4th screenshot](./attachments/4.png)

- After enumerating users, The Id of the user carlos is `3`.
  ![5th screenshot](./attachments/5.png)

- Right now, return to Site Map, and you'll find the `deleteOrganizationInput` mutation, send it to repeater, perform changes, and send the request.
  ![6th screenshot](./attachments/6.png)

- You'll notice that the request is accepted and the lab is solved.
  ![7th screenshot](./attachments/7.png)

---
