# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yami", color= "#7b6ac5ff")
define s = Character("Étranger", color= "#951d1d")
define d = Character("???", color= "#ffffff")
define k = Character("Prof. Kure", color= "#ffffff")
define t = Character("Tenshi", color= "#d69bea")
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
            jump choice1_yes

        "Continuer à marcher":
            jump choice1_no

label choice1_yes:

    $ menu_flag = True

    player_name "A bien y réfléchir... Rester à la maison me semble mieux, et plus réconfortant. Je vais commander un plat chinois à emporter. "

    "Bonus Ending: Takeout"

    # This ends the game

    jump choice1_done

label choice1_no:

    $ menu_flag = False

    player_name "Une petite visite ne fait pas de mal, en plus c'est très calme dans ce quartier."

    jump choice1_done

label choice1_done:

    # ... the game continues here.

    "Vous vous dirigez vers l'îlot où se trouve le congélateur."

    player_name "Mmm... Rien de plaisant..."

    "Vous vous dirigez vers un autre région dans le magasin, regardant les nouilles instantanées sur l'étagère afin d'en prendre une pour le dîner de ce soir."

    "Vous vous rendez à l'arrière du magasin pour trouver l'endroit où les boissons sont conservées. Vous jetez un coup d'œil pour voir le milkshake à la fraise en édition limitée, et il est coincé entre quelques autres boissons à l'arrière."

    player_name "Pas question que j'obtienne cela d'aussi loin !"

    "Vous êtes donc reparti déçu de ne pas avoir pu acheter la boisson que vous vouliez, et vous êtes allé acheter quelques collation pour le lendemain."

    "En les ramassant et en les tenant dans vos mains, vous avez vu un homme de grande taille ouvrir la porte des boissons et attraper facilement la dernière bouteille de lait à la fraise."

    "Vous soupirez de défaite. Encore une fois, le milkshake à la fraise est hors service !"

    "Le grand homme vêtu de noir s'approche de vous, vous vous préparez à la rencontre."

    s "C'est ce que vous vouliez... ? Je t'ai vu tout à l'heure le regarder, mais tu ne l'as pas pris. J'ai donc décidé de vous aider un peu."

    menu:
        "Le remercier":
            jump choice2_yes

        "Se méfier":
            jump choice2_no

label choice2_yes
    $ menu_flag = True

    player_name "Merci beaucoup!"

    s "Pas de problème, est-ce que vous voulez d'aide avec d'autre choses?"

    "Il a regardé vos mains pleines de collation et votre dîner."

    s "Tu sais quoi, je vais payer pour tes affaires. Je pense que je vous connais de quelque part."

    player_name "Vraiment? Quelle université fréquentez-vous ?"

    s "Université de Moonshell."

    player_name "Tu blague pas? Moi aussi!"

    jump choice2_done
    
# ... the game continues here.

"bing bong"


label choice2_no
    $ menu_flag = False

    player_name "Uhm... Merci..."

    "Vous prenez avec précaution la boisson que vous vouliez dans sa main, en le regardant à plusieurs reprises, lui et sa main."

    "L'homme regarde votre pile remplie d'en-cas et votre dîner."

    s "Avez-vous besoin d'aide pour ces... ?"

    player_name "Non ! Pas du tout ! Je n'ai pas besoin d'un étranger pour m'aider !"

    "Vous essayez de marcher rapidement jusqu'à la caisse."

    "Vous payez vos affaires et quittez le magasin immédiatement."

    player_name "Finalement... À la maison sans cet étranger me suivre ou essaie de me parler..."

    "Ending 2: Tu t'es enfui"

# This ends the game

label choice2_done


    

    

 

    







    # This ends the game.

    return
