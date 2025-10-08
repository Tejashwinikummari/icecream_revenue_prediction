import pandas as pd

# User input
temperature = float(input("Enter today's temperature: "))
day = input("Enter day of the week (e.g., Monday): ")

# Create a DataFrame with same column names
input_data = pd.DataFrame({
    'DayOfWeek': [day],
    'Temperature': [temperature]
})

# Predict
predicted_sales = model.predict(input_data)
print(f"Predicted Ice Cream Sales: {predicted_sales[0]:.0f}")