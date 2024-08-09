from tkinter import *
from PIL import Image, ImageTk
import customtkinter as CTK

primaryColor = "#EDE0D4"
secondaryColor="#E6CCB2"
thirdColor="#DDB892"
btnColor="#9C6644"
hovColor="#B08968"

image_refs = {}
# Create the main window
Categories = CTK.CTk()
Categories.title("Art Gallery")
Categories.geometry("1100x600+300+150")
Categories.resizable(False, False)
# Set the background color of the root window
Categories.config(bg='#EDE0D4')


def navigationBar():
    nav_frame = CTK.CTkFrame(Categories,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
    nav_frame.grid(row=0,column=0,sticky="nw") 
    
    artist_img = Image.open("images/painter.png")
    artist_img = artist_img.resize((50,50))
    artist_img_tk = ImageTk.PhotoImage(artist_img)
    artist_lbl = CTK.CTkLabel(nav_frame,text="",image=artist_img_tk)
    artist_lbl.grid(row=0,column=0,pady=(30,0))

    icons_frame = CTK.CTkFrame(nav_frame,width=150,height=600,fg_color="#7F5539",bg_color="#7F5539")
    icons_frame.grid(row=1,column=0,pady=(80,250))

    categoryIcon = Image.open("images/choice.png")
    categoryIcon = categoryIcon.resize((45,45))
    profileIcon_tk = ImageTk.PhotoImage(categoryIcon)    
    profile_btn = CTK.CTkButton(icons_frame,image=profileIcon_tk,text="Arts",bg_color="transparent",fg_color="transparent",hover_color=hovColor)
    profile_btn.grid(pady=(0,40))

    def events():
        Categories.destroy()
        import events

    eventIcon = Image.open("images/event.png")
    eventIcon = eventIcon.resize((50,50))
    postIcon_tk = ImageTk.PhotoImage(eventIcon)    
    post_btn = CTK.CTkButton(icons_frame,image=postIcon_tk,text="Events",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=events)
    post_btn.grid(pady=(0,40))

    def logout():
        Categories.destroy()
        import Registeration

    logoutIcon = Image.open("images/logout .png")
    logoutIcon = logoutIcon.resize((50,50))
    logoutIcon_tk = ImageTk.PhotoImage(logoutIcon)    
    logout_btn = CTK.CTkButton(icons_frame,image=logoutIcon_tk,text="Logout",bg_color="transparent",fg_color="transparent",hover_color=hovColor,command=logout)
    logout_btn.grid()


navigationBar()

# Create a label for the first line of text
label1 = CTK.CTkLabel(Categories, text="Welcome to our Art Gallery!", font=("Arial", 30, 'bold'), bg_color='#EDE0D4', text_color='black')
label1.place(x=380, y=20)

# Create a label for the second line of text
label2 = CTK.CTkLabel(Categories, text="Select your Category", font=("Arial", 26, 'bold'), bg_color='#EDE0D4', text_color='black')
label2.place(x=450, y=80)

# Function to load and keep a reference to images
def load_image(path, size):
    image = Image.open(path)
    image = image.resize(size)
    image_tk = ImageTk.PhotoImage(image)
    image_refs[path] = image_tk
    return image_tk

photo1 = load_image('images/painting art.jpeg', (250, 200))
photo2 = load_image('images/Expressionism arts.jpeg', (250, 200))
photo3 = load_image('images/Figuratve art.jpeg', (250, 200))
photo4 = load_image('images/Abstrct art.jpeg', (250, 200))
photo5 = load_image('images/Sculpture arts.jpeg', (250, 200))
photo6 = load_image('images/Visual arts.jpeg', (250, 200))

def onTap(catg):
    Categories.destroy()
    import categoryArts
    categoryArts.Arts(catg)

# Create the buttons
btn1 = CTK.CTkButton(Categories, text='Painting Arts', image=photo1, font=("Arial", 12, 'bold'), command=lambda:onTap("Painting Art"), fg_color=btnColor,bg_color=btnColor, compound='top',hover_color=hovColor)
btn2 = CTK.CTkButton(Categories, text='Expressionism Arts', image=photo2, font=("Arial", 12, 'bold'), command=lambda:onTap("Expressionism Art"), fg_color=btnColor,bg_color=btnColor,compound='top', hover_color=hovColor)
btn3 = CTK.CTkButton(Categories, text='Figuratve Arts', image=photo3, font=("Arial", 12, 'bold'), command=lambda:onTap("Figurative Art"), fg_color=btnColor,bg_color=btnColor,compound='top',hover_color=hovColor)
btn4 = CTK.CTkButton(Categories, text='Abstract Arts', image=photo4, font=("Arial", 12, 'bold'), command=lambda:onTap("Abstract Art"), fg_color=btnColor,bg_color=btnColor,compound='top',hover_color=hovColor)
btn5 = CTK.CTkButton(Categories, text='Sculpture arts', image=photo5, font=("Arial", 12, 'bold'), command=lambda:onTap("Sculpture Art"), fg_color=btnColor,bg_color=btnColor,compound='top', hover_color=hovColor)
btn6 = CTK.CTkButton(Categories, text='Visual arts', image=photo6, font=("Arial", 12, 'bold'), command=lambda:onTap("Visual Art"), fg_color=btnColor,bg_color=btnColor,compound='top', hover_color=hovColor)

# Arrange the buttons in a grid
btn1.place(x=270, y=140)
btn2.place(x=540, y=140)
btn3.place(x=800, y=140)
btn4.place(x=270, y=370)
btn5.place(x=540, y=370)
btn6.place(x=800, y=370)

Categories.mainloop()