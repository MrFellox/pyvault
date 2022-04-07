# PyVault

A webpage to manage your passwords.

## Installation

1. Create venv and install dependencies

```cmd
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

2. Install npm dependencies

```cmd
$ npm install ./
```

3. Create database

```cmd
$ cat db.sql | sqlite3
```

3. Run Flask

```cmd
$ python app.py
```

**IN CASE OF BAD STYLING, TRY TO UPDATE TAILWIND CSS**

```cmd
$ npx tailwindcss -i ./pyvault/static/styles.css -o ./pyvault/static/css/main.css
```
