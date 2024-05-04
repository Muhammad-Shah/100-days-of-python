# Lists i pthon

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticuts", "Massachusetts", "Meryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island"]
a=len(states_of_america)
print(a)
print(states_of_america[0])
print(states_of_america[-1])

# If we want to change an item int the list
states_of_america[1] = "Pensilvania"
print(states_of_america[1])

# If we want to add another item to the list
states_of_america.append("muhammadland")
print(states_of_america[-1])

# If we want to extend a list then we should add another list to it
states_of_america.extend(["My Land", "His Land", "Their Land"])
print(states_of_america)

