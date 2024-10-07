import os
import json
import secrets  # for generating secure tokens
from models.user_model import UserModel
class LoginController:
    def __init__(self, view):
        self.view = view
        self.session_file = 'session.json'
        self.session_data = self.load_session()

    def load_session(self):
        if os.path.exists(self.session_file):
            with open(self.session_file, 'r') as f:
                return json.load(f)
        return {}

    def save_session(self):
        with open(self.session_file, 'w') as f:
            json.dump(self.session_data, f)

    def authenticate_user(self, username, password):
        user = UserModel.verify_user(username, password)
        if user:
            session_token = secrets.token_hex(16)  # Generate a random session token
            self.session_data['username'] = username
            self.session_data['session_token'] = session_token
            self.save_session()

            self.view.show_message("Login Successful", "Welcome!")
            self.view.redirect_to_main_view(username)
        else:
            self.view.show_message("Login Failed", "Invalid username or password.")

    def check_session(self):
        return False

    def get_username(self):
        return self.session_data.get('username', '')

    def logout(self):
        self.session_data = {}
        if os.path.exists(self.session_file):
            os.remove(self.session_file)
