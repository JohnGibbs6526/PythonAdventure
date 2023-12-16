def validify():
    print("\nPlease pick a valid answer.\n")

def start():
    print("""
You wake up in your bed. Your alarm clock reads "8:00", with the sun shining its
glorious rays on your nightstand. You decide to get out of bed and walk to the
bathroom. You take off your pajamas and take a quick, hot shower. After you have
dried yourself off, you put on some pants and try to pick out a shirt.
""")

    pick_shirt()

def pick_shirt():
    wake_up = input("""
Which shirt do you pick? Type "1" for a white shirt, and "2" for a black shirt.
""")

    if wake_up == "1":
        whiteshirt()
        go_eat()
    elif wake_up == "2":
        blackshirt()
        go_eat()
    else:
        validify()
        pick_shirt()

def whiteshirt():
    print("""
You pick out the white shirt. You feel that it suits your needs in case it ever
gets too hot outside.
""")

def blackshirt():
    print("""
You pick out the black shirt. You have a feeling it might get a little chilly
later on, but who knows? If it does, your black shirt is more likely to absorb
heat.
""")

def go_eat():
    print("""
You head on down to the kitchen to make yourself some breakfast. You make an
"everything" bagel with regular cream cheese. Later, you choose to brush your
teeth, but as you look in the mirror, you are reminded that you are the Python
programming language. Yes, I'm serious. You forgot that you are the famous
"Python" that everyone knows and loves.
""")
    
    say_what = input("""
What do you decide to say?
""")

    print("""
"{}!" you shout as you fail to understand why you are feeling so bad right now.
Maybe it's because you have been doing nothing for the past 5 days as you were
too busy NOT KNOWING THAT YOU ARE PYTHON?! Anyway, you decide to go outside and
start to hear meowing. You look over and notice a cat high up in a tree, unable
to get down. Since you are a programming language, you might as well use your
coding skills to save the cat.""".format(say_what))

    get_that_cat()

def get_that_cat():
    save_the_cat = input("""
What will you do to save the cat?

1. Assign a variable with the string "ladder".
2. Create an object for "ladder".
""")

    if save_the_cat == "1":
        string_ladder()
        cat_thanks_you()
    elif save_the_cat == "2":
        cat_thanks_you()
    else:
        validify()
        get_that_cat()

def string_ladder():
    print("""
You type "
    ladder = 'ladder'" and run the code. Sure enough, a ladder appears,
but it is old and worn out. You decide you use it anyway, so you prop it against
the tree and climb the rungs. You reach for the cat and grab her in your arms.
As you are about to climb down, the ladder breaks and sends you tumbling down.
You land on your Python tail with a sharp pain on your side, but the cat comes
out OK. You realize that maybe you should have used an object so you could have
defined the properties of 'not crappy'. It seems your code just picked a random
ladder. You think about this next time you want to help someone.
""")

def object_ladder():
    print("""
You type "
    class Utility:
        def__init__(self, name, material):
            self.name = name
            self.material = material
    
    ladder = Utility("ladder", "metal")
"
A metal ladder appears in front of you. You stand it next to the tree and get to
climbing. You safely get the cat in your arms and climb down with no difficulty.
    """)

def cat_thanks_you():
    print("""
The cat purrs as it rubs up against you. Her adorableness makes you not mind her
following you on your way to who knows where. You walk off with the cat on your
side.
""")

    print("""
To be continued...
""")

start()