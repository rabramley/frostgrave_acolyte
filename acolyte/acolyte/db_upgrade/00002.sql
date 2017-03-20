CREATE TABLE spell (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    school_id INT NOT NULL,
    required INT NOT NULL,
    target VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY(school_id) REFERENCES school(id)
)
;
