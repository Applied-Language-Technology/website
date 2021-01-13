Retrieve learning materials from GitHub
=======================================

The learning materials and exercises are hosted on `GitHub <https://www.github.com>`_. The content on GitHub is organised into *repositories*, which can contain code and other file types, while also keeping track on any modifications made to them.

To retrieve learning materials and exercises from GitHub, navigate to the main view in JupyterLab and follow the instructions below.

1. Click the Terminal button to launch a terminal.

   |

   .. image:: ../img/jl_launch_terminal.gif
      :width: 400
      :alt: Click the "Terminal" button.

   |

2. Terminal opens a command line interface. We will use the command line to establish a connection to GitHub.

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

4. Change back to Terminal in JupyterLab and type the following command.

   .. code-block::

      git clone <address of the GitHub repository>

   You can paste the address of the GitHub repository into the command line by pressing *Control* and *v* at the  same time. Then press *Enter* to execute the command. 

   |

   GitHub will prompt you for your username and password.

   |

   .. image:: ../img/gh_clone_repo.gif
      :width: 600
      :alt: Cloning a repository from GitHub.

   |

   Cloning the repository creates a local copy of the repository on your server. You should now see a directory named after the repository in the File Browser on the left-hand side of JupyterLab.

   |

   When you have completed an exercise, you can `return the exercise to GitHub for grading <github_push.rst>`_.
