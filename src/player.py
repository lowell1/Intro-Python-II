# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room, initial_items = []):
        self.current_room = room
        self.items = initial_items
        
    def take_item(self, item_name):
#        if item in [item.name for item in self.current_room.items]:
#            print(f"You picked up: {item}")
 #           self.items.append(item
#        elif len(self.items) == self.max_items:
#            print("You're inventory is full.")
#        else:
            for index, item in enumerate(self.current_room.items):
                if item.name == item_name:
                    print("You picked up a(n) " + item_name)
                    self.items.append(item)
                    del self.current_room.items[index]
                    return
                    
            print("\nYou look around, but cannot find a(n) " + item_name)
            

    def drop_item(self, item_name):
        for index, item in enumerate(self.items):
            if item.name == item_name:
                print("You dropped a(n) " + item_name)
                self.current_room.items.append(item)
                del self.items[index]
                return
                
        print("You do not have a(n) " + item_name)