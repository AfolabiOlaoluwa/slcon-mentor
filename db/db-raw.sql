CREATE TABLE member(
	mid int primary key auto_increment,
	first_name varchar(30),
	last_name varchar(30),
	nationality varchar(30),
	location varchar(100),
	email varchar(100),
	phone varchar(100),
	password varchar(50)
);

CREATE TABLE mentor(
	mtid int primary key auto_increment,
	mid1 int,
	mid2 int,
	foreign key(mid1) references member(mid),
	foreign key(mid2) references member(mid)
);

CREATE TABLE skill(
	sid int primary key auto_increment,
	skill varchar(20)
);

CREATE TABLE link_type(
	ltid int primary key auto_increment,
	link_type varchar(20)
);

CREATE TABLE link(
	lid int primary key auto_increment,
	ltid int,
	mid int,
	foreign key(ltid) references link_type(ltid),
	foreign key(mid) references member(mid)
);

CREATE TABLE member_skill(
	msid int primary key auto_increment,
	mid int,
	sid int,
	rating int,
	foreign key(mid) references member(mid),
	foreign key(sid) references skill(sid)
);

CREATE TABLE interest(
	iid int primary key auto_increment,
	interest varchar(30)
);

CREATE TABLE project_cat(
	pcid int primary key auto_increment,
	project_cat varchar(20)
);

CREATE TABLE project(
	pid int primary key auto_increment,
	mid int,
	pcid int,
	project_name varchar(50),
	descr text,
	foreign key(mid) references member(mid),
	foreign key(pcid) references project_cat(pcid)
);

CREATE TABLE project_skill(
	psid int primary key auto_increment,
	pid int,
	sid int,
	rating int,
	foreign key(pid) references project(pid),
	foreign key(sid) references skill(sid)
);

CREATE TABLE  member_interest(
	miid int primary key auto_increment,
	iid int,
	mid int,
	foreign key(iid) references interest(iid),
	foreign key(mid) references member(mid)
)