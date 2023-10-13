
-- Create database table

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

-- Generate some dummy data
INSERT INTO task (
    summary,
    description
)
    VALUES (
        "Do dishes",
        "Use dish detergent and do the dishes"
    ),
    (
        "Feed dog",
        "Feed the dog some kibble"
    ),
    (
        "Wash car",
        "Take the car down to the car wash"
    )
    ;
    