import os
Text = []
try:
    with open("text.txt","r") as f:
        Text = [line.rstrip() for line in f]
except FileNotFoundError:
    pass

Undone = []

def write(text):
    global Text
    global Undone
    Text.append(text)
    Undone.clear()

def unDo():
    global Text
    global Undone
    try:
        Undone.append(Text.pop())
        return True
    except IndexError:
        return False

def reDo():
    global Text
    global Undone
    try:
        Text.append(Undone.pop())
        return True
    except IndexError:
        return False

def getInput():
    textInput = input(": ")
    if textInput.lower() == 'z':
        return unDo()
    elif textInput.lower() == 'y':
        return reDo()
    else:
        write(textInput)
        return True
   
def showText():
    os.system('cls' if os.name == 'nt' else 'clear')
    global Text
    for txt in Text:
        print(txt)
def saveFile():
    if not Text:
        return
    with open("text.txt", "w") as f:
        for txt in Text:
            f.write(txt + "\n")
while True:
    showText()
    try:
        success = getInput()
        if not success:
            print("Not a valid action")
    except (KeyboardInterrupt, EOFError):
        saveFile()
        break