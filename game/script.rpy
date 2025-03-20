# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("The guy")
define i = Character("The girl")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg scene1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show student blush:
        xalign 1.0 yalign 0.0
        linear 2 xalign 0.5 yalign 0.0


    i "first dialogue demo"

    hide student blush
    with dissolve

    show guy at right

    e "testing testing"

    menu:
        "option 1":
            jump option1
        "option 2":
            jump option2

    label option1:
        "u selected option 1"
        jump story
    
    label option2:
        "..."
        jump story

    label story:
        "back to the main story"

    # This ends the game.

    return
