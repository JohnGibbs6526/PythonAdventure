def validify():
    print("Please pick a valid answer.")

def start():
    print("""
You wake up in your bed. Your alarm clock reads "8:00", with the sun shining its
glorious rays on your nightstand. You decide to get out of bed and walk to the
bathroom. You take off your pajamas and take a quick, hot shower. After you have
dried yourself off, you put on some pants and try to pick out a shirt.
""")

    wake_up = input("""
Which shirt do you pick? Type "1" for a white shirt, and "2" for a black shirt.
""")

    if wake_up == "1":
        whiteshirt()
    elif wake_up == "2":
        blackshirt()
    else:
        validify()
        start()
    go_eat()

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
    print("""You head on down to the kitchen to make yourself some breakfast. You make an
"everything" bagel with regular cream cheese. Later, you choose to brush your
teeth, but as you look in the mirror, you are reminded that you are the Python
programming language. Yes, I'm serious. You forgot that you are the famous
"Python" that everyone knows and loves.""")
    
    say_what = input("""
What do you decide to say?
""")
    
    print("""
To be continued...
""")

start()