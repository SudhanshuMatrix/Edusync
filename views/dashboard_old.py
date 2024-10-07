import tkinter as tk
from controllers.logout_controller import LogoutController

class Dashboard:
    def __init__(self, root, username, login_controller):
        self.root = root
        self.logout_controller = LogoutController('session.json')  # Initialize LogoutController
        self.is_fullscreen = False

        # Set the window size to the screen size
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.title('Welcome ' + username)

        # Label
        self.l1 = tk.Label(master=self.root, text="Home Page", font=('Century Gothic', 60))
        self.l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Button to logout
        self.button_logout = tk.Button(master=self.root, text="Logout", command=lambda: self.logout(login_controller))
        self.button_logout.pack()

    def minimize(self):
        self.root.iconify()

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)

    def logout(self, login_controller):
        self.logout_controller.logout()
        self.root.destroy()
        import views.login_view
        root = tk.Tk()
        login_view = views.login_view.LoginView(root)
        login_view.show()

    def show(self):
        self.root.mainloop()