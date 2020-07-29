
def forward():
    rows = 5
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')

        print("\r")
    reverse()

def reverse():
    rows = 4
    for asdf in range(rows + 1, 0, -1):
        for j in range(0, asdf - 1):
            print("*", end=' ')
        print(" ")

forward()
