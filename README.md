# Default Empty Flask Template

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dc41f3a0b9a1474caf15043e270ef497)](https://www.codacy.com/app/andreffs18/flask-template-project?utm_source=github.com&utm_medium=referral&utm_content=andreffs18/flask-template-project&utm_campaign=badger)

This is ready-to-go, empty, bootstrapped, **Flask** project with some neat features like, Blueprint Structure, RESTfull api, LoginManager, Tests and Basic Admin CMS. 

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Credits](#credits)
* [License](#license)
<!--* [Wiki and FAQ's](#wiki-and-faqs)-->


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

You have a list of available commands in the project manager. To run this project locally, you will use **runserver**. (To know more about all the commands available you can do ```shell % python manage.py``` or consult the wiki page about [Commands](#)).

```shell
[<venv>] $ python manage.py runserver
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 281-707-369
```

### Creating an admin user

```shell
$ python manage.py shell
>>> import project.user.models as umodels
>>> umodels.User.create('admin', 'youradminpass', True)
<User: admin>
>>> admin = umodels.User.objects.filter(username='admin').first()
>>> admin.is_admin = True
>>> admin.save()
<User: admin>
```

## Contributing

We deeply appreciate if you want to contribute to this project. To do so, please follow [these](#) guidelines.


## Credits

This project could not have been done without the help of everyone @ **the internet**. :satisfied:
- [Base tutorial (~5hours)](https://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&feature=share)
- [Create a flask project by example](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)

If you have sugestions/bugs/requests feel free to PM me @andreffs18


## License

MIT License Copyright (c) 
2017 andreffs18

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<!--## Wiki and FAQ's

We try to keep our wiki uptodate as best as we can, so if you have any questions/problems please use it! If you don't find any solution, create an issue and we will look @ it as soon as we can.-->



Fork, clone, share! 
