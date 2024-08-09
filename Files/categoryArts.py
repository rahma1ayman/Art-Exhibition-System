import customtkinter as CTK
from PIL import Image,ImageTk
import tkinter
from functools import partial
import sqlite3

def Arts(cat):
    #------------------Constants------------------#
    primaryColor = "#EDE0D4"
    secondaryColor="#E6CCB2"
    btnColor="#9C6644"
    hovColor="#B08968"


    categoryArts = CTK.CTk()
    def screenStyle():
        categoryArts.title("New Artwork")
        categoryArts.geometry("1100x600+300+150")
        categoryArts.config(bg=primaryColor)
        categoryArts.resizable(False,False)

    screenStyle()

    def navigationBar():
        nav_frame = CTK.CTkFrame(categoryArts,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
        nav_frame.grid(row=0,column=0,sticky="nw") 
    
        artist_img = Image.open("images/painter.png")
        artist_img = artist_img.resize((100,100))
        artist_img_tk = ImageTk.PhotoImage(artist_img)
        artist_lbl = CTK.CTkLabel(nav_frame,text="",image=artist_img_tk)
        artist_lbl.grid(row=0,column=0,pady=(30,0))

        icons_frame = CTK.CTkFrame(nav_frame,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
        icons_frame.grid(row=1,column=0,pady=(80,250))

        def categoryScreen():
            categoryArts.destroy()
            import categories
    
        categoryIcon = Image.open("images/choice.png")
        categoryIcon = categoryIcon.resize((45,45))
        categoryIcon_tk = ImageTk.PhotoImage(categoryIcon)    
        profile_btn = CTK.CTkButton(icons_frame,image=categoryIcon_tk,text="Arts",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=categoryScreen)
        profile_btn.grid(pady=(0,40))
        
        def event():
             categoryArts.destroy()
             import events
        
        eventIcon = Image.open("images/event.png")
        eventIcon = eventIcon.resize((50,50))
        postIcon_tk = ImageTk.PhotoImage(eventIcon)    
        post_btn = CTK.CTkButton(icons_frame,image=postIcon_tk,text="Events",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=event)
        post_btn.grid(pady=(0,40))

        def logout():
            categoryArts.destroy()
            import Registeration

        logoutIcon = Image.open("images/logout .png")
        logoutIcon = logoutIcon.resize((50,50))
        logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
        logout_btn = CTK.CTkButton(icons_frame,image=logoutIcon_tk,text="Logout",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=logout)
        logout_btn.grid()

    navigationBar()

    masterArtsFrame = CTK.CTkScrollableFrame(categoryArts,border_color=primaryColor,
                                        fg_color=primaryColor,bg_color=primaryColor,
                                        scrollbar_button_color=btnColor,
                                        scrollbar_button_hover_color=hovColor,
                                        width=938,
                                        height=520
                                    )

    artpieceTitle = tkinter.Label(
                       categoryArts,
                       anchor='center',
                       text=cat, # art piece title can be put here
                       foreground='#EDE0D4',
                       bg='#7F5539',
                       width='28',
                       font=("Arial Rounded MT Bold", 60, "bold")
                    )

    def fetch_arts():
        global cur,conn
        conn = sqlite3.connect('ArtGalary.db')
        cur = conn.cursor()
        cur.execute(f'SELECT Img_URL , title ,Date_of_creation, Artist_ID ,ArtWork_ID FROM ArtWork WHERE Category = \'{cat}\'')
        arts = cur.fetchall()
    #conn.close()
    
        return arts 
    def selected(art_id): 
                conn.close()
                categoryArts.destroy()
                import artWorkDisc
                print(f"------------------{art_id}------------------")
                artWorkDisc.artDiscription(art_id,cat)
    def update_arts():
        art_data = fetch_arts()

        for art in art_data :
            artist_id = art[3]
            cur.execute(f"SELECT nick_name FROM Artist WHERE Artist_ID = {artist_id}")
            artist_name = cur.fetchone()[0]
            artFrame= CTK.CTkFrame(masterArtsFrame,fg_color=primaryColor)
            try :
                img = Image.open(art[0])
                img = img.resize((500,300))
                img_tk = ImageTk.PhotoImage(img)
                artFrame.img = img_tk
                art_title = f"Art Title: {art[1]}\nArtist: {artist_name}\nDate Of Creation: {art[2]}"
            except:
                print("no data")

            command = partial(selected,art[4])
            print(f'---------------{command}--------------')

            artBtn = CTK.CTkButton(artFrame,width=200,height=200,text="",image=img_tk,fg_color=primaryColor,hover_color=hovColor,command=command)
            artDisc = CTK.CTkLabel(artFrame,text=art_title,text_color="black",
                               font=("Times new roman", 20, "bold"),
                               justify='left'
                               )

            artBtn.grid(row=0,column=0,pady=20)
            artDisc.grid(row=0,column=1,padx=15)
            artFrame.pack(fill = "x")

    artpieceTitle.grid(row=0,column=1,columnspan=2,sticky="nw",ipadx=10)
    masterArtsFrame.grid(row=0,column=1,columnspan=2,sticky="nw",pady=(70,0))
    update_arts()
    categoryArts.mainloop()
    conn.close()
