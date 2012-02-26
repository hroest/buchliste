create table buch
( id int auto_increment primary key,
    ort varchar(255),
    spalte int,
    zeile int,
    autor text,
    titel text,
    sprache int,
    eigner varchar(255),
    buch_art varchar(255)
);

create table buch_tmp
(
    ort varchar(255),
    spalte int,
    zeile int,
    autor text,
    titel text,
    sprache int,
    eigner varchar(255),
    buch_art varchar(255)
);

load data local infile 'bucherliste.csv' into table buch_tmp
fields terminated by ','
enclosed by '"'
;



insert into buch  (ort  , spalte , zeile , autor, titel , sprache , eigner ,
    buch_art ) select * from buch_tmp where not titel = '';  


alter table buch add column autor_firstname text;
alter table buch add column autor_lastname text;

