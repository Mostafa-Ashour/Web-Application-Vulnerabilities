# Lab: Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped

> Lab Objective: perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function.

- Firstly, Enter simple input like this `test'"><` in the search query tracking functionality, then search for the input in the Source Code.

  > In order to know which character from those `'"><` are either HTML-Encoded, Stripped, etc.

- when viewing the page source code The Input appeared twice.

  - The First time within a `h1` tag with `'"><` html encoded.
    ![1st Screenshot](./Photos/1.png)
  - The second time within a JS string with `'` escaped and `"><` html encoded.
    ![2nd Screenshot](./Photos/2.png)

- I'll inject within the second time with `test\'` to see if it can break out the string, `\` has deon it's job.
  ![3rd Screenshot](./Photos/3.png)

- So inject this payload `test\';alert(0);//`, and the `alert` function is executed successfully.
  ![4th Screenshot](./Photos/4.png)

- Therefore the Lab is solved successfully.
  ![5th Screenshot](./Photos/5.png)

---
