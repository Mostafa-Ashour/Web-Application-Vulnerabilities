# Lab : Finding and exploiting an unused API endpoint

> Lab objective: exploit a hidden API endpoint to buy a Lightweight l33t Leather Jacket.

- Login using provided credentials `wiener:peter`, then add a Lightweight l33t Leather Jacket to your cart and inspect the request made.
  ![1st screenshot](./attachments/1.png)

- Send the request to repeater and change the HTTP request verb to OPTIONS, you'll notice that GET and PATCH methods are allowed.
  ![2nd screenshot](./attachments/2.png)

- Change the HTTP request verb to PATCH, then send the request, in order to know how to send a proper PATCH request.
  ![3rd screenshot](./attachments/3.png)

- Using 'Content Type Converter' extension, convert the content type to JSON.
  ![4th screenshot](./attachments/4.png)

- Send the converted request, and you'll notice that `price` parameter is required.
  ![5th screenshot](./attachments/5.png)

- The value for price must be non-negative integer.
  ![6th screenshot](./attachments/6.png)

- State the value of price to 0, and you'll notice that the request is accepted.
  ![7th screenshot](./attachments/7.png)

- And the price of the product has been changed to 0 on the website's product page.
  ![8th screenshot](./attachments/8.png)

- Try adding the product again to cart, and our modification has taken place.
  ![9th screenshot](./attachments/9.png)

- Place an order, and it's accepted, and the lab is solved.
  ![10th screenshot](./attachments/10.png)

---
