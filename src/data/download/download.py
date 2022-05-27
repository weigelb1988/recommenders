from utils.download_utils import maybe_download
import pandas as pd
COL_USER = "UserId"
COL_ITEM = "MovieId"
COL_RATING = "Rating"
COL_PREDICTION = "Rating"
COL_TIMESTAMP = "Timestamp"

def main(opt):
    filepath = maybe_download(opt.data_url, opt.data_path)
    data = pd.read_csv(filepath, sep="\t", names=[COL_USER, COL_ITEM, COL_RATING, COL_TIMESTAMP])
    print(data.head())
    print(data.describe())

    print(
    "Total number of ratings are\t{}".format(data.shape[0]),
    "Total number of users are\t{}".format(data[COL_USER].nunique()),
    "Total number of items are\t{}".format(data[COL_ITEM].nunique()),
    sep="\n"
)