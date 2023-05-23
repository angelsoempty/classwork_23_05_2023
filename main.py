import logging
# 1
class Calc:
    def __init__(self):
        self.logger = logging.getLogger('Calculator')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self, a, b):
        result = a + b
        self.logger.info(f'{a} + {b} = {result}')
        return result
    def sub(self, a, b):
        result = a - b
        self.logger.info(f'{a} - {b} = {result}')
        return result
    def multiply(self, a, b):
        result = a * b
        self.logger.info(f'{a} * {b} = {result}')
        return result
    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.logger.info(f'{a} / {b} = {result}')
            return result
        else:
            self.logger.error('Помилка! Ділити на нуль неможливо')
            return None

c = Calc()
c.add(2, 2)
c.sub(5, 1)
c.multiply(5, 5)
c.divide(4, 2)