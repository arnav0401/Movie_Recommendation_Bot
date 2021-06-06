# JustWatch
A movie recommendation Telegram bot!

## Motivation
“What movie/show should I watch this evening?”
*Scrolls movie titles for 30 mins*
“I can’t seem to decide!”

Have you ever felt this way before? Personally, we’ve felt like this countless times. Various streaming platforms such as Netflix, Hulu, Disney+ have a plethora of movie/show options for one to choose from. That sounds like a good thing, but in fact, it induces the ‘choice overload’ phenomenon where one cannot decide when there are too many options. 

With this in mind, we realised that the need for a robust movie/show recommendation system is pivotal, considering the ever-growing demand of personalised content for modern consumers. Essentially, this system would also take into account the user’s current mood, setting and direction of interest to narrow down to the best decision possible for that user, at that time and context. 

## Aim
We aim to develop a movie recommendation telegram bot using both quantitative & qualitative metrics, that can ultimately enhance a user’s viewing experience and alleviate the chore of choosing. 

##User Stories
- As a person who is generally very indecisive, I want to be able to get movie recommendations so I do not waste time scrolling through movie titles on the web.
- As a person who is overwhelmed by a large amount of movies available online, I wish to be recommended one movie that I can watch at a time.
- As a movie fanatic, I wish to be recommended movies that best compliment my current mood, environment and setting I am in. 
- As a university student, who uses telegram on a regular basis, I wish to have recommendations given on an accessible chat-like interface, in order to make the process convenient.


### Existing limitations of current Recommendation Systems 

- The current Netflix Recommendation System has few limitations which our project seeks to tackle:
- It recommends a large variety of choices, which increases decision making time and over complicates the process of selecting a show/movie. Our bot attempts to only recommend 1 3 movies/shows at a time to reduce this lag of decision making
- Due to changing psychological mindset and moods of the users, Netflix is unable to detect the current mood of the user, which our bot aims to achieve. This gives rise to a more personalized approach. A potential add-on would be the use of MBTI to determine what kind of shows one would like to watch (eg some prefer to stay within their own sphere of interests but others may like to experiment)
- Lack of qualitative metrics used by Netflix to recommend shows/movies. For instance, Netflix makes heavy use of it’s binary ‘like’ and ‘dislike’ option to classify the shows & movies. Binary judgment is unlikely to yield a fulfilling experience, whether we’re talking about films or human beings. Moreover, it’s algorithm heavily relies on matching the user’s past history and finding similar shows/movies they would like. This prevents netflix from recommending new arrivals of the genres that have not been watched by the user. These few limitations can be tackled by a more qualitative approach that would attempt to understand the psychological state of mind of the user and hence recommend movies. 
- Telegram Bot being more accessible and user friendly. It reduces the hassle of starting Netflix and visiting the ‘recommended for you’ page, only to receive a large list of recommendations, to decide which show/movie a user wants to watch. A telegram bot is much faster and accessible as it can be instantly accessed through multiple electronic devices with one click of the button.

## Scope of the Project
The Website allows new users to create an account as well as explore our recommendation system’s use cases and applications. The website will also host key statistics, in the form of a dashboard, as to which movies/shows or genres were recommended and liked by the user. These figures will be constantly updated as and when more users register and start making use of the bot. This framework will allow our model to be more interpretable in nature.

The Telegram Bot provides a chat-like interface for users to answer the set of questions. These responses will then be used to generate a recommendation. The recommendation will not only comprise the name of the movie/show but also the trailer and synopsis. The bot will also ensure continual training of the model by asking users to rate the recommended movie/show when they initiate the bot again.

A Relational DataBase Management System like MySQL will maintain the database that stores and maintains all the records of the user. It will also constantly be updated with the recommendations that were liked by the user - in attempts to continuously train our model. 

The Recommendation system will be developed using Collaborative Filtering for our telegram bot users. Machine Learning algorithms will be used to train, test and evaluate our mode’s qualitative and quantitative metrics. Deep Learning (Neural Networks) may be used to supplement the model’s development.
