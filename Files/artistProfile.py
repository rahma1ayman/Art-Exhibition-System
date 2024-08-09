import customtkinter
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
from tkinter import Canvas
import tkinter as tk
import sqlite3 

def artistProfile(e_mail):
    primaryColor = "#EDE0D4"
    hovColor="#B08968"

#creat the window
    artistProfile = customtkinter.CTk()
    artistProfile.title('Artist Profile')
    artistProfile.geometry('1100x600')
    artistProfile.config(bg=primaryColor)
    artistProfile.resizable(False,False)

    def profile_pic():
    #creat profile frame
        profile_frame = customtkinter.CTkFrame(artistProfile, width=150, height=150)
        profile_frame.pack(side='left',anchor='nw')

    # add the image
        image = Image.open("images/artist_profile.jfif")
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        label = customtkinter.CTkLabel(profile_frame, image=photo, text='')
        label.grid(row=0,column=0)







#create the bio textbox
    bio_textbox=customtkinter.CTkTextbox(master=artistProfile,text_color='black',font=('consolas',16),fg_color='#f1ede9',bg_color=primaryColor,border_color='#9C6644',border_width=3,corner_radius=0,width=550,height=150)
    bio_textbox.place(relx=0.745,rely=0.13,anchor='center')




#create the paint art frame
    paint_master_frame=customtkinter.CTkScrollableFrame(master=artistProfile,fg_color='#EDE0D4',orientation='vertical',width=900,height=390,bg_color=primaryColor,border_color='#9C6644',border_width=3,corner_radius=16,scrollbar_button_hover_color='#7F5539',scrollbar_button_color='#7F5539')
    paint_master_frame.place(relx=0.57,rely=0.64,anchor='center')




# add the artist data to the profile
    def fetch_artist_data():
        conn = sqlite3.connect('ArtGalary.db')
        cur = conn.cursor()
        quary=f'SELECT Artist_Name,Phone,email,Bio FROM Artist WHERE email =\'{e_mail}\''
        cur.execute(quary)
        artist_data = cur.fetchone()
    #conn.close()
    
        return artist_data

    def add_data():
        data=fetch_artist_data()
        nick_name=data[0]
        nick_name_lbl = customtkinter.CTkLabel(artistProfile, text=nick_name,font=('Bold',24),bg_color=primaryColor,text_color="black")
        nick_name_lbl.place(relx=0.35,rely=0.05,anchor='center')
        phone=data[1]
        phone_lbl=customtkinter.CTkLabel(artistProfile,text=phone,font=("Arial Rounded MT Bold", 12),bg_color=primaryColor,text_color="black")
        phone_lbl.place(relx=0.35,rely=0.13,anchor='center')
        email=data[2]
        email_lbl=customtkinter.CTkLabel(artistProfile,text=email,font=("Arial Rounded MT Bold", 12),bg_color=primaryColor,text_color="black")
        email_lbl.place(relx=0.35,rely=0.09,anchor='center')
        lbl=customtkinter.CTkLabel(artistProfile,text='contact info :',font=("Arial Rounded MT Bold", 12),bg_color=primaryColor,text_color="black")
        lbl.place(relx=1.2,rely=3,anchor='center')
        bio_textbox.insert(tk.END,data[3])

#creat the side frame
    def navigationBar():
        global nav_frame
        nav_frame = customtkinter.CTkFrame(artistProfile,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
        nav_frame.pack(side='left',fill='y')
    
        artist_img = Image.open("images/painter.png")
        artist_img = artist_img.resize((100,100))
        artist_img_tk = ImageTk.PhotoImage(artist_img)
        artist_lbl = customtkinter.CTkLabel(nav_frame,text="",image=artist_img_tk)
        artist_lbl.grid(row=0,column=0,pady=(30,0))

        icons_frame = customtkinter.CTkFrame(nav_frame,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
        icons_frame.grid(row=1,column=0,pady=(80,250))

        profileIcon = Image.open("images/profile.png")
        profileIcon = profileIcon.resize((45,45))
        profileIcon_tk = ImageTk.PhotoImage(profileIcon)    
        profile_btn = customtkinter.CTkButton(icons_frame,image=profileIcon_tk,text="My Profile",bg_color="transparent",fg_color="transparent",hover_color=hovColor)
        profile_btn.grid(pady=(0,40))
    
        def newPost():
            artistProfile.destroy()
            import uploading_artwork
            uploading_artwork.artUpload(e_mail,artistID)

        postIcon = Image.open("images/blog.png")
        postIcon = postIcon.resize((50,50))
        postIcon_tk = ImageTk.PhotoImage(postIcon)    
        post_btn = customtkinter.CTkButton(icons_frame,image=postIcon_tk,text="New Post",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=newPost)
        post_btn.grid(pady=(0,40))

        def logout():
            artistProfile.destroy()
            import Registeration
    
        logoutIcon = Image.open("images/logout .png")
        logoutIcon = logoutIcon.resize((50,50))
        logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
        logout_btn = customtkinter.CTkButton(icons_frame,image=logoutIcon_tk,text="Logout",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=logout)
        logout_btn.grid()







    def fetch_paints():
        global artistID
        conn = sqlite3.connect('ArtGalary.db')
        cur = conn.cursor()
        cur.execute(f"SELECT Artist_ID FROM Artist WHERE email = \'{e_mail}\'")
        artistID=cur.fetchone()[0]
        quary1=f'SELECT Img_URL,title,description,Category,Date_of_creation FROM ArtWork where Artist_ID = {artistID}'
        cur.execute(quary1)
        paints = cur.fetchall()
        conn.close()
    
        return paints



    def update_paints():
        paint_data = fetch_paints()

        for paint in paint_data:
            paint_frame =customtkinter.CTkFrame(paint_master_frame, bg_color='#EDE0D4',corner_radius=16,fg_color='#EDE0D4')
            paint_canvas = Canvas(paint_frame, width=300, height=200, bg='#E6CCB2')
        
            image = Image.open(paint[0])
            image = image.resize((300,300))
            img_tk = ImageTk.PhotoImage(image)
            paint_canvas.create_image(150,100,image=img_tk,anchor=tk.CENTER)
            paint_frame.img = img_tk
            paint_data = f"{paint[1]}\n{paint[3]}\n{paint[4]}\n{paint[2]}\n"

            data_label = customtkinter.CTkLabel(paint_frame,
                            text_color="black",       
                            wraplength=600,
                            text=paint_data,
                            font=("Arial Rounded MT Bold", 18,"bold"),
                            bg_color='#EDE0D4',
                            justify='left')
        
            paint_canvas.grid(row=0, column=0, padx=20, pady=20)
            data_label.grid(row=0,column=1,padx=20, pady=20,)
            paint_frame.pack(fill = 'x')

    
    navigationBar()
    add_data()
    profile_pic()
    update_paints()
    artistProfile.mainloop()

#return artistProfile()