# In Python, there is no way to really hide a variable and prevent other users
# from accessing it. However, if you really want to send a strong signal to
# other programmers that a certain variable should not be modified, you can
# add double underscores to the front of the variable name.

class A:
    def __init__(self):
        self.__x = 5
        self._y = 6
