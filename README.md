# **LICENSE** #

Author: ArenGamerZ <arendevel@gmail.com>

This project is licensed over the GNU GPLv3 license.  
Copyright (C) 2017 ArenGamerZ


Brief license summary: It's a copyleft license so you may copy, modify and redistribute the code but the derived work MUST be licensed the same way as the original.
                       In addition you MUST reproduce the above copyright notice in all the files of the derived work and if the derived work has a user interface,
                       when this user interface enters in interactive mode, it MUST reproduce the same copyright notice.
                       For further information of what are you allowed and what you are not allowed to do, read the full LICENSE file.


# **DESCRIPTION** #

It's a tool that calculates the number of hosts, number of subnets, the network address, the broadcast address from the given IP and MASK. It will also works with files, you can save the results
directly into files or load several IP/MASK from a file.


# **REQUIREMENTS** #

* Python 3.6.1 or greater
* Colorama 0.3.9 or greater (You can install it with 'pip install colorama')


# **DOCUMENTATION** #

* **subnetc.py** - This is the file meant to be executed.
* **example_file.txt** - This is an example file containing to IP/MASK addresses, to show how to load IP/MASK pairs from a file.
* ***Modules:***
    * **modules/bin_converter.py**  - This is a Library from my other project called binary_converter, you can see the full project here: https://ArenGamerZ@bitbucket.org/ArenGamerZ/binary_converter.git
    * **modules/colors.py**         - This is a free licensed file since I took the idea from stackoverflow: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    * **modules/interface.py**      - This is the module that defines how data is represented to the user.
    * **modules/subnetting.py**     - This is the module that makes all the "magic" and computation to get the things we asked it to calculate.