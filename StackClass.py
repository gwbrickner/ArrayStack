# Graeson Brickner
# U4 Lab 1
# STACKS!

class ArrayStack:
    def __init__(self):
        self.__stack = []
        self.__size = 0

    def __is_empty(self):
        """See if stack is empty."""
        if self.__size == 0:
            return True

        else:
            return False

    def push(self, val):
        """Push value to top of stack."""
        self.__stack.append(val)
        self.__size += 1

    def pop(self):
        """Get and remove value from top of stack."""
        if self.__is_empty():
            raise IndexError("cannot pop from list of len 0")

        else:
            returnVal = self.__stack[-1]
            del self.__stack[-1]
            self.__size -= 1
            return returnVal

    def top(self):
        """See value at top of stack."""
        if self.__is_empty():
            raise IndexError("list of len 0")

        else:
            return self.__stack[-1]

    def __len__(self):
        """Return length of stack."""
        return self.__size

    def __str__(self):
        """Display contents of stack"""
        out = ""
        for ele in self.__stack:
            out += str(ele) + ' '

        out += "<TOP"
        return out