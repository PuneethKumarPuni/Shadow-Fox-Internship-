radius = float(input("Enter the radius of the pond in meters: "))
pi = 3.14

area = pi * (radius ** 2)
water_per_sq_meter = 1.4
total_water = int(area * water_per_sq_meter)

print("Area of the pond:", area)
print("Total water in the pond (liters):", total_water)
