import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    mask = (views["author_id"] == views["viewer_id"])
    return views[mask][["author_id"]].drop_duplicates().sort_values(by="author_id").rename(columns={ "author_id" : "id"})
    
