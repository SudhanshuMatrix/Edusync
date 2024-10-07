import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
from controllers.register_controller import RegisterController

class RegisterView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title('Register')

        self.controller = RegisterController(self)
        self.selected_role = None

        # Load images
        self.img1 = ImageTk.PhotoImage(Image.open("./static/assets/images/pattern.png"))

        # Create label with image
        self.l1 = ctk.CTkLabel(master=self.root, image=self.img1)
        self.l1.pack()

        # Create custom frame
        self.frame = ctk.CTkFrame(master=self.l1, width=320, height=560, corner_radius=15, bg_color='#fff',fg_color='#fff')
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Labels, entries, and buttons
        self.l2 = ctk.CTkLabel(master=self.frame,height=24,width=24, text="Create a New Account", font=('Futura', 20))
        self.l2.place(x=60, y=20)

        self.entry1 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='First Name')
        self.entry1.place(x=50, y=70)

        self.entry2 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Last Name')
        self.entry2.place(x=50, y=120)

        self.entry3 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Username')
        self.entry3.place(x=50, y=170)

        self.entry4 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Email')
        self.entry4.place(x=50, y=220)

        self.entry5 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Password', show="*")
        self.entry5.place(x=50, y=270)
        self.entry5.bind('<KeyRelease>', self.update_password_strength)  # Bind key release event to update password strength

        # Label to display password strength
        self.password_strength_label = ctk.CTkLabel(master=self.frame, text="Password Strength:", font=('Helvetica', 12, 'bold'))
        self.password_strength_label.place(x=50, y=310)

        # Label to show strength status
        self.strength_status_label = ctk.CTkLabel(master=self.frame, text="", font=('Helvetica', 12))
        self.strength_status_label.place(x=50, y=330)

        self.entry6 = ctk.CTkEntry(master=self.frame, width=220, placeholder_text='Confirm Password', show="*")
        self.entry6.place(x=50, y=355)
        self.button2 = ctk.CTkButton(master=self.frame, text="Student", width=100, height=20,
                                     fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda: self.select_role("student"))
        self.button2.place(x=50, y=400)

        self.button3 = ctk.CTkButton(master=self.frame, text="Teacher", width=100, height=20,
                                     fg_color='white', text_color='black', hover_color='#AFAFAF', command=lambda: self.select_role("teacher"))
        self.button3.place(x=170, y=400)
        self.button1 = ctk.CTkButton(master=self.frame, width=220, text="Register", command=self.register, corner_radius=6)
        self.button1.place(x=50, y=440)
        self.sign_up_label = ctk.CTkLabel(master=self.frame, text="Already Have an Account? Log in", font=('Futura', 12))
        self.sign_up_label.place(x=70, y=490)
        self.sign_up_label.bind("<Button-1>", self.switch_to_login)


    def select_role(self, role):
        self.selected_role = role
        self.update_role_buttons()

    def switch_to_login(self, event):
        self.root.destroy()
        import views.login_view
        root = tk.Tk()
        login_view = views.login_view.LoginView(root)
        login_view.show()
    def update_role_buttons(self):
        # Update button colors based on selected role
        if self.selected_role == "student":
            self.button2.configure(fg_color='blue', text_color='white')
            self.button3.configure(fg_color='white', text_color='black')
        elif self.selected_role == "teacher":
            self.button2.configure(fg_color='white', text_color='black')
            self.button3.configure(fg_color='blue', text_color='white')
        else:
            self.button2.configure(fg_color='white', text_color='black')
            self.button3.configure(fg_color='white', text_color='black')

    def update_password_strength(self, event):
        password = self.entry5.get()
        strength = self.controller.get_password_strength(password)
        self.update_strength_label(strength)

    def update_strength_label(self, strength):
        if strength < 30:
            self.strength_status_label.configure(text="Weak", text_color="red")
        elif strength < 80:
            self.strength_status_label.configure(text="Medium", text_color="orange")
        else:
            self.strength_status_label.configure(text="Strong",text_color="green")

    def register(self):
        first_name = self.entry1.get()
        last_name = self.entry2.get()
        username = self.entry3.get()
        email = self.entry4.get()
        password = self.entry5.get()
        confirm_password = self.entry6.get()

        if not self.selected_role:
            messagebox.showerror("Error", "Please select a role (Student/Teacher)")
            return

        self.controller.register_user(first_name, last_name, username, email, password, confirm_password, self.selected_role)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def redirect_to_login_view(self):
        self.root.destroy()
        root = tk.Tk()
        from views.login_view import LoginView
        login_view = LoginView(root)
        login_view.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterView(root)
    root.mainloop()
