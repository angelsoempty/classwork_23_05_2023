import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def function(filename):
    try:
        data = input("Введіть дані для запису: ")
        with open(filename, 'w') as file:
            file.write(data)
        logger.info("Дані успішно записано до файлу.")
    except Exception as e:
        logger.error(f"Помилка при записі даних до файлу: {e}")

filename = input("Введіть ім'я файлу: ")
function(filename)
