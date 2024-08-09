from tkinter import *
import customtkinter
import sqlite3
from PIL import Image, ImageTk
import os

def artDiscription(artID, cat):
    hovColor = "#B08968"

    artpiece = Tk()
    artpiece.geometry('1100x600')
    artpiece.resizable(False, False)
    artpiece.config(bg='#EDE0D4')

    conn = sqlite3.connect('ArtGalary.db')
    cur = conn.cursor()
    cur.execute('SELECT title FROM ArtWork WHERE ArtWork_ID = ?', (artID,))
    artpieceTitle = cur.fetchone()

    cur.execute('SELECT Img_URL FROM ArtWork WHERE ArtWork_ID = ?', (artID,))
    artpieceImg = cur.fetchone()

    if artpieceTitle:
        artpiece.title(artpieceTitle[0])
    else:
        artpiece.title("Art Piece")

    title_label = Label(
        artpiece,
        anchor='center',
        text=artpieceTitle[0] if artpieceTitle else "Unknown Title",
        foreground='#EDE0D4',
        bg='#9C6644',
        width='23',
        font=("Arial Rounded MT Bold", 60, "bold")
    )

    # Back Button
    def back():
        artpiece.destroy()
        import categoryArts
        categoryArts.Arts(cat)

    arrow = PhotoImage(file='images/arrow.png')
    artpieceBackBtn = customtkinter.CTkButton(
        title_label,
        text='',
        image=arrow,
        width=20,
        height=20,
        bg_color="transparent",
        fg_color='transparent',
        hover_color=hovColor,
        command=back,
    )

    artpieceFrame = customtkinter.CTkScrollableFrame(
        artpiece,
        border_color='#EDE0D4',
        fg_color='#EDE0D4',
        scrollbar_button_color='#7F5539',
        scrollbar_button_hover_color='#B08968',
        width=100,
    )

    # Art Image
    if artpieceImg:
        img_path = artpieceImg[0]
        if os.path.exists(img_path):
            image = Image.open(img_path)
            img=image.resize((500,300))
            img_tk = ImageTk.PhotoImage(img)
            artpieceImgLabel = Label(artpieceFrame,
                                     anchor='center',
                                     image=img_tk,
                                     font=("Arial Rounded MT Bold", 60, "bold")
                                     )
            artpieceImgLabel.img = img_tk  # Keep a reference to avoid garbage collection
        else:
            artpieceImgLabel = Label(artpieceFrame,
                                     anchor='center',
                                     text="Image file not found",
                                     font=("Arial Rounded MT Bold", 60, "bold")
                                     )
    else:
        artpieceImgLabel = Label(artpieceFrame,
                                 anchor='center',
                                 text="No Image Available",
                                 font=("Arial Rounded MT Bold", 60, "bold")
                                 )

    cur.execute('SELECT Artist_ID FROM ArtWork WHERE ArtWork_ID = ?', (artID,))
    artist_id = cur.fetchone()
    cur.execute('SELECT Category, description, Date_of_creation FROM ArtWork WHERE ArtWork_ID = ?', (artID,))
    data = cur.fetchone()

    if artist_id:
        cur.execute('SELECT Artist_Name FROM Artist WHERE Artist_ID = ?', (artist_id[0],))
        artistData = cur.fetchone()
    else:
        artistData = ["Unknown Artist"]

    conn.close()

    # Art Description
    if data:
        ls = data[1].split()
        des = ""
        sm = 0
        for word in ls:
            if sm + len(word) < 90:
                des = des + word + " "
                sm += len(word) + 1
            else:
                sm = len(word)
                des = des + "\n" + word

        descriptionText = f"""
Artist: {artistData[0]}
Art Category: {data[0]}
Date of creation: {data[2]}
Description: 
{des}
"""
    else:
        descriptionText = "No description available."

    description = Label(artpieceFrame,
                        anchor='center',
                        text=descriptionText,
                        font=("Times new roman", 18, "bold"),
                        bg='#EDE0D4',
                        justify=CENTER
                        )
    title_label.pack(side='top')
    artpieceBackBtn.place(x=0.3)
    artpieceImgLabel.pack()
    description.pack()

    artpieceFrame.pack(fill=BOTH, expand=1)

    artpiece.mainloop()

# Example call to the function
# artDiscription(3, 'category')