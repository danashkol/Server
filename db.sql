create table users
(
    id       int auto_increment
        primary key,
    userName varchar(30)  null,
    name     varchar(30)  null,
    email    text         null,
    password varchar(120) null
);

INSERT INTO one.users (id, userName, name, email, password) VALUES (6, 'User1', 'Yossi', 'yos@gmail.com', '1234');
INSERT INTO one.users (id, userName, name, email, password) VALUES (7, 'User2', 'Shimon', 'shim@gmail.com', '2345');
INSERT INTO one.users (id, userName, name, email, password) VALUES (8, 'User3', 'Romi', 'romi@gmail.com', '3456');
INSERT INTO one.users (id, userName, name, email, password) VALUES (9, 'User4', 'Noam', 'noam@gmail.com', '4567');
INSERT INTO one.users (id, userName, name, email, password) VALUES (10, 'User5', 'Lior', 'lior@gmail.com', '5678');
