***************
Getting Started
***************

.. note::
   The following information is mainly intended for students enrolled at the University of Helsinki. 

   Other users can explore the learning materials and use them interactively on `Binder <https://mybinder.org/>`_

Introducing the learning environments
=====================================

An overview
-----------

The courses use several learning environments, which are directly accessible through your web browser:

1. **GitHub** and **GitHub Classroom**. The course materials and exercises are hosted on GitHub, a service for storing code, documentation and other materials. GitHub Classroom is used to manage the exercises.

2. **CSC Notebooks** is a service provided by CSC, a Finnish non-profit state enterprise that serves Finnish institutions of higher education. CSC Notebooks host the interactive learning materials, which are based on **Jupyter**. We use the Python programming language on Jupyter.

The following diagram provides an overview of the environments and services used.

.. image:: ../img/environment_overview.svg
  :width: 600
  :alt: An overview of the environments and services used.

How to use the learning environments in practice?
-------------------------------------------------

1. :ref:`Access CSC Notebooks<CSCNotebooks>` and :ref:`launch your personal server<CSCNotebooksServer>`.
2. Retrieve learning materials or exercises from GitHub.
3. Interact with the learning materials and complete exercises on Jupyter.
4. Return the exercises to GitHub for grading.

.. _CSCNotebooks:

Accessing CSC Notebooks
=======================

1. Open `CSC Notebooks <https://notebooks.csc.fi/>`_ on your web browser.

2. Choose **Haka** as your login method.
   
   .. image:: ../img/csc_nb_login_method.gif
      :width: 500
      :alt: Click the "Haka Login" button.

3. Choose your university from the drop-down menu and click **Select**.

   .. image:: ../img/csc_nb_haka_affiliation.gif
      :width: 400
      :alt: Choose your university from the drop-down menu and click select.

4. Enter your *university username and password* and click **Login**.

   .. image:: ../img/csc_nb_haka_login.gif
      :width: 300
      :alt: Enter your credentials and click Login.

5. If prompted, click **Accept** to forward your login to CSC Notebooks.
   
   If the login was successful, you should see the environments available on CSC Notebooks.

.. warning::

   If you cannot find an environment named *Applied Language Technology* on the landing page, this means that you are not a member of the course group on CSC Notebooks.

   To join the group, complete the following steps.

   1. Click the *Account* button on the top of the page.

   2. Click the *Join Group* button and enter the code you have received from the course organiser.

   You only need to complete these steps once. 

   The next time you log in you should see the course environment among the available environments.


.. _CSCNotebooksServer:

Launching a server on CSC Notebooks
===================================

1. Click the *Launch new* button once to launch your personal server on CSC Notebooks.

   .. image:: ../img/csc_nb_launch_env.gif
      :width: 400
      :alt: Click the "Launch new" button.

2. When the server has been launched successfully, you will see a link in the *Access* column. 

   Click the *Open in browser* link.

   .. image:: ../img/csc_nb_open_env.gif
      :width: 400
      :alt: Click the "Open in browser" link.

3. This opens a window with a password, which is automatically copied on your clipboard.
   
   Click the *Click to copy password & proceed* button.

   .. image:: ../img/csc_nb_copy_pw.gif
      :width: 400
      :alt: Click the "Click to copy password & proceed" button.

4. This opens a new window with a password prompt.
 
   Paste the password on the clipboard into the box and click the *Log in* button. 

   .. image:: ../img/csc_nb_enter_pw.gif
      :width: 400
      :alt: Paste the password on the clipboard into the box.

   

Launching Jupyter
=================

We will use [Jupyter notebooks](https://jupyter.org/) for both teaching materials and assignments during this course. Notebooks, such as the one you're looking at right now, run in a web browser. In addition of being able to render all sorts of text, images, graphs and interactive widgets, the notebooks allow writing and executing code.

The notebooks are used on a server provided by [CSC – the IT Centre for Science](https://www.csc.fi), which is owned by the government of Finland and Finnish universities. CSC is responsible for providing all kinds of infrastructure and services for scientific computing. These services are free to students and staff at Finnish universities.

We will use [the discussion forum on Github](https://github.com/orgs/uh-eng-3041-2019/teams/students/discussions) for all kinds of discussions and questions about the course, natural language processing and programming in Python. Note that *I will not respond to individual e-mails asking for help*, unless they are about problems with accessing the course environment. All kinds of activity – whether asking questions or answering them – counts towards your final grade. Share your knowledge!
