import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
from controllers.login_controller import LoginController
from views.register_view import RegisterView
class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title('Login')

        self.controller = LoginController(self)

        # Load images
        self.img1 = ImageTk.PhotoImage(Image.open("./static/assets/images/pattern.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("./static/assets/images/Google__G__Logo.webp").resize((20, 20), Image.LANCZOS))
        self.img3 = ImageTk.PhotoImage(Image.open("./static/assets/images/124010.png").resize((20, 20), Image.LANCZOS))

        # Create label with image
        self.l1 = ctk.CTkLabel(master=self.root, image=self.img1)
        self.l1.pack()
        
        # Create custom frame
        self.frame = ctk.CTkFrame(master=self.l1, width=320, height=360, corner_radius=15,bg_color='#fff',fg_color='#fff')
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Labels, entries, and buttons
        self.l2 = ctk.CTkLabel(master=self.frame, text="Log into your Account", font=('Futura', 20))
        self.l2.place(x=60, y=45)

        self.entry1 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Username')
        self.entry1.place(x=50, y=110)

        self.entry2 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Password', show="*")
        self.entry2.place(x=50, y=165)

        self.l3 = ctk.CTkLabel(master=self.frame, text="Forget password?", font=('Century Gothic', 12))
        self.l3.place(x=155, y=195)

        self.button1 = ctk.CTkButton(master=self.frame, width=220, text="Login", command=self.login, corner_radius=6)
        self.button1.place(x=50, y=240)
        self.log_in_label = ctk.CTkLabel(master=self.frame, text="Don't have an Account? Sign Up", font=('Futura', 12))
        self.log_in_label.place(x=70, y=290)
        self.log_in_label.bind("<Button-1>", self.switch_to_register)
        username = self.controller.check_session()
        if username:
            self.redirect_to_main_view(self.controller.get_username())

    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        self.controller.authenticate_user(username, password)
    def switch_to_register(self, event):
        self.root.destroy()
        root = tk.Tk()
        register_view = RegisterView(root)
        register_view.show()
    def show_message(self, title, message):
        messagebox.showinfo(title, message)  # Use messagebox.show_info from tkinter

    def redirect_to_main_view(self,username):
        self.root.destroy()  # Close current window
        root = tk.Tk()
        welcome_view = Dashboard(root,username)
        welcome_view.show()