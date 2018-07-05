DROP DATABASE IF EXISTS `paranuara`;
CREATE DATABASE `paranuara`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON paranuara.* TO 'paranuara_govt'@'localhost' IDENTIFIED BY 'praise_the_fruit';

FLUSH PRIVILEGES;