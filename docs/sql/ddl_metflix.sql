set transaction isolation level serializable;
start transaction;

drop schema if exists metflix;
create schema if not exists metflix;

use metflix;


create table director(
	id int unsigned auto_increment,
    _name varchar(35),
    nationality varchar(40),
    constraint pk_director_id primary key(id)
);

create table movie(
	id int unsigned auto_increment,
    title varchar(60),
	nationality varchar(40),
    production_company varchar(35),
    year_release smallint  unsigned, 
    id_director int unsigned,
    budget bigint unsigned,
	box_office bigint unsigned,
    running_time smallint unsigned, -- minutes
	constraint pk_movie_id primary key(id),
	constraint fk_director_id_director foreign key(id_director)
		references director (id)
			on delete cascade
            on update cascade
);


create table actor(
	id int unsigned auto_increment,
    _name varchar(35),
    nationality varchar(40), 
    born date,
    sex varchar(1), 
    constraint pk_actor_id primary key(id)
);

create table movie_actor(
	id_movie int unsigned ,
    id_actor int unsigned ,
    _role varchar(35),
    is_main_character boolean,
    constraint pk_movie_actor primary key(id_movie,id_actor),
    constraint fk_movie_actor_id_movie foreign key(id_movie)
		references movie(id)
        on delete cascade
        on update cascade,
	 constraint fk_movie_actor_id_actor foreign key(id_actor)
		references actor(id)
        on delete cascade
        on update cascade
);



commit;

-- Notes:
-- + nationalities ==  Abbreviation like: UK, US, NZ, ES,...
-- + sex ==  Abbreviation like: m, f
-- + running_time  == minutes

-- Other notes:
-- This database schema was personalized and translated into english by Luis Moa from an original catalan schema which
-- was slightly different.