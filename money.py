# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        pass

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount
        self.currency = currency

    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        if self.currency.symbol:
            if type(self.amount) == int:
                return f"{self.currency.symbol}{self.amount}.{self.currency.digits *'0'}"
            elif type(self.amount) == float:
                return f"{self.amount}"
        elif not self.currency.symbol:
            # return f"{self.currency.code} {self.amount:.{self.currency.digits}f}"
            that = f"{self.amount}{self.currency.digits * '0'}"
            return f"{self.currency.code} {that[:self.currency.digits + that.find('.')+1]}"

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError
        return Money(self.amount + other.amount, self.currency)
        # Why were these bad ways?
        # You should return a new object. You shouldn't modify existing objects
        # BAD WAY ---------------------------------------------
        # if self.currency.code == other.currency.code:
        #     self.amount += other.amount
        #     return self
        # raise DifferentCurrencyError('Different Currencies')

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError
        return Money(self.amount - other.amount, self.currency)
        # BAD WAY ---------------------------------------------
        # if self.currency.code == other.currency.code:
        #     self.amount -= other.amount
        #     return self
        # raise DifferentCurrencyError('Different Currencies')

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        return Money(self.amount * multiplier, self.currency)
        # BAD WAY ---------------------------------------------
        # self.amount *= multiplier
        # return self

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        return Money(self.amount / divisor, self.currency)
        # BAD WAY ---------------------------------------------
        # self.amount /= divisor
        # return self

    def __add__(self, other):
        """
        Add a money object by another money object with standard mathematics
        """
        if self.currency.code == other.currency.code:
            return Money(self.amount + other.amount, self.currency)
        raise DifferentCurrencyError('Different Currencies')

    def __sub__(self, other):
        """
        Subtract a money object by another money object with standard mathematics
        """
        if self.currency.code == other.currency.code:
            return Money(self.amount - other.amount, self.currency)
        raise DifferentCurrencyError('Different Currencies')

    def __mul__(self, other):
        """
        Multiply a money object by another money object with standard mathematics
        """
        if self.currency.code == other.currency.code:
            return Money(self.amount * other.amount, self.currency)
        raise DifferentCurrencyError('Different Currencies')

    def __truediv__(self, other):
        """
        Divide a money object by another money object with standard mathematics
        """
        if self.currency.code == other.currency.code:
            return Money(self.amount / other.amount, self.currency)
        raise DifferentCurrencyError('Different Currencies')
