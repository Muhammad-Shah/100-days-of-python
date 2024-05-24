# Function with multiple Inputs
def function_with_many_inputs(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}\n")
    print("*-----------------------------*")

function_with_many_inputs("Bellie", "Nowhere")
function_with_many_inputs("Nowhere", "Bellie") # Reversed


function_with_many_inputs(name="Bellie", location="Nowhere")
function_with_many_inputs(location="Nowhere", name="Bellie") # Same