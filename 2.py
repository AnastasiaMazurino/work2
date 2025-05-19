import random
from datetime import datetime

# Клас для зберігання температури та часу
class TemperatureRecord:
    def __init__(self, temperature, timestamp=None):
        self.temperature = temperature
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.temperature}°C"


# Клас логгер, який генерує, зберігає та записує температурні вимірювання у файл
class TemperatureLogger:
    def __init__(self, filename="temperature_log.txt"):
        self.filename = filename
        self.records = []

    def log_temperature(self):
        temp = round(random.uniform(20.0, 30.0), 2)  # Імітація показника з датчика
        record = TemperatureRecord(temp)
        self.records.append(record)

    def generate_logs(self, count):
        for _ in range(count):
            self.log_temperature()

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for record in self.records:
                file.write(str(record) + "\n")
        print(f"Збережено {len(self.records)} записів у файл '{self.filename}'")

    def show_logs(self):
        for record in self.records:
            print(record)


# Приклад використання
logger = TemperatureLogger()
logger.generate_logs(5)  # 5 температурних записів
logger.show_logs()       # консоль
logger.save_to_file()    
