""" This class and associated helper functions implements a simple representation
of mathematical sets.
"""


class MySet:
    def __init__(self, set):
        """ This is the routine called by the constructor. It should process
    the list "set" and save it as the "set" data field. Make sure to only
    store unique items (i.e. remove replicates)
    """
        self.set = self.uniqueList(set)

    def __or__(self, set2):
        """This overloads the bitwise or operator (|) so that it performs the
    union of the sets in self and set2. It should return a MySet object.
    """
        return self.uniqueList(self.set + set2.set)

    def __and__(self, set2):
        """This overloads the bitwise and operator (&) so that it performs the
    intersection of the sets in self and set2 (that is all the items that
    appear in both self.set and set2.set). It should return a MySet
    object.
    """
        set3 = []
        set3 = self.inBoth(self.set, set2.set)
        return MySet(set3)

    def __str__(self):
        """This enables conversion to str. The string representation of a set
    should look like a list with curly braces around it. It should return
    a str object.
    """
        return "{" + str(self.set) + "}"

    def uniqueList(self, lst):
        """This is a helper function that will be useful for the MySet class. It
    takes an input list, lst, and returns a new list with only the unique items
    from lst. It should not alter the original list, lst.
    """
        lst2 = lst[:]
        for i in lst:
            while lst2.count(i) > 1:
                lst2.remove(i)
        lst2.sort()
        return lst2

    def inBoth(self, lst1, lst2):
        """This is a helper function that will be useful for the MySet class. It
    takes two lists as inputs, and returns a new list with only those items
    present in both lists. Neither lst1, nor lst2 should be altered.
    """
        lst3 = []
        for i in lst1:
            if i in lst2:
                lst3.append(i)
        return lst3


""" Here is some code to test the class. The output should look like this:
{[1, 2, 3, 4, 5]}
{[1, 3, 5, 7, 9]}
{[1, 2, 3, 4, 5]} | {[1, 3, 5, 7, 9]} = {[1, 2, 3, 4, 5, 7, 9]}
{[1, 2, 3, 4, 5]} & {[1, 3, 5, 7, 9]} = {[1, 3, 5]}
"""
a = MySet([1, 2, 3, 4, 5, 1, 2, 3])
print(a)
b = MySet([1, 3, 5, 7, 9])
print(b)
print(a, "|", b, "=", a | b)
print(a, "&", b, "=", a & b)
