# Lab: Accessing private GraphQL posts

> Lab Objective: find the hidden blog post and enter the password.

- Access any product, and intercept the request.
  ![1st screenshot](./attachments/1.png)

- Right click on the request > Graphql > Set introspection query, then send the request.

- You'll have access to the mutations for `/graphql/v1` endpoint, including `getAllBlogPost` mutation.
  ![2nd screenshot](./attachments/2.png)

- Use `getAllBlogPost` mutation to retrieve all existing blogs/
  ![3rd screenshot](./attachments/3.png)

- You'll notice that Blog Post with id = 3 is missing, indicating that it's private.

- Therefore, use `getBlogPost` mutation with `id:3` as an argument to retrieve the private blog post.
  ![4th screenshot](./attachments/4.png)

- Retrieve the postPassword value then submit it, and the lab is solved.
  ![5th screenshot](./attachments/5.png)

---
