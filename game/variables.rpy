# Default game variables
default name = "Protag"
default reunion = 0
default rhodesIsland = 0
default Visit_Bob = False
default Visit_Alice = False
default Visit_Chris = False


# Character name replacer variables
define a = Character("Doctor")
define b = Character("[name]")
define c = Character("Chris")
define d = Character("Bob")
define e = Character("Nurse")           # Not used
define f = Character ("???")            # For voices being called out
define g = Character ("Alice")
define h = Character ("Vigilante 1")
define i = Character ("Vigilante 2")
define j = Character ("Vigilante 3")
define k = Character ("Reunion Soldier")
define l = Character ("Rhodes Island Operator")
define m = Character ("Ursus Guard 1")
define n = Character ("Infected")
define o = Character ("Ursus Guard 2")


# Images people
image alice angry = im.Scale("alice angry.png", 500, 600)
image alice cheer = im.Scale("alice cheer.png", 500, 600)
image alice neutral = im.Scale("alice neutral.png", 500, 600)
image alice soft = im.Scale("alice soft.png", 500, 600)
image doctor = im.Scale("Doctor.png", 700, 700)
image mperson = im.Scale("Hellagur.png", 700, 700)
image rs = im.Scale("rs.png", 900, 700)             # Reunion soldier
image ug = im.Scale("ug.png", 900, 700)             # Ursus Guard
image Vigilante = im.Scale("Vigilante.png", 500, 500)


# Images scenary
image clinic = im.Scale("dark_light_clinic.jpg", 1368, 720)
image warehouse = im.Scale("Warehouse.jpg", 1368, 720)
#image dark alley = im.Scale("dark_alley.jpg", 1368, 720)
image street = im.Scale("city_street.jpg", 1368, 720)
image alley = im.Scale("dark_alley.jpg", 1368, 720)
image cata = im.Scale("catastrophe.jpg", 1368, 720)

label start:

    "This game is a work of fiction. Any persons, places, or events occuring in this game that matches real life events is purely coincidential."

    "It's all fun and games. Let's keep it that way, shall we?"

    jump intro
