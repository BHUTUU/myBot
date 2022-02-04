#!/bin/bash
read -p "Enter your word: " WORD
RESPONSE=$(curl -fsSL "http://api.urbandictionary.com/v0/define?term=${WORD}" | jq -r .list[].definition)
printf "RESULTS:+\n${RESPONSE}\n"
