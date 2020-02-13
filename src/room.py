# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, initial_items = []):
        self.name = name
        self.description = description
        self.items = initial_items