from tkinter import filedialog
import AdminConfigurations 
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")

           
def fill_treeview():
        events=AdminConfigurations.select_events()
        tree.delete(*tree.get_children())
        for event in events:
            tree.insert('',END,values=event)



def add_event():
        global imgPath
        id=Event_ID_Entry.get()
        name=Event_Name_Entry.get()
        date=Event_Date_Entry.get()
        description=Event_Description_Entry.get('1.0','end')
        

        if not (id and name and date and description and imgPath):
            messagebox.showerror('Error','Enter All Fields Please')
        elif AdminConfigurations.id_exists(id):
            messagebox.showerror('Error','ID already Exists .')
        else:
            AdminConfigurations.insert_event(id,name,description,date,imgPath)
            fill_treeview()
            messagebox.showinfo('Success','Data has been inserted successfully !')
        
        clear()
        upload_status_label.destroy()


def clear (*cliced):
        if cliced:
            tree.selection_remove(tree.focus())
        Event_ID_Entry.delete(0,END)
        Event_Name_Entry.delete(0,END)
        Event_Date_Entry.delete(0,END)
        Event_Description_Entry.delete('1.0','end')
        
def display_data(event):
        selected_item=tree.focus()
        if selected_item:
            row=tree.item(selected_item)['values']
            clear()
            Event_ID_Entry.insert(0,row[0])
            Event_Name_Entry.insert(0,row[1])
            Event_Date_Entry.insert(0,row[3])
            Event_Description_Entry.insert(END,row[2])

        else : 
            pass



def delete():
        selected_item=tree.focus()
        if not selected_item:
            messagebox.showerror('Erorr','You should choose a row to delete .')
        else:
            result=messagebox.askokcancel('Delete','Are you sure to delete that item?')
            if result:
                id=Event_ID_Entry.get()
                AdminConfigurations.delete_event(id)
                fill_treeview()
                clear()
                messagebox.showinfo('Success','Data has been deleted successfully !')
def update():
        selected_item=tree.focus()
        if not selected_item:
            messagebox.showerror('Erorr','You should choose a row to Update data .')
            return
        else:
            id=Event_ID_Entry.get()
            name=Event_Name_Entry.get()
            date=Event_Date_Entry.get()
            description=Event_Description_Entry.get('1.0','end').strip()
            img=imgPath
            AdminConfigurations.update_event(name,description,date,img,id)
            fill_treeview()
            clear()
            messagebox.showinfo('Success','Data has been updated successfully !')
        upload_status_label.destroy()


#fonts:

font1=('Arial Rounded MT Bold',20,'bold')
font2=('Tahoma',12,'bold')
font3=('Arial Rounded MT Bold',14,'bold')


    # main Page 
app=ctk.CTk()
app.title("Admin Page")
width=1100
height=600

app.geometry(f'{width}x{height}+300+150')
app.resizable(False,False)
    

    # components 
admin_frame= ctk.CTkFrame(app,height=height,width=width)
admin_frame.place(relx=0.5,rely=0.5, anchor='center')


    # Load and display background image
image = Image.open('images/IMG-20240802-WA0002.jpg')
img = image.resize((1370,745))
img_tk = ImageTk.PhotoImage(img)
background_label = Label(admin_frame, image=img_tk)
background_label.place(x=0, y=0)



Event_ID_label=ctk.CTkLabel(admin_frame,
                                text='Event_ID :',
                                font=font1,
                                text_color='#EDE0D4',
                                )
Event_ID_label.place(x=15,y=15)
Event_ID_Entry=ctk.CTkEntry(admin_frame,
                                font=font1,
                                width=250,
                                fg_color='#9C6644',
                                border_color='#EDE0D4',
                                border_width=2)
Event_ID_Entry.place(x=160,y=15)

Event_Name_label=ctk.CTkLabel(admin_frame,
                                text='Event_Name:',
                                font=font1,
                                text_color='#EDE0D4')
Event_Name_label.place(x=15,y=70)
Event_Name_Entry=ctk.CTkEntry(admin_frame,
                                  font=font1,
                                  width=250,
                                  fg_color='#9C6644',
                                  border_color='#EDE0D4',
                                  border_width=2 )
Event_Name_Entry.place(x=160,y=70)

Event_Date_label=ctk.CTkLabel(admin_frame,
                                  text='Event_date :',
                                  font=font1,
                                  text_color='#EDE0D4',
                                  fg_color=None)
Event_Date_label.place(x=15,y=125)
Event_Date_Entry=ctk.CTkEntry(admin_frame,
                                  font=font1,
                                  width=250 ,
                                  fg_color='#9C6644',
                                  border_color='#EDE0D4',
                                  border_width=2)
Event_Date_Entry.place(x=160,y=125)


Event_Description_label=ctk.CTkLabel(admin_frame,
                                        text='Description :',
                                        font=font1,
                                        text_color='#EDE0D4')
Event_Description_label.place(x=15,y=180)
Event_Description_Entry=ctk.CTkTextbox(admin_frame,
                                           font=font1,
                                           height=160,
                                           width=250, 
                                           fg_color='#9C6644',
                                           border_color='#EDE0D4',
                                           border_width=2)
Event_Description_Entry.place(x=160,y=180)

Event_Image_label=ctk.CTkLabel(admin_frame,
                                   text='Upload Image :',
                                   font=font1,
                                   text_color='#EDE0D4',
                                   )
Event_Image_label.place(x=15,y=370)
    
upload_status_label = ctk.CTkLabel(admin_frame,
                                        text="",
                                        font=font3)
upload_status_label.place(x=100, y=405)
def upload_image():
        global imgPath
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            #messagebox.showinfo('Success','Uploaded successfully !')
            imgPath= file_path
            upload_status_label.configure(text="Uploaded Successfully !",
                                        bg_color='#EDE0D4',
                                        text_color="#5E3023")
        else:
            upload_status_label.configure(text="Failed to Upload ",
                                        bg_color='#EDE0D4',
                                        text_color="red")

        
Upload_icon = Image.open('images/UploadImg.png')
Upload_icon=Upload_icon.resize((45,45))
photo = ImageTk.PhotoImage(Upload_icon)
    
upload_button = ctk.CTkButton(admin_frame,
                                text="Upload",
                                image=photo,
                                command=upload_image,
                                font=font1,
                                fg_color='#9C6644',
                                bg_color= "#5E3023",
                                hover_color='#B08968',
                                corner_radius=30,
                                width=20, height=20)
upload_button.place(x=180, y=360)
    

    #buttons

add_button=ctk.CTkButton(admin_frame,
                             command=add_event,
                             text="Add Event",
                             font=font1, 
                             fg_color='#9C6644',
                             hover_color='#B08968',
                
                             corner_radius=15, width=180, height=40)
add_button.place(x=20,y=450)

clear_button=ctk.CTkButton(admin_frame,
                               command=lambda :clear(True),text="Clear",
                               font=font1, 
                               fg_color='#9C6644',
                               hover_color='#B08968',
                               corner_radius=15, width=180, height=40)
clear_button.place(x=20,y=520)

update_button=ctk.CTkButton(admin_frame,
                                command=update,
                                text="Update Event",
                                font=font1,
                                fg_color='#9C6644'
                                ,hover_color='#B08968',
                                corner_radius=15, width=180, height=40)
update_button.place(x=240,y=450)

delete_button=ctk.CTkButton(admin_frame,
                                command=delete,
                                text="Delete Event",
                                font=font1, 
                                fg_color='#5E3023',
                                hover_color='darkred',
                                corner_radius=15, 
                                width=180, 
                                height=40)
delete_button.place(x=240,y=520)



    # treeview
style=ttk.Style(admin_frame)
style.theme_use('default')
style.configure('Treeview.Heading',
                    background='#5E3023',
                    foreground='#EDE0D4',
                    padding=[5,10,5,10],
                    font=font2, hovercolor='#9C6644')
style.configure('Treeview', font=font2, background='#EDE0D4',fieldbackground='#EDE0D4', rowheight=30)
style.configure("Treeview",rowheight=25)
style.map('Treeview', background=[('selected','#7F5539')])
tree=ttk.Treeview(admin_frame,height=60, show='headings')
tree['columns']=('Event_Id','Name','Description','Sheduled_Date')
tree.column('Event_Id', anchor='center',width=120)
tree.column('Name', anchor='center',width=200)
tree.column('Sheduled_Date', anchor='center',width=200)
tree.column('Description', anchor='center',width=280)
tree.heading('Event_Id', text='Event_Id')
tree.heading('Name',text='Name')
tree.heading('Sheduled_Date',text='Sheduled_Date')
tree.heading('Description',text='Description')
tree.place(x=550, y=20,height=550)

tree.bind('<ButtonRelease>',display_data)
fill_treeview()



#====== Navigation Buttons ========#
def logout():
        result=messagebox.askokcancel('Delete','Are you sure to Log out ?')
        if result:
            app.destroy()
            import Registeration


logoutIcon = Image.open("images/logout .png")
logoutIcon = logoutIcon.resize((40,40))
logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
logout_btn = ctk.CTkButton(app,image=logoutIcon_tk,
                           text="Logout",
                           corner_radius=10,
                           fg_color='#5E3023',
                           width=300, 
                           font=font3,
                           hover_color='#B08968',
                           command=logout)
logout_btn.place(x=770,y=485)


def Navigate_to_AddArtist():
    app.destroy()
    import  add_new_artist
    add_new_artist

Admin_btn = ctk.CTkButton(app,
                           text="Artist Configurations ",
                           corner_radius=10,
                           font=font3,
                           fg_color='#9C6644',
                           width=300, 
                           height=40,
                           hover_color='#B08968',
                           command=Navigate_to_AddArtist)
Admin_btn.place(x=450,y=485)




app.mainloop()