class SortObject:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __lt__(self, other):
        response = int(input("Which is better?\n1." + str(self) + "\n2." + str(other) + "\n"))
        if response == 1:
            return False
        if response == 2:
            return True
        raise ValueError("Invalid option selected")

if __name__ == "__main__":
    count = int(input("How many objects are you sorting?\n"))
    l = [None for _ in range(count)]

    for i in range(1, count + 1):
        obj = input("Enter item " + str(i) + ": ")
        l[i - 1] = SortObject(obj)
    
    print("We will begin sorting your items.\n\n")
    l.sort(reverse = True)
    print("Your items have now been sorted in the following order, from best to worst:\n")
    for item in l:
        print(item, "\n")
