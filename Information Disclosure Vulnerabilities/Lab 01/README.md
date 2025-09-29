# Lab: Information disclosure in error messages

> Lab Objective: obtain and submit the version number of this framework.

- View Details for any product, and you'll notice that the request sent was to this endpoint `/product?productId=1`.
  ![1st screenshot](./attachments/1.png)

- Modify the value of the `productId` parameter to `testabc`, and you'll notice that you've received and error message including the Framework version, which is `2.3.31`.
  ![2nd screenshot](./attachments/2.png)

- Submit this value and the lab is solved.
  ![3rd screenshot](./attachments/3.png)

---
