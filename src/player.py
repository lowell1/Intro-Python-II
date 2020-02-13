# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room, initial_items = {}):
        self.current_room = room
        self.items = initial_items