# Setup
1. Install SpotyPy
```shell
pip install spotipy
pip install flask
```
2. Create your own credentials file (`credentials.py`)
```Python
class Credentials:
    SPOTIFY_CLIENT_SECRET = "your spotify client secret"

    SPOTIFY_CLIENT_ID = "your spotify client id"

    SPOTIFY_REDIRECT_URI = "your spotify app redirect uri"
```
3. Now, you are ready. To run the app execute the file `main.py`

