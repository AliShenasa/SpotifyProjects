# Parse top tracks json file from spotify api

import argparse
from email import header
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', type=str, action='store', help='json file')
    args = parser.parse_args()
    jsonfile = args.jsonfile

    outfilename = jsonfile.split('.')[-2].strip('\\') + ".txt"

    with open(jsonfile) as file:
        data = json.load(file)

    PADAMOUNT = 50

    with open(outfilename, 'w') as outfile:
        outfile.write("Top Tracks\n")
        title_left = "Track"
        title_right = "Artist(s)"
        header_padding = " " * (PADAMOUNT - len(title_left))
        outfile.write(title_left + header_padding + title_right + "\n\n")
        for item in data['items']:
            trackname = item['name']
            artists = ", ".join([artist['name'] for artist in item['artists']])
            padding = " " * (PADAMOUNT - len(trackname))
            outfile.write(trackname + padding + artists + '\n')

if __name__ == "__main__":
    main()