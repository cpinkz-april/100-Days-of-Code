def treasure_island():

    print("Welcome to Treasure Island. Find the treasure, and earn your win!")
    
    direction = input("You find a crossroad. There have 2 signs. One sign turning left, and one sign turning right. Which Left or Right sign will you go?")

    if direction == "Right" or direction == "right":
        print("Game over!")
    if direction == "Left" or direction == "left":
        verb = input("Will you swim or wait?")
        if verb == "Wait" or verb == "wait":
            print("Game over!")
        if verb == "Swim" or "swim":
            door_color = input("Congrats! You've reached the final destination. You know a treasure is hidden behind one of these doors. But there are 3 doors with different colors, 'Red' 'Yellow' 'Blue'. You're making the decision... Which color?")
            if door_color == "Red" or door_color =="red" or door_color == "Blue" or door_color == "blue":
                print("You open the door. But sadly there's no any treasure!!")
            if door_color == "yellow" or "Yellow":
                print("You win! You've found the gold!!")

treasure_island()
