import argparse

def getArguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("--frequency_file",
        default=None,
        required=True,
        type = open,
        help = "Frequency file used.")
    parser.add_argument("--hashtag",
        default=None,
        required=True,
        type = ascii,
        help = "Hashtag to split")

    args=parser.parse_args()
    return args
