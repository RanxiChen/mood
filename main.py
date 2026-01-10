#!/usr/bin/python3
import argparse


def classify_mood():
    parser = argparse.ArgumentParser(description="Mood Tracker Application") 
    parser.add_argument("-j","--joy", action="store_true", help="Set mood to joy") #快乐
    parser.add_argument("-cf","--clam_focused", action="store_true", help="Set mood to clam and focused") #平静专注
    parser.add_argument("-id","--irritated_driven", action="store_true", help="Set mood to irritated and driven") #烦躁但有动力
    parser.add_argument("-fb","--frustrated_blocked", action="store_true", help="Set mood to frustrated and blocked") #沮丧受阻
    parser.add_argument("-md","--mentally_drain", action="store_true", help="Set mood to mentally drained") #精神疲惫
    parser.add_argument("-ep","--engaged_positive", action="store_true", help="Set mood to engaged and positive") #投入且积极
    parser.add_argument("-aa","--anxious_alert", action="store_true", help="Set mood to anxious and alert") #焦虑且警觉
    parser.add_argument("-a","--avoidant", action="store_true", help="Set mood to avoidant") #回避
    parser.add_argument("-os","--overstimulated", action="store_true", help="Set mood to overstimulated") #过度刺激
    parser.add_argument("-af","--attension_fragmented", action="store_true", help="Set mood to attention fragmented") #注意力分散
    args = parser.parse_args()

if __name__ == "__main__":
    classify_mood()