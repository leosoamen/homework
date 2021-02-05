number_people = int(input("How many people? "))
number_pizza = int(input("How many pizzas do you have? "))
number_slices = int(input("How many slices do you have? "))

total_slices = number_slices * number_pizza
slices_per_person = total_slices / number_people
print("Each person will have " + str(slices_per_person) +" slices.")

