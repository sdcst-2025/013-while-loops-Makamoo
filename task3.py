#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
cranberry = float(1)
turduckin = float(17)

while cranberry != turduckin:
    gravy = float(input("float number "))
    cranberry = gravy/2
    turkey = int(cranberry)
    turduckin = float(turkey)
    if cranberry != turduckin:
        print("That is not an even integer")

print("That is an even integer")