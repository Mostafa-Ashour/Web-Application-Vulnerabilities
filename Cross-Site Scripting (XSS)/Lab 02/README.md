# Lab: Stored XSS into HTML context with nothing encoded

> Lab Objective: submit a comment that calls the `alert` function when the blog post is viewed.

- Firstly, Enter input like this `test'"><` for comment input fields, then search for the input in the Source Code.

  > In order to know which character from those `'"><` are either HTML-Encoded, Stripped, etd.

  ![1st Screenshot](./Photos/1.png)

- You'll see that the displayed content `test'"><` is displayed and interpreted normally.
  ![2nd Screenshot](./Photos/2.png)

- Therefore, try this payload `<script>alert(0)</script>` in the comment input field.

- When clicking on 'back to blog' button, `alert` function will be executed.
  ![3rd Screenshot](./Photos/3.png)
  ![4th Screenshot](./Photos/4.png)

- The lab is solved successfully
  ![5th Screenshot](./Photos/5.png)

---
