def presents_of_number_of_elements_located(locator, number):
    def inner_func(driver):
        elements = driver.find_elements(*locator)
        if len(elements) == number:
            return elements

    return inner_func


class presents_of_number_of_elements_located2:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.number:
            return elements


if __name__ == '__main__':
    class A:
        def __init__(self, prop):
            self.prop = prop

        # def __add__(self, other):
        #     pass
        # print(self.prop + other.prop)

        def __call__(self, word):
            print(f"Hello, {word}!")

    a = A("Bob")
    b = A("Bob2")

    a("sdfasd")
    # a()
    # a()


if __name__ == '__main__':
    def power_to(pow):
        def power_number(number):
            return number ** pow

        return power_number


    square = power_to(2)
    cube = power_to(3)

    # print(square(5))
    # print(square(2))
    #
    # print(cube(5))
    # print(cube(2))
