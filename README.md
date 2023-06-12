<p align=center><img src=_src/assets/movies_cover.png><p>

# <h1 align=center> **Movies Recomendation using Machine Learning** </h1>

## Introduction

A movie recommendation system, or a movie recommender system, is an ML-based approach to filtering or predicting the
users’ film preferences based on their past choices and behavior. It’s an advanced filtration mechanism that predicts
the possible movie choices of the concerned user and their preferences towards a domain-specific item, aka movie.

## About this project

This is a project for the **SoyHenry** academy.

## Repository content

+ **etl.ipynb**: Contain the ETL process for the `CSV` files and create a clean `CSV`.
+ **movies.py**: Contain the class to process api requests.
+ **api.py**: Contain the `GET` method to process server requests.
+ **eda.ipynb**: Contain the EDA process and recomendation system.
+ **recommendation_system.py**: Contain the machine learning recomendation system.

## Workflow

For the project is used Github Action Project, you can access this project in the following [link](https://github.com/users/fedepacher/projects/2).<br>
This project will follow the conventional commits of the following [link](https://github.com/fedepacher/RecomendationML/wiki/Conventional-Commits).<br>
Each task will be divided into an issue. [Here](https://github.com/fedepacher/RecomendationML/issues) you can find all the issues available at the moment.<br>
The scheduled task timetable can be access in the following [link](https://github.com/users/fedepacher/projects/2/views/2).<br><br>
The following image shows the workflow proposed for this project:<br>

<p align=center><img src=_src/assets/workflow.png><p>


## Data Engineering ETL

For this task it has been created the following [issue](https://github.com/fedepacher/RecomendationML/issues/1) where you can find the description of the task to solve.

## API development

For this task it has created the following [issue](https://github.com/fedepacher/RecomendationML/issues/2) where you can find the description of the task to solve.<br>
It has the following related [issue](https://github.com/fedepacher/RecomendationML/issues/3).

## API Endpoints

To access the endpoints you should use the following path:

```
https://moviesrecomendation.onrender.com/
```

+ `/cantidad_filmaciones_mes/{month}`: Get the amount of movies released in the requested month.
+ `/cantidad_filmaciones_dia{day}`: Get the amount of movies released in the requested day.
+ `/score_titulo/{title}`: Get the released year and the score of the requested title.
+ `/votos_titulo/{title}`: Get the released year, vote count and vote average of the requested title.
+ `/get_actor/{actor}`: Get the amount of movies starred by the actor, the return of the movies and average return of the movie.
+ `/get_director/{director}`: Get a list of movies of the director, the return, the budget and the revenues of each movie as a list.
+ `/recomendacion/{title}`: Get the top 5 movies recommended based on overviews, gendre and score of movies.

### Example:

#### Recommendation
```
https://moviesrecomendation.onrender.com/recomendacion/The Empire Strikes Back
```

#### Movies launched in the selected day
```
https://moviesrecomendation.onrender.com/cantidad_filmaciones_dia/lunes
```

>Note: The endpoint are not key sensitive, that means that you can use lowercase or uppercase.

## Deployment

To deploy the environment it has used the following [tutorial](https://github.com/HX-FNegrete/render-fastapi-tutorial). The related issue can be found [here](https://github.com/fedepacher/RecomendationML/issues/4).

## Exploratory data analysis

For this task it has been created the following [issue](https://github.com/fedepacher/RecomendationML/issues/6) where you can find all the related information.<br>

## Recommendation system

For this task it has been created the following [issue](https://github.com/fedepacher/RecomendationML/issues/7) where you can find all the related information.<br>
You can access the server with the following link:


