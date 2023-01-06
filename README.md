# AireLogicBugTracker

This is a bug tracking application made using:
<ul>
<li>Flask</li>
<li>Flask_SQLAlchemy</li>
<li>Pytest</li>
<li>Blinker</li>
<li>Flask_Testing</li>
<li>Bootstrap</li>
</ul>

It can be used to create, edit and delete members and tickets and allows you to assign and reassign members to tickets.

<h1>An Overview of How it works</h1>
<ul>
<li>App.py is the main entrypoint for the app</li>
<li>Routes.py is where the main logic for the app is, it serves as the API and facitates the rendering of pages and the updating of the database</li>
<li>Core_Model.py is where the database schemas are defined.</li>
<li>All HTML files are located in the templates folder, HTML files use Jinja2 which is provided by Flask and allows us to dynamically render content</li>
<li>All CSS files and Images are located in the static folder</li>
</ul>

<h1>Installing the bug tracker</h1>
<h2>Prerequisites</h2>
<ul>
<li>Ensure that python is downloaded from https://www.python.org/downloads/</li>
<li>Ensure that Visual Studio Code or PyCharm is installed</li>
<li>If using VS Code ensure that the Python extension is downloaded from the extension tab, even if you have python installed from the above link</li>
</ul>

<h2>Installation</h2>
<ul>
<li>Clone the repo into an empty folder</li>
<li>Open the folder in your chosen IDE</li>
<li>Open a new terminal / CMD within this folder and run the following commands</li>
<li>Initialise and activate virtual environment</li>
<li>Linux</li>

```
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate
```

<li>Mac</li>

```
python3 -m venv .venv
source .venv/bin/activate
```
 
<li>Windows</li>
  
```
  py -3 -m venv .venv
  .\.venv\Scripts\activate
```

<li>You can tell if the virtual environment is activated as you will see the text (.venv) at the start of the current and subsequent cmd / terminal lines</li>
<li>Once the virutal environment is activated Install Required packages</li>

```
pip install flask
pip install flask_sqlalchemy
pip install flask_testing
pip install pytest
pip install blinker
```

</ul>

<h1>Running the program</h1>
<ul>
<li>Start the application by typing the following into your terminal / cmd with the virtual environment activated</li>

```flask run```

<li>Alternatively if using VS code you can click the run and debug side menu, followed by pressing the start debugging button (Represented by a green play button)</li>
<li>Connect to the server the app is running on by clicking the link printed by the terminal, by default this should be http://127.0.0.1:5000/</li>
<li>To stop the application press CTRL + C in the terminal</li>
</ul>

<h1>Running tests</h1>
<ul>
<li>Tests can be ran by typing pytest into the terminal with the virtual environment activated</li>

```pytest```

<li>There is currently an issue with running tests this way, however each test functions correctly when ran individually</li>
<li>For Example</li>

```pytest .\bug_tracker\tests\routes_test.py::Routes_Tests::test_home_page_get```

<li>Where test_home_page_get is the name of the test you would like to run</li>

</ul>

<h1>Known bugs / issues</h1>
<ul>
<li>Currently tests pass when run individually but fail when run as a group</li>
<li>If you assign a user to a ticket and edit or delete the user, the name on the ticket does not automatically update</li>
</ul>
