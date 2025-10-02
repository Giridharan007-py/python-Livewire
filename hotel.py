

# THE HOTEL REQUIRED FOR THE TOURIST ACCORDING TO THIER BUDGEET
# USING (if,elif,else)

hotel=input("Which hotel do you want?")
budget=int(input("Enter your budget?"))
if(hotel=="3 star" or budget=="1000"):
    print("rupees:1000 per day")
    print("AIR CONDITIONING")
    print("WI-FI")
    print("Basic tea/coffee-making facilities")
elif(hotel=="4 star" or budget=="5000"):
    print("rupees:5000 per day")
    print("High standard of cleanliness and hygiene")
    print("24/7 reception and concierge services")
    print("On-site parking")
elif(hotel=="5 star" or budget=="10000"):
    print("rupees:10000 per day")
    print("Luxurious, elegant, and meticulously designed interiors")
    print("Impeccable service with a high staff-to-guest ratio")
    print("Multilingual, professionally trained staff")
else:
    pass

