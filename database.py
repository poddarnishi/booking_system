import sqlite3

connection=sqlite3.connect('movieticket_booking.db')
cursor=connection.cursor()

def create_table():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS movie_details(movie_id INT primary key,movie_name TEXT, genre TEXT, rating FLOAT, movie_release_date DATE,movie_duration INT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS booking(movie_id INT,show_date DATE,tickets_remaining INT, price INT, seat_type TEXT,CONSTRAINT fk FOREIGN key(movie_id) references movie_details(movie_id) ON UPDATE CASCADE ON DELETE CASCADE)") 
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS customer(email_id TEXT primary key,name TEXT,password TEXT, phone INT(10), age INT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS record(tickets_booked INT,seat_type TEXT,email_id TEXT,movie_id INT,show_date DATE, CONSTRAINT fk2 FOREIGN KEY(email_id)REFERENCES customer(email_id)ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(movie_id)REFERENCES movies(movie_id)ON UPDATE CASCADE ON DELETE CASCADE,FOREIGN KEY(show_date)REFERENCES booking(show_date)ON UPDATE CASCADE ON DELETE CASCADE)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS upcoming_movie(movie_name TEXT, genre TEXT, movie_ID INT primary key, movie_release_date DATE)")
    
def data_entries():
    #cursor.execute("INSERT INTO movie_details VALUES(453,'Roohi','horror',3.5,'3-11-2021',134)")
    #cursor.execute("INSERT INTO movie_details VALUES(454,'Chaos Walking','adventure',3,'11-3-2021',108)")
    #cursor.execute("INSERT INTO movie_details VALUES(455,'Tom and Jerry','animation',4.5,'19-2-2021',101)")
    #cursor.execute("INSERT INTO movie_details VALUES(456,'Mumbai Saga','Crime',4,'19-3-2021',128)")'''
    pass 
    
def reading():
    cursor.execute('Select * from movies')
   # cursor.execute('Select * from booking')
   # cursor.execute('Select * from customer')
    data=cursor.fetchall()
    print(data)

#def update():
     #cursor.execute("UPDATE movie_details SET movie_release_date='11-3-2021' WHERE movie_id=453")
     #cursor.execute("ALTER TABLE booking ADD COLUMN movie_ID INT")
     #cursor.execute("ALTER TABLE booking ADD CONSTRAINT fk FOREIGN KEY(movie_id) REFERENCES movies(movie_id)ON UPDATE CASCADE ON DELETE CASCADE")
     
create_table()
#update()
#data_entries()
#reading()
connection.commit()
cursor.close()
connection.close()