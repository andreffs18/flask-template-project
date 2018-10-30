All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).


## [0.2.1](https://github.com/andreffs18/flask-template-project/releases/tag/v0.2.1) - 2018-10-30

### Added
* User Management using RBAC (Role Base Access Control) [[!18](https://github.com/andreffs18/flask-template-project/pull/18)]

### Security
* Update **requests** version to 2.20.0 


## [0.2.0](https://github.com/andreffs18/flask-template-project/releases/tag/v0.2.0) - 2018-10-14

### Added
* Basic Admin CMS with **Flask-Admin** [[!14](https://github.com/andreffs18/flask-template-project/pull/14)]
* Basic Auth on Admin pages using **Flask-Basic-Auth** [[!14](https://github.com/andreffs18/flask-template-project/pull/14)]

### Changed
* Replaced **requirements.txt** with **[Pipfile](https://pipenv.readthedocs.io)** to manage project dependencies. [[!16](https://github.com/andreffs18/flask-template-project/pull/16)]

### Security
* Update Flask requirement to 1.0.2 [[!16](https://github.com/andreffs18/flask-template-project/pull/16)]

## [0.1.0](https://github.com/andreffs18/flask-template-project/releases/tag/v0.1.0) - 2018-09-09

### Added
* Flake8 to be PEP8 complaint.  
* SQLAlchemy integration.
* Flask-Restfull API V1 for GET User list

### Changed
* **User** app to follow Single Responsibility Principle.

### Removed
* Support for **MongoEngine**

### Security

* Api Key generation now uses python [secrets](https://docs.python.org/3/library/secrets.html) module instead of random.

## [0.0.1](https://github.com/andreffs18/flask-template-project/releases/tag/v0.0.1) - 2017-02-05

* Initial working version


<!--
### Added for new features.
### Changed for changes in existing functionality.
### Deprecated for soon-to-be removed features.
### Removed for now removed features.
### Fixed for any bug fixes.
### Security in case of vulnerabilities.
-->
