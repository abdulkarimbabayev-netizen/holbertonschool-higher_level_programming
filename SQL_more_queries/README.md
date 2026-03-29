# SQL More Queries - Task 0: Privileges

## Description
This task focuses on displaying the privileges of MySQL users using the `SHOW GRANTS` statement.

## Files
- `0-privileges.sql` - SQL script that lists all privileges for users `user_0d_1` and `user_0d_2`

## Requirements
- MySQL server running on localhost
- Root access to MySQL
- Users `user_0d_1` and `user_0d_2` must exist

## Usage

### Execute the script:
```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

## Expected Output
The script will display the GRANT statements for each user, showing all their privileges on the server.

## SQL Syntax Explained
- `SHOW GRANTS FOR 'username'@'hostname';` - Displays all privileges granted to a specific user
