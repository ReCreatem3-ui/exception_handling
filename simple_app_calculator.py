import os
import time


class Calculator:
    def __init__(self):
        self.current_value = 0.0

    def add(self, value):
        self.current_value += value

    def subtract(self, value):
        self.current_value -= value

    def multiply(self, value):
        self.current_value *= value

    def divide(self, value):
        if value != 0:
            self.current_value /= value
        else:
            return "Error! Division by zero."

    def modulus(self, value):
        self.current_value %= value

    def power(self, value):
        self.current_value **= value

    def reciprocal(self):
        if self.current_value != 0:
            self.current_value = 1 / self.current_value
        else:
            return "Error! Cannot take reciprocal of zero."

    def square(self):
        self.current_value **= 2

    def square_root(self):
        if self.current_value >= 0:
            self.current_value **= 0.5
        else:
            return "Error! Cannot take square root of a negative number."

    def negate(self):
        self.current_value = -self.current_value

    def clear(self):
        self.current_value = 0.0


class Display:
    def __init__(self):
        self.MAX_WIDTH = 43

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def format_result(self, value):
        if abs(value) >= 1_000_000 or (value != 0 and abs(value) < 0.0001):
            return f"{value:.4e}"
        return f"{value:.10g}"

    def draw(self, calc, expression_str="", error_msg=""):
        self.clear_screen()

        MAX_WIDTH = self.MAX_WIDTH
        result_str = self.format_result(calc.current_value)

        if len(expression_str) > MAX_WIDTH:
            expression_str = expression_str[:MAX_WIDTH - 3] + "..."

        expr_display   = expression_str.ljust(MAX_WIDTH)
        result_display = result_str.rjust(MAX_WIDTH)
        error_display  = error_msg.center(MAX_WIDTH) if error_msg else " " * MAX_WIDTH

        calc_lines = [
            "╔═══════════════════════════════════════════╗",
            "║             PYTHON CALCULATOR             ║",
            "╠═══════════════════════════════════════════╣",
            f"║{expr_display}║",
            f"║{error_display}║",
            f"║{result_display}║",
            "╠══════════╦══════════╦══════════╦══════════╣",
            "║          ║          ║          ║          ║",
            "║    %     ║    CE    ║    C     ║   exit   ║",
            "║          ║          ║          ║          ║",
            "╠══════════╬══════════╬══════════╬══════════╣",
            "║          ║          ║          ║          ║",
            "║   1/x    ║     ^    ║   ²√x    ║     ÷    ║",
            "║          ║          ║          ║          ║",
            "╠══════════╬══════════╬══════════╬══════════╣",
            "║          ║          ║          ║          ║",
            "║     7    ║     8    ║     9    ║     x    ║",
            "║          ║          ║          ║          ║",
            "╠══════════╬══════════╬══════════╬══════════╣",
            "║          ║          ║          ║          ║",
            "║     4    ║     5    ║     6    ║     -    ║",
            "║          ║          ║          ║          ║",
            "╠══════════╬══════════╬══════════╬══════════╣",
            "║          ║          ║          ║          ║",
            "║     1    ║     2    ║     3    ║     +    ║",
            "║          ║          ║          ║          ║",
            "╠══════════╬══════════╬══════════╬══════════╣",
            "║          ║          ║          ║          ║",
            "║   +/-    ║     0    ║     .    ║     =    ║",
            "║          ║          ║          ║          ║",
            "╚══════════╩══════════╩══════════╩══════════╝",
        ]

        legend_lines = [
            "  LEGEND",
            " ─────────────────────────────",
            "  +      Add          (+ 5)   ",
            "  -      Subtract     (- 10)  ",
            "  x      Multiply     (x 2)   ",
            "  /      Divide       (/ 4)   ",
            "  %      Modulus      (% 3)   ",
            "  ^      Power        (^ 2)   ",
            "  r      Reciprocal   (r)     ",
            "  sq     Square       (sq)    ",
            "  sqrt   Square Root  (sqrt)  ",
            "  +/-    Negate       (+/-)   ",
            "  clear  Reset to 0          ",
            "  exit   Quit                ",
        ]

        while len(legend_lines) < len(calc_lines):
            legend_lines.append("")

        for i, calc_line in enumerate(calc_lines):
            legend_part = legend_lines[i] if i < len(legend_lines) else ""
            print(f"{calc_line}   {legend_part}")

        print("\nEnter command below:")

    def draw_exit(self):
        self.clear_screen()
        print("╔═══════════════════════════════════════════╗     LEGEND")
        print("║             PYTHON CALCULATOR             ║    ─────────────────────────────")
        print("╠═══════════════════════════════════════════╣     +      Add          (+ 5)   ")
        print("║      Thank you for using Recreatem3's     ║     -      Subtract     (- 10)  ")
        print("║              Python Calculator!           ║     x      Multiply     (x 2)   ")
        print("║                                           ║     /      Divide       (/ 4)   ")
        print("╠══════════╦══════════╦══════════╦══════════╣     %      Modulus      (% 3)   ")
        print("║          ║          ║          ║          ║     ^      Power        (^ 2)   ")
        print("║    %     ║    CE    ║    C     ║   exit   ║     r      Reciprocal   (r)     ")
        print("║          ║          ║          ║          ║     sq     Square       (sq)    ")
        print("╠══════════╬══════════╬══════════╬══════════╣     sqrt   Square Root  (sqrt)  ")
        print("║          ║          ║          ║          ║     +/-    Negate       (+/-)   ")
        print("║   1/x    ║     ^    ║   ²√x    ║     ÷    ║     clear  Reset to 0          ")
        print("║          ║          ║          ║          ║     exit   Quit                ")
        print("╠══════════╬══════════╬══════════╬══════════╣")
        print("║          ║          ║          ║          ║")
        print("║     7    ║     8    ║     9    ║     x    ║")
        print("║          ║          ║          ║          ║")
        print("╠══════════╬══════════╬══════════╬══════════╣")
        print("║          ║          ║          ║          ║")
        print("║     4    ║     5    ║     6    ║     -    ║")
        print("║          ║          ║          ║          ║")
        print("╠══════════╬══════════╬══════════╬══════════╣")
        print("║          ║          ║          ║          ║")
        print("║     1    ║     2    ║     3    ║     +    ║")
        print("║          ║          ║          ║          ║")
        print("╠══════════╬══════════╬══════════╬══════════╣")
        print("║          ║          ║          ║          ║")
        print("║   +/-    ║     0    ║     .    ║     =    ║")
        print("║          ║          ║          ║          ║")
        print("╚══════════╩══════════╩══════════╩══════════╝")


class InputHandler:
    def __init__(self, calc, display):
        self.calc = calc
        self.display = display
        self.expression_str = ""
        self.error_msg = ""

    def handle(self, user_input):
        user_input = user_input.strip().lower()

        if user_input == "exit":
            return "exit"

        elif user_input == "clear":
            self.calc.clear()
            self.expression_str = ""
            return "continue"

        elif user_input == "r":
            result = self.calc.reciprocal()
            if result:
                self.error_msg = result
            else:
                self.expression_str = f"1/({self.display.format_result(self.calc.current_value)})"

        elif user_input == "sq":
            self.expression_str = f"({self.display.format_result(self.calc.current_value)})²"
            self.calc.square()

        elif user_input == "sqrt":
            result = self.calc.square_root()
            if result:
                self.error_msg = result
            else:
                self.expression_str = f"√({self.display.format_result(self.calc.current_value)})"

        elif user_input == "+/-":
            self.expression_str = f"-({self.display.format_result(self.calc.current_value)})"
            self.calc.negate()

        else:
            parts = user_input.split()
            if len(parts) != 2:
                self.error_msg = "Invalid! Example: + 25"
                return "continue"

            op = parts[0]

            try:
                num = float(parts[1])
            except ValueError:
                self.error_msg = "Please enter a valid number!"
                return "continue"

            prev = self.display.format_result(self.calc.current_value)

            if op == "+":
                self.expression_str = f"{prev} + {num}"
                self.calc.add(num)
            elif op == "-":
                self.expression_str = f"{prev} - {num}"
                self.calc.subtract(num)
            elif op == "x":
                self.expression_str = f"{prev} x {num}"
                self.calc.multiply(num)
            elif op == "/":
                result = self.calc.divide(num)
                if result:
                    self.error_msg = result
                else:
                    self.expression_str = f"{prev} / {num}"
            elif op == "%":
                self.expression_str = f"{prev} % {num}"
                self.calc.modulus(num)
            elif op == "^":
                self.expression_str = f"{prev} ^ {num}"
                self.calc.power(num)
            else:
                self.error_msg = "Unknown operation!"

        return "continue"


class App:
    def __init__(self):
        self.calc = Calculator()
        self.display = Display()
        self.handler = InputHandler(self.calc, self.display)

    def run(self):
        while True:
            self.display.draw(self.calc, self.handler.expression_str, self.handler.error_msg)
            self.handler.error_msg = ""

            try:
                user_input = input(">> ")
                result = self.handler.handle(user_input)

                if result == "exit":
                    self.display.draw_exit()
                    break

            except KeyboardInterrupt:
                self.display.draw_exit()
                break

            except Exception:
                self.handler.error_msg = "Numerical limit exceeded"

app = App()
app.run()