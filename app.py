from flask import Flask, render_template

app = Flask(__name__)

# Define riddles and corresponding locations
locations = {
    "location1": {
        "name": "Chill Room",
        "riddle": "Puzzle word: https://urn.fi/ \n\n Next Riddle:\nWhere style is crafted and scissors snip,\nFind the next clue on this stylish trip.\nA place where locks are tamed with care,\nYour journey continues if you find it there."
    },
    "location2": {
        "name": "Saloon",
        "riddle": "Puzzle word: URN:NBN: \n\nNext Riddle:\nWhere the curtains rise and the magic unfolds,\nFind the next clue where the backstage holds.\nLook for a place where the stars prepare,\nAnd the secrets of the stage are hidden there."
    },
    "location3": {
        "name": "tellus backstage",
        "riddle": "Puzzle word: fi:oulu- \n\nNext Riddle:\nWhere ideas take shape and creations are born,\nFind the next clue where the tools are sworn.\nLook for a place where the sparks may fly,\nAnd the future is built before your eye."
    },
    "location4": {
        "name": "FabLab",
        "riddle": "Puzzle word: 2024121 \n\nNext Riddle:\nWhere books abound and minds pursue,\nFind the final clue where scholars accrue.\nAmong the shelves, where stories unfold,\nLies the key to the treasure you hold.\n\nThe topic awaits in the words you’ve found,\nA puzzle of parts, where meaning is bound.\nCombine the pieces, the letters, the theme,\nTo unveil the title of the doctoral dream."
    },
    "location5": {
        "name": "Pegasus Library",
        "riddle": "Final puzzle word: 07169 \n\nYou Found the Treasure Congratulations! Now click the submit button and fill your answers"
    },
    # second set
    "location6": {
        "name": "Foodoo",
        "riddle": "Puzzle word: https://urn.fi/ \n\nNext Riddle:\nWhere aromas blend and flavors entice,\nA spot to dine, both quick and nice.\nNext to the place where subway train reign, \nFind your next clue in the food domain."
    },

    "location7": {
        "name": "Kastari",
        "riddle": "Puzzle word: URN:NBN: \n\nNext Riddle:\nWhere warm delights and flavors embrace, \nFind the next clue in a welcoming space. \nNear the lonely giant Hall, in the entryway, \nA place to gather, relax, and stay."
    },

    "location8": {
        "name": "Foobar",
        "riddle": "Puzzle word: fi:oulu-202 \n\nNext Riddle:\nWhere modern flavors meet a lively scene, \nA place to sip and dine between. \nNear the stage, by the entrance wide, \nYour next clue waits just inside."
    },
    "location9": {
        "name": "Pegasus Library",
        "riddle": "Puzzle word: 40506 \n\nNext Riddle:\nWhere books abound and minds pursue,\nFind the final clue where scholars accrue.\nAmong the shelves, where stories unfold,\nLies the key to the treasure you hold.\n\nThe topic awaits in the words you’ve found,\nA puzzle of parts, where meaning is bound.\nCombine the pieces, the letters, the theme,\nTo unveil the title of the doctoral dream."
    },
    "location10": {
        "name": "Pegasus Library",
        "riddle": "Final Puzzle word: 3145 \n\nYou Found the Treasure Congratulations! Now click the submit button and fill your answers"
    },


}

@app.route("/")
def home():
    return render_template("index.html", locations=locations)

if __name__ == "__main__":
    app.run(debug=True)
