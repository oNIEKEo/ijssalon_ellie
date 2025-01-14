def presenteer():
    mijn_dict = {
        'vis': 10, 
        'vlees': 25, 
        'overig': 15
    }
    totaal = sum(mijn_dict.values())

    for item, waarde in mijn_dict.items():
        print(f"{item} : {waarde} euro")
    print("=" * 15)
    print(f"totaal : {totaal} euro")
presenteer()
