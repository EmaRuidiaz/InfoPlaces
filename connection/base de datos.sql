create database InfoPlaces;
use InfoPlaces;

create table PERSON (
id int primary key auto_increment,
user_name varchar(20) not null,
`type` int(1) not null,
first_name varchar(20) not null,
last_name varchar(20) not null,
email varchar(30) not null,
`password` varchar(20) not null);

create table SHOP (
id int primary key auto_increment,
`name` varchar(20) not null,
street_name varchar(30) not null,
street_num int(6),
phone_num int(13),
id_person int not null,
foreign key (id_person) references PERSON(id));

create table `COMMENT` (
id int primary key auto_increment,
content varchar(150) not null,
`datetime` datetime not null,
id_person int not null,
foreign key (id_person) references PERSON(id),
id_shop int not null,
foreign key (id_shop) references SHOP(id));

create table ANSWER (
id int primary key auto_increment,
content varchar(150) not null,
`datetime` datetime not null,
id_person int not null,
foreign key (id_person) references PERSON(id),
id_comment int not null,
foreign key (id_comment) references `COMMENT`(id));

create table RATING (
id int primary key auto_increment,
id_person int,
foreign key (id_person) references PERSON(id),
id_shop int,
foreign key (id_shop) references SHOP(id),
rating int);