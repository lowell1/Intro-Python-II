# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room, initial_items = {}):
        self.current_room = room
        self.items = initial_items
        
    def take_item(self, item):
        if item not in current_room.items:
            print(f"You look around, but cannot find a(n) {item}")
        elif len(self.items) == max_items:
            print("You're inventory is full.")
        else:
            print(f"You picked up: {item}")

#    def drop_item(self, item)
  #      if item in self.items: