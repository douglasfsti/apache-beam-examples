import apache_beam as beam
from random import randint


class LuckyNumberController(beam.DoFn):
    def process(self, element, *args, **kwargs):
        element.lucky_number = randint(1, 100)
        return [element]
