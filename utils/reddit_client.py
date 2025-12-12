# utils/reddit_client.py

```python
import praw

def get_reddit(config):
    return praw.Reddit(
        client_id=config["client_id"],
        client_secret=config["client_secret"],
        username=config["username"],
        password=config["password"],
        user_agent=config["user_agent"],
    )
```
