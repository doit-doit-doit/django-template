CREATE DATABASE [IF NOT EXISTS] `test` DEFAULT CHARACTER SET = `utf8` DEFAULT COLLATE = `utf8_general_ci`;
CREATE USER [IF NOT EXISTS] 'test'@'%' identified by '1234';
grant all privileges on test.* to 'test'@'%';