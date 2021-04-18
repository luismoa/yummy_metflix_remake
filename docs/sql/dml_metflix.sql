set transaction isolation level serializable;
start transaction;

use metflix;

alter table movie drop constraint fk_director_id_director ;
alter table movie_actor drop constraint fk_movie_actor_id_movie ;
alter table movie_actor drop constraint fk_movie_actor_id_actor ;

truncate table director;
truncate table movie;
truncate table actor;
truncate table movie_actor;

alter table movie add constraint fk_director_id_director foreign key(id_director) references  director(id) on update cascade on delete cascade;
alter table movie_actor add constraint fk_movie_actor_id_movie foreign key(id_movie) references  movie(id) on update cascade on delete cascade;
alter table movie_actor add constraint fk_movie_actor_id_actor foreign key(id_actor) references  actor(id) on update cascade on delete cascade;



insert into director (_name,nationality)  
	values 
		('Peter Jackson','NZ'),
        ('Joe Johnston','US'),
        ('David Twohy','US');
        

insert into movie (title,nationality,production_company,year_release,id_director,budget,box_office,running_time)  
	values 
		('The Lord of the Rings: The Fellowship of the Ring','US,NZ','New Line Cinema',2001,1,93000000,888300000,178),
		('The Lord of the Rings: The Fellowship of the Ring (Extended)','US,NZ','New Line Cinema',2002,1,93000000,888300000,228),
        ('The Lord of the Rings: The Two Towers','US,NZ','New Line Cinema',2002,1,94000000,951200000,179),
        ('The Lord of the Rings: The Two Towers (Extended)','US,NZ','New Line Cinema',2003,1,94000000,951200000,226),
		('The Lord of the Rings: The Return of the King','US,NZ','New Line Cinema',2003,1,94000000,1142000000,201),
        ('The Lord of the Rings: The Return of the King (Extended)','US,NZ','New Line Cinema',2004,1,94000000,1142000000,251),
		('Captian America: The First Avenger','US','Marvel Studios',2011,2,216600000,370600000,124),
        ('The Chronicles of Riddick','US','Radar Pictures',2004,2,120000000,115800000,119);
        
insert into actor (_name,nationality,born,sex)  
	values 
		('Elijah Wood','US', '2000-01-28','m'),
        ('Sir Ian Murray McKellen','UK', '1939-05-25','m'),
		('Viggo Peter Mortensen Jr.','US', '1958-10-20','m'),
		('Christ Evans','US', '1981-06-13','m'),
        ('Mark Sinclair (Vin Diesel)','US', '1967-07-18','m');
        
insert into movie_actor (id_movie,id_actor,_role,is_main_character)  
	values 
		(1,1,'Frodo Baggings',1),
        (1,2,'Gandalf the Grey',1),
        (1,3,'Aragorn "Strider"',1),

        (2,1,'Frodo Baggings',1),
        (2,2,'Gandalf the Grey',1),
        (2,3,'Aragorn "Strider"',1),
        
        (3,1,'Frodo Baggings',1),
        (3,2,'Gandalf the Grey',1),
        (3,3,'Aragorn "Strider"',1),
        
		(4,1,'Frodo Baggings',1),
        (4,2,'Gandalf the Grey',1),
        (4,3,'Aragorn "Strider"',1),
        
		(5,1,'Frodo Baggings',1),
        (5,2,'Gandalf the Grey',1),
        (5,3,'Aragorn "Strider"',1),
        
        (6,1,'Frodo Baggings',1),
        (6,2,'Gandalf the Grey',1),
        (6,3,'Aragorn "Strider"',1),
        
        (7,4,'Steve Rogers (Captian America)',1),
        
        (8,5,'Richard B. Riddick',1);
        
        


commit;

-- Note: 
-- 	I need to drop the FK constraints before truncate and then add again those constraints if not we got 1064 error because we're truncating a record with  a constraint


-- Other notes:
-- I'm using some of the things I've been learning from Inserting data into a table (the problems we could face and other stuff)