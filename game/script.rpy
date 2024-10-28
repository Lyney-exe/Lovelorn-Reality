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
    
    scene bg livingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    tv "Please my darling! Stay with me! I cannot lose you like this, why did you have to do it on our honeymoon! Why did you have to do it at all?!"

    tv "Oh my dear… The time has come and death shall put me to peace…"

    tv "Please do not end your life! You have so much more ahead of you!"

    tv "Oh my dear husband... Life has already gave me everything..."

    tv "Don't close your eyes just yet, look at me and breathe darling... Please..."

    tv "Hold me close to your heart... And I'll... be with you, forever..."

    tv "Yes my love... I shall see you, in our next life..."

    "Grumble... Grumble..."

    player_name "Ugh... I'm so hungry..."

    "You get up from the couch and turn off your TV, heading your way to the kitchen side of your dorm."

    player_name "Alright, let's see..."

    player_name "!!!"

    player_name "Are you kidding me?! I swear, I went grocery shopping yesterday!"

    "You gave out one long sigh and shut the empty fridge door closed. You whined as you knew what you had to do."

    player_name "Argh, now I have to go to the supermarket AGAIN. Tough day, no relaxing for me today I guess."

    "You walk over to the front door of the dorm and slide your shoes on while taking a hoodie to wear on your way out to the nearest corner store."

    







    # This ends the game.

    return
