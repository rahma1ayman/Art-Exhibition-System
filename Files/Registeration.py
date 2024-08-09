import sqlite3
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


font1=("Arial", 12, 'bold')
font2=("Arial", 10, 'bold')
app=ctk.CTk()

app.geometry('1100x600+300+150')
app.resizable(False, False)
app.title('Login and Registration Page')

LoginPage = ctk.CTkFrame(app,height=600,width=1100)
RegistrationPage = ctk.CTkFrame(app)
for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)



#====== on login frame ============#
frame1=ctk.CTkFrame(LoginPage,height=600,width=1100)
frame1.pack()
frame2 = ctk.CTkFrame(LoginPage,width=450,height=400,fg_color='#EDE0D4')
frame2.place(relx=0.5,rely=0.5,anchor='center')

# background Image
image = Image.open('images/IMG-20240802-WA0002.jpg')
img1 = image.resize((1370,745))
img_tk1 = ImageTk.PhotoImage(img1)
background_Login = Label(frame1, image=img_tk1)
background_Login.place(x=0, y=0)


# ===== Welcome Label ==============
welcome_label = ctk.CTkLabel(frame2, text='Welcome!', 
                             font=('Arial Rounded MT Bold',30,'bold'),
                             text_color='#000000')
welcome_label.place(x=148, y=60)


#====== email Entry =========#
email_entry = Entry(frame2, font=font1, highlightthickness=2)
email_entry.place(x=134, y=190, width=300, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(frame2, text='• Email account',bg='#EDE0D4', font=font1)
email_label.place(x=130, y=155)

# ==== Password ==================
password_entry = Entry(frame2, font=font1, show='•', highlightthickness=2)
password_entry.place(x=134, y=270, width=300, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(frame2, text='• Password', bg='#EDE0D4', font=font1)
password_label.place(x=130, y=235)


# function for show and hide password
def show_password():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
    else:
        password_entry.config(show='•')


# ====== checkbutton for show password  ==============
checkButton = Checkbutton(frame2, bg='#EDE0D4', command=show_password, text='show password',font=font2)
checkButton.place(x=140, y=315)


# ==== LOGIN Button ============

login_button=ctk.CTkButton(frame2,text="Login",
                           font=font1, 
                           fg_color='#9C6644', hover_color='#B08968',
                           corner_radius=15, width=248, height=40,
                           command=lambda: login(email_entry.get(), password_entry.get()))
login_button.place(x=105, y=300)



# ===== Email icon =========
email_icon = Image.open('images/email-icon.png')
email_photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(frame2, image=email_photo,bg='#EDE0D4',fg='#9C6644')
emailIcon_label.image = email_photo
emailIcon_label.place(x=105, y=190)

# ===== password icon =========
password_icon = Image.open('images/pass-icon.png')
pass_photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(frame2, image=pass_photo, bg='#EDE0D4')
password_icon_label.image = pass_photo
password_icon_label.place(x=105, y=270)

# ===== Account icon =========
Account_icon = Image.open('images/pic-icon.png')
Account_photo = ImageTk.PhotoImage(Account_icon)
picture_icon_label = Label(frame2, image=Account_photo ,  bg='#EDE0D4')
picture_icon_label.image = Account_photo 
picture_icon_label.place(x=250, y=20)

# create new account
newaccount_label=ctk.CTkLabel(frame2,
                               text='Not a member ? : ',
                               font=font1,text_color='#000000')
newaccount_label.place(x=160,y=350)

SignUp_button = Button(frame2, text='Sign up',
                        font=font1,
                        bg='#EDE0D4',fg='#5E3023',
                        command=lambda: show_frame(RegistrationPage), 
                        borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=310, y=440)



    
def forgot_password():
    def update_password():
        email = email_entry.get()
        new_password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if new_password == confirm_password:
            # Update the password in the database
            try:
                conn = sqlite3.connect('ArtGalary.db')
                cursor = conn.cursor()
                cursor.execute('''UPDATE USERS
                SET Password = ? where email= ?''', (new_password, email))
                conn.commit()
                
                # Notify the user that the password was updated successfully
                ctk.CTkLabel(forget_pass_frame, text="Password updated successfully!", text_color="green").place(x=155, y=350)
            except sqlite3.Error as error:
                print("Failed to update password", error)
                ctk.CTkLabel(forget_pass_frame, text="Failed to update password.", text_color="red").place(x=155, y=350)
        else:
            ctk.CTkLabel(forget_pass_frame, text="Passwords do not match.", text_color="red").place(x=155, y=350)
        
        conn.close()
        


    #### Update password window : 

    win = Toplevel()
    window_width = 600
    window_height = 500
    
    win.geometry(f'{window_width}x{window_height}+300+250')
    win.title('Forgot Password')
    win.configure(bg='#EDE0D4')
    win.resizable(0, 0)
    forget_pass_frame=ctk.CTkFrame(win, width=500,height=400, fg_color='#EDE0D4')
    forget_pass_frame.place(relx=0.5,rely=0.5, anchor='center')

    #label for address 
    forgetLabel= ctk.CTkLabel(forget_pass_frame, text='Reset Password',
                               font=('Arial Rounded MT Bold',20,'bold')
                               ,text_color='#000000')
    forgetLabel.place(x=160,y=15)


    # ============email entry =============#
    email_entry = Entry(forget_pass_frame, font=font1, highlightthickness=2)
    email_entry.place(x=155, y=120, width=300, height=34)
    email_entry.config(highlightbackground="black", highlightcolor="black")
    email_label = Label(forget_pass_frame, text='• Email account',bg='#EDE0D4', font=font1)
    email_label.place(x=150, y=80)


    # ========== Password ==================#
    password_entry = Entry(forget_pass_frame, font=font1, show='•', highlightthickness=2)
    password_entry.place(x=155, y=200, width=300, height=34)
    password_entry.config(highlightbackground="black", highlightcolor="black")
    password_label = Label(forget_pass_frame, text='• Password', bg='#EDE0D4', font=font1)
    password_label.place(x=150, y=165)

    # ==== Confirm _Password ==================
    confirm_password_entry = Entry(forget_pass_frame, font=font1, show='•', highlightthickness=2)
    confirm_password_entry.place(x=155, y=280, width=300, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(forget_pass_frame, text='• Confirm Password', bg='#EDE0D4', font=font1)
    confirm_password_label.place(x=150, y=240)

    Update_button=ctk.CTkButton(forget_pass_frame,text="Update Password",
                                font=font1, 
                                fg_color='#9C6644',
                                hover_color='#B08968',
                                corner_radius=15,
                                width=248, height=40,
                                command=update_password)
    Update_button.place(x=125, y=300)
    
    
# ================ forgetPassword button====================== :

forgotPassword = Button(frame2, text='Forgot password ?', 
                        font=font2, bg='#EDE0D4',
                        borderwidth=0, activebackground='#f8f8f8',
                        command=lambda: forgot_password(), cursor="hand2")
forgotPassword.place(x=330, y=315)


def login(email, password):
    # Connect to the database
    conn = sqlite3.connect('ArtGalary.db')
    c = conn.cursor()

    # Query to find the user
    c.execute("SELECT * FROM USERS WHERE email=? AND password=?", (email, password))
    user = c.fetchone()

    if user:
        messagebox.showinfo("Success", "Logged in successfully")
        if "admin" in email:
            app.destroy()
            import add_new_artist
        elif "artist" in email:
            app.destroy()
            import artistProfile
            artistProfile.artistProfile(email)
        else:
            app.destroy()
            import categories
    else:
        messagebox.showerror("Error", "Invalid username or password")
    conn.close()
    email_entry.delete('0',END)
    password_entry.delete('0',END)









#=============================================================================#







# Create the SignUp page UI
frame3 = ctk.CTkFrame(RegistrationPage, height=600, width=1100)
frame3.pack()
frame4 = ctk.CTkFrame(RegistrationPage, width=450, height=500, fg_color='#EDE0D4')
frame4.place(relx=0.5, rely=0.5, anchor='center')


# background Image  :
image2 = Image.open('images/IMG-20240802-WA0002.jpg')
img2 = image.resize((1370,745))
img_tk2 = ImageTk.PhotoImage(img2)
background_signUp = Label(frame3, image=img_tk2)
background_signUp.place(x=0, y=0)

# ===== Welcome Label ==============
SignUp_label = ctk.CTkLabel(frame4, text='SignUp',
                            font=('Arial Rounded MT Bold',30,'bold'),
                            text_color='#000000')
SignUp_label.place(x=170, y=50)


#===== User Name  ==========#
name_entry_reg = Entry(frame4, font=font1, highlightthickness=2)
name_entry_reg.place(x=134, y=160, width=300, height=34)
name_entry_reg.config(highlightbackground="black", highlightcolor="black")
name_label_reg = Label(frame4, text='• Name', bg='#EDE0D4', font=font1)
name_label_reg.place(x=130, y=125)


# ============Email  ================#
email_entry_reg = Entry(frame4, font=font1, highlightthickness=2)
email_entry_reg.place(x=134, y=230, width=300, height=34)
email_entry_reg.config(highlightbackground="black", highlightcolor="black")
email_label_reg = Label(frame4, text='• Email account', bg='#EDE0D4', font=font1)
email_label_reg.place(x=130, y=195)



#==============password ==============#
password_entry_reg = Entry(frame4, font=font1, show='•', highlightthickness=2)
password_entry_reg.place(x=134, y=310, width=300, height=34)
password_entry_reg.config(highlightbackground="black", highlightcolor="black")
password_label_reg = Label(frame4, text='• Password', bg='#EDE0D4', font=font1)
password_label_reg.place(x=130, y=275)


#============== Confirm password ==========#
confirm_password_entry_reg = Entry(frame4, font=font1, show='•', highlightthickness=2)
confirm_password_entry_reg.place(x=134, y=390, width=300, height=34)
confirm_password_entry_reg.config(highlightbackground="black", highlightcolor="black")
confirm_password_label_reg = Label(frame4, text='• Confirm Password', bg='#EDE0D4', font=font1)
confirm_password_label_reg.place(x=130, y=350)

def show_password_signUp():
    if password_entry_reg.cget('show') == '•':
        password_entry_reg.config(show='')
        confirm_password_entry_reg.config(show='')
        
    else:
        password_entry_reg.config(show='•')
        confirm_password_entry_reg.config(show='•')


checkButton_reg = Checkbutton(frame4, bg='#EDE0D4',
                            command=show_password_signUp,
                            text='show password', font=font1)
checkButton_reg.place(x=140, y=440)

# ===== name icon ========
name_icon = Image.open('images/name-icon.png')
name_photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(frame4, image=name_photo,  bg='#EDE0D4',fg='#9C6644')
nameIcon_label.image = name_photo
nameIcon_label.place(x=100, y=165)

# ===== Email icon =========
email_icon = Image.open('images/email-icon.png')
email_photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(frame4, image=email_photo,  bg='#EDE0D4',fg='#9C6644')
emailIcon_label.image = email_photo
emailIcon_label.place(x=100, y=235)

# ===== password icon =========
password_icon = Image.open('images/pass-icon.png')
pass_photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(frame4, image=pass_photo, bg='#EDE0D4')
password_icon_label.image = pass_photo
password_icon_label.place(x=105, y=310)

# ===== confirm password icon =========
confirm_password_icon = Image.open('images/pass-icon.png')
c_pass_photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(frame4, image=c_pass_photo, bg='#EDE0D4')
password_icon_label.image = c_pass_photo
password_icon_label.place(x=105, y=390)

# ===== pic icon =========
pic_icon = Image.open('images/pic-icon.png')
pic_photo = ImageTk.PhotoImage(pic_icon)
pic_icon_label = Label(frame4, image=pic_photo,  bg='#EDE0D4')
pic_icon_label.image = pic_photo
pic_icon_label.place(x=250, y=10)

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

    try:
        
        c.execute("INSERT INTO USERS (UserName,Email, Password) VALUES (? , ? , ?)",
                   (username, email, password))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully")
        show_frame(LoginPage)
        
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")
    finally:
        conn.close()


register_button = ctk.CTkButton(frame4, 
                                text="Create Account", 
                                font=font1,
                                fg_color='#9C6644',
                                hover_color='#B08968',
                                corner_radius=15,
                                width=248, height=40,
                                command= register)
register_button.place(x=105, y=400)

existing_label = ctk.CTkLabel(frame4, text='Already have an account? :', 
                              font=font1, text_color='#000000')
existing_label.place(x=130, y=450)

Login_button = Button(frame4, text='Login', font=font1,bg='#EDE0D4',fg='#5E3023',
                       command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
Login_button.place(x=355, y=565)



app.mainloop()