import numpy as np

# 1. Створюємо одновимірний масив з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, size=200)
print("Original array (first 10 elements):", arr[:10])

# 2. Використовуючи маску, фільтруємо всі додатні числа в масиві
mask_positive = arr > 0
positive_numbers = arr[mask_positive]
print("\nFiltered positive numbers (first 10):", positive_numbers[:10])

# 3. Замінюємо всі від’ємні значення на нулі в оригінальному масиві
arr[arr < 0] = 0
print("\nArray after replacing negative values with zeros (first 10):", arr[:10])

# 4. Обчислюємо середнє значення отриманого масиву
mean_value = np.mean(arr)
print("\nMean value of the updated array:", mean_value)