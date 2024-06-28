# Function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provode valid inputs."
    f_name = f_name.title()
    l_name = l_name.title()
    # return f_name+" "+l_name
    return f"{f_name} {l_name}"

# Function Call
name = format_name(f_name=input("Enter Your First Name: "), l_name=input("Enter Your Last Name: "))
print(f"Your Name is: {name} ")
