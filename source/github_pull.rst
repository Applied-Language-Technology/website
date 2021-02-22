Retrieve learning materials from GitHub
=======================================
.. image:: https://img.shields.io/badge/watch-youtube-red.svg
   :target: https://youtu.be/uukaUqOLRr4

|

The learning materials and exercises for this course are hosted on `GitHub <https://www.github.com>`_. 

GitHub is a service that allows hosting code for programs and various other file types, which are organised into *repositories*. The name of the service alludes to the underlying program, `Git <https://en.wikipedia.org/wiki/Git>`_, which keeps track of any modifications to the files and retains a history of changes made to previous versions of the file. Git is responsible for *version control*: GitHub enables multiple people to collaborate on the same repository, while Git keeps track of the changes made.

To retrieve learning materials and exercises from GitHub, navigate to the main view in JupyterLab and follow the instructions below.

1. Click the Terminal button to launch a terminal.

   |

   .. image:: ../img/jl_launch_terminal.gif
      :width: 400
      :alt: Click the "Terminal" button.

   |

2. Terminal opens a command line interface. We will use the command line interface to establish a connection to GitHub.

   |

   .. image:: ../img/jl_terminal_idle.gif
      :width: 600
      :alt: A view of the command line interface.

   |

3. Navigate to the repository on GitHub in another browser window and copy the address of the repository from the top-right hand corner.

   |

   .. image:: ../img/gh_copy_https.gif
      :width: 350
      :alt: Copying the address of a repository from GitHub.

   |

4. Change back to Terminal in JupyterLab and type the following command:

   .. code-block:: console

      git clone <address of the GitHub repository>

   You can paste the address of the GitHub repository into the command line by pressing *Control* and *v* at the  same time. Then press *Enter* to execute the command. 

   |

   GitHub will prompt you for your username and password.

   |

   .. image:: ../img/gh_clone_repo.gif
      :width: 600
      :alt: Cloning a repository from GitHub.

   |

   Cloning the repository creates a local copy of the repository on your server. You should now see a directory named after the repository in the File Browser on the left-hand side of the main view in JupyterLab.

   .. warning::

      Cloning a repository establishes a connection between the local repository on your server and the remote repository on GitHub.

      |

      To incorporate any changes to the remote repository to your local repository, you do not need to clone the repository again. You can use the command below to apply the changes to your local repository:

      .. code-block:: console

         git pull

   |

5. When you have completed an exercise, you must `return the exercise to GitHub for grading <github_push.rst>`_.
