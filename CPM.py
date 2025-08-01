def gift_cards():
    ## This part is only run if the user selects gift cards in main()
    ## All the gift card data:
    
    gift_cards_data = {
        'giftcards.com': 4, 'visa gift card': 4, 'mastercard gift card': 4, 'airbnb gift card': 4,
        'doordash gift card': 4, 'uber gift card': 4, 'uber eats gift card': 4, 'starbucks gift card': 4,
        'target gift card': 1.3, 'cvs gift card': 4, 'giant eagle gift card': 4, 'fanatics gift card': 4,
        'melting pot gift card': 4, 'thirdlove gift card': 4, 'tops friendly markets gift card': 4,
        'jtv gift card': 4, 'zappos gift card': 4, "claire's gift card": 4, "famous dave's gift card": 4,
        'on the border gift card': 4, 'circle k gift card': 4, "fazoli's gift card": 4,
        'boxlunch gift card': 4, 'bonefish grill gift card': 4, "mcdonald's gift card": 4,
        'turo gift card': 4, 'golfnow gift card': 4, 'chewy gift card': 4, 'siriusxm gift card': 4,
        'l.l. bean gift card': 4, 'carnival cruises gift card': 0.6, 'best buy gift card': 0.6,
        'alamo drafthouse cinemas gift card': 4, 'quince gift card': 4, "mcalister's deli gift card": 4,
        'emagine theaters gift card': 4, "friendly's gift card": 4, "cheddar's scratch kitchen gift card": 4,
        'dazn gift card': 4, "dave & buster's gift card": 4, "ruth's chris steak house gift card": 4,
        'fogo de chao gift card': 4, "morton's steakhouse gift card": 4, 'pacsun gift card': 4,
        'the container store gift card': 4, 'uno pizzeria & grill gift card': 4, "bj's restaurants gift card": 4,
        "logan's roadhouse gift card": 4, 'bob evans gift card': 4, 'lorna jane gift card': 4,
        'lane bryant gift card': 4, 'guess gift card': 4, 'shutterfly gift card': 4,
        'bubba gump gift card': 4, 'ace hardware gift card': 4, 'quiznos gift card': 4,
        'thredup gift card': 4, 'hopper gift card': 4, 'tommy bahama gift card': 4,
        "carrabba's italian grill gift card": 4, 'sweetfrog gift card': 4, 'qdoba gift card': 4,
        "dick's sporting goods gift card": 1.3, 'american airlines gift card': 1.3,
        "dunkin' gift card": 1.3, 'zara gift card': 1.3, 'apple gift card': 1.3, 'nike gift card': 0.6,
        'chuck e. cheese gift card': 4, 'pandora gift card': 4, "bloomingdale's gift card": 4,
        'belk gift card': 4, 'athleta gift card': 4, 'barnes & noble gift card': 4,
        'virgin experience gifts gift card': 4, 'jcpenney gift card': 4, 'spafinder gift card': 4,
        'build-a-bear gift card': 4, 'california pizza kitchen gift card': 4, 'ruby tuesday gift card': 4,
        'smoothie king gift card': 4, 'old navy gift card': 4, 'aerie gift card': 4,
        'advance auto parts gift card': 4, 'tillys gift card': 4, 'guitar center gift card': 4,
        'vudu gift card': 4, 'topgolf gift card': 4, 'the coffee bean & tea leaf gift card': 4,
        'white house black market gift card': 4, 'wawa gift card': 4, 'dollar shave club gift card': 4,
        'untuckit gift card': 4, 'torrid gift card': 4, 'pep boys gift card': 4,
        'famous footwear gift card': 4, 'jiffy lube gift card': 4, 'cold stone creamery gift card': 4,
        'sling tv gift card': 4, 'buffalo wild wings gift card': 4, "auntie anne's gift card": 4,
        'cinnabon gift card': 4, 'kfc gift card': 4, "bass pro shops / cabela's gift card": 4,
        'gap gift card': 4, 'hotels.com gift card': 4, 'disney gift card': 4, 'american girl gift card': 4,
        "carter's / oshkosh b'gosh gift card": 4, 'eddie bauer gift card': 4, "chico's gift card": 4,
        'poshmark gift card': 4, 'oura ring gift card': 4, 'american eagle gift card': 4,
        'aeropostale gift card': 4, 'hollister gift card': 4, 'abercrombie & fitch gift card': 4,
        'twitch gift card': 4, 'crutchfield gift card': 4, 'lulus gift card': 4, "lands' end gift card": 4,
        'michaels gift card': 4, "kirkland's gift card": 4, 'h&m gift card': 4, 'hulu gift card': 4,
        'meijer gift card': 4, 'crate & barrel gift card': 4, 'firebirds wood fired grill gift card': 4,
        'red robin gift card': 4, 'ihop gift card': 4, 'krispy kreme gift card': 4,
        'outback steakhouse gift card': 4, 'olive garden gift card': 4, 'speedway gift card': 4,
        'shell gift card': 4, 'sonic drive-in gift card': 4, 'texas roadhouse gift card': 4,
        'subway gift card': 4, 'red lobster gift card': 4, 'papa johns gift card': 4,
        'panda express gift card': 4, 'meta quest gift card': 4, "macy's gift card": 4,
        "jersey mike's gift card": 4, 'taco bell gift card': 4, 'five guys gift card': 4,
        "chili's gift card": 4, 'burger king gift card': 4, 'rei gift card': 4, 'marshalls gift card': 4,
        'homegoods gift card': 4, 'lego gift card': 4, 'gamestop gift card': 4,
        'academy sports + outdoors gift card': 4, 'roblox gift card': 4, 'nordstrom gift card': 4,
        'chipotle gift card': 4, 'the home depot gift card': 4, 'wayfair gift card': 4,
        "victoria's secret gift card": 4, 'tire discounters gift card': 4, 'dsw gift card': 4,
        'stop & shop gift card': 4, 'nintendo eshop gift card': 4, 'the cheesecake factory gift card': 4,
        'nordstrom rack gift card': 4, 'petsmart gift card': 4, 'tj maxx gift card': 4,
        'lululemon gift card': 4, 'spotify gift card': 4, 'lyft gift card': 4, "domino's gift card": 4,
        'southwest airlines gift card': 4, 'sony playstation gift card': 4, 'microsoft xbox gift card': 4,
        'autozone gift card': 4, 'saks off 5th gift card': 4, 'adidas gift card': 4,
        'ulta beauty gift card': 4, 'bath & body works gift card': 4, 'amtrak gift card': 4,
        'petco gift card': 4, 'saks fifth avenue gift card': 4, 'total wine & more gift card': 4,
        'instacart gift card': 4, 'google play gift card': 4, 'regal cinemas gift card': 4,
        'bp amoco gift card': 4, 'grubhub gift card': 4, 'panera bread gift card': 4,
        "kohl's gift card": 4, 'cinemark gift card': 4, 'delta air lines gift card': 4,
        'netflix gift card': 4, 'ikea gift card': 4, 'fandango gift card': 4, "lowe's gift card": 4,
        'sephora gift card': 4, "applebee's gift card": 4, 'amc theatres gift card': 4,
        'gift card outlets': 0.9
    }
    print("\n====== Rove Miles Earned for Gift Cards ======") 
    print()
    user_input = input("Please enter the gift card name in the following format: ('store' gift card) ").lower()

    if user_input in gift_cards_data:
        gift_card_value = gift_cards_data[user_input]
        print(f"\nWhen purchasing a {user_input.upper()}, you earn {gift_card_value} Rove miles per $1 spent.")
        try_again = input("Would you like to try another gift card? (y/n)")
        if try_again == "y":
            gift_cards()
        else:
            main()
    else:
        try_again = input("We do not have that gift card in our system. Would you like to try another one? (y/n)")
        if try_again == "y":
            gift_cards()
        else:
            main()

def calculate_cpm(item_type):
    ## This part is only run if the user selects flights or hotels in main()
    
    print(f"\n===== CPM Calculator for {item_type.capitalize()} =====")
    print()
    
    extra_info = {}
    if item_type == "flights":
        extra_info['origin'] = input("What is the origin of the flight (3 letter code): ").upper().strip()
        extra_info['destination'] = input("What is the destination of the flight (3 letter code): ").upper().strip()
        extra_info['airline'] = input("What is the airline you are flying with: ").upper().strip()
    elif item_type == "hotels":
        extra_info['name'] = input("Please enter the name of the hotel: ").upper().strip()

    try:
        miles_redeemed = int(input("Number of miles redeemed: "))
        cash_price = float(input("Price total (in dollars): "))
        taxes = float(input("Taxes (in dollars): "))
    except ValueError:
        print("\nInvalid input. Please enter numbers for miles, price, and taxes.")
        try_again = input("Would you like to try inputting again? (y/n) ")
        if try_again == "y":
            calculate_cpm(item_type)
        else:
            main()
        return

    if miles_redeemed <= 0:
        print("Miles redeemed must be greater than zero.")
        try_again = input("Would you like to try inputting again? (y/n) ")
        if try_again == "y":
            calculate_cpm(item_type)
        else:
            main()
        return

    cpm_value = ((cash_price - taxes) / miles_redeemed) * 100 # CPM in cents per mile

    if item_type == "flights":
        print(f"The CPM for a flight from {extra_info['origin']} to {extra_info['destination']} on {extra_info['airline']} is {cpm_value:.2f} cents per mile.")
    elif item_type == "hotels":
        print(f"The CPM for {extra_info['name']} is {cpm_value:.2f} cents per mile.")
    
    try_again = input("Would you like to try again? (y/n) ")
    if try_again == "y":
        calculate_cpm(item_type)
    else:
        main()

def main():
    ## This is the main function that runs the program 

    start = input("\nstart or stop the program? ")
    if start == "start":
        print()
    else:
        exit()
        
    print("\n=========== Rove Miles Value Calculator =================")
    redemptions = ["Flights", "Hotels", "Gift Cards"]
    print("Pick a redemption type to calculate its value:")
    
    for index, redemption_type in enumerate(redemptions):
        print(f"{index + 1}. {redemption_type}")
    
    try:
        answer = int(input("\nEnter the number corresponding to your choice: --> "))
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your choice.")
        print()
        main()
        return

    match answer:
        case 1:
            calculate_cpm("flights")
        case 2:
            calculate_cpm("hotels")
        case 3:
            gift_cards()
        case _:
            print("\nInvalid choice. Please select a number between 1 and 3.")

    try_again = input("Would you like to try again? (y/n) --> ")
    if try_again == "y":
        main()
    else:
        exit()

if __name__ =="__main__":
    main()