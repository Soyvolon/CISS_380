if __name__ == "integer_array":
    from arrays import Array
else:   
    from .arrays import Array

# Write a subclass IntArray of an Array class defined in arrays.py. It is similar to array
# but it allows only integer elements. Add methods to this class that allow for overloading 
# operators +,-, *, //, %, and **. (that is methods __add__, __sub__, __mul__, __floordiv__, __mod__ and __pow__)

# The first two operators should allow for two IntArray operands and addition/subtraction 
# should be elementwise, for example

# [1, 2,3] + [ 7,4,2] = [8, 6, 3]

# The result should be also an IntArray object.

# The remaining operators should allow for one IntArray parameter (left one) and one integer 
# parameter. The result should be a new IntArray objects with elements which are original 
# operad elements multiplied/divided/exponentiated by the integer operand. For example

# [3, 6, 9] // 2 = [3//2 , 6 // 2, 9 // 2] = [1, 3, 4]  

# When non integer values are used in any operations with IntArray (including object creation, 
# assignment, insertion, deletion and all numeric operands) your class should raise ValueError. 

class IntArray(Array):
    def __init__(self, capacity, fill = 0):
        self._validate_int(fill)
        super().__init__(capacity, fill)

    def insert(self, index, val: int):
        self._validate_int(val)
        super().insert(index, val)

    def _validate_int(self, obj: object):
        if not isinstance(obj, int):
            raise ValueError("Value must be of type int")

    def _validate_int_arr(self, obj: object):
        if not isinstance(obj, IntArray):
            raise ValueError("Value must be of type IntArray")

    def __add__(self, o: object):
        self._validate_int_arr(o)
        
        ls = self.size()
        rs = o.size()
        lrg = ls
        if rs > ls:
            lrg = rs

        dat = IntArray(lrg)

        for i in range(0, lrg):
            a = self.default()
            if i < ls:
                a = self[i]
            b = o.default()
            if i < rs:
                b = o[i]

            dat.insert(i, a + b)

        return dat


    def __sub__(self, o: object):
        self._validate_int_arr(o)
        
        ls = self.size()
        rs = o.size()
        lrg = ls
        if rs > ls:
            lrg = rs

        dat = IntArray(lrg)

        for i in range(0, lrg):
            a = self.default()
            if i < ls:
                a = self[i]
            b = o.default()
            if i < rs:
                b = o[i]

            dat.insert(i, a - b)

        return dat

    def __mul__(self, o: object):
        self._validate_int(o)
        
        lrg = self.size()

        dat = IntArray(lrg)

        for i in range(0, lrg):
            a = self[i]

            dat.insert(i, a * o)

        return dat

    def __truediv__(self, o: object):
        return self.__floordiv__(o)

    def __floordiv__(self, o: object):
        self._validate_int(o)
        
        lrg = self.size()

        dat = IntArray(lrg)

        for i in range(0, lrg):
            a = self[i]

            dat.insert(i, a // o)

        return dat

    def __pow__(self, o: object):
        self._validate_int(o)
        
        lrg = self.size()

        dat = IntArray(lrg)

        for i in range(0, lrg):
            a = self[i]

            dat.insert(i, a ** o)

        return dat