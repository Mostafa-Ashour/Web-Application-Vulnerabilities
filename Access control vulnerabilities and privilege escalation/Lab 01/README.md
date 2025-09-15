# Lab: Unprotected admin functionality

> Lab Objective: Solve the lab by deleting the user carlos.

- Firstly, visit `robots.txt`, and you'll find Admin Panel path which is `/administrator-panel`
  ![1st screenshot](./attachments/1.png)

- Send a request to `/administrator-panel`, and you'll be able to access Admin Panel, also you'll be able to delete the user carlos via sending a `GET` request to `/administrator-panel/delete?username=carlos`.
  ![2nd screenshot](./attachments/2.png)

- Send a `GET` Request to `/administrator-panel/delete?username=carlos`.
  ![3rd screenshot](./attachments/3.png)

- Follow redirection to `/administrator-panel` and you'll find that the user has deleted successfully.
  ![4th screenshot](./attachments/4.png)

- And the lab is solved.
  ![5th screenshot](./attachments/5.png)

---
