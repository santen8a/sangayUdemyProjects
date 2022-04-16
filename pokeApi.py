import requests
isRunning = True

print("Welcome to POKE PORTAL")

while isRunning:
    userInput = input("Enter Pokemon Name:")
    url = "https://pokeapi.co/api/v2/pokemon/"+userInput.lower()
    req = requests.get(url)

    if req.status_code == 200:
        #PokeInfo
        pokeData = req.json()
        # print(pokeData)
        print(f"Name \t {pokeData['name']}")
        print(f"Weight \t {pokeData['weight']}")

        print("Abilities")
        for ability in pokeData['abilities']:
            print("\t",ability['ability']['name'])
    elif req.status_code == 404:
        print("Error, Pokemon not found")
    else:
        print("Error: Please contact admin")
   
    continueQuestion = input("Do you wish to search for more info? (y/n)")
    if(continueQuestion == 'n'):
        isRunning = False
    elif(continueQuestion == 'y'):
        isRunning = True
    else:
        print("Input not understood, moving to main menu")

print("Bye Bye, see you again!!!")