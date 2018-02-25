rollback;
begin;

create table Keyword_Consumer (
	Keyword varchar(50),
	Category varchar (50),
	Sub_Category varchar(50)
);

COPY Keyword_Consumer FROM 'C:\Program Files\PostgreSQL\Keywords.csv' WITH CSV HEADER;

create table Keyword_Expert (
	Keyword varchar(50),
	Category varchar (50),
	Sub_Category varchar(50)
);

COPY Keyword_Expert FROM 'C:\Program Files\PostgreSQL\Keywords_Expert.csv' WITH CSV HEADER;

	create table Consumers (
	CID varchar(50),
    Contents text,
    Car varchar(50),
    Review_Type varchar(50),
	primary key (CID)
);

COPY Consumers FROM 'C:\Program Files\PostgreSQL\Consumer.csv' WITH CSV HEADER;



create table Expert (
	CID varchar(50),
    Contents text,
    Car varchar(50),
    Review_Type varchar(50),
	primary key (CID)
);

COPY Expert FROM 'C:\Program Files\PostgreSQL\Expert.csv' WITH CSV HEADER;

commit;