# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class ArrayList:

    def __init__(self):
        self.inArray = [0 for i in range(10)]
        self.count = 0

    def get(self, i):
        return self.inArray[i]

    def len(self):
        return self.count

    def set(self, i, e):
        self.inArray[i] = e

    def append(self, e):

        if self.count > len(self.inArray):
            self.count *= 2


