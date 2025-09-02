# Lab: SSRF with whitelist-based input filter

> Lab Objective: change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos

- Check Stock for any product then inspect the Request.

- You'll notice that the Request utilizes an URL that is used by the server to fetch the stock number for the specified product.

- When changing the value of stockAPi to `http://localhost`, it's blocked.
  ![1st screenshot](./attachments/1.png)

- When placing the normal URL but adding `localhost.` to the beginning of it, it's blocked:

  - The Payload (it's URL encoded before the request is sent):
    `http://localhost.stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1`

  ![2nd screenshot](./attachments/2.png)

- But when using this format `http://localhost:80#@stock.weliketoshop.net:8080` (with # double url encoded), the response will be internal server error.
  ![3rd screenshot](./attachments/3.png)

- When using the following payload the user carlos is deleted and the lab is solved:
  `http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos`
  ![4th screenshot](./attachments/4.png)

---
