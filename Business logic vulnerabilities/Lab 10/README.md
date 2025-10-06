# Lab: Infinite money logic flaw

> Lab Objective: exploit the flaw in purchasing workflow to buy a "Lightweight l33t leather jacket".

- Login using provided credentials `wiener:peter`.

- Signup for newsletter and you'll get a 30% discount via `SIGNUP30` coupon.
  ![1st screenshot](./attachments/1.png)

- You'll notice that you can buy a gift card for $10 and it will redeem $10 into your balance.

- Add 1 Gift card to your card then apply the coupon.
  ![2nd screenshot](./attachments/2.png)

- Then place an order.
  ![3rd screenshot](./attachments/3.png)

- Take the gift card code and redeem it from My Account page, and you'll notice that your balance has increased by $3.
  ![4th screenshot](./attachments/4.png)
  ![5th screenshot](./attachments/5.png)

- Repeat this process again, and you'll notice that it succeeded.
  ![6th screenshot](./attachments/6.png)

- All you need to repeat is the following 4 requests:

  - Add 1 Gift Card to your cart.
    ![7th screenshot](./attachments/7.png)
  - Apply the coupon.
    ![8th screenshot](./attachments/8.png)
  - Perform checkout, and follow redirection to retrieve the gift card code.
    ![9th screenshot](./attachments/9.png)
    ![10th screenshot](./attachments/10.png)
  - Add the code in the request that redeems the gift card.
    ![11th screenshot](./attachments/11.png)

- Repeat this process using Burp Macro or a python script until you have enough money to buy the specified Jacket.
  ![12th screenshot](./attachments/12.png)

- Add the jacket to your cart.
  ![13th screenshot](./attachments/13.png)

- Place an order, and the lab is solved.
  ![14th screenshot](./attachments/14.png)

---
