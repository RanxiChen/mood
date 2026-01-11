#!/usr/bin/python3
import argparse
from importlib.resources import path
import json
from pathlib import Path
from datetime import datetime
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mood Tracker Application") 
    parser.add_argument("-j","--joy", action="store_true", help="Set mood to joy:快乐")
    parser.add_argument("-cf","--clam_focused", action="store_true", help="Set mood to clam and focused:平静专注")
    parser.add_argument("-id","--irritated_driven", action="store_true", help="Set mood to irritated and driven:烦躁但有动力")
    parser.add_argument("-fb","--frustrated_blocked", action="store_true", help="Set mood to frustrated and blocked:沮丧受阻")
    parser.add_argument("-md","--mentally_drain", action="store_true", help="Set mood to mentally drained:精神疲惫")
    parser.add_argument("-ep","--engaged_positive", action="store_true", help="Set mood to engaged and positive:投入且积极")
    parser.add_argument("-aa","--anxious_alert", action="store_true", help="Set mood to anxious and alert:焦虑且警觉")
    parser.add_argument("-a","--avoidant", action="store_true", help="Set mood to avoidant:回避")
    parser.add_argument("-os","--overstimulated", action="store_true", help="Set mood to overstimulated:过度刺激")
    parser.add_argument("-af","--attension_fragmented", action="store_true", help="Set mood to attention fragmented:注意力分散")
    args = parser.parse_args()

    # First, we parse the command-line arguments to determine the selected mood
    flags = [
        args.joy,
        args.clam_focused,
        args.irritated_driven,
        args.frustrated_blocked,
        args.mentally_drain,
        args.engaged_positive,
        args.anxious_alert,
        args.avoidant,
        args.overstimulated,
        args.attension_fragmented
    ]
    assert sum(flags) <= 1, "Please select only one mood at a time."
    # Here you would add the logic to handle each mood based on the parsed arguments
    path = Path("~/.mood/mood.json").expanduser()
    def platform_init():
        logging.basicConfig(
            filename="mood.log",
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )

    # store to file
    # First check if the file exists
    def read_moods():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            logging.info(f"Creating new mood file at {path}")
            with open(path, "w") as f:
                json.dump({}, f)
        # Load existing moods
        with open(path, "r") as f:
            logging.info(f"Loading moods from {path}")
            moods = json.load(f)
        return moods
    
    

    def add_mood(mood_name,mood_dict):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M")
        mood_dict.setdefault(date_str, {})[time_str] = mood_name
        print(f"Adding mood: {mood_name} at {date_str} {time_str}")
        logging.info(f"Added mood: {mood_name} at {date_str} {time_str}")
        #print(mood_dict)

    def save_moods(mood_dict):
        tmp = path.with_suffix(".tmp")
        with tmp.open("w") as f:
            json.dump(mood_dict, f, indent=2)
        tmp.replace(path)
        logging.info(f"Saved moods to {path}")

    # main logic
    platform_init()
    moods = read_moods()
    current_mood = "x"
    if(args.joy):
        current_mood = "j"
    elif(args.clam_focused):
        current_mood = "cf"
    elif(args.irritated_driven):
        current_mood = "id"
    elif(args.frustrated_blocked):
        current_mood = "fb"
    elif(args.mentally_drain):
        current_mood = "md"
    elif(args.engaged_positive):
        current_mood = "ep"
    elif(args.anxious_alert):
        current_mood = "aa"
    elif(args.avoidant):
        current_mood = "a"
    elif(args.overstimulated):
        current_mood = "os"
    elif(args.attension_fragmented):
        current_mood = "af"
    if current_mood != "x":
        add_mood(current_mood, moods)
        save_moods(moods)
    else:
        print("No mood selected. Use -h for help.")