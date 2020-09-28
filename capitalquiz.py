############################################################
# Captal Cities Of Europe Quiz!                            #
# Run the program and try to answer the questions.         #
# Answers are not case sensitive.                          #
#                                                          #
#                                                          #
# This script is written in python as a learning code.     #
# Use it at on your own risk!                              #
# Author : Adam Jalal                                      #
# Date : 2020-09-28                                        #
############################################################

import random
answer=""
question1="What's the capital city of "
score=0
answeredquestions=0
questions=[

  ["Sweden?","stockholm"],
  ["Norway?","oslo"],
  ["Finland?","helsinki"],
  ["Denmark?","copenhagen"],
  ["Iceland?","reykjavik"],
  ["United Kingdom?","london"],
  ["Ireland?","dublin"],
  ["Estonia?","talinn"],
  ["Latvia?","riga"],
  ["Lithuania?","vilnius"],
  ["Russia?","moscow"],
  ["Germany?","berlin"],
  ["Belgium?","brussels"],
  ["Netherlands?","amsterdam"],
  ["Luxemburg?","luxemburg"],
  ["Poland?","warsawa"],
  ["Belarus?","minsk"],
  ["France?","paris"],
  ["Spain?","madrid"],
  ["Portugal?","lisbon"],
  ["Italy?","rome"],
  ["Switzerland?","bern"],
  ["Austria?","vienna"],
  ["Ukraine?","kiev"],
  ["Czech Republic?","prague"],
  ["Moldova?","chisinau"],
  ["Romania?","bucharest"],
  ["Hungary?","budapest"],
  ["Slovakia?","bratislava"],
  ["Slovenia?","ljubljana"],
  ["Croatia?","zagreb"],
  ["Bosnia & Herzegovina?","sarajevo"],
  ["Montenegro?","podgorica"],
  ["Albania?","tirana"],
  ["Serbia?","belgrade"],
  ["Kosovo?","pristina"],
  ["Macedonia?","skopje"],
  ["Greece?","athens"],
  ["Bulgaria?","sofia"],
  ["Monaco?","monaco"],
  ["Turkey?","ankara"],
  ["Liechtenstein?","vaduz"],
  ["Malta?","valletta"],
  ["San Marino?","san marino"],
  ["Vatican City?","vatican city"],
]
usedID=[]
usedID=[0 for i in range(45)]


def getID():
 result=False
 counter= 0
 while True:
   rng = int(random.randrange(0, 45, 1))
   i=0
   if(usedID[rng]==0):
      usedID[rng]=1
      return rng
   counter=counter+1
   if (counter >10000):
       return -1

import os
os.system("red")
print ('Capital Cities Of Europe Quiz!')


print("To exit write: exit")
print("Please answer these questions.")

counter=0
while True:
   g = getID()
   if (g==-1):
      print("Game Over...")
      print("You played ",answeredquestions)
      print("Your score was ",score)
      quit();
   usedID[g]=1
   print(question1)
   answer=input(questions[g][0]+"  ")
   answer=answer.lower()
   if answer=="exit":
      print("Game Over...")
      print("You played ",answeredquestions)
      print("Your score was ",score)
      quit()
   temp=questions[g][1]
   if(answer==temp):
      score=score+1
   answeredquestions=answeredquestions+1

