import os
from get_data import read_params
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

def split_save(config_path):
    config=read_params(config_path)
    train_path=config["split_data"]["train_data"]
    test_path=config["split_data"]["test_data"]
    split_size=config["split_data"]["test_size"]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    random_state=config["base"]["random_state"]

    df=pd.read_csv(raw_data_path)
    train,test=train_test_split(df, test_size=split_size, random_state=random_state)
    train.to_csv(train_path)
    test.to_csv(test_path)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    split_save(parsed_args.config)