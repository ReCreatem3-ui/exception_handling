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

# print("""
# ╔═══════════════════════════════════════════╗     LEGEND")
# ║             PYTHON CALCULATOR             ║    ─────────────────────────────
# ╠═══════════════════════════════════════════╣     +      Add          (+ 5)   
# ║                                           ║     -      Subtract     (- 10)  
# ║                                           ║     x      Multiply     (x 2)   
# ║                                           ║     /      Divide       (/ 4)   
# ╠══════════╦══════════╦══════════╦══════════╣     %      Modulus      (% 3)   
# ║          ║          ║          ║          ║     ^      Power        (^ 2)   
# ║    %     ║    CE    ║    C     ║   exit   ║     r      Reciprocal   (r)     
# ║          ║          ║          ║          ║     sq     Square       (sq)    
# ╠══════════╬══════════╬══════════╬══════════╣     sqrt   Square Root  (sqrt)  
# ║          ║          ║          ║          ║     +/-    Negate       (+/-)   
# ║   1/x    ║     ^    ║   ²√x    ║     ÷    ║     clear  Reset to 0          
# ║          ║          ║          ║          ║     exit   Quit                
# ╠══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║
# ║     7    ║     8    ║     9    ║     x    ║
# ║          ║          ║          ║          ║
# ╠══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║
# ║     4    ║     5    ║     6    ║     -    ║
# ║          ║          ║          ║          ║
# ╠══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║
# ║     1    ║     2    ║     3    ║     +    ║
# ║          ║          ║          ║          ║
# ╠══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║
# ║   +/-    ║     0    ║     .    ║     =    ║
# ║          ║          ║          ║          ║
# ╚══════════╩══════════╩══════════╩══════════╝
#       """)
    