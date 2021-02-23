import random


def get_paint_number():
    f = open("SpinTheWheel/PaintNumbers/CompletedNumbers.txt", )
    data = f.read()
    f.close()
    x = random.randint(0, 24)
    format_x = "," + str(x) + ","
    if format_x in data and len(data) >= 64:
        return "All numbers Completed"
    elif format_x in data:
        get_paint_number()
    else:
        u = open("SpinTheWheel/PaintNumbers/CompletedNumbers.txt", "a")
        u.write(str(x) + ",")
        u.close()
        return x
