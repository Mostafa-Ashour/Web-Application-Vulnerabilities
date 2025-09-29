# Lab: Information disclosure in version control history

> Lab Objective: obtain the password for the administrator user then log in and delete the user carlos.

- Try to access `/.git`, and you're able to access it normally.
  ![1st screenshot](./attachments/1.png)

- Therefore, download the `.git` file using the following command:

```
wget -r YOUR_LAB_ID/.git
```

![3rd screenshot](./attachments/3.png)

- To see the differences use the following command:

```
git diff
```

![2nd screenshot](./attachments/2.png)

- Firstly, see the commits log using `git log`.
  ![4th screenshot](./attachments/4.png)

- Secondly take the hash of the first commit then switch to this commit using `git checkout c5a37a546518db4e3d66e1dbd564ff10050dff31`
  ![5th screenshot](./attachments/5.png)

- Then run `ls -la` to see existing files and directories
  ![6th screenshot](./attachments/6.png)

- Finally, `cat admin.conf`, and you'll be able to retrieve the admin password.
  ![7th screenshot](./attachments/7.png)

- Login as an Admin using the following credentials `administrator:oflhfggag06ju42whvk7`
  ![8th screenshot](./attachments/8.png)

- Access the admin panel and delete the user carlos, and the lab is solved.
  ![9th screenshot](./attachments/9.png)

---
