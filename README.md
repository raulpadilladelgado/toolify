# Welcome to
![toolify.png](source_code/infrastructure/static3/images/toolify.png)

Toolify it's an web application written at python
using the web framework flask and the spotify api wrapper 
library spotipy.

Using it, you can manage your playlist with several features
that you can't get from the official spotify client
# Setup local environment
1. Install dependencies
```shell
pip install -r requirements.txt
```
2. Create your own .env file by copying the .env-sample file, and fill it with the required environment variables:
- TOOLIFY_SECRET_KEY
- SPOTIFY_REDIRECT_URI
- SPOTIFY_CLIENT_SECRET
- SPOTIFY_CLIENT_ID
- FLASK_APP (you must keep the provided value at the sample file)
3. Now, you can launch the server with:
```shell
flask run
```

# Other tips for development
To launch the test suite you must be placed at the root directory of the project and execute:
```shell
python3 -m unittest
```

To launch gunicorn (our WSGI HTTP server), you must be placed at the root directory of the project and execute:
```shell
gunicorn --bind 0.0.0.0:5000 source_code.infrastructure.app:app
```

