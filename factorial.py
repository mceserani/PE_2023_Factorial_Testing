"""Funzioni per il calcolo del fattoriale"""

def factorial(n):
    """Calcola il fattoriale di n"""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    return n * factorial(n-1)
