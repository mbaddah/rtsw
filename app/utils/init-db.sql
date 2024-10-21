CREATE DATABASE IF NOT EXISTS `dst_data`;
USE dst_data;

CREATE TABLE IF NOT EXISTS solar_wind (
        id INT AUTO_INCREMENT PRIMARY KEY,
        time_tag DATETIME,
        bx_gsm FLOAT,
        by_gsm FLOAT,
        bz_gsm FLOAT,
        lon_gsm FLOAT,
        lat_gsm FLOAT,
        bt FLOAT
);
