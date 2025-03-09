# ElonaPlusGXDownload for Windows

Quick script to download and setup Elona+GX on Windows installs.

Please visit **[Ruin0x11](https://github.com/Ruin0x11/ElonaPlusCustom-GX)**'s repo as they are the ones to thank.

# How to Install:

(Make sure you have **_Python3.10_** or higher prior)

Just go to the _dist_ folder and download the package.

Go to the folder you downloaded the package to and install it with the following command.

## Installation:
```
pip install elonal
```
## Install stragiht from .whl or tar.gz packages
```
pip install elonadl-<VERSION>-py3-none-any.whl
```

or

```
py -m pip install elonadl-<VERSION>-py3-none-any.whl
```

To run the module just run the following command. _**Whenever there is a new update for Custom-GX simply rerun this command and it'll update your installation.**_

```
py -m elonadl
```

The game will be setup in your **%APPDATA%** folder.
The script will inform you of the steps in the command line.

# How to Remove Package.

This won't impact the Elona+CGX setup, just remove the elonadl package from your computer.

```
pip uninstall elonadl
```

or

```
py -m pip uninstall elonadl
```

# In case there are new releases:

If you see a newer release to a newer version of Elona+ just rerun `py -m elonadl` it'll automatically create a new install for the latest version and not touch your older install.

# To Create a new Build

```
py setup.py bdist_wheel
```

_Make sure in have `wheel` package installed on your system prior to building_
Make sure to alter the attributes in **setup.py**
