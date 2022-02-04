#!/usr/bin/env python3
#By: Suman Kumar ~BHUTUU
import requests, argparse
parser = argparse.ArgumentParser()
parser.add_argument("tank", type=str)
args = parser.parse_args()
word = args.tank
response = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
print(response.text)
