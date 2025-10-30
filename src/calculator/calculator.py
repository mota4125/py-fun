from __future__ import annotations
from typing import Iterable, List, Union

Number = Union[int, float]

def _roman_to_int(s: str) -> int:
    # supports I,V,X (enough for single-digits and examples up to X)
    s = s.strip().upper()
    if not s:
        raise ValueError("Empty roman numeral")
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total, prev = 0, 0
    for ch in reversed(s):
        v = values.get(ch)
        if v is None:
            raise ValueError(f"Invalid roman numeral char: {ch}")
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    return total

# multilingual single-digit mapping
_WORDS = {
    # English
    "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
    # German (allow umlaut + fallback)
    "null":0, "eins":1, "zwei":2, "drei":3, "vier":4, "fünf":5, "funf":5, "sechs":6, "sieben":7, "acht":8, "neun":9,
    # Spanish
    "cero":0, "uno":1, "dos":2, "tres":3, "cuatro":4, "cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9,
    # Russian (Cyrillic)
    "ноль":0, "один":1, "два":2, "три":3, "четыре":4, "пять":5, "шесть":6, "семь":7, "восемь":8, "девять":9,
    # Chinese (common ideograms for 0..9)
    "零":0, "〇":0, "一":1, "二":2, "三":3, "四":4, "五":5, "六":6, "七":7, "八":8, "九":9,
}

def _to_number(x: Union[str, Number]) -> Number:
    if isinstance(x, (int, float)):
        return x
    if isinstance(x, str):
        s = x.strip()
        if not s:
            raise ValueError("empty string is not a number")

        # Try plain decimal first (handles "1", "1.600")
        try:
            # normalize comma decimals if user ever inputs "1,6"
            if s.count(',') == 1 and s.replace(',', '.').replace('.', '', 1).replace('-', '', 1).isdigit():
                s = s.replace(',', '.')
            return float(s) if ('.' in s or 'e' in s.lower()) else int(s)
        except ValueError:
            pass

        low = s.lower() #three

        # Try word digits (multilingual)
        if low in _WORDS:
            return _WORDS[low]

        # Try roman numerals
        try:
            rn = _roman_to_int(s)
            return rn
        except Exception:
            pass

    raise ValueError(f"Unsupported numeric input: {x!r}")

def _ensure_numeric(a, b):
    a2, b2 = _to_number(a), _to_number(b)
    return a2, b2

def _as_result_type(a: Number, b: Number, v: float) -> Number:
    # If both were ints and operation is exact int, return int; else float
    if isinstance(a, int) and isinstance(b, int) and abs(v - int(v)) < 1e-12:
        return int(v)
    return v

def _prime_factors(n: int) -> List[int]:
    if n < 2:
        return [n] if n == 1 else []
    factors: List[int] = []
    # handle 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # odd factors
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    if n > 1:
        factors.append(n)
    return factors

class Calculator:
    """
    Singleton Calculator.
    Supports add, sub, mul, div with multilingual digits and roman numerals,
    and factorize for prime factors.
    """
    _instance: "Calculator" | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # arithmetic
    def add(self, a, b): #a=three   b=1.6
        a2, b2 = _ensure_numeric(a, b)
        return _as_result_type(a2, b2, a2 + b2)

    def sub(self, a, b):
        a2, b2 = _ensure_numeric(a, b)
        return _as_result_type(a2, b2, a2 - b2)

    def mul(self, a, b):
        a2, b2 = _ensure_numeric(a, b)
        return _as_result_type(a2, b2, a2 * b2)

    def div(self, a, b):
        a2, b2 = _ensure_numeric(a, b)
        if b2 == 0:
            raise ZeroDivisionError("division by zero")
        return a2 / b2  # division should produce float

    # factorization
    def factorize(self, n) -> List[int]:
        v = _to_number(n)
        # accept float only if it is an integer value (e.g., 8.0)
        if isinstance(v, float) and abs(v - round(v)) < 1e-12:
            v = int(round(v))
        if not isinstance(v, int):
            raise ValueError(f"factorize expects an integer-like value, got {n!r}")
        return _prime_factors(v)
