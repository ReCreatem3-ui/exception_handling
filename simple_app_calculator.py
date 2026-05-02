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
                  print("Error: Division by zero")
      
      def modulus(self, value):
            self.current_value %= value
      
      def power(self, value):
            self.current_value **= value
      
      def reciprocal(self):
            if self.current_value != 0:
                  self.current_value = 1 / self.current_value
            else:
                  print("Error: Cannot take reciprocal of zero")
      
      def square(self):
            self.current_value **= 2
      
      def square_root(self):
            if self.current_value >= 0:
                  self.current_value **= 0.5
            else:
                  print("Error: Cannot take square root of a negative number")
      
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

      def draw_calculator(self, calc, expression_str = "", error_msg = ""):
            self.clear_screen()

            MAX_WIDTH = self.MAX_WIDTH = 43
            result_str = self.format_result(calc.current_value)

            if len(expression_str) > MAX_WIDTH:
                  expression_str = "..." + expression_str[:MAX_WIDTH - 3]
            
            expression_display = expression_str.ljust(MAX_WIDTH)
            result_display = result_str.rjust(MAX_WIDTH)
            error_display = error_msg.center(MAX_WIDTH)

            calculator_body = [
                  "╔═══════════════════════════════════════════╗",
                  "║             PYTHON CALCULATOR             ║",
                  "╠═══════════════════════════════════════════╣",
                  f"║{expression_display}║",
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





print("""
╔═══════════════════════════════════════════╗     LEGEND")
║             PYTHON CALCULATOR             ║    ─────────────────────────────
╠═══════════════════════════════════════════╣     +      Add          (+ 5)   
║                                           ║     -      Subtract     (- 10)  
║                                           ║     x      Multiply     (x 2)   
║                                           ║     /      Divide       (/ 4)   
╠══════════╦══════════╦══════════╦══════════╣     %      Modulus      (% 3)   
║          ║          ║          ║          ║     ^      Power        (^ 2)   
║    %     ║    CE    ║    C     ║   exit   ║     r      Reciprocal   (r)     
║          ║          ║          ║          ║     sq     Square       (sq)    
╠══════════╬══════════╬══════════╬══════════╣     sqrt   Square Root  (sqrt)  
║          ║          ║          ║          ║     +/-    Negate       (+/-)   
║   1/x    ║     ^    ║   ²√x    ║     ÷    ║     clear  Reset to 0          
║          ║          ║          ║          ║     exit   Quit                
╠══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║
║     7    ║     8    ║     9    ║     x    ║
║          ║          ║          ║          ║
╠══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║
║     4    ║     5    ║     6    ║     -    ║
║          ║          ║          ║          ║
╠══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║
║     1    ║     2    ║     3    ║     +    ║
║          ║          ║          ║          ║
╠══════════╬══════════╬══════════╬══════════╣
║          ║          ║          ║          ║
║   +/-    ║     0    ║     .    ║     =    ║
║          ║          ║          ║          ║
╚══════════╩══════════╩══════════╩══════════╝
      """)
    