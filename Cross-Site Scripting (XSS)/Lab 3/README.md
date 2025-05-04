# Lab: DOM XSS in document.write sink using source location.search

> Lab Objective: perform a cross-site scripting attack that calls the alert function.

- Firstly, Enter simple input like this `test'"><` in search query tracking functionality, then search for the input in the Source Code.

  > In order to know which character from those `'"><` are either HTML-Encoded, Stripped, etc.

- When you search for the input in the source code, you'll see that these characters `'"><` are HTML-Encoded.
  ![1st Screenshot](./Photos/1.png)

- But you'll find JS code that manipulates User Input using DOM.
  ![2nd Screenshot](./Photos/2.png)

- The Code gets the value associated with the parameter **_search_**, then appends it in an image tag, using `document.write` without proper validation/sanitization for user input.
  ![3rd Screenshot](./Photos/3.png)

- I'll use the fact that `document.write` function accepts script elements, and include this payload `"><script>alert(0)</script><!--`

  > this payload will close the `img` tag created by `document.write` function, then append the `script` and comments trailing characters

- When entering the previous payload in search query tracking functionality, `alert` function is executed successfully.
  ![4th Screenshot](./Photos/4.png)

- Code after payload being executed.
  ![5th Screenshot](./Photos/5.png)

- Therefore, the Lab is solved Successfully.
  ![6th Screenshot](./Photos/6.png)

---
