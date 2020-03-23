class calc:


    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
     try:
        return num1 / num2
     except ZeroDivisionError:
        print("Divide by Zero is not possible")

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def sq(a):
        return a ** 2

    @staticmethod
    def rt( a):
        return a ** 0.5

if __name__ == "__main__":
        c = calc()
        print("1.Add 2. Subtract 3. Multiply 4. Divide 5. Square 6. Square Root")
        i = int(input())
        if i == 1:
            print(c.add(10, 20))
        elif i == 2:
            print(c.sub(10, 20))
        elif i == 3:
            print(c.mul(10, 20))
        elif i == 4:
            print(c.div(10, 20))
        elif i == 5:
            print(c.sq(10))
        elif i == 6:
            print(c.rt(100))
        else:
            print("error")
