Return exercises to GitHub
==========================

1. Move to the directory that contains the Git repository using the following command.

   .. code::
      
      cd <name of the directory>

   Git keeps track of modifications to the files in the directory. Use the following command to check if tracked files have been modified.

   .. code::

      git status

   .. image:: ../img/jl_git_status.gif
      :width: 600
      :alt: Change directory and check the status of git repository.
  
   |

2. Any files that have been modified must be *added* to a *commit* in preparation for adding these changes to the remote repository on GitHub. Use the following command to add files to a commit:

   .. code::

      git add <filename or directory>

   |

   .. image:: ../img/jl_git_add.gif
      :width: 600
      :alt: Add files to a commit, which are then pushed to GitHub.

   |

3. When all the requested changes have been *staged* into a commit, you must verify the commit and add a message that describes the changes made using the following command:

   .. code::

      git commit -m "your message here"

   This will prepare the commit, which can now be *pushed* to the remote repository on GitHub using the following command:

   .. code::

      git push

   .. image:: ../img/jl_git_push.gif
      :width: 600
      :alt: Push a commit to GitHub.