import logging
from typing import List
import time

logging.basicConfig(level=logging.INFO)

class DataAccessor:
    def __init__(self, filename: str):
        self.filename = filename

    def get_data(self) -> List[int]:
        with open(self.filename, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data

class DataAccessorProxy:
    def __init__(self, filename: str):
        self.filename = filename
        self.data_accessor = DataAccessor(filename)
        self.logger = Logger()

    def get_data(self) -> List[int]:
        data = self.data_accessor.get_data()
        self.logger.log("Accessed dataset")
        return data

class Logger:
    def log(self, message: str):
        logging.info(message)

def calculate_operations(data: List[int]):
    total_sum = sum(data)
    max_value = max(data)
    min_value = min(data)
    logging.info(f"Operations: Sum={total_sum}, Max={max_value}, Min={min_value}")

if __name__ == "__main__":
    filename = "data.txt"
    proxy = DataAccessorProxy(filename)

    while True:
        dataset = proxy.get_data()
        calculate_operations(dataset)
        time.sleep(1)
