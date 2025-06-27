import numpy as np

# 1. Convert List to 1D Array
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("1D Array:", array_1d)

# 2. Create 3x3 Matrix with values from 2 to 10
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("\n3x3 Matrix:\n", matrix_3x3)

# 3. Null Vector of size 10 and update sixth value to 11
null_vector = np.zeros(10)
null_vector[6] = 11
print("\nUpdated Null Vector:", null_vector)

# 4. Array from 12 to 38 (excluding 38)
array_12_38 = np.arange(12, 38)
print("\nArray from 12 to 38:", array_12_38)

# 5. Convert Array to Float Type
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("\nArray in float:", float_array)

# 6. Celsius to Fahrenheit
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.0])
fahrenheit = celsius * 9/5 + 32
print("\nCelsius:", celsius)
print("Fahrenheit:", fahrenheit)

# 8. Array Statistical Functions
random_array = np.random.rand(10)
print("\nRandom Array:", random_array)
print("Mean:", np.mean(random_array))
print("Median:", np.median(random_array))
print("Standard Deviation:", np.std(random_array))

# 9. Find min and max in 10x10 array
array_10x10 = np.random.rand(10, 10)
print("\nMin value:", np.min(array_10x10))
print("Max value:", np.max(array_10x10))

# 10. Create 3x3x3 array with random values
array_3x3x3 = np.random.rand(3, 3, 3)
print("\n3x3x3 Array:\n", array_3x3x3)
