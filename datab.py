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
        