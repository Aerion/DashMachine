# DashMachine
### Another web application bookmark dashboard, with fun features.

![screenshot](https://i.ibb.co/chbBkzk/2020-02-02-09-46.png)

![screenshot](https://i.ibb.co/HXbfhnp/2020-02-02-09-47.png)

### Features
* creates a dashboard to view web pages
* uses a single .ini file for configuration
* dark mode/light mode and accent colors
* custom backgrounds and icons
* web interface to edit the config file and add image files
* ability to open web pages in current tab, new tab or iframe
* hideable sidebar with dragable reveal button
* user login system
* 'app templates' which are sample config entries for popular self hosted apps
* ability to display rest api data on application cards

## Installation
### Docker
```
docker create \
  --name=dashmachine \
  -p 5000:5000 \
  -v path/to/data:/DashMachine/dashmachine/user_data \
  --restart unless-stopped \
  rmountjoy/dashmachine:latest
```

### Python
Instructions are for linux.
```
virtualenv DashMachineEnv
cd DashMachineEnv && source bin/activate
git clone https://git.wolf-house.net/ross/DashMachine.git
cd DashMachine && pip install -r requirements.txt
python3 run.py
```
Then open a web browser and go to localhost:5000

## Default user/password
```
User: admin
Password: adminadmin
```

## Configuration
The user data folder is located at DashMachine/dashmachine/user_data. This is where the config.ini, custom backgrounds/icons, and the database file live. A reference for what can go into the config.ini file can be found on the settings page of the dashmachine by clicking the info icon next to 'Config'. 

### Note
If you change the config.ini file, you either have to restart the container (or python script) or click the 'save' button in the config section of settings for the config to be applied. Pictures added to the backgrounds/icons folders are available immediately.

## Tech used
* Flask
* SQLalchemy w/ SQLite
* Jinja2
* Materialize css
* JavaScript/jQuery/jQueryUI
* Requests (python)