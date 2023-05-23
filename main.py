import logging #стандартна бібліотека для логування перебігу програми
logging.basicConfig(level=logging.DEBUG,
                    filename= 'logs.log',
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug')
logging.info('info')
logging.error('error')
logging.warning('warning')
logging.critical('critical!!!')
try:
    print(10/0)
except Exception:
    logging.exception('Помилка')
#факторіал числа

def factorial(n):
    logging.info(f'Розпочато обчислення факторіалу числа {n}')
    result = 1
    for i in range(1, n + 1):
        result *= i #1*2*3...
    logging.info(f'Обчислення факторіалу числа завершено {n}.Результат {result}')
    return result
logging.basicConfig(level=logging.INFO)
factorial(5)
