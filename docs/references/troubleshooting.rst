.. _troubleshooting:

===============
Troubleshooting
===============

Installation
------------

Python package "pygraphviz"
###########################

The installation of pygraphviz can cause errors.
You can circumvent this issue by setting the :code:`simulation_setting`, :code:`plot_nx_graph` to :code:`False`.
If you need to plot the network graphs (set parameter :code:`plot_nx_graph` to :code:`True`) or run all pytests,
check if we already have a solution for your OS/distribution:

**Ubuntu 18.4**:
Pygraphviz could not be installed with pip. Solution:

    sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config

    pip install pygraphviz

**Windows 10**
Installing via

   pip install -r requirements.txt

results in an error:

    error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/

You can find fixes on `stackoverflow <https://stackoverflow.com/questions/40809758/howto-install-pygraphviz-on-windows-10-64bit>`__
If you have :code:`conda` installed, activate your environment and run

    conda install -c alubbock graphviz pygraphviz

Then you need to configure the :code:`dot` command on your computer to be able to use graphviz

    dot -c

Python package "xlrd"
#####################

On **Windows** there can be issues installing xlrd. This could solve your troubles:

1. Delete :code:`xlrd` from requirements.txt
2. Download the :code:`xlrd-1.2.0-py2.py3-none-any.whl` file from `here <https://pypi.org/project/xlrd/#files>`__.
3. Copy the file to main directory of the project on your laptop
4. Install it manually writing :code:`pip install xlrd-1.2.0-py2.py3-none-any.whl`

Python package "wkhtmltopdf"
############################

There can be issues installing :code:`wkhtmltopdf`. Solution can be found on the `packages documentation <https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf>`__.

cbc-solver
##########

While with Ubuntu the installation of the cbc solver should work rather well, even when adding it to the environment variables (like described in the installation instructions) can sometimes not work on Windows. This was experienced with Windows 10.

A workaround is to directly put the :code:`cbc.exe` file into the root of the MVS repository, ie. in the same folder where also the :code:`CHANGELOG.md` file is located. Python/Oemof/Pyomo then are able to find the solver.

pyppeteer
##########

If you are using OS X, you might need to install this package separately with :code:`conda` using:

    `conda install -c conda-forge pyppeteer`

or

    `conda install -c conda-forge/label/cf202003 pyppeteer`

More information is available on `their website <https://anaconda.org/conda-forge/pyppeteer>`__.

Error messages and MVS termination
----------------------------------

Even though we try to keep the error messages of the MVS clear and concise, there might be a some that are harder to understand.
This especially applies to error messages that occur due to the termination of the oemof optimization process.

json.decoder.JSONDecodeError
############################

If the error :code:`json.decoder.JSONDecodeError` is raised, there is a formatting issue with the json file that is used as an input file.

Have you changed the json file manually? Please check for correct formatting, ie. apostrophes, commas, brackets, and so on.

If you have not changed the Json file yourself please consider raising an issue in the github project.

