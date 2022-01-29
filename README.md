# Welcome to
![toolify.png](static/toolify.png)

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
2. Create your own .env file, and fill it with the required environment variables:
- TOOLIFY_SECRET_KEY
- SPOTIFY_REDIRECT_URI
- SPOTIFY_CLIENT_SECRET
- SPOTIFY_CLIENT_ID
3. Now, you can launch the server with:
```shell
flask run
```

