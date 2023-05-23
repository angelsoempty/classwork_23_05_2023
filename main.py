import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def function(filename, num):
    try:
        with open(filename, 'w') as file:
            for i in range(num):
                number = random.randint(1, 100)
                file.write(str(number) + '\n')
                logger.info(f"Згенеровано та записано число: {number}")
        logger.info("Усі числа успішно записано до файлу.")
    except Exception as e:
        logger.error(f"Помилка при записі чисел до файлу: {e}")


filename = input("Введіть ім'я файлу: ")
num_numbers = int(input("Введіть кількість чисел для генерації: "))
function(filename, num_numbers)
