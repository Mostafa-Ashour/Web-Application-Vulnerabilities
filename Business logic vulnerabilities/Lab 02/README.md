# Lab: High-level logic vulnerability

> Lab Objective: buy a "Lightweight l33t leather jacket".

- Login using provided credentials `wiener:peter`, then inspect normal behavior for purchase process.

- Normal Process:

  - Visit product page.
  - Add it to cart.
    ![1st screenshot](./attachments/1.png)
  - View Your cart.
    ![2nd screenshot](./attachments/2.png)
  - Place order (even you don't have enough balance).
    ![3rd screenshot](./attachments/3.png)

- When adding arbitrary big numbers, it's accepted.
  ![4th screenshot](./attachments/4.png)

- Try adding negative amount, it's also accepted.
  ![5th screenshot](./attachments/5.png)
  ![6th screenshot](./attachments/6.png)

- Therefore:

  - Add 1 jacket.
    ![7th screenshot](./attachments/7.png)
    ![8th screenshot](./attachments/8.png)
  - then add another product with negative numbers until total price is less than your balance.
    ![9th screenshot](./attachments/9.png)

- Currently, the total price is $9.05, try to place an order, and it's placed successfully, and the lab is solved.
  ![10th screenshot](./attachments/10.png)
