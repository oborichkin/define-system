import argparse
from define.utils import dict_from_csv, list_from_csv
from define.main import classify


def main():
    parser = argparse.ArgumentParser(description="Classify element using DEFINE system")
    parser.add_argument("train", type=str, help="Path to train CSV file")
    parser.add_argument("test", type=str, help="Path to test CSV file")

    args = parser.parse_args()

    train = dict_from_csv(args.train)
    test = list_from_csv(args.test)

    print(classify(train, test))
