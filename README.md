# Welcome to
![toolify.png](static/images/toolify.png)

Toolify it's an web application written at python
using the web framework flask and the spotify api wrapper 
library spotipy.

Using it, you can manage your playlist with several features
that you can't get from the official spotify client
# Setup local environment
1. Install dependencies
```shell
make install
```
2. Fill .env file with the required environment variables:
- TOOLIFY_SECRET_KEY
- SPOTIFY_REDIRECT_URI
- SPOTIFY_CLIENT_SECRET
- SPOTIFY_CLIENT_ID
- FLASK_APP (you must keep the provided value)
3. Now, you can launch the server with:
```shell
make run
```

# Other tips for development
To launch the test suite you must be placed at the root directory of the project and execute:
```shell
make test
```

To launch gunicorn (our WSGI HTTP server), you must be placed at the root directory of the project and execute:
```shell
make run-with-gunicorn
```

