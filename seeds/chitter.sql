-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS peeps CASCADE;
DROP SEQUENCE IF EXISTS peeps_id_seq;

DROP TABLE IF EXISTS users CASCADE;
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

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    time TIME,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, username, email, password) VALUES ('Mark Lovejoy', 'lovejoy01', 'marklovejoy@gmail.com', '$2b$12$ACQTlgOvHATuVHbR8kus/OUNihpeEaequhPHKdQltSV0CGTQOGCl2');

INSERT INTO peeps (title, content, time, user_id) VALUES ('My First Peep', 'This is the content of my first peep.', '12:34', 1);
