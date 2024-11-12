#Exercise 8-Simple Search

Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_term = input("Enter the Name you want to search for: ")

if search_term in Names:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} wasn't found in the list.")
