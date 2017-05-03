import apache_beam as beam
from random import randint


class AgeController(beam.DoFn):
    def process(self, element, *args, **kwargs):
        element.age = randint(18, 30)
        return [element]
