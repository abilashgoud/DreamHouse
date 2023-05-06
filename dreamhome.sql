CREATE DATABASE dreamhome;
USE dreamhome;

CREATE TABLE branch
(branchNo int PRIMARY key,
 address varchar(35) NOT NULL,
 city varchar(20) NOT NULL,
 postcode varchar(10) NOT NULL,
 teleNo char(15) NOT NULL,
 constraint branch_city_check check (length(city)>=3 and length(city)<=20)
);

INSERT INTO branch (branchNo, address, city, postcode, teleNo) VALUES
(1001, '123 Main St', 'New York', '10001', '555-1234'),
(1002, '456 Market St', 'San Francisco', '94103', '555-5678'),
(1003, '789 Broadway', 'New York', '10003', '555-9012'),
(1004, '321 Pine St', 'Seattle', '98101', '555-3456'),
(1005, '654 Oak St', 'Los Angeles', '90001', '555-7890');

CREATE TABLE staff
(staffNo int PRIMARY KEY ,
 fName varchar(40) NOT NULL,
 position varchar(10) NOT NULL,
 supervisorNo int default null,
 sex char(1) check(sex in('M','F')) NOT NULL,
 DOB date NOT NULL,
 salary int NOT NULL check(salary >0),
 branchNo int NOT NULL,
 managerStartDate date default null,
 foreign key (branchNo) references branch(branchNo)
);

INSERT INTO staff (staffNo, fName, position, supervisorNo, sex, DOB, salary, branchNo, managerStartDate) 
VALUES 
(50001, 'John Doe', 'Manager', NULL, 'M', '1985-01-15', 70000, 1001, '2019-01-01'),
(50002, 'Jane Smith', 'Assistant', 50001, 'F', '1990-06-22', 40000, 1001, NULL),
(50003, 'Tom Wilson', 'Assistant', 50001, 'M', '1992-09-05', 45000, 1001, NULL),
(50004, 'Emily Chen', 'Manager', NULL, 'F', '1982-04-18', 75000, 1002, '2018-03-01'),
(50005, 'Peter Lee', 'Assistant', 50004, 'M', '1993-11-09', 42000, 1002, NULL),
(50006, 'Maggie Johnson', 'Assistant', 50004, 'F', '1991-02-28', 47000, 1002, NULL),
(50007, 'James Brown', 'Manager', NULL, 'M', '1978-07-13', 80000, 1003, '2017-06-01'),
(50008, 'Sarah Davis', 'Assistant', 50007, 'F', '1994-12-04', 43000, 1003, NULL),
(50009, 'Chris Taylor', 'Assistant', 50007, 'M', '1989-03-20', 48000, 1003, NULL),
(50010, 'Anna Kim', 'Manager', NULL, 'F', '1980-11-12', 90000, 1004, '2016-05-01'),
(50011, 'Kevin Wong', 'Assistant', 50010, 'M', '1995-08-07', 44000, 1004, NULL),
(50012, 'Olivia Lee', 'Assistant', 50010, 'F', '1990-01-25', 49000, 1004,NULL),
(50013, 'David Lee', 'Manager', NULL, 'M', '1981-06-09', 85000, 1005, '2015-01-01'),
(50014, 'Samantha Brown', 'Assistant', 50013, 'F', '1992-04-02', 46000, 1005, NULL),
(50015, 'Alex Johnson', 'Assistant', 50013, 'M', '1987-09-18', 51000, 1005, NULL);

CREATE TABLE privateOwner
(ownerNo int PRIMARY KEY ,
 fName varchar(40) NOT NULL,
 address varchar(50) NOT NULL,
 telNo char(15) NOT NULL,
 email varchar(50) UNIQUE NOT NULL
);

INSERT INTO privateOwner (ownerNo, fName, address, telNo, email)
VALUES
(60001, 'John Smith', '123 Main St', '555-1234', 'jsmith@email.com'),
(60002, 'Mary Johnson', '456 Maple Ave', '555-5678', 'mjohnson@email.com'),
(60003, 'James Brown', '789 Oak St', '555-9012', 'jbrown@email.com'),
(60004, 'Emily Davis', '234 Elm St', '555-3456', 'edavis@email.com'),
(60005, 'David Wilson', '567 Pine St', '555-7890', 'dwilson@email.com'),
(60006, 'Susan Lee', '890 Cedar St', '555-1234', 'slee@email.com'),
(60007, 'Robert Johnson', '123 Main St', '555-5678', 'rjohnson@email.com'),
(60008, 'Jessica Garcia', '456 Maple Ave', '555-9012', 'jgarcia@email.com'),
(60009, 'William Davis', '789 Oak St', '555-3456', 'wdavis@email.com'),
(60010, 'Amanda Perez', '234 Elm St', '555-7890', 'aperez@email.com'),
(60011, 'Michael Wilson', '567 Pine St', '555-1234', 'mwilson@email.com'),
(60012, 'Jennifer Martinez', '890 Cedar St', '555-5678', 'jmartinez@email.com'),
(60013, 'Christopher Thompson', '123 Main St', '555-9012', 'cthompson@email.com'),
(60014, 'Ashley Hernandez', '456 Maple Ave', '555-3456', 'ahernandez@email.com'),
(60015, 'Daniel Brown', '789 Oak St', '555-7890', 'dbrown@email.com');

CREATE TABLE propertyForRent
(propertyNo int PRIMARY KEY ,
 address varchar(35),
 city varchar(20),
 postcode varchar(10),
 type varchar(10),
 rooms smallint,
 rent int,
 currentStatus char(3) check(currentStatus in('Y','N')),
 ownerNo int NOT NULL,
 staffNo int,
 branchNo int,
 foreign key (ownerNo) references privateOwner(ownerNo),
 foreign key (staffNo) references staff(staffNo),
 foreign key (branchNo) references branch(branchNo)
);

INSERT INTO propertyForRent (propertyNo, address, city, postcode, type, rooms, rent, currentStatus, ownerNo, staffNo, branchNo) VALUES 
(3001, '123 Main St', 'New York', '10001', 'Apartment', 2, 2000, 'Y', 60001, 50001, 1001),
(3002, '456 Oak Ave', 'Los Angeles', '90001', 'House', 3, 3000, 'N', 60002, 50002, 1002),
(3003, '789 Pine St', 'San Francisco', '94101', 'Apartment', 1, 1500, 'Y',60003,50003, 1003),
(3004, '456 Elm St', 'Boston', '02101', 'Condo', 2, 2500, 'N', 60004, 50004, 1004),
(3005, '321 Maple Ave', 'Chicago', '60601', 'House', 4, 4000, 'Y', 60005, 50005, 1005),
(3006, '987 Birch St', 'New York', '10002', 'Apartment', 1, 1200, 'N', 60006, 50006, 1001),
(3007, '654 Oak Ave', 'Los Angeles', '90002', 'House', 2, 2500, 'Y', 60007, 50007,1002),
(3008, '321 Pine St', 'San Francisco', '94102', 'Apartment', 3, 1800, 'N', 60008, 50008, 1003),
(3009, '888 Elm St', 'Boston', '02102', 'Condo', 1, 2000, 'Y', 60009, 50009, 1004),
(3010, '555 Maple Ave', 'Chicago', '60602', 'House', 5, 4500, 'N', 60010, 50010, 1005),
(3011, '222 Birch St', 'New York', '10003', 'Apartment', 2, 2200, 'Y', 60011, 50011, 1001),
(3012, '777 Oak Ave', 'Los Angeles', '90003', 'House', 3, 3500, 'N', 60012, 50012, 1002),
(3013, '444 Pine St', 'San Francisco', '94103', 'Apartment', 1, 1300, 'Y', 60013, 50013, 1003),
(3014, '111 Elm St', 'Boston', '02103', 'Condo', 2, 2700, 'N', 60014, 50014, 1004),
(3015, '444 Maple Ave', 'Chicago', '60603', 'House', 4, 4200, 'Y', 60015, 50015, 1005),
(3016, '888 Birch St', 'New York', '10004', 'Apartment', 1, 1000, 'N', 60001, 50001, 1001);

CREATE TABLE client
(clientNo int PRIMARY KEY ,
 fName varchar(40) NOT NULL,
 prefType varchar(10) NOT NULL,
 maxRent int NOT NULL,
 branchNo int NOT NULL,
 staffNo int NOT NULL,
 regDate date NOT NULL
);

INSERT INTO client (clientNo, fName, prefType, maxRent, branchNo, staffNo, regDate)
VALUES 
    (40001, 'John Smith', 'House', 2000, 1001, 50001, '2022-01-01'),
    (40002, 'Sarah Johnson', 'Apartment', 1500, 1002, 50002, '2022-01-02'),
    (40003, 'Michael Brown', 'Condo', 1800, 1003, 50003, '2022-01-03'),
    (40004, 'Jennifer Lee', 'Duplex', 2200, 1001, 50001, '2022-01-04'),
    (40005, 'David Garcia', 'Townhouse', 1900, 1002, 50002, '2022-01-05'),
    (40006, 'Maria Hernandez', 'House', 2500, 1003, 50003, '2022-01-06'),
    (40007, 'James Wilson', 'Apartment', 1300, 1001, 50001, '2022-01-07'),
    (40008, 'Laura Martinez', 'Condo', 1700, 1002, 50002, '2022-01-08'),
    (40009, 'Robert Taylor', 'Duplex', 2400, 1003, 50003, '2022-01-09'),
    (40010, 'Karen Anderson', 'Townhouse', 2100, 1001, 50001, '2022-01-10'),
    (40011, 'William Davis', 'House', 1800, 1002, 50002, '2022-01-11'),
    (40012, 'Emma Rodriguez', 'Apartment', 1400, 1003, 50003, '2022-01-12'),
    (40013, 'Daniel Martinez', 'Condo', 2000, 1001, 50001, '2022-01-13'),
    (40014, 'Jessica Wilson', 'Duplex', 2200, 1002, 50002, '2022-01-14'),
    (40015, 'Christopher Clark', 'Townhouse', 1900, 1003, 50003, '2022-01-15');


CREATE TABLE  viewing
(clientNo int NOT NULL,
 propertyNo int NOT NULL,
 viewDate date,
 comment varchar(100),
 primary key (clientNo, propertyNo,viewDate),
 constraint chk_comment check (length(comment)<=100),
 foreign key (clientNo) references client(clientNo),
 foreign key (propertyNo) references propertyForRent(propertyNo)
);

INSERT INTO viewing (clientNo, propertyNo, viewDate, comment)
VALUES (40001, 3001, '2023-05-01', 'Nice property, but needs some maintenance work.'),
       (40002, 3002, '2023-04-20', 'Great location, but too small for my family.'),
       (40003, 3003, '2023-05-10', 'I love this property, but the rent is too high.'),
       (40004, 3004, '2023-04-23', 'The property is in good condition, but the neighborhood is not great.'),
       (40005, 3005, '2023-04-27', 'I am interested in renting this property.'),
       (40006, 3001, '2023-04-21', 'The property is in a convenient location.'),
       (40007, 3002, '2023-04-22', 'The property is clean and well-maintained.'),
       (40008, 3003, '2023-05-05', 'The property is too far from my workplace.'),
       (40009, 3004, '2023-05-02', 'The property is spacious and has a great view.'),
       (40010, 3005, '2023-05-07', 'The property is too expensive for me.');

CREATE TABLE registration
(clientNo int NOT NULL,
 propertyNo int NOT NULL,
 branchNo int NOT NULL,
 staffNo int NOT NULL,
 dateJoined date,
 rentalPeriod int NOT NULL,
 rentPaid int NOT NULL,
 paymentMethod varchar(20) NOT NULL,
 primary key (clientNo, propertyNo, branchNo, staffNo),
 foreign key (clientNo) references client (clientNo),
 foreign key (propertyNo) references propertyForRent (propertyNo),
 foreign key (branchNo) references branch(branchNo),
 foreign key (staffNo) references staff(staffNo)
);

INSERT INTO registration 
VALUES (40001, 3001, 1001, 50001, '2022-03-01', 12, 1200,'Cheque'),
       (40002, 3002, 1002, 50002, '2022-04-01', 6, 1800,'Cash'),
       (40003, 3003, 1003, 50003, '2022-05-01', 12, 1500,'Cheque'),
       (40004, 3004, 1004, 50004, '2022-06-01', 9, 2000,'Cash'),
       (40005, 3005, 1005, 50005, '2022-07-01', 12, 2200,'Cash'),
       (40006, 3002, 1002, 50002, '2022-08-01', 12, 2400,'Cheque'),
       (40007, 3003, 1003, 50003, '2022-09-01', 6, 1200,'Cash');
       
drop database dreamhome;

-- first set

-- a
select * from branch where city='New York';

-- b
select city,count(*) as totalBranch from branch group by city;

-- c
select fName,position,salary from staff
where branchNo=1003 order by fName;

-- d
SELECT COUNT(*) AS totalStaff, SUM(salary) AS totalSalary
FROM staff;

-- e
select position,count(*) as totalStaff from staff, branch 
where staff.branchNo=branch.branchNo
and branch.city = 'New York' group by position;

-- f
select branch.address,branch.city,staff.fName as managerName
from staff,branch where staff.branchNo=branch.branchNo and 
staff.position='Manager' order by branch.address;

-- g
select fName from staff where supervisorNo=
(select staffNo from staff where fName="John Doe");

-- h
select propertyNo, address, city, type, rent from propertyforrent
where city='New York' order by rent;

-- i
select * from propertyforrent where staffNo=
(select staffNo from staff where fname='Peter Lee');

-- j
select staff.fName, count(*) as propertyCount from staff, propertyforrent
where staff.staffNo=propertyforrent.staffNo and  staff.branchNo=1003 
group by staff.staffNo;

-- l
select b.branchNo, b.city, p.type, count(*) as totalProperties from 
branch b, propertyforrent p where p.branchNo=B.branchNo group by
b.branchNo,b.city,p.type;

-- m
select p.ownerNo,o.fName,count(*) as propertyCount from 
propertyforrent p ,privateowner o where p.ownerNo=o.ownerNo 
group by p.ownerNo having count(*)>1;

-- n
select * from propertyforrent where type='Apartment' and city='New York' and 
rooms>=2 and rent<=2000;

-- o
select distinct c.clientNo, c.fName ,c.prefType from client c,
propertyforrent p where c.prefType=p.type and c.maxRent>=p.rent and
p.branchNo=1003;

-- p
select propertyNo, count(*) as advertisingCount from viewing group by 
propertyNo having count(*)>(select avg(advertisingCount) from(select count(*) 
as advertisingCount from viewing group by propertyNo)as advertisingCount);

-- q

-- r
select registration.branchNo,count(*) as totalWithLessThanAYear from registration,propertyforrent 
where rentalPeriod<12 group by branchNo;


-- s
select branchNo,sum(rentPaid/30) as dailyRental from registration group by branchNo;

-- second set

-- a
select fName from staff where supervisorNo=
(select staffNo from staff where fName="James Brown") and branchNo=1003;

-- b
select * from staff where position="Assistant" and branchNo=1003 
order by fName;

-- c
select p.propertyNo, p.rent,o.ownerNo,  o.fName,  o.email
from propertyForRent p inner join privateowner o on p.ownerNo=o.ownerNo where currentStatus="N";


-- d
SELECT p.propertyNo, o.*, s.staffNo
FROM propertyForRent p
JOIN privateOwner o ON p.ownerNo= o.ownerNo
JOIN staff s ON p.staffNo = s.staffNo
WHERE s.fName = 'John Doe';


-- e
SELECT c.clientNo,c.Fname,c.staffNo, s.fName AS staffName,s.branchNo
FROM client c JOIN staff s ON c.staffNo = s.staffNo;

-- f
select propertyNo,address,city,postcode,rent from propertyforrent where city="New York" and rent<2000;

-- g
select p.propertyNo,p.address,p.city,p.ownerNo,o.fname as ownerName,o.telNo 
from propertyforrent p,privateowner o where p.ownerNo=o.ownerNo;

-- h
select * from viewing where  propertyNo=3001;

-- i
select c.clientNo,c.fName from client c join viewing v 
on c.clientNo=v.clientNo where v.comment IS NULL;

-- j
select r.clientNo,c.fName,r.propertyNo,concat(p.address,",",p.city) as propertyAddress,r.rentPaid, r.dateJoined,
r.rentalPeriod,r.paymentMethod,(select date_add(r.dateJoined,interval r.rentalPeriod month)) as expiryDate from
registration r,client c,propertyforrent p where r.clientNo=c.clientNo and p.propertyNo=r.propertyNo;

-- k

-- l
SELECT p.propertyNo, p.type, p.rooms, p.rent, p.ownerNo
FROM propertyForRent  p
LEFT JOIN viewing v ON p.propertyNo = v.propertyNo
WHERE v.viewDate IS NULL OR v.viewDate < DATE_SUB(NOW(), INTERVAL 3 MONTH);

-- m
SELECT * FROM client c
WHERE c.prefType = (SELECT type FROM propertyForRent WHERE propertyNo = 3001);



show tables;
select * from staff;
select * from client;
select * from privateowner;
select * from branch;
select * from propertyforrent;
select * from viewing;
select * from registration;

select r.clientNo,c.fName,r.propertyNo,concat(p.address,",",p.city) as propertyAddress,r.rentPaid, r.dateJoined,
r.rentalPeriod,r.paymentMethod,(select date_add(r.dateJoined,interval r.rentalPeriod month)) as expiryDate from
registration r,client c,propertyforrent p where r.clientNo=c.clientNo and p.propertyNo=r.propertyNo and r.clientNo=40007;