# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yami", color= "#7b6ac5ff")
define s = Character("Stranger", color= "#951d1d")
define d = Character("???", color= "#ffffff")
define k = Character("Prof. Kure", color= "#ffffff")
define t = Character("Tenshi", color= "#d69bea")
define tv = Character("Television", color= "#01ff3c")

# The game starts here.

label start:
    $ player_name = renpy.input("Write a name to begin your journey...")

    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Kyu"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    tv "Please my darling! Stay with me! I cannot lose you like this, why did you have to do it on our honeymoon! Why did you have to do it at all?!"

    tv "Oh my dear… The time has come and death shall put me to peace…"

    "Grumble... Grumble..."

    "Ugh... I'm so hungry..."

    # This ends the game.

    return
