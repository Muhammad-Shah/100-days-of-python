# Function with Outputs

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    # return f_name+" "+l_name
    return f"{f_name} {l_name}"

first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")

name = format_name(f_name=first_name, l_name=last_name)
print(f"Your Name is: {name} ")
