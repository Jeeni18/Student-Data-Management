class NoMatchingNameError(Exception):
    """
    Exception raised when no matching record is found for a given name.
    """
    def __init__(self, name):
        self.message = f"No matching record found for the name: {name}."
        super().__init__(self.message)
        # print(self.message)

class NoMatchingIdError(Exception):
    """
    Exception raised when no matching record is found for a given ID.
    """
    def __init__(self, id):
        self.message = f"No matching record found for the ID: {id}."
        super().__init__(self.message)
        # print(self.message)

class AuthenticationError(Exception):
    """
    Exception raised when authentication fails.
    """
    def __init__(self, name, id):
        self.message = f"Authentication failed for user: {name} with ID: {id}."
        super().__init__(self.message)
        # print(self.message)
