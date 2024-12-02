
# Cinos Ordering System

This project implements a drink ordering system for a fictional café named Cinos. It supports:
- Multiple drink options with customizable sizes and flavors.
- Dynamic pricing based on size and additional flavors.
- Comprehensive order management with tax calculations.
- Detailed receipt generation.

## Features

### Drink Class
- Handles individual drink properties (base, flavors, size).
- Dynamically calculates costs.
- Supports custom sizes through an Enum.

### Order Class
- Manages multiple drinks in a single order.
- Calculates subtotal, tax, and total.
- Generates a detailed receipt.

### Unit Tests
- **test_drink.py**: Unit tests for the `Drink` class.
- **test_order.py**: Unit tests for the `Order` class.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/WalidJTECH/CinosOrdringSystem.git
   cd CinosOrdringSystem
   ```

2. Ensure you have Python 3.7 or later installed.

3. Install dependencies if required:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the example script:
```bash
python CinosOrdringSystem.py
```

Run tests:
```bash
python -m unittest test_drink.py
python -m unittest test_order.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
