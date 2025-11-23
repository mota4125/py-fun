
class Expressions:
    """"
    Fill in one-line expressions (no own functions) to initialize attributes
    self.b .. self.k with specified values.

    Use Python built-in functions, list expressions and list comprehension,
    but NOT own functions.

    Complete tasks one after another. Once you are done with one task,
    uncomment test cases in test_expressions.py. Remove comments for
      # Test_case_b = Test_case
      # Test_case_c = Test_case
      # Test_case_d = Test_case
      # ...
    Run tests in IDE and in a terminal:
      python test_expressions.py
      python -m unittest
    """

    default_numbers=[4, 12, 3, 8, 17, 12, 1, 8, 7]

    def get_first_three(numbers):
        return numbers[:3]

    def get_last_three(numbers):
        return numbers[-3:]

    def get_last_three_reversed(numbers):
        return numbers[-3:][::-1]

    def get_odd_numbers(numbers):
        return [n for n in numbers if n % 2 == 1]

    def count_odd_numbers(numbers):
        return sum(1 for n in numbers if n % 2 == 1)

    def sum_odd_numbers(numbers):
        return sum(n for n in numbers if n % 2 == 1)

    def remove_duplicates(numbers):
        return list(dict.fromkeys(numbers))  # preserves order

    def count_duplicates(numbers):
        return len(numbers) - len(Expressions.remove_duplicates(numbers))

    def get_squared_sorted_unique(numbers):
        return sorted({n ** 2 for n in numbers})

    def get_length_label(numbers):
        length = len(numbers)
        if length == 0:
            return "EMPTY_LIST"
        return "ODD_LIST" if length % 2 == 1 else "EVEN_LIST"


    def __init__(self, _numbers=default_numbers):
        """
        Constructor to initialize member variables.
        """
        self.numbers = _numbers

        # a) initialize with number of numbers: 9
        self.a = len(self.numbers)

        # b) initialize with first three numbers: [4, 12, 3]
        self.b = Expressions.get_first_three(self.numbers)

        # c) initialize with last three numbers: [1, 8, 7]
        self.c = Expressions.get_last_three(self.numbers)

        # d) initialize with last three numbers reverse: [7, 8, 1]
        self.d = Expressions.get_last_three_reversed(self.numbers)

        # e) initialize with odd numbers: [3, 17, 1, 7]
        self.e = Expressions.get_odd_numbers(self.numbers)

        # f) initialize with number of odd numbers: 4
        self.f = Expressions.count_odd_numbers(self.numbers)

        # g) initialize with sum_ of odd numbers: 28
        self.g = Expressions.sum_odd_numbers(self.numbers)

        # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
        self.h = Expressions.remove_duplicates(self.numbers)

        # i) number of duplicate numbers: 2
        self.i = Expressions.count_duplicates(self.numbers)

        # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
        self.j = Expressions.get_squared_sorted_unique(self.numbers)

        # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
        self.k = Expressions.get_length_label(self.numbers)


    def print_results(self):
        print(f'\nnumbers: {self.numbers}\n#')
        fmt = {
            # key: (value, output string)
            'a': (self.a, 'number of numbers'),
            'b': (self.b, 'first three numbers'),
            'c': (self.c, 'last three numbers'),
            'd': (self.d, 'last three numbers reverse'),
            'e': (self.e, 'odd numbers'),
            'f': (self.f, 'number of odd numbers'),
            'g': (self.g, 'sum of odd numbers'),
            'h': (self.h, 'duplicate numbers removed'),
            'i': (self.i, 'number of duplicate numbers'),
            'j': (self.j, 'ascending, de-dup (n^2) numbers'),
            'k': (self.k, 'length'),
        }
        # format output, e.g.: "b) first three numbers: [1, 4, 6]"
        for k in sorted(fmt.keys()):
            print(f'{k}) {fmt[k][1]}: {fmt[k][0]}')
