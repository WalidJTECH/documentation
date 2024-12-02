class TestOrder(unittest.TestCase):
    """Unit tests for the Order class."""

    def test_add_drink(self):
        """Ensure a drink can be added to the order."""
        order = Order()
        drink = Drink(base="Latte", size="Large")
        order.add_drink(drink)
        self.assertEqual(len(order.drinks), 1)

    def test_get_total(self):
        """Validate the order's total calculation with tax."""
        order = Order()
        drink1 = Drink(base="Flat White", size="Large")
        drink2 = Drink(base="Americano", size="Small")
        order.add_drink(drink1)
        order.add_drink(drink2)

        totals = order.get_total()
        expected_subtotal = drink1.cost + drink2.cost
        expected_tax = expected_subtotal * Order.TAX_RATE
        expected_total = expected_subtotal + expected_tax

        self.assertAlmostEqual(totals["subtotal"], expected_subtotal, places=2)
        self.assertAlmostEqual(totals["tax"], expected_tax, places=2)
        self.assertAlmostEqual(totals["total"], expected_total, places=2)


if __name__ == "__main__":
    unittest.main()
