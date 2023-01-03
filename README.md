# AireLogicFrontEnd

This is a bug tracking application made using:
<ul>
<li>Flask</li>
<li>SQL Alchemy</li>
<li>Blinker</li>
<li>Pytest</li>
<li>Flask Testing</li>
<li>Bootstrap</li>
</ul>

It can be used to create and edit users, tickets and allows you to assign and reassign people to tickets.

<h1>An Overview of How it works</h1>
<ul>
<li>App.py is the main entrypoint for the app</li>
<li>Routes.py is where the main logic for the app is, it serves as the API and facitates the rendering of pages and the updating of the database</li>
<li>Core_Model.py is where the database schemas are defined.</li>
<li>All HTML files are located in the templates folder, HTML files use Jinja2 which is provided by Flask and allows us to dynamically render content</li>
<li>All CSS and Images are located in the static folder</li>
</ul>

<h1>Known bugs / issues</h1>
<ul>
<li>Currently tests pass when run individually but fail when run as a group</li>
</ul>
