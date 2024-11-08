import math
import time
import random
from decimal import Decimal



def series(A, n, X):
    output = 0
    coefficient = 1
    term_A = A**n  # Start with A^n
    term_X = 1          # Corresponds to X^0 initially
    
    for k in range(n, -1, -2):
        term = term_A * coefficient * term_X
        
        # Update terms for next cycle
        term_A /= A * A  # A^(k-2) = A^k / A^2
        term_X *= X      # X^(n-k)/2 + 1 = X^(n-k)/2 * X
        
        # Prep coefficient for next cycle
        coefficient *= k * (k - 1) / ((n - k + 1) * (n - k + 2))
        
        output += term
    
    return output * 2

start = time.process_time()
for i in range(100):
    result = (8 + math.sqrt(58))**i
    result = (7 + math.sqrt(58)) ** i
print(result)
end = time.process_time()
save = end - start
start = time.process_time()

for i in range(100):
    result = series(8, i, 58)
    result = series(7, i, 58)
end = time.process_time()

print(result)
print(print('%.2E' % Decimal(str(save))), print('%.2E' % Decimal(str(end-start))))






