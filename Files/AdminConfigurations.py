import sqlite3
def select_events():
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Event")
    events=cursor.fetchall()
    conn.close()
    return events

def insert_event(id,name,description,date,img):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute('''INSERT INTO Event(Event_ID, name, description, scheduled_date, Img_URL)
        VALUES (?,?,?,?,?)''',(id,name,description,date,img))
    conn.commit()
    conn.close()


def delete_event(id):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Event WHERE Event_ID = ?",(id,))
    conn.commit()
    conn.close()

def update_event(new_name,new_description,new_date,img,id):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute('''UPDATE Event 
    SET name=?, description=?, scheduled_date=?, Img_URL=? WHERE Event_ID=?''',
                (new_name,new_description,new_date,img,id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute("SELECT count(*) FROM Event WHERE Event_ID=?",(id,))
    result=cursor.fetchone()
    conn.close()
    return result[0]> 0


