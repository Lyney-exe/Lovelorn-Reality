# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yami", color= "#7b6ac5ff")
define s = Character("Étranger", color= "#951d1d")
define tv = Character("Television", color= "#01ff3c")

# The game starts here.

label start:
    $ player_name = renpy.input("Inscrivez un nom pour commencer votre journée: ")

    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Kyu";

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg livingroom
    with dissolve
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    tv "S'il te plaît, ma chérie ! Reste avec moi ! Je ne peux pas te perdre comme ça, pourquoi as-tu fait ça pendant notre lune de miel ! Pourquoi fallait-il que tu le fasses tout court ? !"

    tv "Oh mon cher... L'heure est venue et la mort m'apportera la paix..."

    tv "S'il vous plaît, ne mettez pas fin à votre vie ! Tu as encore tant de choses devant toi !"

    tv "Oh mon cher mari... La vie m'a déjà tout donné..."

    tv "Ne ferme pas encore les yeux, regarde-moi et respire, chérie... S'il te plaît..."

    tv "Tiens-moi près de ton coeur... Et je serai... avec toi, pour toujours..."

    tv "Oui, mon amour... Je te reverrai dans notre prochaine vie..."

    "Grumble... Grumble..."

    player_name "Ugh... Je suis tellement faim..."

    "Tu te lèves du canapé, tu éteins la télé et tu te diriges vers la cuisine de ton dortoir."

    player_name "D'accord, voyons voir..."

    player_name "!!!" with vpunch

    player_name "Est-ce que tu blague ?! Je jure que j'ai fait du magazinage hier!"

    "Tu as poussé un long soupir et tu as refermé la porte du réfrigérateur vide. Tu as pleurniché en sachant ce qu'il te restait à faire."

    player_name "Argh, Maintenant, je dois encore aller au supermarché. Dure journée, pas de détente pour moi aujourd'hui, je suppose."

    "Vous vous dirigez vers la porte d'entrée du dortoir et vous enfilez vos chaussures tout en prenant un sweat à capuche que vous porterez en allant au magasin du coin le plus proche."

    "La brise fraîche de l'air froid frappe votre visage alors que vous sortez, vous retournant, vous assurant que la porte est bien fermée derrière vous."

    "En marchant sur le bord de la route, vous vous rendez compte que le soleil s'est couché plus tôt que vous ne le pensiez."

    menu:
        "Retourner à la maison":
            $ menu_flag = True

            player_name "A bien y réfléchir... Rester à la maison me semble mieux, et plus réconfortant. Je vais commander un plat chinois à emporter. "

            "Bonus Ending: Takeout"

            return

        "Continuer à marcher":
            $ menu_flag = False

            player_name "Une petite visite ne fait pas de mal, en plus c'est très calme dans ce quartier."




label after_walking:

# ... the game continues here.

    "Vous vous dirigez vers l'îlot où se trouve le congélateur."

    player_name "Mmm... Rien de plaisant..."

    "Vous vous dirigez vers un autre région dans le magasin, regardant les nouilles instantanées sur l'étagère afin d'en prendre une pour le dîner de ce soir."

    "Vous vous rendez à l'arrière du magasin pour trouver l'endroit où les boissons sont conservées. Vous jetez un coup d'œil pour voir le milkshake à la fraise en édition limitée, et il est coincé entre quelques autres boissons à l'arrière."

    player_name "Pas question que j'obtienne cela d'aussi loin !"

    "Vous êtes donc reparti déçu de ne pas avoir pu acheter la boisson que vous vouliez, et vous êtes allé acheter quelques collation pour le lendemain."

    "En les ramassant et en les tenant dans vos mains, vous avez vu un homme de grande taille ouvrir la porte des boissons et attraper facilement la dernière bouteille de lait à la fraise."

    "Vous soupirez de défaite. Encore une fois, le milkshake à la fraise est hors service !"

    show yami neutral with dissolve

    init:
        image yami neutral:
            "yami neutral.png"
            zoom 1.3

    "Le grand homme vêtu de noir s'approche de vous, vous vous préparez à la rencontre."
    
    show yami confusedtalking

    init:
        image yami confusedtalking:
            "yami confusedtalking.png"
            zoom 1.3

    s "C'est ce que vous vouliez... ? Je t'ai vu tout à l'heure le regarder, mais tu ne l'as pas pris. J'ai donc décidé de vous aider un peu."

    menu:
        "Le remercier":
            jump thank_yami

        "Se méfier":
            jump wary_of_yami

label thank_yami:
    $ menu_flag = True

    show yami neutral

    player_name "Merci beaucoup!"

    show yami neutraltalking
    init:
        image yami neutraltalking:
            "yami neutraltalking.png"
            zoom 1.3

    s "Pas de problème, est-ce que vous voulez d'aide avec d'autre choses?"

    show yami neutral

    "Il a regardé vos mains pleines de collation et votre dîner."

    show yami neutraltalking

    s "Tu sais quoi, je vais payer pour tes affaires. Je pense que je vous connais de quelque part."

    show yami neutral

    player_name "Vraiment? Quelle université fréquentez-vous ?"

    show yami neutraltalking

    s "Université de Moonshell."

    player_name "Tu blague pas? Moi aussi!"

    jump after_yami

label wary_of_yami:
    $ menu_flag = False

    player_name "Uhm... Merci..."

    "Vous prenez avec précaution la boisson que vous vouliez dans sa main, en le regardant à plusieurs reprises, lui et sa main."

    "L'homme regarde votre pile remplie d'en-cas et votre dîner."

    s "Avez-vous besoin d'aide pour ces... ?"

    player_name "Non ! Pas du tout ! Je n'ai pas besoin d'un étranger pour m'aider !"

    "Vous essayez de marcher rapidement jusqu'à la caisse."

    "Vous payez vos affaires et quittez le magasin immédiatement."

    player_name "Finalement... À la maison sans cet étranger me suivre ou essaie de me parler..."

    "Ending 2: Tu t'es t'enfui"

    return

label after_yami:

# ... the game continues here.

    player_name "Hmmm..."

    play music "Good_ending.mp3" fadeout 1

    # Initialize variables to track completed choices
    $ option1_done = False
    $ option2_done = False

    # Call the choices menu
    call choices

    # Continue the game after all options are completed # Continue the game after all options are completed
    y "Le soleil commence à se coucher, nous devrions tous les deux rentrer chez nous, mais j'ai été ravi de vous rencontrer !"
    player_name "Oui, moi aussi ! À plus tard, et peut-être à l'université."
    "Vous vous saluez tous les deux et Yami n'est bientôt plus visible."
    "Ending 1: Tu t'es fait un nouvel ami"
    return

label choices:
    menu:
        # Option 1, remains visible even after being selected
        "Qu'est-ce que vous étudiez ?":
            if not option1_done:
                s "J'étudie le Génie Civil."
                player_name "Mais c'est difficile, non ?"
                s "Pas Vraiment, sa me prenais beaucoup de temps pour en finir mes laboratoires, mais avec du temps en apprendre, sa devient plus facile."

                $ option1_done = True
            else:
                s "J'étudie le Génie Civil."
                player_name "Mais c'est difficile, non ?"
                s "Pas Vraiment, sa me prenais beaucoup de temps pour en finir mes laboratoires, mais avec du temps en apprendre, sa devient plus facile."

        # Option 2, remains visible even after being selected
        "Quels sont les professeurs que vous avez ce semestre ?":
            if not option2_done:
                s "Je pense que j'ai M. Alfred pour mon cours d'algèbre..."
                s "J'ai aucune idée, ce n'est pas comme si je m'en souciais de toute façon, j'en veut juste apprendre et passé mes examens."
                $ option2_done = True
            else:
                s "Je pense que j'ai M. Alfred pour mon cours d'algèbre..."
                s "J'ai aucune idée, ce n'est pas comme si je m'en souciais de toute façon, j'en veut juste apprendre et passé mes examens."
               

        # Option 3, only appears when both Option 1 and Option 2 are done
        "Quel est votre nom ?" if option1_done and option2_done:
            y "Mon nom est Yami, et vous ? Quelle est votre nom ?"
            player_name "Ah ! Je m'apelle [player_name] !"
            y "Enchanté de vous rencontre [player_name]."

            return


        # Add any effects or actions here

    # Loop back to the choices menu
    jump choices

        # ... the game continues here.

   
    

    


        
    

    

 

    







    # This ends the game.

    return
