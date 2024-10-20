CREATE DATABASE IF NOT EXISTS `dst_data`;
USE dst_data;

CREATE TABLE IF NOT EXISTS kyoto_dst (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_tag DATETIME,
    dst FLOAT
);
