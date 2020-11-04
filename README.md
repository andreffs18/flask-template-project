# Default Empty Flask Template

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dc41f3a0b9a1474caf15043e270ef497)](https://www.codacy.com/app/andreffs18/flask-template-project?utm_source=github.com&utm_medium=referral&utm_content=andreffs18/flask-template-project&utm_campaign=badger)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/dc41f3a0b9a1474caf15043e270ef497)](https://www.codacy.com/app/andreffs18/flask-template-project?utm_source=github.com&utm_medium=referral&utm_content=andreffs18/flask-template-project&utm_campaign=Badge_Coverage)


This is ready-to-go, bootstrapped **Flask 1.0** project with some neat features like, Python3.6, Blueprint Structure, RESTfull api, Login & User Management, Basic Admin CMS with Basic Auth with a complete test suit! 

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
SECRET_KEY=KeepThisS3cr3t
SQLALCHEMY_DATABASE_URI=postgresql://localhost/database
BASIC_AUTH_USERNAME=me
BASIC_AUTH_PASSWORD=me
```

> **Note:** To generate a fresh **SECRET_KEY** you can select any key from this website: [http://randomkeygen.com/](http://randomkeygen.com/)

This project uses [**Pipenv**](https://pipenv.readthedocs.io/en/latest/) to install and manage all it's dependencies. So you just need to simply run:

```shell
$ pipenv install
(flask-template-project-Ad2ZDIA5) $ pipenv shell
```

And your virtual environment will be configured! 

## Usage

You have a list of available commands in the project manager. To run this project locally, you will use **runserver**. (To know more about all the commands available you can do ```$ python manage.py``` or consult the wiki page about [Commands](#)).

```shell
(flask-template-project-Ad2ZDIA5) $ python manage.py runserver
 * Serving Flask app "project" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 859-626-128
```


#### Flake8 configuration
Some custom properties were set when configuring Flake8 to validate if the codebase is PEP8 complain.

A new configuration file **"flake8"** was created on `~/.config/` folder.

> You can find more following [Flake8's documentation](http://flake8.pycqa.org/en/latest/user/configuration.html#user-configuration).
```
[flake8]
max-line-length = 120
ignore = E704  # Multiple statements on one line
```

## Contributing

We deeply appreciate if you want to contribute to this project. To do so, please follow [these](CONTRIBUTING.md) guidelines.


## Credits

This project could not have been done without the help of everyone involved. A **HUGE** thanks to [@johnsardine](https://github.com/johnsardine) :thumbsup:

Some resources that you can use to understand better this project:
- [Discover Flask, by Michael Herman](https://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&feature=share)
- [Flask by example - Project Setup](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)
- [Microservices with Python and Flask - PyCon 2017](https://www.youtube.com/watch?v=nrzLdMWTRMM)


## License

[MIT License Copyright (c)](/LICENSE.md) 2018 andreffs18


## Wiki and FAQ's

We try to keep our wiki up-to-date as best as we can, so if you have any questions, please use it! 
If you don't find anything regarding what you are looking for or if you have any suggestions, then create an issue and we will look at it as soon as possible. :+1:



Fork, clone, share! 
