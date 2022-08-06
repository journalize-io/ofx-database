# ofx-database

This repository hosts information for how to connect to various 
banks and financial institutions via OFX. 

The data here is sourced by the community, and special thanks goes to
@jliesch who created and maintained ofxhome.com for more than a decade.

## Updating Data

OFX data for each bank is listed in the `ofx/` directory. Each bank has its own
YAML file, containing information about URLs, IDs, and other notes for connecting.

To update data, please make a PR!

## Running Locally

The website is run via `mkdocs`. Here are steps to get started:

Install project dependencies:

```
pip3 install -r requirements.txt
```

Convert YAML data into Markdown files:

```
python3 generate.py
```

Run the documentation locally:

```
mkdocs serve
```