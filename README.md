# AirBnB clone - The console

## Background Context

![](./AirBnB.png)
*Welcome to the AirBnB clone project!*

_Before starting, please read the AirBnB concept page._

## Description of the Project
**First step:** Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

* Each task is linked and will help you to:
put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What's a command interpreter?
Do you remember the Shell? It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

## Description of the command interpreter:
A command interpreter, also known as a shell, is a program that provides a user interface for access to an operating system's services. It enables users to interact with the operating system by executing commands and providing input to the system. The shell provides a command-line interface that allows users to execute operating system commands, run scripts, and perform various other tasks.

to start the console `./console.py`

Example in Interractive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
```
Example in Non-Interractive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

## Authors
* **Adeyemo Raphael** - *Software Engineer* - [@cyber1ord](https://github.com/cyber1ord)

* **Esianyo Dzisenu** - *Software Engineer* - [@esianyo](https://github.com/esianyo)