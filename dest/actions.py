
def add_destination(my_destinations):
    print("****** in add_destination")
    new_dest_name = input("Please enter new destination name: ")
    new_dest_score = int(input("Please enter new score: "))
    new_dest_description = input("Please enter new description: ")
    new_desti = {"name":new_dest_name,"score": new_dest_score,"description": new_dest_description}
    my_destinations.append(new_desti)
    print("****** added succesfuly")

def print_destinations(my_destinations):
    for desti in my_destinations:
        print(f"name: {desti["name"]}, score: {desti["score"]}, descripton: {desti['description']}")