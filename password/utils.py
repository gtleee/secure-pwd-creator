import secrets


class PasswordGenerator:
    """
    A class to generate secure passwords with given specifications.
    """

    def __init__(self, length=12, uppercase=True, lowercase=True, numbers=True, symbols=True):
        """
        Initializes a new instance of the PasswordGenerator class.

        :param length: int, The length of the password to generate
        :param uppercase: bool, whether to include uppercase letters
        :param lowercase: bool, whether to include lowercase letters
        :param numbers: bool, whether to include digits
        :param symbols: bool, wheter to include punctuation characters
        """
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.symbols = symbols
        self.characters = ''

        # Build the set of characters based on the user's preferences
        if self.uppercase:
            self.characters += 'ABCDEFGHJKLMNPQRSTUVWXYZ'
        if self.lowercase:
            self.characters += 'abcdefghjklmnpqrstuvwxyz'
        if self.numbers:
            self.characters += '23456789'
        if self.symbols:
            self.characters += '!#$%*@'

    def generate(self):
        """
        Generate a secure password with the specified characteristics.

        :return: str, the generated password
        :raise VauleError: if no character sets are selected
        """
        if not self.characters:
            raise ValueError('No character sets selected')

        # Secure select characters from the pool and concatenate them into a password
        return ''.join(secrets.choice(self.characters) for _ in range(self.length))
