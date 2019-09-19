## TweetFX
Is a system the allows user:
1. User will be abled to login or register in order to access the system
2. Search for tweets about a certain forex pair.
3. Label the tweets buy,sell or neutral and save the tweets with the label and save it to a database.
4. Future requirement Machine Learning as a service once enough tweets are labelled.
    
## Technologies Used
1. Python programming language for backend development and building the sentiment analysis model.
2. Angular 5 Typescript for front-end development.
3. Bootstrap to added a pretty look and feel to the Web Site.
4. Python flask was used to connect the backend to the front-end using REST API.
5. SQLAlchemy by flask is to persist a sqlite database.

## Database
1. The database has 2 tables for users and labelled tweets
2. User table holds the users id, username, email and password
3. Labelled tweets table holds id, tweet, datestamp and sentiment

## Development server

Run python server using `python run.py` command, which is located in the TweetFX.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files. Which will be run from the directory TweetFX-ui.

