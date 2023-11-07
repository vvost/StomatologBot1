create database smth_wrong;
use smth_wrong
create table stomatolog_application(
	id bigint AUTO_INCREMENT PRIMARY KEY, 
	first_name varchar(100),
	last_name varchar(100), 
	contact_info varchar(100), 
	service varchar(100), 
	appointment_date date, 
	end_time time(6), 
	start_time time(6)
    );