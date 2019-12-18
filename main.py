# Author      : Isaiah Jared
# Description : Generates passwords based on user input then writes the password and the correlating
#               website/app name to a .txt file.

import os
import sys
import random

def main():
    charList = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~','t']
    userOS = str(sys.platform)
    print("ILJ Password Generator\n")
    siteName = input("\nPlease enter the website/app name this password is for: ")
    
    try:
        charCount = int(input("Please enter the character length of the password (no fewer than 6): "))

        if charCount < 6:
        
            if "win32" not in userOS:
                os.system('clear')
            else:
                os.system('cls')
                
            input("Password length must have 6 or more characters! Press any key to go back: ")
            
            if "win32" not in userOS:
                os.system('clear')
            else:
                os.system('cls')
            main()
            
        else:
            i = 0
            passChars = []
            while i < charCount:
                passChars.append(random.choice(charList))
                i += 1

            finalPass = ''.join(passChars)
            infoToTXT = siteName + " : " + finalPass

            if not os.path.exists("generated.txt"):
                with open("generated.txt", "w") as file:
                    file.write("{}".format(infoToTXT))
            else:
                with open("generated.txt", "a") as file:
                    file.write("\n{}".format(infoToTXT))

            if "win32" not in userOS:
                os.system('clear')
            else:
                os.system('cls')
                
            print("Password generation complete!")
            
            
    except:
        if "win32" not in userOS:
            os.system('clear')
        else:
            os.system('cls')
            
        input("Password length value must be an integer! Press any key to go back: ")
        
        if "win32" not in userOS:
            os.system('clear')
        else:
            os.system('cls')
            
        main()

main()
input("\nPress any key to exit: ")
