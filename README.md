# Spotify Data Project

## Skills

- Python
- Spotipy (API)
- Kedro (Open-source framework for project structure)

## Spotipy Authentication

### Client Credentials Flow

- Only endpoints that **do not access user information** can be accessed.

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
```
### Authorization Code Flow

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```