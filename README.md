# Fellow
### EECS 371: Knowledge Representation and Reasoning | W2019
 
## Setup
We use [pipenv](https://github.com/pypa/pipenv) for managing package dependencies.

1. Install pipenv using the link above.
2. Run `pipenv install` to install package dependencies and `pipenv shell` to start virtual environment with installed dependencies.

## Generating KRF File
1. Navigate to `dev/scraping/`
2. Run `python generate_krf.py` to scrape data from the Google Sheet and generate a single krf file for Companion.
3. Output file can be found in `dist/krf`.
