{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sys import exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are in a haunted house.\n",
      "There is a door to your right and left.\n",
      "Which one do you take?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      ">  right one\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here you see evil monsters.\n",
      "Hey, if you look into their eyes, you will go insane.\n",
      "Do you flee for your life or eat your head?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      ">  eat\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here you see evil monsters.\n",
      "Hey, if you look into their eyes, you will go insane.\n",
      "Do you flee for your life or eat your head?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      ">  head\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Well that was tasty!! Bad choice!!! \n",
      "YOU LOOSE!!!\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "0",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 0\n"
     ]
    }
   ],
   "source": [
    "def treasure_chambre():\n",
    "    print(\"Wow, this room is filled with great treasures!!\")\n",
    "    print(\"How much treasures would you like to take with you?\")\n",
    "    \n",
    "    take = int(input(\"> \"))\n",
    "    \n",
    "    if take < 50:\n",
    "        print(\"Well done, you are not greedy, you may keep these treasures!\")\n",
    "        print(\"YOU WIN!!!\")\n",
    "        exit(0)\n",
    "    else:\n",
    "        dead(\"you greedy bastard!!!\")\n",
    "        \n",
    "def zombie_room():\n",
    "    print(\"There is a zombie here.\")\n",
    "    print(\"the zombie is chewing on a bone\")\n",
    "    print(\"The zombie blocks another door...\")\n",
    "    print(\"How are you going to move this zombie?\")\n",
    "    print(\"you can choose between: 'take bone' or 'taunt zombie'.\\n\", \"What will be your choice?\")\n",
    "    zombie_moved = False\n",
    "    \n",
    "    while True:\n",
    "        choice = input(\"> \")\n",
    "        \n",
    "        if choice == \"take bone\":\n",
    "            dead(\"The zombie will eat you now\")\n",
    "        elif choice == 'taunt zombie' and not zombie_moved:\n",
    "            print(\"The zombie has moved from the door.\")\n",
    "            print(\"You can go through now\")\n",
    "            print(\"Now open the door with the command 'open door'. \")\n",
    "            zombie_moved = True\n",
    "        elif choice == \"Taunt zombie\" and zombie_moved:\n",
    "            dead(\"the zombie gets pissed off and eats you anyway\")\n",
    "        elif choice == \"open door\" and zombie_moved:\n",
    "            treasure_chambre()\n",
    "        else:\n",
    "            print(\"I have no idea what that means.\")\n",
    "\n",
    "def monster_room():\n",
    "    print(\"Here you see evil monsters.\")\n",
    "    print(\"Hey, if you look into their eyes, you will go insane.\")\n",
    "    print(\"Do you flee for your life or eat your head?\")\n",
    "    \n",
    "    choice = input(\"> \")\n",
    "    \n",
    "    if \"flee\" in choice:\n",
    "        start()\n",
    "    elif 'head' in choice or \"eat\" in choice:\n",
    "        dead(\"Well that was tasty!!\")\n",
    "    else:\n",
    "        monster_room()\n",
    "        \n",
    "def dead(why):\n",
    "    print(why, \"Bad choice!!! \\nYOU LOOSE!!!\")\n",
    "    exit(0)\n",
    "    \n",
    "def start():\n",
    "    print(\"You are in a haunted house.\")\n",
    "    print(\"There is a door to your right and left.\")\n",
    "    print(\"Which one do you take?\")\n",
    "    \n",
    "    choice = input(\"> \")\n",
    "    \n",
    "    if \"left\" in choice:\n",
    "        zombie_room()\n",
    "    elif \"right\" in choice:\n",
    "        monster_room()\n",
    "    else:\n",
    "        dead(\"You stumble arount the room until you starve.\")\n",
    "\n",
    "start()\n"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
