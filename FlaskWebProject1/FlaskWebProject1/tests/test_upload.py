import unittest
import requests
import random

class Test_test1(unittest.TestCase):
    def test_A(self):
        rand = random.uniform(10, 20)
        with open(str(rand), 'rb') as f:
            f.writelines([str(rand) + "\n"])
        files = {'file': open(str(rand), 'rb')}
        requests.post(url, files=files)


if __name__ == '__main__':
    unittest.main()
