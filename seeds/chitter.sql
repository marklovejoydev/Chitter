-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    username text,
    email text,
    password text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, username, email, password) VALUES ('Mark Lovejoy', 'lovejoy01', 'marklovejoy@gmail.com', 'Test123');

