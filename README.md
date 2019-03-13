# Fellow
### EECS 371: Knowledge Representation and Reasoning | W2019
Fellow creates a querying and reasoning structure that allows students to find other like-minded individuals based on academic year, program, career goals, hobbies, and software experience. The long-term goal for this project is to build a web app that can be interacted with not only to find similar students, but also professor, university organizations, events, and more.

Note: the current repository already contains the generated KRF file to load it and run it in Companion. Feel free to skip to the section "Running Companion".

## Setup
We use [pipenv](https://github.com/pypa/pipenv) for managing package dependencies.

1. Install pipenv using the link above.
2. Run `pipenv install` to install package dependencies and `pipenv shell` to start virtual environment with installed dependencies.

## Generating KRF File
1. Navigate to `dev/scraping/`
2. Run `python generate_krf.py` to scrape data from the Google Sheet and generate a single krf file for Companion.
3. Output file can be found in `dist/krf`.

## Running Companion
1. Startup companion and load the `dist/krf/fellow.krf` flat file into the interaction manager.
2. Browse the agent of the interaction manager to input queries and explore the knowledge base.
3. To make sure everything is loaded correctly, try running the following query:
```
(sameAcademicYear DestinyLivingston ?suggestedPerson)
```
This should output students that have the same academic year as Destiny Livingston.

## Available Queries
Feel free to test more of the available queries and compose custom ones by checking out the documentation in `dist/docs/public.html`.

## Customizing and Adding More Data
1. If you want to create a new entity representing a NU student in the knowledge base, please check `dev/krf/people.krf`
2. Follow the structure and syntax, replacing information as needed.
3. To facilitate the process, append the newly created data to the bottom of `dist/krf/fellow.krf` and reload it in Companion.
4. Now try running some queries related to your new user like such:
```
(sameAcademicYear newUser ?suggestedPerson)
```
