import apache_beam as beam
from random import choice


class DrinkController(beam.DoFn):
    def process(self, element, *args, **kwargs):
        element.drink = choice(["water", "coffee", "beer", "milk"])
        return [element]
