Retrieve learning materials from GitHub
=======================================

The learning materials and exercises are hosted on GitHub. The content on GitHub is organised into *repositories*, which can contain code and other file types, while also keeping track on any modifications made to them.

To retrieve learning materials and exercises from GitHub, navigate to the main view in JupyterLab and follow the instructions below.

1. Click the Terminal button to launch a terminal.

   |

   .. image:: ../img/jl_launch_terminal.gif
      :width: 400
      :alt: Click the "Terminal" button.

   |

2. Terminal opens a command line interface that can be used to establish a connection to GitHub.

3. Navigate to the course repository on GitHub in another browser window. To access GitHub using the command line, we must copy the address of the repository, which can be found in the top-right hand corner.

4. Change back to the Terminal in JupyterLab. Type the command below and press **Enter** to *clone* the repository from GitHub.

   ``git clone``

   GitHub will prompt you for your username and password.

5. Cloning the repository creates a local copy on your personal server. If the repository was cloned successfully, you should now see a directory with the same name as the repository in JupyterLab.