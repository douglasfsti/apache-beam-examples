# Apache Beam

Apache Beam provides an advanced unified programming model, allowing you to
implement batch and streaming data processing jobs that can run on any execution engine.

**Apache Beam** is:
- UNIFIED - Use a single programming model for both batch and streaming use cases.
- PORTABLE - Execute pipelines on multiple execution environments, including Apache Apex, Apache Flink, Apache Spark, and **Google Cloud Dataflow**.
- EXTENSIBLE - Write and share new SDKs, IO connectors, and transformation libraries.

To use Beam, you need to first create a driver program using the classes in one of the Beam SDKs.
Your driver program defines your pipeline, including all of the inputs, transforms, and outputs;
it also sets execution options for your pipeline (typically passed in using command-line options).
These include the Pipeline Runner, which, in turn, determines what back-end your pipeline will run on.

The Beam SDKs provide a number of abstractions that simplify the mechanics
of large-scale distributed data processing.
The same Beam abstractions work with both batch and streaming data sources.
When you create your Beam pipeline, you can think about your data processing task
in terms of these abstractions. They include:
- **Pipeline**: A Pipeline encapsulates your entire data processing task, from start to finish.
              This includes reading input data, transforming that data, and writing output data.
              All Beam driver programs must create a Pipeline. When you create the Pipeline,
              you must also specify the execution options that tell the Pipeline where and how to run.
- **PCollection**: A PCollection represents a distributed data set that your Beam pipeline operates on.
                 The data set can be bounded, meaning it comes from a fixed source like a file,
                 or unbounded, meaning it comes from a continuously updating source via a subscription
                 or other mechanism. Your pipeline typically creates an initial PCollection
                 by reading data from an external data source, but you can also create a PCollection
                 from in-memory data within your driver program.
                 From there, PCollections are the inputs and outputs for each step in your pipeline.
- **Transform**: A Transform represents a data processing operation, or a step, in your pipeline.
               Every Transform takes one or more PCollection objects as input, performs a processing
               function that you provide on the elements of that PCollection, and produces one or more
               output PCollection objects.
- **I/O Source and Sink**: Beam provides Source and Sink APIs to represent reading and writing data,
                         respectively. Source encapsulates the code necessary to read data into your
                         Beam pipeline from some external source, such as cloud file storage or a
                         subscription to a streaming data source. Sink likewise encapsulates the code
                         necessary to write the elements of a PCollection to an external data sink.

[For more information, read the docs](https://beam.apache.org/documentation/programming-guide/)
