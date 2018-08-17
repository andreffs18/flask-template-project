# Default Empty Flask Template

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dc41f3a0b9a1474caf15043e270ef497)](https://www.codacy.com/app/andreffs18/flask-template-project?utm_source=github.com&utm_medium=referral&utm_content=andreffs18/flask-template-project&utm_campaign=badger)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/dc41f3a0b9a1474caf15043e270ef497)](https://www.codacy.com/app/andreffs18/flask-template-project?utm_source=github.com&utm_medium=referral&utm_content=andreffs18/flask-template-project&utm_campaign=Badge_Coverage)


This is ready-to-go, empty, bootstrapped, **Flask** project with some neat features like, Python3.6, Blueprint Structure, RESTfull api, LoginManager, Tests and Basic Admin CMS. 

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Credits](#credits)
* [License](#license)
* [Wiki and FAQ's](#wiki-and-faqs)


## Installation

First you need to create an Environment file. To do so, inside the projects root folder create a file named **.env** with the following _key-value_ table:
```python
APP_ENV=localhost
SECRET_KEY=<SECRET_KEY>
MONGO_DB=your_db_nam
MONGO_DB_TEST=your_test_db_name
```

> **Note:** To generate a fresh **SECRET_KEY** you can select any key from this website: [http://randomkeygen.com/](http://randomkeygen.com/)

Now that you have a **.env** file, you need to create a **virtual environment** in your local machine and install the **requirements.txt** file that exists in the project's root folder. To do so, you need to:
```shell
$ mkvirtualenv <venv>
[<venv>] $ pip install -r requirements.txt
```


## Usage

You have a list of available commands in the project manager. To run this project locally, you will use **runserver**. (To know more about all the commands available you can do ```$ python manage.py``` or consult the wiki page about [Commands](#)).

```shell
[<venv>] $ python manage.py runserver
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 123-456-789
```


#### Flake8 configuration
Some custom properties were set when configuring Flake8 to validate if the codebase is PEP8 complain.

A new configuration file **"flake8"** was created on `~/.config/` folder.

> You can find more following Flake8's documentation: http://flake8.pycqa.org/en/latest/user/configuration.html#user-configuration
```
[flake8]
max-line-length = 120
ignore = E704  # Multiple statements on one line
```

## Contributing

We deeply appreciate if you want to contribute to this project. To do so, please follow [these](contributing.md) guidelines.


## Credits

This project could not have been done without the help of everyone involved. A **HUGE** thanks to [@johnsardine](https://github.com/johnsardine) :satisfied:

Some resources that you can use to understand better this project:
- [Discover Flask, by Michael Herman](https://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&feature=share)
- [Flask by example - Project Setup](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)
- [Microservices with Python and Flask - PyCon 2017](https://www.youtube.com/watch?v=nrzLdMWTRMM)

If you have suggestions/bugs/requests feel free to send me a message.


## License

[MIT License Copyright (c)](/LICENCE.md) 2018 andreffs18


## Wiki and FAQ's

We try to keep our wiki up-to-date as best as we can, so if you have any questions, please use it! If you don't find anything regarding what you are looking for, then create an issue and we will look at it as soon as possible. :+1:



Fork, clone, share! 
