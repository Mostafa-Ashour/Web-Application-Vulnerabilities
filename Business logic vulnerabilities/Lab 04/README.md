# Lab: Flawed enforcement of business rules

> Lab Objective: exploit the flaw in purchasing workflow to buy a "Lightweight l33t leather jacket".

- Login using provided credentials `wiener:peter`, you'll notice that there is a discount coupon for new customers (which is `NEWCUST5`).
  ![1st screenshot](./attachments/1.png)

- Add a product and apply the coupon code.
  ![2nd screenshot](./attachments/2.png)

- Sign to the newsletter at the footer of the page, and you'll gain another coupon `SIGNUP30`.
  ![3rd screenshot](./attachments/3.png)
  ![4th screenshot](./attachments/4.png)

- If you tried to apply the same coupon twice, it'll be rejected
  ![5th screenshot](./attachments/5.png)

- But if you apply `NEWCUST5`, then `SIGNUP30`, then `NEWCUST5` again, it'll be aplied twice normally
  ![6th screenshot](./attachments/6.png)

- Therefore, alternate between them until you reach Zero dollars.
  ![7th screenshot](./attachments/7.png)

- Place Order, and the lab is solved.
  ![8th screenshot](./attachments/8.png)

---
