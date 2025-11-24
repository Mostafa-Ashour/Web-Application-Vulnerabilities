# Lab: Exploiting server-side parameter pollution in a REST URL

> Lab Objective: log in as the administrator and delete carlos.

- Capture the request made to `/forgot-password` to endpoint.
  ![1st screenshot](./attachments/1.png)

- If you added `#` to the end of the username, you'll notice that the response indicates an invalid route and to check the API definition for further information.
  ![2nd screenshot](./attachments/2.png)

- Which is an indication of path traversal vulnerability to access API Documentation.

- If you added `./` before a valid username (`administrator`, for instance), you'll notice that the response is valid with no errors, indicating that I can traverse through the file system.
  ![3rd screenshot](./attachments/3.png)

- For instance, I'm going to search for `openapi.json` which is an endpoint that might point to the API documentation.
  ![4th screenshot](./attachments/4.png)
  ![5th screenshot](./attachments/5.png)
  ![6th screenshot](./attachments/6.png)

- After several failed trials, this path `../../../../openapi.json` results in an error.
  ![7th screenshot](./attachments/7.png)

- But since the back-end server, builds the API URL internally, therefore using `#` (in the url-encoded form) at the end of the path, will result in the revealing of API Definition.
  ![8th screenshot](./attachments/8.png)

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "User API",
    "version": "2.0.0"
  },
  "paths": {
    "/api/internal/v1/users/{username}/field/{field}": {
      "get": {
        "tags": ["users"],
        "summary": "Find user by username",
        "description": "API Version 1",
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "Username",
            "required": true,
            "schema": {}
          }
        ]
      }
    }
  }
}
```

- Since this `/api/internal/v1/users/{username}/field/{field}` is the path, therefore placing `administrator/field/test%23` as the username, results in an error in the response indicating that the only allowed field is `email`.
  ![9th screenshot](./attachments/9.png)

- When specifying the email as the field, it returns the normal request as if specifying a valid username within the username parameter.
  ![10th screenshot](./attachments/10.png)

- But when changing the API version to `v1` through this path `../../v1/users/administrator/field/test%23`, the error message in the response changed, indicating that there might be another fields I'm able to retrieve through field parameter.
  ![11th screenshot](./attachments/11.png)

- Inspect requests made when loading forget password page from Network Tab, you'll notice that there a js file called `forgotPassword.js` which contains the parameter name for the reset token called `passwordResetToken`.

- Include it in the field, and you'll be able to retrieve the password reset token for the administrator.
  ![12th screenshot](./attachments/12.png)

- Use this token to change the administrator's password.
  ![13th screenshot](./attachments/13.png)

- Login as the admin, and access the admin panek.
  ![14th screenshot](./attachments/14.png)
  ![15th screenshot](./attachments/15.png)

- Delete the user carlos and the lab is solved.
  ![16th screenshot](./attachments/16.png)

---
