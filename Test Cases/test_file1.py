

class Test_Py:
    def test_addition(self):
        a = 3
        b = 4
        c = a + b
        if c == 7:
            print("Test case is passed")
            assert True
        else:
            print("Test case is wrong")
            assert False


    def test_mul(self):
        a = 3
        b = 4
        c = a * b
        if c == 12:
            print("Test case is passed")
            assert True
        else:
            print("Test case is wrong")
            assert False
