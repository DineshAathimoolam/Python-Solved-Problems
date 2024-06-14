name=input("Enter your name:")
Score=int(input("Enter your Mark :"))
if Score <35:
    print(f"{name} is Poor Student")
elif (Score > 35) and (Score <75):
    print(f"{name} is Average Student")
elif (Score > 75) and (Score <100):
    print(f"{name} is Good Student")

