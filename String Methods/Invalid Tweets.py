import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    results = tweets[tweets['content'].str.len() > 15]['tweet_id']
    results_df = pd.DataFrame(results)
    return results_df
