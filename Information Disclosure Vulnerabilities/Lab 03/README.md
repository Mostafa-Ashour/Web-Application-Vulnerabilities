# Lab: Source code disclosure via backup files

> Lab Objective: identify and submit the database password, which is hard-coded in the leaked source code.

- View Details for any product, then inspect the endpoint, which is `/product?productId=1`.
  ![1st screenshot](./attachments/1.png)

- Change the value of productId `parameter` to `testabc`, you'll notice that there's no error messages appeared.
  ![2nd screenshot](./attachments/2.png)

- Try to view source code for this normal endpoint `/product?productId=1`, and you'll notice that there's no useful comments or paths exist.
  ![3rd screenshot](./attachments/3.png)

- Try to access `/robots.txt` file, and you'll find a backup directory located at `/backup`.
  ![4th screenshot](./attachments/4.png)

- Access this folder using the provided path `/backup`.
  ![5th screenshot](./attachments/5.png)

- You'll find a source code file with the name of `ProductTemplate.java.bak`.

- Access this source code file, and you'll find a function that initiates a connection with the Database.
  ![6th screenshot](./attachments/6.png)

- Submit this `by30soymieol9fbos6r8pj19gh7tdojm` as the database password, and the lab is solved.
  ![7th screenshot](./attachments/7.png)

---
