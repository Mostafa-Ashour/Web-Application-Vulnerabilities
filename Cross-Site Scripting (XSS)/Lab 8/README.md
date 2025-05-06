# Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

> Lab Objective: submit a comment that calls the alert function when the comment author name is clicked.

- Firstly, Enter simple input like this `test'"><` in submitting a comment fields, then search for the input in the Source Code.

  > In order to know which character from those `'"><` are either HTML-Encoded, Stripped, etc.

  ![1st Screenshot](./Photos/1.png)

- In comment and name fields these characters `'"><` are HTML-Encoded, but in website field only `"` is html-encoded.
  ![2nd Screenshot](./Photos/2.png)

- Try using `javascript:alert(0)` in the website field when submitting a new comment.
  ![3rd Screenshot](./Photos/3.png)

- When submitting this comment and clicking on the author name, `alert(0)` function is executed successfully.
  ![4th Screenshot](./Photos/4.png)

- Therefore, the lab is solved successfully.
  ![5th Screenshot](./Photos/5.png)

---
