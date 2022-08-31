import argparse

def getArguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("--frequency_file",
        default = None,
        required = True,
        type = open,
        help = "Frequency file used.")
    parser.add_argument("--hashtag",
        default = None,
        required = True,
        type = ascii,
        help = "Hashtag to split")
    parser.add_argument("--remove_diacritics",
        default = 'Yes',
        choices = ['Yes', 'No'],
        help = "Asks if user wants to remove diacritics.")
    parser.add_argument("--lower",
        default = 'Yes',
        choices = ['Yes', 'No'],
        help = "Asks if user wants the expression to be all lowercase.")
    parser.add_argument("--process_frequency_list",
        default = 'No',
        choices = ['Yes', 'No'],
        help = "Asks if user wants to apply the lower and remove_diacritics arguments to the frequency list.")

    args=parser.parse_args()
    return args
