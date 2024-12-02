class Size(Enum):
    """Enum representing available drink sizes and their corresponding costs."""
    SMALL = 1.50
    MEDIUM = 1.75
    LARGE = 2.05
    MEGA = 2.15

class Drink:
    """Represents a drink with a base, flavors, and size.

    Allows for dynamic calculation of drink costs based on size and number of flavors.
    """
    FLAVOR_COST = 0.15

    def __init__(self, base, flavors=None, size="MEDIUM"):
        """Initializes a Drink instance.

        Args:
            base (str): The base type of the drink (e.g., 'Latte').
            flavors (list of str, optional): List of added flavors. Defaults to None.
            size (str): The size of the drink (e.g., 'SMALL', 'MEDIUM'). Defaults to 'MEDIUM'.

        Raises:
            ValueError: If the provided size is not valid.
        """
        try:
            self.base = base.capitalize()
            self.flavors = [flavor.capitalize() for flavor in (flavors or [])]
            self.size = Size[size.upper()]
        except KeyError:
            raise ValueError(f"Invalid size '{size}'. Available sizes: {[s.name for s in Size]}")

    def get_size(self):
        """Gets the size of the drink.

        Returns:
            str: The size of the drink.
        """
        return self.size.name

    def set_size(self, size):
        """Sets the size of the drink.

        Args:
            size (str): The new size for the drink.

        Raises:
            ValueError: If the provided size is not valid.
        """
        try:
            self.size = Size[size.upper()]
        except KeyError:
            raise ValueError(f"Invalid size '{size}'. Available sizes: {[s.name for s in Size]}")

    @property
    def cost(self):
        """Dynamically calculates the cost of the drink.

        Returns:
            float: The total cost of the drink.
        """
        base_cost = self.size.value
        flavors_cost = len(self.flavors) * self.FLAVOR_COST
        return base_cost + flavors_cost

    def __repr__(self):
        """Returns a string representation of the Drink instance.

        Returns:
            str: A descriptive string for the Drink.
        """
        flavors = ", ".join(self.flavors) if self.flavors else "None"
        return (f"Drink(base='{self.base}', size='{self.size.name}', flavors=[{flavors}], "
                f"cost=${self.cost:.2f})")

class Order:
    """Represents an order consisting of multiple drinks."""
    TAX_RATE = 0.0725

    def __init__(self):
        """Initializes an Order instance."""
        self.drinks = []

    def add_drink(self, drink):
        """Adds a drink to the order.

        Args:
            drink (Drink): The drink to be added.

        Raises:
            TypeError: If the provided item is not a Drink instance.
        """
        if not isinstance(drink, Drink):
            raise TypeError("Only Drink instances can be added to the order.")
        self.drinks.append(drink)

    def get_total(self):
        """Calculates the total cost of the order, including tax.

        Returns:
            dict: A dictionary with subtotal, tax, and total amounts.
        """
        subtotal = sum(drink.cost for drink in self.drinks)
        tax = subtotal * self.TAX_RATE
        total = subtotal + tax
        return {
            "subtotal": round(subtotal, 2),
            "tax": round(tax, 2),
            "total": round(total, 2),
        }

    def get_receipt(self):
        """Generates a detailed receipt for the order.

        Returns:
            dict: A dictionary containing drink details, subtotal, tax, and total.
        """
        drink_details = [
            {"base": drink.base, "size": drink.get_size(), "cost": round(drink.cost, 2)}
            for drink in self.drinks
        ]
        totals = self.get_total()
        return {
            "drinks": drink_details,
            "subtotal": totals["subtotal"],
            "tax": totals["tax"],
            "total": totals["total"],
        }

# Example Usage
if __name__ == "__main__":
    drink1 = Drink(base="Latte", flavors=["Vanilla"], size="Large")  # Large Latte with Vanilla
    drink2 = Drink(base="Espresso", size="Small")  # Small Espresso

    order = Order()
    order.add_drink(drink1)
    order.add_drink(drink2)

    receipt = order.get_receipt()
    print(receipt)  # Display receipt

    print(drink1)  # Custom description of drink
