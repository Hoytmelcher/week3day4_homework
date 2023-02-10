from cart_main import Cart, Item, Shop

import unittest

class CartTest(unittest.TestCase):
    def test_add(self):
        test_cart = Cart()
        test_cart.add('milk', 3, 4)

        self.assertEqual(len(test_cart.items),1)

        self.assertIsInstance(test_cart.items['milk'], Item)

    
    def test_item_instantiation(self):
        test_item = Item('milk', 3, 4)

        self.assertEqual(test_item.name, 'milk')
        self.assertEqual(test_item.quantity, 3)
        self.assertEqual(test_item.price, 4)

    def test_delete(self):
        test_cart = Cart()
        test_cart.add('milk', 3, 4)
        test_cart.add('eggs', 2, 7)
        test_cart.delete('milk')

        self.assertEqual(len(test_cart.items), 1)
        

unittest.main()

