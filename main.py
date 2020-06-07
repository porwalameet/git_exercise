import sys
x = int(raw_input("enter numeric value for y :")
y = int(raw_input("enter numeric value for y :")

choice = int(raw_input("Enter the operataion: \
        1. Press 1 for addition \
        2. Press 2 for Subtraction \
        3. Press 3 for Multiplication \
        4. Press 4 for Division")
if choice == 1:
    add(x,y)
elif choice == 2 :
    subtract(x,y)
elif choice == 3 :
    multiply(x,y)
else:
    division(x,y)
