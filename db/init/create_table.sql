use test;

CREATE TABLE `boards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(30) DEFAULT NULL,
  `name` varchar(10) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

CREATE TABLE `comments` (
  `id` int DEFAULT NULL,
  `contents` varchar(100) DEFAULT NULL,
  KEY `id` (`id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`id`) REFERENCES `boards` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
