
class TestDrink(unittest.TestCase):
    """Unit tests for the Drink class."""

    def test_get_size(self):
        """Ensure the get_size method returns the correct size."""
        drink = Drink(base="Cappuccino", size="Large")
        self.assertEqual(drink.get_size(), "LARGE")

    def test_set_size(self):
        """Ensure the set_size method updates the drink size."""
        drink = Drink(base="Mocha", size="Small")
        drink.set_size("Mega")
        self.assertEqual(drink.get_size(), "MEGA")

    def test_cost(self):
        """Validate the cost calculation with multiple flavors."""
        drink = Drink(base="Macchiato", flavors=["Hazelnut", "Vanilla"], size="Medium")
        expected_cost = 1.75 + 2 * 0.15
        self.assertAlmostEqual(drink.cost, expected_cost, places=2)

    def test_invalid_size(self):
        """Verify that invalid size inputs raise a ValueError."""
        with self.assertRaises(ValueError):
            Drink(base="Espresso", size="Extra Small")


if __name__ == "__main__":
    unittest.main()
