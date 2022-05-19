# gig-scraper

This app scrapes gig venue websites for upcoming events and finds the artist playing at the event. It then takes this artists top song, using the spotify api, and puts it in a specified playlist.

##Before Running

1. Change "user_id" in global variables to your account
2. Setup spotify developer account
3. Setup SpotifyOAuth - https://spotipy.readthedocs.io/en/2.19.0/#authorization-code-flow
4. Add venue websites to website-urls.json and decide best scraping method 
