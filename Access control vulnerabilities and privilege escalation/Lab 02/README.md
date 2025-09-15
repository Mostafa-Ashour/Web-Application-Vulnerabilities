# Lab: Unprotected admin functionality with unpredictable URL

> Lab Objective: Solve the lab by accessing the admin panel, and using it to delete the user carlos.

- `robots.txt` file is not found.
  ![1st screenshot](./attachments/1.png)

- Same as trying to access `admin` or `administrator-panel` endpoints.
  ![2nd screenshot](./attachments/2.png)

- But when viewing source code, you'll a JS code the identifies the path to the admin panel as `/admin-hh6rux`
  ![3rd screenshot](./attachments/3.png)

- When accessing this path you will be able to access the admin panel and deleting the user carlos via sending a `GET` request to `/admin-hh6rux/delete?username=carlos`.
  ![4th screenshot](./attachments/4.png)

- Send a `GET` request to `/admin-hh6rux/delete?username=carlos`, then follow redirection to `/admin-hh6rux` and you'll notice that the user is successfully deleted.
  ![5th screenshot](./attachments/5.png)
  ![6th screenshot](./attachments/6.png)

- And the lab is solved.
  ![7th screenshot](./attachments/7.png)

---
