# Lab: Excessive trust in client-side controls

> Lab Objective: buy a "Lightweight l33t leather jacket".

- Login using provided credentials `wiener:peter`.

- Then visit `Lightweight "l33t" Leather Jacket` Product page, and add 1 piece of this product to the cart and intercept this request.

- You'll notice that the price of the product is sent within the request via POST data.
  ![1st screenshot](./attachments/1.png)

- If you've sent a normal behavior without manipulation, the product will be added to the cart with it's normal price.
  ![2nd screenshot](./attachments/2.png)

- But return to the add to cart request and change the product price to 0, then view your cart.
  ![3rd screenshot](./attachments/3.png)

- When viewing your cart, you'll notice that the product wasn't added.
  ![4th screenshot](./attachments/4.png)

- Return to add to cart request again, and change the price to 1.
  ![5th screenshot](./attachments/5.png)

- View you cart, and you'll notice that the price of the product has changed to $0.01.
  ![6th screenshot](./attachments/6.png)

- Place order for this amount of money, you'll notice that the order is placed with $0.01 and the lab is solved.
  ![7th screenshot](./attachments/7.png)

---
