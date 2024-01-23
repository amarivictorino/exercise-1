def calculate_product_or_sum(number_one, number_two):
  """
  This function calculates the product and sum of two numbers, returning the product if it's
  equal to or lower than 1000, and the sum otherwise.

  Args:
    number_one: The first number (integer).
    number_two: The second number (integer).

  Returns:
    The product if it's equal to or lower than 1000, otherwise the sum.
  """

  # Initialize temporary variables
  product = number_one * number_two
  comparison = product <= 1000

  # Use conditional expression to return product or sum based on comparison
  return product if comparison else number_one + number_two

# Example usage
first_number = 20
second_number = 30
result = calculate_product_or_sum(first_number, second_number)
print(f"The result is: {result}")

