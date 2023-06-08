from fastapi import FastAPI
from movies import Movies


movies_obj = Movies()
app = FastAPI()

@app.get('/movie/month/{month}')
def get_count_movies_month(month: str):
    """Get the amount of movies released in the requested month.

    Args:
        month (str, optional): Released month. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_count_movies_month(month=month)


@app.get('/movie/day/{day}')
def get_count_movies_day(day: str):
    """Get the amount of movies released in the requested day.

    Args:
        day (str, optional): Released day. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_count_movies_day(day=day)


@app.get('/movie/score/{title}')
def get_score_title(title: str):
    """Get the released year and the score of the requested title.

    Args:
        title (str, optional): Movie to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_score_title(title=title)


@app.get('/movie/vote/{title}')
def get_votes_title(title: str):
    """Get the released year, vote count and vote average of the requested title.

    Args:
        title (str, optional): Movie to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_votes_title(title=title)


@app.get('/movie/actor/{actor}')
def get_actor(actor: str):
    """Get the actor movies, themaximun return ans the average return.

    Args:
        actor (str, optional): Actor to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_actor(actor=actor)


@app.get('/movie/director/{director}')
def get_director(director: str):
    """Get all the movies, released year, return, revenue and budget of the requested director.

    Args:
        director (str, optional): Director to be searched. Defaults to ''.

    Returns:
        dict: Message with the information requested.
    """
    return movies_obj.get_director(director=director)
