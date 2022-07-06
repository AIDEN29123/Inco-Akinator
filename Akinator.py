import time

ans = input("Is your charactor male? ")
if ans == "yes":
    ans = input("Is your character in the movie? ")
    if ans == "yes":
        ans = input("Does your character save the world? ")
        if ans == "yes":
            ans = input("Does your character use suit as his weapon? ")
            if ans == "yes":
                print("I think your character is... \n Iron Man (Marvel Hero)")
                time.sleep(10)
            elif ans == "no":
                ans = input("Is your character related to thunder? ")
                if ans == "yes":
                    print("I think your character is... \n Thor (Marvel Hero)")
                    time.sleep(10)
                elif ans == "no":
                    ans = input("Is your hero's skin green when he is angry?")
                    if ans == "yes":
                        print("I think your character is... \n Hulk (Marvel Hero)")
                        time.sleep(10)
                    elif ans == "no":
                        print("I don't know your character. You won! :)")
                        time.sleep(10)
        elif ans == "no":
            print("I don't know your character. You won! :)")
            time.sleep(10)
    elif ans == "no":
        ans = input("Is your character above 18 years old? ")
        if ans == "yes":
            print("I think your character is... \n Thor (Marvel Hero)")
        elif ans == "no":
            print("Is your hero's skin green when he is angry?")




elif ans == "no":
    ans = input("Is your character female? ")
    if ans == "yes":
        ans = input("Is your character in movie? ")
        if ans == "yes":
            print("I don't know your character. You won! :)")
            time.sleep(10)
        elif ans == "no":
            print("I don't know your character. You won! :)")
            time.sleep(10)
    elif ans == "no":
        print("I don't know your character. You won! :)")
        time.sleep(10)

else:
    print("Please write it only yes/no")
    time.sleep(10)