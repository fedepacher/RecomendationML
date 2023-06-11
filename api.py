from fastapi import FastAPI
from movies import Movies
from recommendation_system import Recommendation


movies_obj = Movies()
recomendation_obj = Recommendation()
app = FastAPI()

@app.get('/cantidad_filmaciones_mes/{month}')
def get_count_movies_month(month: str):
    """Get the amount of movies released in the requested month.

    Args:
        month (str, optional): Released month. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_count_movies_month(month=month)


@app.get('/cantidad_filmaciones_dia/{day}')
def get_count_movies_day(day: str):
    """Get the amount of movies released in the requested day.

    Args:
        day (str, optional): Released day. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_count_movies_day(day=day)


@app.get('/score_titulo/{title}')
def get_score_title(title: str):
    """Get the released year and the score of the requested title.

    Args:
        title (str, optional): Movie to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_score_title(title=title)


@app.get('/votos_titulo/{title}')
def get_votes_title(title: str):
    """Get the released year, vote count and vote average of the requested title.

    Args:
        title (str, optional): Movie to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_votes_title(title=title)


@app.get('/get_actor/{actor}')
def get_actor(actor: str):
    """Get the actor movies, themaximun return ans the average return.

    Args:
        actor (str, optional): Actor to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_actor(actor=actor)


@app.get('/get_director/{director}')
def get_director(director: str):
    """Get all the movies, released year, return, revenue and budget of the requested director.

    Args:
        director (str, optional): Director to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_director(director=director)


@app.get('/recomendacion/{title}')
def get_recomendation(title: str):
    """Get the recomendation accordint to requested title.

    Args:
        title (str, optional): Movie to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return recomendation_obj.recommendation(title=title)
