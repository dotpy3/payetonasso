# payetonasso
A WebService to allow UTC students to ask them for payments to UTC student clubs.

## Installation
1. Execute `pip install -r requirements.txt` to update dependencies.
2. Set up your own local settings (see "Local Settings").
3. Migrate your database with `python manage.py migrate`. If this command fails to work, make sure your database settings are correct.
4. Launch the server with `python manage.py runserver`.

### Local Settings
To add local settings to _Paye ton asso!_, add a `payemoi/local_settings.py` file. The new settings will override the old ones.
These are the settings that are mandatory for _Paye ton asso!_ to work:
* Database settings
