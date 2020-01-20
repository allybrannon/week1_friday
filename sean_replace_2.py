# working on removing names from a list and replacing with another name

staff_list = ["Sean", "David", "Mary Ella", "Liz", "Natalie", "Tasha", "Jake", "Max"]

print(staff_list)

staff_list[staff_list.index("Sean")] = "Ranger"

print(staff_list)


if "David" in staff_list:
    indexofDavid = staff_list.index("David")
    staff_list.insert(indexofDavid, "Not David")
    staff_list.remove("David")

print(staff_list)
