import customtkinter
import time,threading
from tkinter import *
from PIL import Image , ImageTk


app = customtkinter.CTk()
app.geometry('1100x600+300+150')
app.title('welcome')
app.resizable(False,False)
app.config(bg='#EDE0D4')


def navigate_to_Registeration():
    app.destroy()
    import Registeration

#create the main frame
main_frame = customtkinter.CTkFrame(app, width=600, height=1100)
main_frame.pack(side='left',anchor='nw')

# add the image
image = Image.open("images/wallpaperflare.com_wallpaper (2).jpg")
image = image.resize((1375, 750))
photo = ImageTk.PhotoImage(image)
lable=customtkinter.CTkLabel(main_frame,image=photo,text='')
lable.grid(row=0,column=0)


#creating welcome lable
welcome_lbl = customtkinter.CTkLabel(main_frame, image=photo, text='Welcome To Our Art Gallery',fg_color='white',width=600)
welcome_lbl.configure(font=('Curlz MT',26,'bold'))
welcome_lbl.place(relx=0.5,rely=0.45,anchor='center')


# add the dots for loading 
image_a=ImageTk.PhotoImage(Image.open('images/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('images/c1.png'))


def animate_loading():
    for _ in range(5):  # 5 loops
        l1 = Label(main_frame, image=image_a, border=0, relief=SUNKEN).place(relx=0.45, rely=0.7)
        l2 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.47, rely=0.7)
        l3 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.49, rely=0.7)
        l4 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.51, rely=0.7)
        main_frame.update_idletasks()
        time.sleep(0.5)

        l1 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.45, rely=0.7)
        l2 = Label(main_frame, image=image_a, border=0, relief=SUNKEN).place(relx=0.47, rely=0.7)
        l3 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.49, rely=0.7)
        l4 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.51, rely=0.7)
        main_frame.update_idletasks()
        time.sleep(0.5)

        l1 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.45, rely=0.7)
        l2 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.47, rely=0.7)
        l3 = Label(main_frame, image=image_a, border=0, relief=SUNKEN).place(relx=0.49, rely=0.7)
        l4 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.51, rely=0.7)
        main_frame.update_idletasks()
        time.sleep(0.5)

        l1 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.45, rely=0.7)
        l2 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.47, rely=0.7)
        l3 = Label(main_frame, image=image_b, border=0, relief=SUNKEN).place(relx=0.49, rely=0.7)
        l4 = Label(main_frame, image=image_a, border=0, relief=SUNKEN).place(relx=0.51, rely=0.7)
        main_frame.update_idletasks()
        time.sleep(0.5)

# Start the animation in a separate thread
animation_thread = threading.Thread(target=animate_loading)
animation_thread.start()

# Schedule navigation to the new page after 5 seconds
app.after(2000, navigate_to_Registeration)

app.mainloop()