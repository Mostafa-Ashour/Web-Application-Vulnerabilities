# Lab: SSRF with blacklist-based input filter

> Lab Objective: change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

- Check Stock for any product, and inspect the request.

- You'll notice that the POST request utilizes a URL which is used to fetch the stock number of a specified product.
  ![1st screenshot](./attachments/1.png)

- Set the value of stockApi to `http://localhost/` and `http://127.0.0.1/`, and you'll notice that external requests to check stock is blocked.
  ![2nd screenshot](./attachments/2.png)
  ![3rd screenshot](./attachments/3.png)

- When using the shorthand for Localhost IP `http://127.1/`, I was able to retrieve the home page which includes the Admin Panel at `/admin`
  ![4th screenshot](./attachments/4.png)
  ![5th screenshot](./attachments/5.png)

- But when using this path `http://127.1/admin/`, but it was blocked.
  ![6th screenshot](./attachments/6.png)

- But when using `http://127.1/AdMiN/` you'll be able to get the Admin Panel and delete the user carlos through this get request `/admin/delete?username=carlos`
  ![7th screenshot](./attachments/7.png)
  ![8th screenshot](./attachments/8.png)

- Set the value of stockApi to `http://127.1/AdMiN/delete?username=carlos`, and the user carlos was deleted successfully.
  ![9th screenshot](./attachments/9.png)
  ![10th screenshot](./attachments/10.png)

- The Lab is solved successfully.
  ![11th screenshot](./attachments/11.png)

---
