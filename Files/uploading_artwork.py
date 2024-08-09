import customtkinter as CTK
from tkinter import filedialog,StringVar,messagebox
from PIL import Image , ImageTk
from tkcalendar import Calendar
import sqlite3

imgLabel = None

def artUpload(email,id):
    con = sqlite3.connect("ArtGalary.db")
    cur = con.cursor()


    primaryColor = "#EDE0D4"
    secondaryColor="#E6CCB2"
    btnColor="#9C6644"
    hovColor="#B08968"
    date_window = None


    artWork = CTK.CTk()
    frame = CTK.CTkFrame(artWork,width=950,height=600,bg_color=primaryColor,fg_color=primaryColor)
    frame.grid(row=0,column=1,sticky="nw")

# chracterstics of root
    def screenStyle():
        artWork.title("New Artwork")
        artWork.geometry("1100x600+300+150")
        artWork.config(bg=primaryColor)
        artWork.resizable(False,False)

    screenStyle()

    def navigationBar():
        nav_frame = CTK.CTkFrame(artWork,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
        nav_frame.grid(row=0,column=0,sticky="nw") 
    
        artist_img = Image.open("images/painter.png")
        artist_img = artist_img.resize((100,100))
        artist_img_tk = ImageTk.PhotoImage(artist_img)
        artist_lbl = CTK.CTkLabel(nav_frame,text="",image=artist_img_tk)
        artist_lbl.grid(row=0,column=0,pady=(30,0))

        icons_frame = CTK.CTkFrame(nav_frame,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
        icons_frame.grid(row=1,column=0,pady=(80,250))
    
        def profile():
            artWork.destroy()
            import artistProfile
            artistProfile.artistProfile(email)
    
        profileIcon = Image.open("images/profile.png")
        profileIcon = profileIcon.resize((45,45))
        profileIcon_tk = ImageTk.PhotoImage(profileIcon)    
        profile_btn = CTK.CTkButton(icons_frame,image=profileIcon_tk,text="My Profile",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=profile)
        profile_btn.grid(pady=(0,40))

        postIcon = Image.open("images/blog.png")
        postIcon = postIcon.resize((50,50))
        postIcon_tk = ImageTk.PhotoImage(postIcon)    
        post_btn = CTK.CTkButton(icons_frame,image=postIcon_tk,text="New Post",bg_color="transparent",fg_color="transparent",hover_color=hovColor)
        post_btn.grid(pady=(0,40))

        def logout():
            artWork.destroy()
            import Registeration
    
        logoutIcon = Image.open("images/logout .png")
        logoutIcon = logoutIcon.resize((50,50))
        logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
        logout_btn = CTK.CTkButton(icons_frame,image=logoutIcon_tk,text="Logout",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=logout)
        logout_btn.grid()

    navigationBar()

# def show_frame(frame):
#     frame.tkraise()

# title of artWork
    def addArtTitle():
        global title_entry

        title_frame = CTK.CTkFrame(frame,fg_color=primaryColor,bg_color=primaryColor)
        title_frame.grid(row = 1,column = 1,sticky="nw",padx=(20,0),pady=10,rowspan = 2)

        title_lable = CTK.CTkLabel(title_frame,text="Art Title",text_color="black",font=("Tahoma",18,"bold"))
        title_lable.grid(row = 0,column = 0,padx=5,sticky="w")

        title_entry = CTK.CTkEntry(title_frame,bg_color=primaryColor,fg_color=secondaryColor,width=200,height=60,text_color="black",border_color=btnColor)
        title_entry.grid(row = 1, column =0,pady=15)

    addArtTitle()
     
# upload image from PC
    def uploadImage():
        global imgLabel
        global file_path

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
        if imgLabel:
            imgLabel.destroy()
        else:
            if file_path:
               img = Image.open(file_path)
               img = img.resize((450,200),)
               img_tk = ImageTk.PhotoImage(img)
               imgLabel = CTK.CTkLabel(img_frame,image=img_tk,text="",width=450,height=200)
               upload_btn.grid_forget()
               imgLabel.pack()

    upload_frame= CTK.CTkFrame(frame,width=500,height=250,fg_color=primaryColor)
    upload_frame.grid(row=1,column=2,columnspan=2,sticky="nw",padx=(20,0))

    lbl = CTK.CTkLabel(upload_frame,text="Upload Image",text_color="black",font=("Tahoma",18,"bold"))
    lbl.grid(row=0,column=0,sticky="nw",padx=50,pady=10)

    img_frame = CTK.CTkFrame(upload_frame,width=450,height=200,fg_color=secondaryColor,border_color=btnColor)
    img_frame.grid(row=1,column=0,pady=5,padx=30,sticky="nw")

    upload_btn = CTK.CTkButton(img_frame,text="Upload",width=130,height=40,fg_color=btnColor,font=("tahoma",18),hover_color=hovColor,command=uploadImage,)
    upload_btn.grid(row=1,column = 0,padx=160,pady=80)

# delete image 
    def deleteImage():
        global imgLabel
        global delete
        def delete():
            if imgLabel:
               imgLabel.destroy()
               upload_btn.grid(row=1,column = 0,padx=160,pady=80)
    
        delt_img = Image.open("images/trash (1).png")
        delt_img = delt_img.resize((40,40))
        delt_img_tk = ImageTk.PhotoImage(delt_img)

        delete_btn = CTK.CTkButton(upload_frame,image=delt_img_tk,text="",fg_color="transparent",hover_color=hovColor,width=40,height=40,command=delete)
        delete_btn.grid(row=1,column=2,sticky="s")

# upload another image
    def editImage():
        edit_img = Image.open("images/upload.png")
        edit_img = edit_img.resize((40,40))
        edit_img_tk = ImageTk.PhotoImage(edit_img)

        edit_btn = CTK.CTkButton(upload_frame,image=edit_img_tk,text="",fg_color="transparent",hover_color=hovColor,width=40,height=40,command=uploadImage)
        edit_btn.grid(row=1,column=3,padx=5,sticky="s")

# add art caption
    def artCaption():
        global caption_box

        caption_frame = CTK.CTkFrame(frame,width= 200,height=210,fg_color=primaryColor,bg_color=primaryColor,border_color=btnColor)
        caption_frame.grid(row=2,column =1 ,sticky="w",padx=(20,0))

        caption_lbl = CTK.CTkLabel(caption_frame,text="Art Caption",text_color="black",font=("Tahoma",18,"bold"))
        caption_lbl.grid(row = 0,column = 0,padx=5,sticky="w")

        caption_box = CTK.CTkTextbox(caption_frame,width=200,height=200,text_color="black",fg_color=secondaryColor,border_color=btnColor,)
        caption_box.grid(row =1 ,column=0,padx=5,pady=(15,0),sticky="w")

# select category of artWork
    def artCategory():
        global category_combBox
        global category_var
        global values

        category_lbl = CTK.CTkLabel(category_frame,text="Category",text_color="black",font=("Tahoma",18,"bold"))
        category_lbl.grid(row = 0,column =0,sticky="w",padx=50,pady=10)

        values=["Visual Arts","Abstract Art","Figurative Art","Expression Art","Sculpture Art","Painting Art"]
        category_var = StringVar()
        category_var.set(values[0])
        category_combBox=CTK.CTkComboBox(category_frame,values=values,variable=category_var,dropdown_font=("Helvetica",14),font=("Helvetica",14),width=200,fg_color=secondaryColor,button_color=btnColor,bg_color=secondaryColor,text_color="black",dropdown_fg_color=btnColor,dropdown_text_color="black",state="readonly",dropdown_hover_color=hovColor)
        category_combBox.grid(row=1,column=0,padx=50)

# what's your new ?
    def panner():
        disc_frame=CTK.CTkFrame(frame,fg_color=primaryColor,height=20)
        disc_frame.grid(row=0,column=1,columnspan=2,pady=(5,0))

        disc_lbl = CTK.CTkLabel(disc_frame,text="What is Your New Post?",text_color="black",font=("Arial",22,"bold"))
        disc_lbl.grid(row=0,column=0,padx=(210,0))
        disc_lbl2 = CTK.CTkLabel(disc_frame,text="  Upload Art Data",text_color="#6b705c",font=("Arial",16,"bold"))
        disc_lbl2.grid(row=0,column=2,rowspan=3)

    panner()


    deleteImage()

    editImage()

    artCaption()

    category_frame = CTK.CTkFrame(frame,fg_color=primaryColor)
    category_frame.grid(row = 2,column = 2,sticky="nw",padx=(20,0))

    artCategory()

# screen of calender
    def openCalender():
        global date_window

        date_window= CTK.CTkToplevel(artWork,fg_color=primaryColor)
        date_window.geometry("250x250")
        date_window.title("Calender")
        cal = Calendar(date_window, selectmode = 'day',
               year = 2024, month = 5,
               day = 22)
 
        cal.grid(padx=30,pady = 20,sticky="nsew")
        def grad_date():
            if date_entry:
                date_entry.delete(0,CTK.END)
            date_entry.insert(0,cal.get_date())
 
        CTK.CTkButton(date_window, text = "Get",width=200,height=30,fg_color=btnColor,font=("tahoma",18),hover_color=hovColor,
       command = grad_date).grid(pady = 10)

# date of creation of artWork
    def artDate():
       global date_entry

       date_lbl = CTK.CTkLabel(category_frame,text="Date Of Creation",text_color="black",font=("Tahoma",18,"bold"))
       date_lbl.grid(row=2,column=0,sticky="w",padx=50,pady=(25,0))

       date_entry = CTK.CTkEntry(category_frame,bg_color=primaryColor,fg_color=secondaryColor,width=200,height=30,text_color="black",border_color=btnColor)
       date_entry.grid(row=3,column =0,sticky="w",padx=50,pady=(10,0))

       date_img = Image.open("images/calendar.png")
       date_img = date_img.resize((40,40))
       date_img_tk = ImageTk.PhotoImage(date_img)

       date_btn = CTK.CTkButton(category_frame,image=date_img_tk,text="",fg_color="transparent",hover_color=hovColor,width=40,height=40,command=openCalender)
       date_btn.grid(row=3,column=1,sticky="w")

    artDate()

    def artist():
        artist_img_frame = CTK.CTkFrame(frame,fg_color=primaryColor)
        artist_img_frame.grid(row=2,column =3)
        artist_img = Image.open("images/artist.jpeg")
        artist_img = artist_img.resize((390,200),)
        artist_img_tk = ImageTk.PhotoImage(artist_img)
        artist_img_label = CTK.CTkLabel(artist_img_frame,image=artist_img_tk,text="",width=390,height=200)
        artist_img_label.grid(sticky = "nw")

    artist()

    btn_frame = CTK.CTkFrame(frame,fg_color=primaryColor)
    btn_frame.grid(row=3,column=2,sticky="n",columnspan=3)

# post artWork
    def postButton():
        try:
           title = title_entry.get()
           caption = caption_box.get("1.0", "end")
           category = category_combBox.get()
           date = date_entry.get()
       
           if not (title and caption and category and date and file_path):
                messagebox.showerror(title="Error", message="Please fill in all required fields.")
                return
        #    cur.execute(f"SELECT Artist_ID FROM Artist WHERE email = \'{email}\'")
        #    artistID=cur.fetchone()[0]
           cur.execute("INSERT INTO ArtWork (title,Category,description,Date_of_creation,Img_URL,Artist_ID)VALUES(?,?,?,?,?,?)",(title,category,caption,date,file_path,id))
           con.commit()
           messagebox.showinfo(title="success",message="Successfully Posting New ArtWork")
           if date_window:
              date_window.destroy()
           title_entry.delete(0,"end")
           caption_box.delete("1.0","end")
           category_var.set(values[0])
           date_entry.delete(0,"end")
           delete()
       #con.close()
        except:
            messagebox.showerror(title="Error",message="There was an error! \n please make sure that you enter all requirments.")

# cancel post new artWork
    def cancelButton():
        if date_window:
            date_window.destroy()
        title_entry.delete(0,"end")
        caption_box.delete("1.0","end")
        category_var.set(values[0])
        date_entry.delete(0,"end")
        delete()


    post_btn = CTK.CTkButton(btn_frame,text="Post",width=300,height=40,fg_color=btnColor,font=("tahoma",18),hover_color=hovColor,command=postButton)
    cancel_btn = CTK.CTkButton(btn_frame,text="Cancel",width=300,height=40,fg_color=btnColor,font=("tahoma",18),hover_color=hovColor,command=cancelButton)

    post_btn.grid(row = 0,column =0,pady=(0,20))
    cancel_btn.grid(row=0,column=1,padx=(70,0),pady=(0,20))


    artWork.mainloop()

