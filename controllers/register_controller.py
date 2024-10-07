import re
from models.user_model import UserModel

class RegisterController:
    def __init__(self, view):
        self.view = view

    def is_strong_password(self, password):
        if len(password) < 8:
            return False, "Password must be at least 8 characters long."
        if not re.search("[a-z]", password):
            return False, "Password must contain at least one lowercase letter."
        if not re.search("[A-Z]", password):
            return False, "Password must contain at least one uppercase letter."
        if not re.search("[0-9]", password):
            return False, "Password must contain at least one digit."
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character."
        return True, "Password is strong."

    def get_password_strength(self, password):
        strength = 0
        if len(password) >= 8:
            strength += 20
        if re.search("[a-z]", password):
            strength += 20
        if re.search("[A-Z]", password):
            strength += 20
        if re.search("[0-9]", password):
            strength += 20
        if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            strength += 20
        return strength

    def register_user(self, first_name, last_name, username, email, password, confirm_password, role):
        if first_name == '' or last_name == '' or email == '' or password == '':
            self.view.show_message("Error", "Please Fill All the Fields!")
            return
        
        if password != confirm_password:
            self.view.show_message("Error", "Passwords do not match!")
            return

        is_strong, message = self.is_strong_password(password)
        if not is_strong:
            self.view.show_message("Error", message)
            return

        if UserModel.user_exists(username, email):
            self.view.show_message("Error", "Username or Email already exists!")
            return

        UserModel.create_user(first_name, last_name, username, email, password, role)
        self.view.show_message("Success", "User registered successfully!")
        self.view.redirect_to_login_view()
