Introduction
============

On this chapter Whitewater is introduced, along its main objectives and
motivations.
It also includes a section about topics that are related but beyond the scope
of this project.
Finally, it includes an overview of the project report structure.


Description
-----------
Data Science has seen exponential growth in the market on recent years, with
some predictions stating that one million data scientists will be needed by
2018 [@onemillion].
Data scientists find themselves on a golden age, for the Harvard Business
Review it is the sexiest job of the 21st century [@sexy].
Despite all the hype, there is a shortage of skilled data scientists, the field
is inherently multidisciplinary [@venn], as coding, statistics and domain
knowledge are required, making the path to mastery long and complex, leading
to the so called Unicorn hunts [@unicorn] and [@hunt].

Tools such as scikit-learn[^skl], Weka or Tableau provide a very high
level access to some of the required tools data scientists require, easing the
learning curve and widening the pool of available data scientists.
However these tools either require coding, focus on just preprocessing tasks
(cleaning of the data) or provide a very limited interface.

Whitewater aims to provide a visual interface for scikit-learn, giving the
ability to create pipelines without a single line of code, thus giving most of
the power of hand coding the pipelines with a helpful visual representation.

In order to accomplish this the project explores the following topics,

* Dataflow Programming. This paradigm presents programs as a directed acyclic
    graph, pioneered on the 60 at MIT and Bell labs [@bell].
    It models programs as a stream of data that is run through a pipeline of
    instructions rather than a set of instructions that operates on external
    data, i.e. the instructions are flowing through data, not the other way
    around.
    This results in parallel programs by default, closer to the functional
    paradigm than imperative programming and the Von Neumann architecture, as
    mentioned in functional programming seminal paper [@backus1978can].

* Visual Programming. The natural fit for a dataflow representation is a visual
    interface, as we can present the graph visually [@shu1988visual].
    Further improvements include type-checking at write time, i.e. when
    connecting the blocks only allow for connections that are type safe.

* User Experience. The project is driven by the users' feedback and engagement
    with the prototype.
    The interface needs to convey the intended course of action, and give the
    user hints in order to ease the difficulty curve.
<!-- Add citation -->

* Software Engineering. Interfacing with previous existing code, laying
    well-defined interfaces and organizing code though object-oriented
    techniques.
<!-- Add citation -->

* Machine Learning. Although there is no writing implementation of new
    algorithms extensive knowledge of current implementations is needed in
    order to surface all the available options, as sklearn provides many ways
    to modify their configuration through parameters [@scikitlearn].

* Data Wrangling. Some preconditions about the data have to be assumed or
    the user has to be provided with the tools to perform the transformation.

* Compilers. The graphical form of a workflow involving several steps is
    compiled down to Python source code (Transcompilation).

The hypothesis of the project is that the visual representation of the workflow
and the associated concepts can help to both learn and use Machine Learning
techniques and to accelerate early exploratory datascience work.

This hypothesis converges with the spirit of sklearn, [see @scikitlearn, pp29]
that also tries to bring the Machine Learning techniques out of PhD
dissertations and niche libraries into the mainstream, providing high-level,
easy to use access to those resources.
This strategy seems to have worked for sklearn, becoming one of the
most important open source machine learning libraries in the process, with over
16000 stars on [Github](https://github.com/scikit-learn/scikit-learn), and is
being used on companies such as Spotify, Facebook or Evernote [@whosklearn].


Motivation
----------
After learning about Machine Learning at university last year I got an
internship on an algorithmic trading company as part of the quant team.

My main task was helping moving the existing codebase from `MATLAB` to
`Python`, and during that process I observed how some of my co-workers were
struggling with the language switch.

They all came from backgrounds such as Maths, Physics, Electric Engineering,
Statistics or Aerospace Engineering.
But there were no Computer Scientists even though their role as quants
requires, apart from maths and stats knowledge, a very good level of
programming expertise.

Experts from these fields tend to have weaker programming skills,
as they mostly work with scientific computing oriented languages such as
`MATLAB`, `R` or `Julia`, and moving to a general purpose language such as
`Python` involves learning about a plethora of additional topics, such as
Object Oriented Programming, custom complex Data structures or cache
optimization.

The situation is even more complex for newcomers to Machine Learning, as
they not only have to deal with the programming barrier but also have to
overcome the difficulties of learning the algorithms themselves.


Objectives
----------
<!--
Research:

:   On terms of research this project touches on a multitude of topics, from
    the theoretical aspects inherent to creating what is essentially a domain
    specific language to the relevant current commercial solutions available.
    All of this requires a compilation and reading of scientific sources.

Requirements:

:   The system is defined on the requirements fixated at the start of the
    project, it is necesary to provide both a good description of each, as well
    as some kind of development plan connecting them all.
    A good risk analysis can also prevent failures in a multitude of areas
    such as time management or technical debt.

Testing:

:   The software needs to be testable, as to allow for the automation of
    testing on the source repository, caching bugs faster in the process.
-->

Feasibility:
:   The project has to explore the space of possible solutions on visual
    machine learning approaches, trying different estrategies for both the
    front and backend of the application (Flow based programming, Dataflow
    programming, etc).

Design and Usability:
:   The system has to be designed in accordance to requirements, both
    in terms of making it easy to progress through the milestones, as well as
    producing usable software at each stage.
    In all cases it must balance complexity against expresivity, trying to
    provide the user with a powerful tool while avoiding complex and
    unusable interface.

Evaluation:
:   The software will be evaluated by participants that belong to the intended
    audience of the system, a form must be prepared detailing the task they
    will have to perform, as well as how their data will be treated.

Learning Tool:
:   The software will help both with the programming barrier, easing the
    learning curve of Machine Learning as to allow the learner to focus on the
    connections, intuitions and mathematical basis of the algorithms and not on
    the implementation details and the quirks of the language.

Faster Exploratory Work:
:    By providing an easy to use, drag and drop interface the user can try a
     plethora of different estimators and adjusting the hyper-parameters as
     they see fit faster, and without writing a single line of code.

Implementation:
:   There are some **non-functional requirements**, such as the project running
    on the desktop platform, being able to pack it into a executable (to make
    evaluation easier for participants), have a framerate good enough for
    pleasant use (minimum 30 FPS), or support multithreading (as to not block
    the main/UI thread from running when executing the backend),


What the project is not
-----------------------
The project is not concerned with the following:

* General Data Cleaning/Wrangling. Although there is some data manipulation
    that is necesary and included on sklearn it is outside the scope of the
    project, Whitewater only works with clean data. This is done because it is
    very hard to translate code-based data manipulation into a visual
    representation.
* Data Visualization. Since this kind of work is very hard to represent without
    requiring explict coding on a case by case basis, as it is highly dependent
    on the characteristics of the data to visualize.
* General Purpose Visual Programming. Since focusing on Machine Learning allows
    Whitewater to make assumptions about the possible programs that enable
    features such as type simplification (check type chapter) or removing
    explicit flow management (more on the literature review chapter).

Project Structure
-----------------
The project structure follows closely the development timeline of the system.
Firstly the literature review is introduced.
On the following chapter the project milestones are explained, including a
Gantt chart.
Following is the risk analysis table as well as the development methodology.

The implementation chapter explains the iterative process on each of the
iterations of the project, some interesting technical problems, and the
immediate representation of Whitewater.

After this, the important concept of workflows is explained, and the interface
design, including the sketches or the color palette.
The type checking sections introduces a lot of theory from functional
programming and type theory.
The final section before the post-mortem explains the evaluation process and
results.
On the final post mortem sections the conclusions of the project are laid down,
as well a recap of what went wrong, what went right, what was achieved, and
the potential future improvements.

[^skl]: Scikit-learn is a python library that aims to bring machine learning to
    a more general public, by providing a high-level API that allows the ease of
    use and interchange of different estimators.
