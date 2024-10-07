import os

class LogoutController:
    def __init__(self, session_file='session.json'):
        self.session_file = session_file  # Set the path to the session.json file

    def logout(self):
        """Deletes the session.json file to log out the user."""
        try:
            # Check if the session file exists
            if os.path.exists(self.session_file):
                # Delete the session.json file
                os.remove(self.session_file)
                print("Session file deleted successfully.")
            else:
                print("Session file does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the LogoutController with the path to session.json (optional)
    controller = LogoutController('path/to/session.json')  # Modify the path if needed
    controller.logout()