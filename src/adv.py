from room import Room
from player import Player
from textwrap3 import TextWrapper
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("item1", "?????????"), Item("item2", "?????????")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(room["outside"])

cmd = ""

directions = ("south", "north", "west", "east")

textwrap = TextWrapper(initial_indent = "      ", subsequent_indent = "      ", width=50)

while cmd != "q":
    print(f"\n\n\nYou are in the {player.current_room.name} room\n\n{textwrap.fill(player.current_room.description)}\n")
    
    current_room_item_names = [item.name for item in player.current_room.items]
    print("In the room you see the following items: " + (", ".join(current_room_item_names) or "(no items)"))
    
    player_item_names = [item.name for item in player.items]
    print("Your items: " + (", ".join(player_item_names) or "(no items)"))

    #the directions you can go from the current room (north, east, west, south)
    possible_directions = [f"({ele[0]}){ele[1:]}" for ele in directions if hasattr(player.current_room, ele[0] + "_to")]
    
    cmd = input("Enter %s, take <item>, drop <item>, (q)uit: " % ", ".join(possible_directions)).lower()
    
    if cmd in ("n", "e", "w", "s"):
        #if the user enters a direction (e,n,w,s), concatenate "_to" to make "e_to", "n_to" etc
        #make sure room has this attribute or else getattr will raise an error
        #set "player.current_room" to the instance of "Room" that the attribute "?_to" references
        if hasattr(player.current_room, cmd + "_to"):
            player.current_room = getattr(player.current_room, cmd + "_to")
        else:
            print("invalid direction")
    elif cmd[:4] == "take":
        player.take_item(cmd[5:])
    elif cmd[:4] == "drop":
        player.drop_item(cmd[5:])
    elif cmd != "q":
        print("unknown command")
    
