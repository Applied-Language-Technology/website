**************************
Frequently Asked Questions
**************************

**Question:** When I attempt to test my exercises using :ref:`TMC <tmc_usage>` by entering the command :code:`tmc test`, I receive an error that says "Error in plugin". What should I do?

**Answer:** This means that your code causes the Jupyter Notebook that contains the exercise to crash. Before running the command :code:`tmc test`, make sure you can run all the cells in the notebook without crashing the notebook. Note that this does not cover errors raised by your code.

**Question:** When I submit my exercises to the :ref:`TMC <tmc_usage>` server, the submission takes a long time and finishes with an error. What should I do?

**Answer:** This probably means that your code has an infinite :code:`for` loop or another problem, which causes the TMC server to terminate the submission. All exercises should run within a reasonable amount of time.

**Question:** When I submit my exercises to the :ref:`TMC <tmc_usage>` server, the server raises the error :code:`413 Payload Too Large`.

**Answer:** The size of submissions to the TMC server is limited to 30 megabytes. Make sure your Jupyter Notebook does not contain excessive output e.g. for debugging purposes, and that you have not placed big files (e.g. language models) into the exercise directory.