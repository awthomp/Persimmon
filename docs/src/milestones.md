Milestones
==========

In order to guarantee the delivery of the software an incremental approach
has been chosen, this implies breaking down the objectives into
smaller milestones that can be accomplished more easily, so in case the last
milestone is not reached there is still a substantial product to submit.


Tree
----

![Milestones Tree](images/objectives.pdf)

**Capped** is more than a minimum viable product, a extensive proof-of-concept,
with a few limited algorithms and the ability of inputing `.csv` files, with a
restricted interface in which algorithms are not dragged and dropped but merely
selected through buttons.

**Parity** means a more or less complete parity in terms of features and visual
interaction.
It is not very important to have the same number of underlying algorithms
because that's not the focus of the project, and creating new blocks having the
underlying algorithm is easy.

And the final milestone is **Compilation**, the ability to get the python
source code from the visual representation, also improving the interface to
have a better flow, more akin to Unreal Engine, as discussed on the literature
review chapter, state of the art section.

This milestone would bring Whitewater utility beyond the realm of learning tool,
as it would be a convenient tool for the exploratory work of any ML solution
(business case, a Kaggle[^kaggle] competition, etc...).

Out of scope, but possible further applications of the system are **web/junyper**
integration, which would mean the system would be accessible from a website
interface, and script **synthesization**, which is the opposite of compilation,
in other words the ability to translate a python source file to the Whitewater
visual representation.


Gantt Chart
-----------
With the defined milestones a Gantt chart of the project development was
drawn.

<!-- Improve Gantt Diagram according to previous feedback?. -->
![Gantt Diagram of the project development.](images/gantt.pdf)


Development Methodology
-----------------------
The chosen methodology is based on agile methodologies such as **Scrum** or
**Extreme Programming**, meaning that there is not a complete model of the
desired system like in model driven development [@selic2003pragmatics], nor a
complete planning of every development detail at the start of development, such
as on Waterfall [@petersen2009waterfall], instead there are continuous
iterations, faster and smaller than traditional development iterations that
allow for more opportunity to react and adapt to change [@beck2001manifesto].
These iterations last two weeks and are called sprints, and a board is used to
keep track of all current and future tasks.

On a traditional Scrum methodology, the product owner puts uses cases (*items*)
into the product backlog.
Each sprint the scrum master and the development team have a meeting called
*Sprint Planning event* [@schwaber2002agile], where items the current sprint
items from the product backlog to be done are decided and broken down into
tasks to be done.
Items can also be pushed back into the backlog if they are not achievable or
have a lower priority.

However, this methodology does not really fit the development of this project,
since there is no team, there is no need for superfluous and unnecessary
processes.
There is no retrospective after each sprint and there is no specific weight or
cost assigned to each task.
During a sprint the next sprint tasks are moved from the product backlog into
the sprint planning column and broken down further if necessary.

Task are defined by use cases and can be broken down further by using
checklists on the tasks.

If a task is not fully completed it can be moved back onto the product backlog.

The planning board can be found at [https://trello.com/b/JmG3xy0U/whitewater]

Source Code
-----------
The source code for this project is hosted on
[https://github.com/AlvarBer/Whitewater], the organization of the code follows
the feature branch workflow [@featworkflow], it can be described in terms of
its branches.

Master branch.

:   The master is the main branch, meaning that it is the default on the remote
    web interface, and the only branch where deployments happen, there is no
    actual development apart from hotfixes, insetead it merges commits from
    dev, forming a release on each merge.

Dev branch.

:   The dev branch represents the most recent commits, commits are made usually
    direct to this branch. Test are run when commits from this branch are pushed
    to the repo, but not deployment.

Feature-specific branches

:   Sometimes feature specific branches are done in order to test whether the
    feature is feasible or not. This branches are usually short lived, and
    if it is decides to merge that code it must be to dev.

Continuous Integration runs on travis CI, more on that on the Appendix How was
this document made?

[https://github.com/AlvarBer/Whitewater]: https://github.com/AlvarBer/Whitewater
[https://trello.com/b/JmG3xy0U/whitewater]: https://trello.com/b/JmG3xy0U/whitewater
[^kaggle]: [Kaggle.com](https://www.kaggle.com/)
[^trello]: trello is a software for having a digital board where tracks can be

