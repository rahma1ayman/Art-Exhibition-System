import sqlite3


def select_artist():
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute("SELECT Artist_ID,Artist_Name,email,Password FROM Artist")
    artists=cursor.fetchall()
    conn.close()
    return artists


def delete_artist(id,email):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Artist WHERE Artist_ID = ?",(id,))
    cursor.execute("DELETE FROM USERS WHERE Email = ? ",(email,))
    conn.commit()
    conn.close()

def update_Artist(new_name,new_email,new_password,id):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute('''UPDATE Artist 
    SET Artist_Name=?,email=?,Password=? WHERE Artist_ID=?''',
                (new_name,new_email,new_password,id))
    conn.commit()
    conn.close()

def email_exists(email):
    conn=sqlite3.connect("ArtGalary.db")
    cursor=conn.cursor()
    cursor.execute("SELECT count(*) FROM Artist WHERE email=?",(email,))
    result=cursor.fetchone()
    conn.close()
    return result[0]> 0


