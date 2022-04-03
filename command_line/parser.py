from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SearchParser:

    def __init__(self):
        self.google_search = "https://google.com/search?q="
        self.sites = ["stackoverflow.com"]
        self.parsed_results = []

    def search(self, query, result, page):

        if result < 0:

            results = self.getData(query=query, page=page)

            self.parseResults(results=results)

            if len(self.parsed_results) == 0:
                print(bcolors.FAIL + "No results found.")
                return

            reversed_results = list(reversed(self.parsed_results))

            for res in reversed_results:

                print(res['name'])
                print(res['url'])
                print(res['divider'])

        else:
            self.searchAndOpen(query, result, page)

    def searchAndOpen(self, query, result, page):

        if len(self.sites) == 1:

            results = self.getData(query, page)

            self.parseResults(results=results)

            if len(self.parsed_results) > 0 and result < len(self.parsed_results):

                os.system(
                    f'python -m webbrowser https://{self.sites[0]}/questions/{self.parsed_results[result]["url"].split("/")[-2]}')
                print(bcolors.OKGREEN +
                      f"Opened {self.parsed_results[result]['url']}")

                return

            if len(self.parsed_results) == 0:
                print(bcolors.FAIL + "No results found.")
                return

            if result >= len(self.parsed_results):
                print(bcolors.FAIL + f"The number {result} is out of range")
                return

    def getData(self, query, page):

        if len(self.sites) == 1:

            page = f"&start={(page * 10 - 10)}" if page != -1 else ""

            url = self.google_search + \
                query.replace(" ", "+")+f"+site:{self.sites[0]}" + page

            response = requests.get(url)

        return response

    def parseResults(self, results):

        if len(self.sites) == 1:

            soup = BeautifulSoup(results.text, 'html.parser')

            for result in soup.find_all('a'):

                if f'{self.sites[0]}/questions' not in result['href']:
                    continue

                self.parsed_results.append({
                    "name": bcolors.HEADER + " ".join(result['href'].split('/')
                                                      [-1].split('&')[0].split("-")).title() + bcolors.BOLD,
                    "url": bcolors.OKBLUE + result['href'].replace("/url?q=", ''),
                    "divider": bcolors.WARNING + '--------------------------------------'
                })

    def showSites(self):

        for i in range(len(self.sites)):

            print(i, self.sites[i])

        return


def main():

    search_parser = SearchParser()

    program_name = "Dev Helper - your friendly neighborhood CLI helper."
    description = "We help you find answers to your coding problems right from the command line."

    parser = ArgumentParser(
        prog=program_name, description=description, allow_abbrev=False)

    parser.add_argument('-question', '-q', type=str)

    parser.add_argument('-open', '-o', type=int, default=-1)

    parser.add_argument('-page', '-p', type=int, default=-1)

    args = parser.parse_args()

    if args.question:

        search_parser.search(args.question, args.open, args.page)


if __name__ == "__main__":
    main()
