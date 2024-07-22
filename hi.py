import streamlit as st

def calculate_guntha(length, breadth):
  """Calculates the area of a rectangle in guntha.

  Args:
      length: Length of the rectangle in feet.
      breadth: Breadth of the rectangle in feet.

  Returns:
      Area of the rectangle in guntha.
  """
  # Convert feet to square feet
  area_sq_ft = length * breadth

  # Convert square feet to guntha using the conversion factor
  conversion_factor = 0.0009182736455
  area_guntha = area_sq_ft * conversion_factor

  return area_guntha

def is_valid_input(value):
  """Checks if the input is a positive number."""
  return value > 0

st.title("Guntha Area Calculator")

# Input fields for length and breadth
length = st.number_input("Enter Length (feet)", format="%f", on_change=is_valid_input)
breadth = st.number_input("Enter Breadth (feet)", format="%f", on_change=is_valid_input)

# Calculation button
if st.button("Calculate Area"):
  # Validate input values (using the is_valid_input function)
  if not is_valid_input(length) or not is_valid_input(breadth):
    st.error("Please enter valid positive values for length and breadth.")
  else:
    # Perform calculation and display result
    area_guntha = calculate_guntha(length, breadth)
    st.write(f"The area of the rectangle is: {area_guntha:.4f} guntha")
