# This file holds all the variables that will be used throughout the game.
# Thanks to Ren'Py, all of the variables declared here are treated as global variables.
# As such, there is no need to declare the variables in each of the files.
# They are also declared here to avoid variable declaration clutter in the other files

# Default game variables. Controls flags and holds strings
default name = "Ren"
default reunion = 0
default rhodesIsland = 0
default Visit_Bob = False
default Visit_Alice = False
default Visit_Chris = False
default argument = "I am unsure of whether this path will bring us joy, but I will fight for what i think is right for the infected."


# Character name replacer variables
define doc = Character("Doctor")
define protag = Character("[name]")
define chris = Character("Chris")
define bob = Character("Bob")
define unknown = Character ("???")            # For voices being called out
define alice = Character ("Alice")
define vig1 = Character ("Vigilante 1")
define vig2 = Character ("Vigilante 2")
define vig3 = Character ("Vigilante 3")
define re_so = Character ("Reunion Soldier")
define ri_op = Character ("Rhodes Island Operator")
define inf = Character ("Infected")


# Images of people
image alice angry = im.Scale("alice angry.png", 500, 600)
image alice cheer = im.Scale("alice cheer.png", 500, 600)
image alice neutral = im.Scale("alice neutral.png", 500, 600)
image alice soft = im.Scale("alice soft.png", 500, 600)
image doctor = im.Scale("Doctor.png", 700, 700)
image mperson = im.Scale("Hellagur.png", 700, 700)
image rs = im.Scale("rs.png", 900, 700)             # Reunion soldier
image ug = im.Scale("ug.png", 900, 700)             # Ursus Guard
image Vigilante = im.Scale("Vigilante.png", 500, 500)
image rio = im.Scale("rio.png", 900, 700)


# Images of scenary
image clinic = im.Scale("dark_light_clinic.jpg", 1368, 720)
image warehouse = im.Scale("Warehouse.jpg", 1368, 720)
image street = im.Scale("city_street.jpg", 1368, 720)
image alley = im.Scale("dark_alley.jpg", 1368, 720)
image cata = im.Scale("catastrophe.jpg", 1368, 720)



# Ren'Py requires usage of label start to know where the start of the game is
label start:

    "This game is a work of fiction. Any persons, places, or events occuring in this game that matches real life events is purely coincidential."

    "It's all fun and games. Let's keep it that way, shall we?"

    jump intro
