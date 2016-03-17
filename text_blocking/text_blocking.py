import re
import itertools


class TextBlocking(object):

    @staticmethod
    def execute(lines):
        if not isinstance(lines, list):
            raise TypeError('lines must be a list')

        if 0 == len(lines) or len(lines) >= 50:
            raise ValueError('lines length out of range')

        base_length = len(lines[0])
        regex = re.compile(r"^[A-Z]{1,50}$")

        for idx, line in enumerate(lines):
            if not isinstance(line, str) or regex.match(line) is None:
                raise ValueError('invalid string line format')

            if idx != 0 and len(line) != base_length:
                raise ValueError('mismatch line length')

        return [''.join(t) for t in itertools.izip(*lines)]

