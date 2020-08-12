import random

def main():
    
    charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!',
                '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
                ']', '^', '_', '`', '{', '|', '}', '~', 't']

    running = True
    while running == True:
        try:
            charCount = int(input("Please enter the character length of the password (no fewer than 6): "))

            if charCount < 6:
                input("Password length value must be an integer! Press Enter to go back: ")
            else:
                i = 0
                passChars = []
                while i < charCount:
                    passChars.append(random.choice(charList))
                    i += 1

                password = ''.join(passChars)

                print(f'Your generated password: {password}')
                break

        except:
            input("Password length value must be an integer! Press any key to go back: ")

main()
input("\nPress any key to exit: ")
