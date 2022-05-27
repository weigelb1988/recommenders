import logging
import pandas as pd
from utils.constants import DEFAULT_ITEM_COL, DEFAULT_RATING_COL, DEFAULT_TIMESTAMP_COL, DEFAULT_USER_COL
from datetime import datetime, timedelta
logger = logging.getLogger(__name__)

try:
    from pyspark.sql import functions as F, Window
except ImportError:
    pass  # so the environment without spark doesn't break

from data.format.splitters.types.python_splitters import (
    python_random_split, 
    python_chrono_split, 
    python_stratified_split
)


def main(opt):
    
    data = pd.read_csv(opt.data_path, sep="\t", names=[DEFAULT_USER_COL, DEFAULT_ITEM_COL, DEFAULT_RATING_COL, DEFAULT_TIMESTAMP_COL])

    ## fix the time
    data[DEFAULT_TIMESTAMP_COL]= data.apply(
        lambda x: datetime.strftime(datetime(1970, 1, 1, 0, 0, 0) + timedelta(seconds=x[DEFAULT_TIMESTAMP_COL].item()), "%Y-%m-%d %H:%M:%S"), 
        axis=1
    )
    if opt.split_method == "random":
        data_train, data_test, data_val = python_random_split(data, ratio=opt.ratio)
    if opt.split_method == "chrono":
        # users/items do not appear across train/test/val
        data_train, data_test, data_val = python_chrono_split(
            data, ratio=opt.ratio, filter_by=opt.filter_by, min_rating=opt.min_samples, 
            col_user=DEFAULT_USER_COL, col_item=DEFAULT_ITEM_COL, col_timestamp=DEFAULT_TIMESTAMP_COL
        )
    if opt.split_method == "strat":
        # users/items in both train/test
        data_train, data_test, data_val = python_stratified_split(
            data, filter_by="user", min_rating=opt.min_samples, ratio=opt.ratio,
            col_user=DEFAULT_USER_COL, col_item=DEFAULT_ITEM_COL
        )
    if opt.split_method == "spark":
        print("Not implemented")
        return
    try:
        data_train.to_csv(opt.train_path)
    except:
        print("Unable to save train data, check paths")
    
    try:
        data_test.to_csv(opt.test_path)
    except:
        print("Unable to save test data, check paths")

    try:
        data_val.to_csv(opt.val_path)
    except:
        print("Unable to save val data, check paths")
    return