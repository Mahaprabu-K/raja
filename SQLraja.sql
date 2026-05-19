CREATE DATABASE StudentDB;
GO

USE StudentDB;
GO

CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    age INT
);
GO


select * from users;
