class Rectangle:
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height

    def square(self):
        print(self.wight*self.height)

    def perimetr(self):
        print(2*(self.wight + self.height))


obj1 = Rectangle(14, 2)
obj2 = Rectangle(5, 7)
obj3 = Rectangle(1, 11)

obj1.square()
obj1.perimetr()
obj2.square()
obj2.perimetr()
obj3.square()
obj3.perimetr()

print('  ')


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):

        print(self.a * self.b)

    def division(self):

        print(self.a / self.b)

    def subtraction(self):

        print(self.a - self.b)


param = Math(15, 3)

param.addition()
param.multiplication()
param.division()
param.subtraction()

print(' ')


class Button:

    def __init__(self, text, type='кнопка', loc=' '):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print('Клик по кнопке {}'.format(self.text))


menuTB = Button('Text Box')
menuCB = Button('Check Box')
menuRB = Button('Radio Button')
menuWT = Button('Web Tables')
menuB = Button('Buttons')
menuL = Button('Links')
menuBL_I = Button('Broker Links - Image')
menuUaD = Button('Upload and Download')
menuDP = Button('Dynamic Properties')


menuTB.click()
menuCB.click()
menuRB.click()
menuWT.click()
menuB.click()
menuL.click()
menuBL_I.click()
menuUaD.click()
menuDP.click()

