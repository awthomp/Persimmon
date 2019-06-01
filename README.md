What is it?
-----------
Whitewater is a *proof of concept* visual dataflow language for creating GPU accelerated sklearn pipelines. The GUI has been forked from AlvarBer/Persimmon. Currently focused on linear regression, Whitewater substitutes Pandas' read_csv calls with those from [RAPIDS](https://rapids.ai/) cuDF and Linear Regression from cuML. Data size is assumed to contain 6 columns -- 5 for the X variable and 1 for y.

Visual Demo is located on [YouTube](https://www.youtube.com/watch?v=nqKDqTUqPKA&feature=youtu.be)

It represents functions as blocks, inputs and outputs are presented as pins,
and type safety is enforced when the connection is being made.

![Type safety](docs/images/type_safety.gif)

A smart bubble helps suggesting suitable context-sensitive blocks when making
a connection, showing only the blocks which are type safe.
There is also a search box that can be used for finding a particular block.

![Smart bubble](docs/images/smubble.gif)


How to install?
---------------
Whitewater leverages the RAPIDS cuDF, cuML, and cuGraph nightly builds. I recommend using Anaconda as the base package manager.
    
Install Whitewater dependencies

`conda env create --name whitewater --file requirements-cuda10.0.yml`

Activate Whitewater environment

`conda activate whitewater`

Install Whitewater (first time use)

`python setup.py build`
`python setup.py install`

To execute use

`python -m whitewater`

![Full use](docs/images/full_use.gif)


[releases page]: https://github.com/AlvarBer/Whitewater/releases
