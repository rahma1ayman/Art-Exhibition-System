import sqlite3
import ArtistConfigurations
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
ctk.set_appearance_mode("dark")



#============= function used ==============#
def fill_treeview():
        artists= ArtistConfigurations.select_artist()
        tree.delete(*tree.get_children())
        for artist in artists:
            tree.insert('',END,values=artist)

def clear (*cliced):
        if cliced:
            tree.selection_remove(tree.focus())
        name_entry_reg.delete(0,END)
        email_entry_reg.delete(0,END)
        password_entry_reg.delete(0,END)
        confirm_password_entry_reg.delete(0,END)


def display_data(event):
        selected_item=tree.focus()
        if selected_item:
            row=tree.item(selected_item)['values']
            clear()
            name_entry_reg.insert(0,row[1])
            email_entry_reg.insert(0,row[2])
            password_entry_reg.insert(0,row[3])
            confirm_password_entry_reg.insert(0,row[3])

        else : 
            pass
def delete():
        selected_item=tree.focus()
        if not selected_item:
            messagebox.showerror('Erorr','You should choose a row to delete .')
        else:
            row=tree.item(selected_item)['values']
            id=row[0]
            result=messagebox.askokcancel('Delete','Are you sure to delete that item?')
            if result:
                email=email_entry_reg.get()
                ArtistConfigurations.delete_artist(id,email)
                fill_treeview()
                clear()
                messagebox.showinfo('Success','Data has been deleted successfully !')
def update():
        selected_item=tree.focus()
        if not selected_item:
            messagebox.showerror('Erorr','You should choose a row to Update data .')
            return
        else:
            name=name_entry_reg.get()
            email=email_entry_reg.get()
            password=password_entry_reg.get()
            row=tree.item(selected_item)['values']
            id=row[0]
            ArtistConfigurations.update_Artist(name,email,password,id)
            fill_treeview()
            clear()
            messagebox.showinfo('Success','Data has been updated successfully !')
        



#fonts:

font1=("Arial", 12, 'bold')
font2=("Arial", 10, 'bold')
font3=('Arial Rounded MT Bold',14,'bold')


    # main Page 
app=ctk.CTk()
app.title("Add Artist")
width=1100
height=600

app.geometry(f'{width}x{height}+300+150')
app.resizable(False,False)
    

    # components 
master= ctk.CTkFrame(app,height=height,width=width)
master.place(relx=0.5,rely=0.5, anchor='center')


    # Load and display background image
image = Image.open('images/IMG-20240802-WA0002.jpg')
img = image.resize((1370,745))
img_tk = ImageTk.PhotoImage(img)
background_label = Label(master, image=img_tk)
background_label.place(x=0, y=0)


frame1 = ctk.CTkFrame(master, width=400, height=420, fg_color='#EDE0D4')
frame1.place(x=20, y=20)



# ===== Welcome Label ==============
Add_Artist_label = ctk.CTkLabel(frame1, text='Add Artist',
                            font=('Arial Rounded MT Bold',30,'bold'),
                            text_color='#000000')
Add_Artist_label.place(x=120, y=20)


#===== User Name  ==========#
name_entry_reg = Entry(frame1, font=font1, highlightthickness=2)
name_entry_reg.place(x=104, y=130, width=300, height=34)
name_entry_reg.config(highlightbackground="black", highlightcolor="black")
name_label_reg = Label(frame1, text='• Name', bg='#EDE0D4', font=font1)
name_label_reg.place(x=100, y=95)


# ============Email  ================#
email_entry_reg = Entry(frame1, font=font1, highlightthickness=2)
email_entry_reg.place(x=104, y=200, width=300, height=34)
email_entry_reg.config(highlightbackground="black", highlightcolor="black")
email_label_reg = Label(frame1, text='• Email account', bg='#EDE0D4', font=font1)
email_label_reg.place(x=100, y=165)



#==============password ==============#
password_entry_reg = Entry(frame1, font=font1, show='•', highlightthickness=2)
password_entry_reg.place(x=104, y=280, width=300, height=34)
password_entry_reg.config(highlightbackground="black", highlightcolor="black")
password_label_reg = Label(frame1, text='• Password', bg='#EDE0D4', font=font1)
password_label_reg.place(x=100, y=245)


#============== Confirm password ==========#
confirm_password_entry_reg = Entry(frame1, font=font1, show='•', highlightthickness=2)
confirm_password_entry_reg.place(x=104, y=360, width=300, height=34)
confirm_password_entry_reg.config(highlightbackground="black", highlightcolor="black")
confirm_password_label_reg = Label(frame1, text='• Confirm Password', bg='#EDE0D4', font=font1)
confirm_password_label_reg.place(x=100, y=320)

def show_password_signUp():
    if password_entry_reg.cget('show') == '•':
        password_entry_reg.config(show='')
        confirm_password_entry_reg.config(show='')
        
    else:
        password_entry_reg.config(show='•')
        confirm_password_entry_reg.config(show='•')


checkButton_reg = Checkbutton(frame1, bg='#EDE0D4',
                            command=show_password_signUp,
                            text='show password', font=font1)
checkButton_reg.place(x=110, y=410)

# ===== name icon ========
name_icon = Image.open('images/name-icon.png')
name_photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(frame1, image=name_photo,  bg='#EDE0D4',fg='#9C6644')
nameIcon_label.image = name_photo
nameIcon_label.place(x=70, y=135)

# ===== Email icon =========
email_icon = Image.open('images/email-icon.png')
email_photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(frame1, image=email_photo,  bg='#EDE0D4',fg='#9C6644')
emailIcon_label.image = email_photo
emailIcon_label.place(x=70, y=205)

# ===== password icon =========
password_icon = Image.open('images/pass-icon.png')
pass_photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(frame1, image=pass_photo, bg='#EDE0D4')
password_icon_label.image = pass_photo
password_icon_label.place(x=75, y=280)

# ===== confirm password icon =========
confirm_password_icon = Image.open('images/pass-icon.png')
c_pass_photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(frame1, image=c_pass_photo, bg='#EDE0D4')
password_icon_label.image = c_pass_photo
password_icon_label.place(x=75, y=360)



def register():
    username = name_entry_reg.get()
    email = email_entry_reg.get()
    password = password_entry_reg.get()
    confirm_password = confirm_password_entry_reg.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Connect to the database
    conn = sqlite3.connect('ArtGalary.db')
    c = conn.cursor()
    if not (username and email and password and confirm_password):
         messagebox.showerror('Error','Enter All Fields Please')
    elif ArtistConfigurations.email_exists(email):
            messagebox.showerror('Error','email already Exists .')
    else:
         
        try:
            
            c.execute("INSERT INTO USERS (UserName,Email, Password) VALUES (? , ? , ?)",
                    (username, email, password))
            c.execute("INSERT INTO Artist (Artist_Name, email,Password)VALUES (?,?,?)",
                    (username,email,password))
            conn.commit()
            messagebox.showinfo("Success", "Artist added successfully")
            fill_treeview()
            clear()
            
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        finally:
            conn.close()


register_button = ctk.CTkButton(frame1, 
                                text="Add Artist", 
                                font=font3,
                                fg_color='#9C6644',
                                hover_color='#B08968',
                                corner_radius=15,
                                width=248, height=40,
                                command= register)
register_button.place(x=80, y=360)







   #======================  treeview  =====================#
style=ttk.Style(master)
style.theme_use('default')
style.configure('Treeview.Heading',
                    background='#5E3023',
                    foreground='#EDE0D4',
                    padding=[5,10,5,10],
                    font=font2, hovercolor='#9C6644')
style.configure('Treeview', font=font2, background='#EDE0D4',fieldbackground='#EDE0D4', rowheight=30)
style.configure("Treeview",rowheight=25)
style.map('Treeview', background=[('selected','#7F5539')])
tree=ttk.Treeview(master,height=60, show='headings')
tree['columns']=('Artist_ID','Name','email','Password')
tree.column('Artist_ID', anchor='center',width=120)
tree.column('Name', anchor='center',width=200)
tree.column('email', anchor='center',width=200)
tree.column('Password', anchor='center',width=280)
tree.heading('Artist_ID', text='Artist_ID')
tree.heading('Name',text='Name')
tree.heading('email',text='email')
tree.heading('Password',text='Password')
tree.place(x=550, y=20,height=530)

tree.bind('<ButtonRelease>',display_data)
fill_treeview()







#=====================Buttons==============#
clear_button=ctk.CTkButton(master,
                               command=lambda :clear(True),text="Clear",
                               font=font3, 
                               fg_color='#9C6644',
                               hover_color='#B08968',
                               corner_radius=10,
                               width=185, height=40)
clear_button.place(x=20,y=450)

update_button=ctk.CTkButton(master,
                                command=update,
                                text="Update Account",
                                font=font3,
                                fg_color='#9C6644'
                                ,hover_color='#B08968',
                                corner_radius=10,
                                width=185, height=40)
update_button.place(x=230,y=450)

delete_button=ctk.CTkButton(master,
                                command=delete,
                                text="Delete Account",
                                font=font3, 
                                fg_color='#5E3023',
                                hover_color='darkred',
                                corner_radius=10, 
                                width=320, 
                                height=40)
delete_button.place(x=60,y=510)


def logout():
        result=messagebox.askokcancel('Delete','Are you sure to Log out ?')
        if result:
            app.destroy()
            import Registeration


logoutIcon = Image.open("images/logout .png")
logoutIcon = logoutIcon.resize((40,40))
logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
logout_btn = ctk.CTkButton(master,image=logoutIcon_tk,
                           text="Logout",
                           corner_radius=10,
                           fg_color='#5E3023',
                           width=300, 
                           font=font3,
                           hover_color='#B08968',
                           command=logout)
logout_btn.place(x=770,y=485)


def Navigate_to_adminPage():
    app.destroy()
    import  add_new_event

Admin_btn = ctk.CTkButton(master,
                           text="Event Configurations ",
                           corner_radius=10,
                           font=font3,
                           fg_color='#9C6644',
                           width=300, 
                           height=40,
                           hover_color='#B08968',
                           command=Navigate_to_adminPage)
Admin_btn.place(x=450,y=485)




app.mainloop()
