class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest
from unittest import TestCase, main


class CatTests(TestCase):

    def test_increase_size_eating(self):
        caty = Cat('Caty')
        caty.eat()
        self.assertEqual(1, caty.size)

    def test_cat_is_fed_after_eating(self):
        caty = Cat('Caty')
        caty.eat()
        self.assertEqual(True, caty.fed)

    def test_cat_can_not_eat_if_already_fed(self):
        caty = Cat('Caty')
        caty.eat()
        with self.assertRaises(Exception) as ex:
            caty.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cannot_fall_asleep_if_not_fed(self):
        caty = Cat('Caty')
        with self.assertRaises(Exception) as ex:
            caty.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        caty = Cat('Caty')
        caty.eat()
        caty.sleep()
        self.assertEqual(False, caty.sleepy)


if __name__ == '__main__':
    main()
