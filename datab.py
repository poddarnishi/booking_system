import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="nineten910",
  database="BOOKING"
)
cursor = mydb.cursor()
def create_table():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS movie_details(movie_id INT primary key,movie_name VARCHAR(20), genre VARCHAR(20), rating FLOAT, movie_release_date DATE,movie_duration VARCHAR(20))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS booking(movie_id INT,show_date DATE,tickets_remaining INT, price INT, seat_type VARCHAR(20),CONSTRAINT fk FOREIGN key(movie_id) references movie_details(movie_id) ON UPDATE CASCADE ON DELETE CASCADE)") 
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(email_id VARCHAR(20) primary key,name VARCHAR(20),password VARCHAR(20), phone INT(10), age INT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS record(tickets_booked INT,seat_type VARCHAR(20),email_id VARCHAR(20),movie_id INT,show_date DATE, CONSTRAINT fk2 FOREIGN KEY(email_id)REFERENCES customer(email_id)ON UPDATE CASCADE ON DELETE CASCADE,CONSTRAINT fk3 FOREIGN KEY(movie_id)REFERENCES movie_details(movie_id)ON UPDATE CASCADE ON DELETE CASCADE,CONSTRAINT fk4 FOREIGN KEY(show_date)REFERENCES booking(show_date)ON UPDATE CASCADE ON DELETE CASCADE)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS upcoming_movie(movie_name VARCHAR(20), genre VARCHAR(20), movie_ID INT primary key, movie_release_date DATE)")
def entries():
    cursor.execute(INSERT INTO movie_details VALUES(100,'Avengers Endgame','Sci-Fi',4.5,'2021-04-09',180),
    (101,'Bohemian Rhapsody','Drama',4,'2021-04-09',133),(102,'1917','Action',4,'2021-04-09',119),
    (103,'Jojo Rabbit','Comedy',4.5,'2021-04-02',108),(104,'Joker','Thriller',3.5,'2021-04-02',122),
    (105,'Ford vs Ferrari','Action',4,'2021-04-02',152))  

    cursor.execute(INSERT INTO booking VALUES(100,'2021-04-10',30,150,"Silver"),(100,'2021-04-10',20,200,"Gold"),
    (101,'2021-04-10',30,150,"Silver"),(101,'2021-04-10',20,200,"Gold"),
    (102,'2021-04-10',30,160,"Silver"),(102,'2021-04-10',20,200,"Gold"),
    (103,'2021-04-10',30,160,"Silver"),(103,'2021-04-10',20,220,"Gold")
    ,(104,'2021-04-10',30,180,"Silver"),(104,'2021-04-10',20,220,"Gold"),
    (105,'2021-04-10',30,180,"Silver"),(105,'2021-04-10',20,230,"Gold"),
    (100,'2021-04-11',30,170,"Silver"),(100,'2021-04-11',20,250,"Gold"),
    (101,'2021-04-11',30,170,"Silver"),(101,'2021-04-11',20,250,"Gold"),
    (102,'2021-04-11',30,180,"Silver"),(102,'2021-04-11',20,250,"Gold"),
    (103,'2021-04-11',30,180,"Silver"),(103,'2021-04-11',20,260,"Gold")
    ,(104,'2021-04-11',30,190,"Silver"),(104,'2021-04-11',20,260,"Gold"),
    (105,'2021-04-11',30,190,"Silver"),(105,'2021-04-11',20,270,"Gold"),
    (100,'2021-04-12',30,170,"Silver"),(100,'2021-04-12',20,250,"Gold"),
    (101,'2021-04-12',30,170,"Silver"),(101,'2021-04-12',20,250,"Gold"),
    (102,'2021-04-12',30,180,"Silver"),(102,'2021-04-12',20,250,"Gold"),
    (103,'2021-04-12',30,180,"Silver"),(103,'2021-04-12',20,260,"Gold")
    ,(104,'2021-04-12',30,190,"Silver"),(104,'2021-04-12',20,260,"Gold"),
    (105,'2021-04-12',30,190,"Silver"),(105,'2021-04-12',20,270,"Gold")) 
