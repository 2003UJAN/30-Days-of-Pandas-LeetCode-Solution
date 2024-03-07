import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id matches viewer_id
    filtered_views = views[views['author_id'] == views['viewer_id']]
    
    # Extract unique author_ids
    unique_ids = filtered_views['author_id'].drop_duplicates().sort_values().rename('id')
    
    # Convert the Series to a DataFrame
    result_df = pd.DataFrame(unique_ids)
    
    return result_df
