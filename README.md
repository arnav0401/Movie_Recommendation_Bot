# Just_Watch_Bot
Just Watch is an intelligent movie recommendation system which uses both qualitative as well as quantitative metrics for recommending movies. This bot is currently built using an ensemble of 3 different machine learning models and can be found on Telegram 

## Motivation 
“What movie/show should I watch this evening?” Scrolls movie titles for 30 mins “I can’t seem to decide!”

Have you ever felt this way before? Personally, we’ve felt like this countless times. Various streaming platforms such as Netflix, Hulu, Disney+ have a plethora of movie/show options for one to choose from. That sounds like a good thing, but in fact, it induces the ‘choice overload’ phenomenon where one cannot decide when there are too many options.

With this in mind, we realised that the need for a robust movie/show recommendation system is pivotal, considering the ever-growing demand of personalised content for modern consumers. Essentially, this system would also take into account the user’s current mood, setting and direction of interest to narrow down to the best decision possible for that user, at that time and context.

## Aim
We aim to develop a movie recommendation telegram bot using both quantitative & qualitative metrics, that can ultimately enhance a user’s viewing experience and alleviate the chore of choosing.

## User Stories
- As a person who is generally very indecisive, I want to be able to get movie recommendations so I do not waste time scrolling through movie titles on the web.
- As a person who is overwhelmed by a large amount of movies available online, I wish to be recommended one movie that I can watch at a time.
- As a movie fanatic, I wish to be recommended movies that best compliment my current mood, environment and setting I am in.
- As a university student, who uses telegram on a regular basis, I wish to have recommendations given on an accessible chat-like interface, in order to make the process convenient.

## Existing Limitations of Current Recommendation Systems
The current Netflix Recommendation System has few limitations which our project seeks to tackle:
- It recommends a large variety of choices, which increases decision making time and over complicates the process of selecting a show/movie. Our bot attempts to only recommend 1 3 movies/shows at a time to reduce this lag of decision making

- Due to changing psychological mindset and moods of the users, Netflix is unable to detect the current mood of the user, which our bot aims to achieve. This gives rise to a more personalized approach. A potential add-on would be the use of MBTI to determine what kind of shows one would like to watch (eg some prefer to stay within their own sphere of interests but others may like to experiment)

- Lack of qualitative metrics used by Netflix to recommend shows/movies. For instance, Netflix makes heavy use of it’s binary ‘like’ and ‘dislike’ option to classify the shows & movies. Binary judgment is unlikely to yield a fulfilling experience, whether we’re talking about films or human beings. Moreover, it’s algorithm heavily relies on matching the user’s past history and finding similar shows/movies they would like. This prevents netflix from recommending new arrivals of the genres that have not been watched by the user. These few limitations can be tackled by a more qualitative approach that would attempt to understand the psychological state of mind of the user and hence recommend movies.

- Telegram Bot being more accessible and user friendly. It reduces the hassle of starting Netflix and visiting the ‘recommended for you’ page, only to receive a large list of recommendations, to decide which show/movie a user wants to watch. A telegram bot is much faster and accessible as it can be instantly accessed through multiple electronic devices with one click of the button.

## Scope of the Project
The Telegram Bot provides a chat-like interface for users to generate a movie recommendation. There are 3 different paths they can take:
- Random Recommendation: model generates any random movie
- Genre Recommendation: model generates any random movie from the desired genre
- Personalized Recommendation: model asks user a set of questions and then recommends a movie which best match his qualitative responses. We have largely made use of collaboraitve filtering here by matching the client to an existing user in the Movie Lens Dataset we are using. This ensures the client is only recommended movies which are closely liked by the matched user in the dataset.
 The Model will ensure continual training of the model by asking users to rate the recommended movie/show when they initiate the bot again. 
 
The Website acts as a frontend dashboard that hosts statistics regarding the world of movies. It is an informative easy to look up tool which provides key insights. The website even has a page which allows users to access the IMDB page of the top 10 grossing movies in the world for quick access to information. The site further hosts information about our project and the rationale of building such a model!

A Relational DataBase Management System like MySQL will maintain the database that stores and maintains all the records of the user. It will also constantly be updated with the recommendations that were liked by the user - in attempts to continuously train our model.

The model is an ensemble of 3 different machine learning algorthms, namely:
1. Content Based Filtering
2. Popularity Based Filtering
3. Collaborative Filtering

- The Popularity Model is the most basic algorithm that filters movies according to the cumultative ratings given by users. We set a benchmark of 85th percentile and only return the top 15% of the movies in the world, across all genres.
- The Content Based Filtering is a more personalized approach that calculates the cosine similarity between movies that are similar in 3 things:
    a. Movie Overview & Tagline
    b. Movie Cast, Crew & Keywords
    c. Genre
- Collaborative Filtering is a more personalized approach which maps the client to existing users in the dataset and recommends movies that those users most liked. To filter out the movies, we ask users a set of questions where the answer to each question narrows down the scope of recommendation. This makes the recommendation as accurate and reliable as possible.

Our final model is built as an ensemble of these 3 algorithms combined.

## Tech Stack
- Front End
  - Python (Flask Framework)
  - CSS, HTML & JavaScript
  - Telegram bot Interface
- Back End
  - Python with relevant libraries
  - Machine Learning & Natural Language Processing
  - Tableau 
  - Fauna (NoSQL Transactional Database)
