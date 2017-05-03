import apache_beam as beam


class PersonController(beam.DoFn):
    def process(self, element, *args, **kwargs):
        return [str(element)]
