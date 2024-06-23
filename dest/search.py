
def search_name(my_destinations):
    print("!!!! search_name entered")
    search_str = input("Please enter name to search: ")
    found = False
    for desti in my_destinations:
        if (
            (search_str.lower() == desti["name"].lower())
        ):
            print(f"name: {desti["name"]}, score: {desti["score"]}, descripton: {desti['description']}")
            found = True
    if not found:
        print("not found!")

def search_by_score(my_destinations):
    print("!!!! search by score entered")
    scr = float(input("enter a score you want destinations with score bigger: "))
    found = False
    for desti in my_destinations:
        if scr <= desti["score"]:
            print(f"name: {desti["name"]}, score: {desti["score"]}, descripton: {desti['description']}")
            found = True
    if not found:
        print("not found!") 