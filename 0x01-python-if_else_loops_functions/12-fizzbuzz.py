def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        else:
            if i == 100:
                print(i)
            else:
                print(f"{i} ", end="")
