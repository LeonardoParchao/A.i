import time

def name():
    print("what's your name?")
    name = input(">>>")
    print("what can i do for you",name,"?")
    choice = input(">>>")
    def ifs():
        if choice == "wait a sec":
             time.sleep(1)
        if choice == "good bye":
            print("bye")
            time.sleep(5)
            exit
        if choice == "tell me a joke":
            print("what type of joke?")
            choice = input(">>>")
            if choice == "knock knock joke":
                print("knock knock")
                choice = input(">>>")
                if choice == "who's there":
                    print(name)
                    choice = input(">>>")
                    if choice == "who's there?":
                        print(name,"that's who i am :>")
                    else:
                        print(error)
                else:
                    print(error)
            else:
                print(error)
        else:
            print(error)

          if choice = "Tell me a joke": 
            print("What type of joke?")
            choice = input(">>>")
            if choice == "Knock knock joke":
                print("Knock knock")
                choice = input(">>>")
                if choice == "Who's there":
                    print(name)
                    choice = input(">>>")
                    if choice == name,"who?":
                        print(name,"that's who i am :>")
                    else:
                        print(error)
                else:
                    print(error)
            else:
                print(error)
        else:
            print(error)
        if name == "Leonardo Parcaho":
            print("enter password")
            password = input(">>>")
            if password == "Stevenu":
                  print("hello creator")
                  choice = input(">>>")
                  if choice == "Debug menu":
                        print("debug commands")
                        print("dumb mode:makes me dumb")
                        print("anti-virus mode:makes me an antivrus")
                        choice = input(">>>")
                        if choice == "dumb mode":
                            name = input("Enter name:")
                            print ("hello",name)
                        if choice == "anti-virus":
                             open "antivirus.bat"
        if =! "Stevenu":
            print("wrong please try again")
            password = input(">>>")
             if password == "Flute":
                  print("hello creator")
                  choice = input(">>>")
                  if choice == "Debug menu":
                        print("debug commands")
                        print("dumb mode:makes me dumb")
                        choice = input(">>>")
                        if choice == "dumb mode":
                            name = input("Enter name:")
                            print ("hello",name)
    ifs()
    
#____________________________________________________________________________________________________________

name()
