Whitewater [![Travis](https://img.shields.io/travis/AlvarBer/Whitewater.svg)](https://travis-ci.org/AlvarBer/Whitewater) [![AppVeyor](https://img.shields.io/appveyor/ci/AlvarBer/Whitewater.svg)](https://ci.appveyor.com/project/AlvarBer/whitewater) [![PyPI](https://img.shields.io/pypi/v/Whitewater.svg)](https://pypi.python.org/pypi/whitewater) [![GitHub (pre-)release](https://img.shields.io/github/release/AlvarBer/Whitewater/all.svg)](https://github.com/AlvarBer/Whitewater/releases)
===================

![Final aspect](docs/images/final_aspect.png)

What is it?
-----------
Whitewater is a visual dataflow language for creating sklearn pipelines.

It represents functions as blocks, inputs and outputs are presented as pins,
and type safety is enforced when the connection is being made.

![Type safety](docs/images/type_safety.gif)

A smart bubble helps suggesting suitable context-sensitive blocks when making
a connection, showing only the blocks which are type safe.
There is also a search box that can be used for finding a particular block.

![Smart bubble](docs/images/smubble.gif)


How to install?
---------------
If you have pip (Python 3.5+) you can simply type

`$> pip install whitewater`

To execute use.

`$> python -m whitewater`

For windows self-contained executables can be found on the [releases page].


![Full use](docs/images/full_use.gif)


[releases page]: https://github.com/AlvarBer/Whitewater/releases
