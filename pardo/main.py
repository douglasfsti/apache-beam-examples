import apache_beam as beam
from person import Person
from agecontroller import AgeController
from drinkcontroller import DrinkController
from luckynumbercontroller import LuckyNumberController
from personcontroller import PersonController

# Create a pipeline executing on a direct runner (local, non-cloud).
p = beam.Pipeline("DirectRunner")

# Create a PCollection with names and write it to a file.
(p
    | "create" >> beam.Create([Person("Doug"),
                               Person("Kbelo"),
                               Person("Shodas"),
                               Person("Daniboy")])
    | "add age" >> beam.ParDo(AgeController())
    | "add drink" >> beam.ParDo(DrinkController())
    | "add lucky number" >> beam.ParDo(LuckyNumberController())
    | "to string" >> beam.ParDo(PersonController())
    | "save" >> beam.io.WriteToText("./people"))

# Execute the pipeline.
p.run()
