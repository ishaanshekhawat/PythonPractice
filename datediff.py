import datetime as dt  # Import the datetime module and alias it as 'dt' for convenience

# Get today's date (based on the system's current date)
d1 = dt.date.today()

# Create a date object for a specific date (August 16, 2025) using ISO format (YYYY-MM-DD)
d2 = dt.date.fromisoformat('2025-08-16')

# Subtract d2 from d1 — this gives a timedelta object representing the difference in days
print(d1 - d2)  # Output: the number of days between today and August 16, 2025 (can be negative or positive)
