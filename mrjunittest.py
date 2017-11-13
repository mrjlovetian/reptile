import unittest

class TestAddition(unittest.TestCase):
    # def setUp(self):
    #     print("setting up the test")
    #
    # def tearDown(self):
    #     print("tear down the test")

    # 此函数可以用来代替setUp和tearDown的方法
    def setUpClass():
        print("start and end !")

    def test_twoPlus(self):
        total = 2+2
        self.assertEqual(4, total)
        print('test function')

if __name__ == '__main__':
    test = TestAddition()
    # unittest.main()
