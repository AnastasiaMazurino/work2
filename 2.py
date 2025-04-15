import random
from datetime import datetime

# Клас сенсор температур
class TemperatureSensor:
    def get_temperature(self):
        # Симуляція отримання температури
        return round(random.uniform(-20, 40), 2)

# Клас для зберігання температури та часу
class TemperatureLogger:
    def __init__(self, num_records, file_name):
        self.num_records = num_records
        self.file_name = file_name
        self.records = []

    def log_temperature(self, temperature):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.records.append((timestamp, temperature))
        if len(self.records) > self.num_records:
            self.records.pop(0)  # Видалити найстаріший запис

    def save_to_file(self):
        with open(self.file_name, 'w') as file:
            for record in self.records:
                file.write(f'{record[0]} - {record[1]}°C\n')

# Використання
if __name__ == "__main__":
    sensor = TemperatureSensor()
    logger = TemperatureLogger(num_records=10, file_name="temperature_log.txt")

    for _ in range(15):  # Генерація кількох вимірювань
        temperature = sensor.get_temperature()
        logger.log_temperature(temperature)

    logger.save_to_file()
    print("Логування завершено. Дані збережено в файлі temperature_log.txt.")