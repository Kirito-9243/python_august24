 create table persons(id int primary key auto_increment,name varchar(50) not null,gender varchar(2),location varchar(50),age int check(age>0));
  select * from persons;
insert into persons(name,gender,location,age) values("Ishwar","M","Dharwad","20");
 insert into persons(name,gender,location,age) values("Nitish","M","Hubli","19");
 insert into persons(name,gender,location,age) values("Anirudh","M","Hubli","19");
   insert into persons(name,gender,location,age) values("Ganavi","F","Dharwad","20");
   insert into persons(name,gender,location,age) values("Vinay","M","Hubli","19");
   insert into persons(name,gender,location,age) values("Ishan","M","Bangalore","19");
   insert into persons(name,gender,age) values("Anoop","M","19");
   insert into persons(name,gender,location,age) values("Siddharth","M","Mysore","19");
    insert into persons(name,gender) values("Kirito","M");
    insert into persons(name) values("Prime");
    insert into persons(name,gender,location) values("Ezio","M","Italy");
    insert into persons(name) values("Alien X");
     insert into persons(name,gender,location,age) values("Jain","F","Bangalure","19");
      insert into persons(name,gender,location,age) values("Rishith","M","Mumbai","20");
       insert into persons(name,gender,location,age) values("Malenia","M","The Lands Between","20");
        insert into persons(name,gender,location) values("Radahn","M","The Lands Between");
         select distinct location from persons;
          select * from persons where age<20;
           select * from persons where location = "Hubli";
           select * from persons where age between 20 and 50;
           select * from persons where name like "A%";
            select * from persons where location in("Hubli","Dharwad","The Lands Between");
 ALTER TABLE persons modify location varchar(50) not null;
-- ERROR 1138 (22004): Invalid use of NULL value
-- the error is because the location column contains null values
   
   
   
   
   
   
   
   
   
   
   