import apache_beam as beam

# Create a pipeline executing on a direct runner (local, non-cloud).
p = beam.Pipeline('DirectRunner')

# Read a file containing names, add a greeting to each name, and write to a file.
(p
    | 'load names' >> beam.io.ReadFromText('./names')
    | 'add greeting' >> beam.Map(lambda name, msg: '%s, %s!' % (msg, name), 'Hello')
    | 'save' >> beam.io.WriteToText('./greetings'))

p.run()
