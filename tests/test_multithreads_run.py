import time
from pytest import mark


@mark.multi
class MulitTests:
    def test_result1(self):
        time.sleep(5)
        print('Test number 1 completed')

    def test_result2(self):
        time.sleep(5)
        print('Test number 2 completed')

    def test_result3(self):
        time.sleep(5)
        print('Test number 3 completed')

    def test_result4(self):
        time.sleep(5)
        print('Test number 4 completed')

    def test_result5(self):
        time.sleep(5)
        print('Test number 5 completed')

    def test_result6(self):
        time.sleep(5)
        print('Test number 6 completed')

    def test_result7(self):
        time.sleep(5)
        print('Test number 7 completed')

    def test_result8(self):
        time.sleep(5)
        print('Test number 8 completed')


