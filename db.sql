CREATE TABLE users(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    service_name TEXT NOT NULL,
    service_username TEXT NOT NULL,
    service_email TEXT NOT NULL,
    password TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

.save "pyvault.db"
.exit