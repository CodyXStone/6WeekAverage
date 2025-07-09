class RollingAverage:
    def __init__(self): #Initialize max number 6
        self.numbers = []
        self.max_size = 6

    def add_number(self, number):
        if len(self.numbers) >= self.max_size:
            self.numbers.pop(0)  # Remove the oldest number
        self.numbers.append(number)
        return self.calculate_average()

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

if __name__ == "__main__":
    rolling_avg = RollingAverage()
    while True:
        try:
            user_input = input("Enter a number (or type 'exit' to quit): ") #Ask for input
            if user_input.lower() == 'exit':
                break
            number = float(user_input)  # Convert input to float
            average = rolling_avg.add_number(number)
            print(f"Current rolling average of last 6 numbers: {average:.2f}") #Return the average of the number set.
        except ValueError:
            print("Please enter a valid number.")
