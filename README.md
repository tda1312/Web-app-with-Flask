# Web-app-with-Flask

_My attempt to build a simple Flask web application **from scartch**_

### Tools

* OS: Ubuntu
* Framework: Flask
* Python3
* Jinja
* SQLAlchemy
* SQLite

### Run
* Open terminal
* Navigate to the application directory
* Python version later than 3.4 is required, as virtual environments are supported natively.
  + <code>python3 -m venv venv</code>
  * In case you dont have one, you can consider installing a third-party tool called virtualenv, then create virtual environment via virtualenv
    + <code>virtualenv venv</code>
* Activate virtual environment
  + <code>source venv/bin/activate</code>
* Install flask
  + <code>pip install flask</code>
* Install python-dotenv package. Although I've already registered environment variables for flask in the .flaskenv file, the aforementioned package is required to use this option
  + <code>pip install python-dotenv</code>
* Run
  + <code>flask run</code>
    + Just in case, if you still encounter flask environment variables error, try
      <code>export FLASK_APP=microblog.py</code>
* If the terminal returns a missing module name, you should <code>pip install module_name</code> to install that module, then <code>flask run</code> again. I'll make a list of required module at your disposal so you can install all at once for convenience when I have time later.
* Open web browser and access site of your IP address
* Explore the app and enjoy!
