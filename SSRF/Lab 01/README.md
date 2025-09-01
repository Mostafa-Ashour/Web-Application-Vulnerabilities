# Lab: Basic SSRF against the local server

> Lab Objective: change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

- Check Stock for any product, then inspect the request sent.

- You'll notice that the request passes an URL to the server which is used to retrieve the Stock number for specified product.
  ![1st screenshot](./attachments/1.png)

- Change the value of `stockApi` to `http://localhost`, you'll notice that the response contain the Home Page with an Admin Panel Path.
  ![2nd screenshot](./attachments/2.png)
  ![3rd screenshot](./attachments/3.png)

- Change the value of `stockApi` to `http://localhost/admin`, you'll notice that you've accessed the Admin Panel, and you can delete existing users through a get request, for instance: `/admin/delete?username=carlos`
  ![4th screenshot](./attachments/4.png)
  ![5th screenshot](./attachments/5.png)

- The Lab Objective is to delete the user carlos, therefore change the stockApi value to `http://localhost/admin/delete?username=carlos`.

- The user was deleted successfully.
  ![6th screenshot](./attachments/6.png)
  ![7th screenshot](./attachments/7.png)

- the lab is solved successfully.
  ![8th screenshot](./attachments/8.png)

---
