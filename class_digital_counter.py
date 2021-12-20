"""
Реализовать класс цифрового счетчика. В классе реализовать методы:
установки максимального, минимального и начального значения счётчика
увеличения счетчика на 1
возвращения текущего значения счётчика
"""

class Counter:
    current_position = 0

    def __init__(self, start_value, stop_value):
        self.current_position = start_value
        self.stop_counter = stop_value

    def increase_counter(self):
        if self.current_position < self.stop_counter:
            self.current_position += 1
        return self.current_position

    def coun_position_now(self) -> int:
        return self.current_position


counter = Counter(100, 1000)
print(counter.increase_counter())
print(counter.increase_counter())
print(counter.increase_counter())
print('Current counter state now:', counter.coun_position_now())
