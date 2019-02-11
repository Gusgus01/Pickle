import unittest
import os
import pickle
import piickle


class PicklePresence(unittest.TestCase):
    test_string = "pickle"
    filename = "temp.pickled"

    def test_pickle_presence(self):
        with open(self.filename, "wb") as file:
            piickle.dump(self.test_string, file)
        self.check_for_pickle(self.filename)
        os.remove(self.filename)

    def test_monkey_patching(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.test_string, file)
        self.check_for_pickle(self.filename)
        with open(self.filename, "rb") as file:
            check = pickle.load(file)
            self.assertEqual(check, self.test_string)
        os.remove(self.filename)

    def check_for_pickle(self, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            try:
                file.readline().index("🥒")
            except ValueError:
                self.fail("No pickle found.")


if __name__ == '__main__':
    unittest.main()
