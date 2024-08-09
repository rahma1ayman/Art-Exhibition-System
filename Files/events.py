from tkinter import *
import customtkinter as CTK
import sqlite3
from PIL import Image, ImageTk

hovColor="#B08968"

events = CTK.CTk()


events.geometry('1100x600+300+150')
events.resizable(False, False)
events.title("Events")
events.config(bg='#EDE0D4')

EventsTitleLbl = CTK.CTkLabel(events,
                       anchor='center',
                       text="Events", 
                       fg_color='#EDE0D4',
                       bg_color='#9C6644',
                       width=23,
                       font=("Arial Rounded MT Bold", 60, "bold")
                       )

image = Image.open('images/arrow.png')
img = image.resize((50,50))
img_tk = ImageTk.PhotoImage(img)


eventsBackBtn = Button(EventsTitleLbl,
                       text='Back',
                       image=img_tk,
                       relief="sunken",
                       bg='#9C6644',
                       cursor='hand2',
                       highlightthickness=0,
                       borderwidth=0)

def navigationBar():
    nav_frame = CTK.CTkFrame(events,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
    nav_frame.grid(row=0,column=0,sticky="nw") 
    
    artist_img = Image.open("images/painter.png")
    artist_img = artist_img.resize((100,100))
    artist_img_tk = ImageTk.PhotoImage(artist_img)
    artist_lbl = CTK.CTkLabel(nav_frame,text="",image=artist_img_tk)
    artist_lbl.grid(row=0,column=0,pady=(30,0))

    icons_frame = CTK.CTkFrame(nav_frame,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
    icons_frame.grid(row=1,column=0,pady=(80,250))

    def categoryScreen():
        events.destroy()
        import categories
    
    categoryIcon = Image.open("images/choice.png")
    categoryIcon = categoryIcon.resize((45,45))
    categoryIcon_tk = ImageTk.PhotoImage(categoryIcon)    
    profile_btn = CTK.CTkButton(icons_frame,image=categoryIcon_tk,text="Arts",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=categoryScreen)
    profile_btn.grid(pady=(0,40))

    eventIcon = Image.open("images/event.png")
    eventIcon = eventIcon.resize((50,50))
    postIcon_tk = ImageTk.PhotoImage(eventIcon)    
    post_btn = CTK.CTkButton(icons_frame,image=postIcon_tk,text="Events",bg_color="transparent",fg_color="transparent",hover_color=hovColor)
    post_btn.grid(pady=(0,40))

    def logout():
        events.destroy()
        import Registeration

    logoutIcon = Image.open("images/logout .png")
    logoutIcon = logoutIcon.resize((50,50))
    logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
    logout_btn = CTK.CTkButton(icons_frame,image=logoutIcon_tk,text="Logout",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=logout)
    logout_btn.grid()


navigationBar()

eventMasterFrame = CTK.CTkScrollableFrame(events,
                                                    border_color='#EDE0D4',
                                                    fg_color='#EDE0D4',
                                                    bg_color='#EDE0D4',
                                                    scrollbar_button_color='#7F5539',
                                                    scrollbar_button_hover_color='#B08968',width=935,height=600)

coming_soon = PhotoImage(file="images/coming_soon.png")

def fetch_events():
    conn = sqlite3.connect('ArtGalary.db')
    cur = conn.cursor()
    
    cur.execute('SELECT name, description, scheduled_date, Img_URL FROM event')
    events = cur.fetchall()
    conn.close()
    
    return events

# def clear_event_frames():
#     for widget in eventMasterFrame.winfo_children():
#         widget.destroy()

def update_events():
    event_data = fetch_events()
    # clear_event_frames()
    
    for event in event_data:
        event_frame = CTK.CTkFrame(eventMasterFrame, bg_color='#EDE0D4',fg_color="#EDE0D4")
        event_canvas = Canvas(event_frame, width=300, height=200, bg='#E6CCB2')
        
        try:
            image = Image.open(event[3])
            image = image.resize((200,200))
            img_tk = ImageTk.PhotoImage(image)
            event_canvas.create_image(153, 100, image=img_tk)
            event_frame.img = img_tk
            event_text = f"{event[0]}\n{event[1]}on {event[2]}"
        except:
            event_canvas.create_image(153, 100, image=coming_soon)
            event_text = "Coming Soon!"
        
        event_label = CTK.CTkLabel(event_frame,
                            text_color="black",       
                            wraplength=600,
                            text=event_text,
                            font=("Arial Rounded MT Bold", 18,"bold"),
                            bg_color='#EDE0D4',
                            justify='left')
        
        event_canvas.grid(row=0, column=0, padx=20, pady=20)
        event_label.grid(row=0, column=1, padx=20, pady=20)
        event_frame.pack(fill='x')
    

EventsTitleLbl.grid(row = 0,column =1,sticky="nw")
eventsBackBtn.place(width=85, height=88)

eventMasterFrame.grid(row=0,column=1,sticky="nw")

update_events()  

events.mainloop()
