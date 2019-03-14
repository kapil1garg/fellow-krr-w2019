# Fellow
### EECS 371: Knowledge Representation and Reasoning | W2019
### Andres Kim, Veronica Medrano, Kapil Garg 
Fellow creates a querying and reasoning structure that allows students to find other like-minded individuals based on academic year, program, career goals, hobbies, and software experience. The long-term goal for this project is to build a web app that can be interacted with not only to find similar students, but also professor, university organizations, events, and more.

_Note:_ the current repository already contains the final generated KRF file in `dist/krf/fellow.krf`. To load it and run it in Companion, feel free to skip to the section [Running Companion](#running-companion).

## Setup
### Pipenv
We use [pipenv](https://github.com/pypa/pipenv) for managing package dependencies.

1. Install pipenv using the link above.
2. Run `pipenv install` to install package dependencies and `pipenv shell` to start virtual environment with installed dependencies.

### Credentials
You will need Google authentication credentials in order to access Google Sheets.

1. Follow the instructions from the [gspread](https://github.com/burnash/gspread) repository to get a `credential.json` file.
2. Put your `credential.json` file in `dev/scraping`.

### .env File
We pull the spreadsheet URL from a `.env` file that is loaded into the pipenv virtual environment when you run `pipenv shell`. Generate one of these files using the format below and place it in the root of the cloned repository:
```
SHEET_URL=YOUR_GOOGLE_SPREADSHEET_URL
```

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
Feel free to test more of the available queries and compose custom ones.

####  Who is in the same academic program as me?
```
(sameAcademicProgram ?person ?suggestedPerson)
```
Example Query: `(sameAcademicProgram DestinyLivingston ?suggestedPerson)`

#### Who is in the same academic year as me?
```
(sameAcademicYear ?person ?suggestedPerson)
```
Example Query: `(sameAcademicYear DestinyLivingston ?suggestedPerson)`

#### Who is in the same field of work as me?
```
(sameFieldOfWork ?person ?suggestedPerson)
```
Example Query: `(sameFieldOfWork DestinyLivingston ?suggestedPerson)`

#### Who has the same software experience as me?
```
(sameSoftwareExperience ?person ?suggestedPerson)
```
Example Query: `(sameSoftwareExperience DestinyLivingston ?suggestedPerson)`

#### Who has the same academic interests as me?
```
(sameAcademicInterests ?person ?suggestedPerson)
```
Example Query: `(sameAcademicInterests DestinyLivingston ?suggestedPerson)`

#### Who has the same hobbies as me?
```
(sameHobbies ?person ?suggestedPerson)
```
Example Query: `(sameHobbies DestinyLivingston ?suggestedPerson)`

#### What are some interesting events that would be related to me?
```
(interestingEvents ?person ?event)
```
Example Query: `(interestingEvents DestinyLivingston ?event)`

#### Who is someone who is experienced in a specific software?
```
(personExperiencedWith ?suggestedPerson ?program)
```
Example Query: `(personExperiencedWith ?suggestedPerson GameDevelopment)`

#### Who is similar to me?
```
(similarNUPerson ?person ?suggestedPerson)
```
Example Query: `(similarNUPerson DestinyLivingston ?suggestedPerson)`

#### Pre-defined Composite Queries
The queries below are compositions of the basic queries listed above:
```
(sameHobbiesAndYear ?person ?suggestedPerson)
```
```
(sameMajorAndYear ?person ?suggestedPerson)
```
```
(sameHobbiesAndField ?person ?suggestedPerson)
```
```
(sameHobbiesWithExperienceIn ?person ?suggestedPerson ?program)
```

#### Custom Composite Queries
We define 3 custom queries that take the simple queries from earlier as input, along with a person to match to. These are custom queries that can be used to run any combination of simpler queries.


Example Query: `(customQuery2 sameAcademicInterests sameHobbies DestinyLivingston ?suggestedPerson)`
```
(customQuery2 ?query1 ?query2 ?person ?suggestedPerson)
```
```
(customQuery3 ?query1 ?query2 ?query3 ?person ?suggestedPerson)
```
```
(customQuery4 ?query1 ?query2 ?query3 ?query4 ?person ?suggestedPerson)
```

## Customizing and Adding More Data
1. If you want to create a new entity representing a NU student in the knowledge base, please check `dev/krf/people.krf`
2. Follow the structure and syntax, replacing information as needed.
3. To facilitate the process, append the newly created data to the bottom of `dist/krf/fellow.krf` and reload it in Companion.
4. Now try running some queries related to your new user like such:
```
(sameAcademicYear newUser ?suggestedPerson)
```
