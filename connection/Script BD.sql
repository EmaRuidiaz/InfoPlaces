create database infoplaces;
use infoplaces;

create table person(
user_name	varchar(20) primary key,
first_name	varchar(20) not null,
last_name	varchar(20) not null,
type	int(1) not null,
email	varchar(30) not null,
password	varchar(20) not null,
birthdate	date not null,
phone_number	varchar(13));

create table shop(
id	int	auto_increment primary key,
name varchar(20),
street_name varchar(20),
street_num	varchar(20),
person	varchar(20),
foreign key(person) references person(user_name));

create table schedule(
id int auto_increment primary key,
shop int(11),
day	varchar(10),
turn	varchar(10),
opening	time,
closing	time,
foreign key(shop) references shop(id));


-- EJECUTAR DESDE ACÁ
drop table answer;
drop table comment;

create table comment(
id	int auto_increment primary key,
content varchar(150),
datetime	datetime,
idperson	varchar(20),
idshop	int,
foreign key(idperson) references person(user_name),
foreign key(idshop) references shop(id));

create table answer(
id	int auto_increment primary key,
content	varchar(150),
datetime	datetime,
idperson	varchar(20),
idcomment	int,
foreign key(idperson) references person(user_name),
foreign key(idcomment) references comment(id));

-- HASTA ACÁ

create table rating(
id	int auto_increment primary key,
id_person	varchar(20),
idshop	int,
rating	int(1),
foreign key(id_person) references person(user_name),
foreign key(idshop) references shop(id));

create table photo(
id	int auto_increment primary key,
user_name	varchar(20),
shop	int,
image	blob);

alter table shop add type varchar(15); #Le faltó a la def de shop.
alter table shop add description text;
INSERT INTO person(user_name, type, first_name, last_name, email, password, birthdate, phone_number) VALUES ('Owner', 2, 'Juan', 'Gonzales', "JuanGonzales@hotmail.com", "123456789", "1998-06-16", null);
INSERT INTO person(user_name, type, first_name, last_name, email, password, birthdate, phone_number) VALUES ('User', 1, 'Pepe', 'Diaz', "PepeDiaz@hotmail.com", "123456789", "2007-05-02", null);