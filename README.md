# Dev Helper

A simple Google Search scraper that helps you find answers in StackOverflow from the command line.

## Installation

From the command line type: \
`git clone https://github.com/luigicfh/dev-helper.git`

`python setup.py install`

Once installed call the command dh plus one or more arguments, for example:

#### Search

`dh -q "how to lowercase string in python"`

#### Search plus page number

`dh -q "how to lowercase string in python" -p 2`

#### Search and open result (the -open argument starts at 0 index)

`dh -q "how to lowercase string in python" -o 2`
