def part_1_2():
    for x in range(0, 10):
        print(x, end=" ")

    print(" ")
    for y in range(4, 31, 2):
        print(y, end=' ' )
part_1_2()


def beer():
    while True:
        try:
            number = int(input(f"How many bottles of beer are on the wall?: "))
            break
        except ValueError:
            print("Please enter a whole number")

    if number <= 100:
        for b in range(number, 0, -1):
            print(f"{b} bottles of beer on the wall!")
            print(f"{b} bottles of beer on the wall! 99 bottles of beer! You  take on down, pass it around!")
    else:
        print("That is to many beers on the wall! It can't handle it. Please make it less then 500")
        beer()

print(" ")
beer()

print("0 bottles of beer on the wall")