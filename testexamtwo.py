import unittest

from examtwo import Order, User, PaymentProcessor, Meal

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.burger = Meal("Cheeseburger", "Burgers", 5.99)
        self.pasta = Meal("Spaghetti Carbonara", "Pasta", 8.50)
        self.order = Order()

    def test_add_item_to_order(self):
        self.order.add_item(self.burger)
        self.assertEqual(len(self.order.items), 1)
        self.assertIn(self.burger, self.order.items)

    def test_remove_item_from_order(self):
        self.order.add_item(self.burger)
        self.order.remove_item(self.burger)
        self.assertEqual(len(self.order.items), 0)
        self.assertNotIn(self.burger, self.order.items)

    def test_place_order(self):
        self.order.place_order()
        self.assertEqual(self.order.status, "Placed")

    def test_cancel_order(self):
        self.order.cancel_order()
        self.assertEqual(self.order.status, "Cancelled")

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.user = User("John", 50)
        self.payment_processor = PaymentProcessor()

    def test_successful_payment(self):
        self.assertTrue(self.payment_processor.process_payment(self.user, 20))
        self.assertEqual(self.user.balance, 30)

    def test_insufficient_balance_payment(self):
        self.assertFalse(self.payment_processor.process_payment(self.user, 60))
        self.assertEqual(self.user.balance, 50)

if __name__ == '__main__':
    unittest.main()
