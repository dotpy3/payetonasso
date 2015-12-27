# payetonasso
A WebService to allow UTC students to ask them for payments to UTC student clubs.

## Installation
1. Execute `pip install -r requirements.txt` to update dependencies.
2. Set up your own local settings (see "Local Settings"). We advise you to create a `local_settings.py` file - it will automatically override any setting defined in `settings.py`.
3. Migrate your database with `python manage.py migrate`. If this command fails to work, make sure your database settings are correct.
4. If you don't have Bower yet, [install it](http://bower.io/) on your own machine. Go to `payetonasso/static`, then run `bower install`.
5. Launch the server with `python manage.py runserver`.

### Local Settings
To add local settings to _Paye ton asso!_, add a `payemoi/local_settings.py` file. The new settings will override the old ones.
These are the settings that are mandatory for _Paye ton asso!_ to work:
* Database settings
* A Nemopay API key disposing of `WEBSALE` rights on all fundations
* If you want to use Ginger as a user authentification system, a [Ginger API Key](https://github.com/simde-utc).
* E-mail parameters (all the parameters at the end of `settings.py` that are prefixed by `EMAIL`).
* A default sender email, `DEFAULT_FROM_EMAIL`. Recommended format recognized and interpreted by e-mail clients : `Name <mailadress@provider.org>`.