import pandas as pd


class Movies():
    """Class that contains all the functions that the API needs."""

    def __init__(self):
        """Constructor"""
        url='https://drive.google.com/file/d/1QuvhMiZLka18ZXnx8o1P5C8Cf5oHCgjL/view?usp=sharing'
        url='https://drive.google.com/uc?id=' + url.split('/')[-2]
        self._df_movies = pd.read_csv(url)
        self._df_movies['release_date'] = pd.to_datetime(self._df_movies['release_date'],
                                                         format='%Y-%m-%d')


    def get_count_movies_month(self, month=''):
        """Get the amount of movies released in the requested month.

        Args:
            month (str, optional): Released month. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        valid_months = {'enero': '1', 'febrero': '2', 'marzo': '3', 'abril': '4',
                        'mayo': '5', 'junio': '6', 'julio': '7', 'agosto': '8',
                        'septiembre': '9', 'setiembre': '9', 'octubre': '10',
                        'noviembre': '11', 'diciembre': '12'}

        if month.lower() in valid_months:
            condition = self._df_movies['release_date'].dt.strftime('%m') == valid_months.get(month.lower())
            return {'month': month, 'amount': self._df_movies[condition]["title"].count()}

        return {'message': f'Month not exists: {month}'}


    def get_count_movies_day(self, day=''):
        """Get the amount of movies released in the requested day.

        Args:
            day (str, optional): Released day. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        valid_days = {'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
                      'viernes': 4, 'sabado': 5, 'domingo': 6}

        if day.lower() in valid_days:
            condition = self._df_movies['release_date'].dt.dayofweek == valid_days.get(day.lower())
            return {'day': day, 'amount': self._df_movies[condition]["title"].count()}

        return {'message': f'Mes no existente: {day}'}


    def get_score_title(self, title=''):
        """Get the released year and the score of the requested title.

        Args:
            title (str, optional): Movie to be searched. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        df_aux = self._df_movies['title'].str.lower()
        index = df_aux[df_aux == title.lower()].index
        if len(index.values) > 0:
            df_aux = self._df_movies.iloc[index][['title', 'release_year', 'popularity']]
            return {'title': df_aux["title"].values[0],
                    'year': df_aux["release_year"].values[0],
                    'popularity': df_aux["popularity"].values[0].round(1)}

        return {'message': f'Movie `{title}` not found'}


    def get_votes_title(self, title=''):
        """Get the released year, vote count and vote average of the requested title.

        Args:
            title (str, optional): Movie to be searched. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        df_aux = self._df_movies['title'].str.lower()
        index = df_aux[df_aux == title.lower()].index
        if len(index.values) > 0:
            df_aux = self._df_movies.iloc[index][['title', 'release_year', 'vote_count', 'vote_average']]
            if df_aux["vote_count"].values[0] >= 2000:
                return {'title': df_aux["title"].values[0],
                        'year': df_aux["release_year"].values[0],
                        'total_votes': int(df_aux["vote_count"].values[0]),
                        'average_votes': df_aux["vote_average"].values[0].round(1)}

            return {'message': f'Movie `{title}` has not enough votes'}

        return {'message': f'Movie `{title}` not found'}


    def get_actor(self, actor=''):
        """Get the actor movies, themaximun return ans the average return.

        Args:
            actor (str, optional): Actor to be searched. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        df_aux = self._df_movies['cast'].str.lower()
        index_list = list(df_aux[df_aux.str.contains(actor.lower())].index.values)
        movies_count = len(index_list)
        if movies_count > 0:
            ret_mean = 0
            for index in index_list:
                ret_mean += self._df_movies.iloc[index]['return']
            if movies_count > 0:
                ret_mean = (ret_mean/movies_count).round(1)
            else:
                ret_mean = 0
            return_list = [self._df_movies['return'].iloc[ret] for ret in index_list]
            max_value = max(return_list)
            index_max_return = index_list[return_list.index(max_value)]
            return {'actor': actor,
                    'movie_count': movies_count,
                    'max_return': self._df_movies.iloc[index_max_return]["return"].round(1),
                    'average_return': ret_mean}

        return {'message': f'Actor `{actor}` not found'}


    def get_director(self, director=''):
        """Get all the movies, released year, return, revenue and budget of the requested director.

        Args:
            director (str, optional): Director to be searched. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        df_aux = self._df_movies['director'].str.lower()
        index_list = list(df_aux[df_aux.str.contains(director.lower())].index.values)
        if len(index_list)> 0:
            m_list = [self._df_movies['title'].iloc[ret] for ret in index_list]
            d_list = [self._df_movies['release_year'].iloc[ret] for ret in index_list]
            rev_list = [self._df_movies['revenue'].iloc[ret] for ret in index_list]
            c_list = [self._df_movies['budget'].iloc[ret] for ret in index_list]
            ret_list = [self._df_movies['return'].iloc[ret] for ret in index_list]
            max_value = max(ret_list)

            index_var = index_list[ret_list.index(max_value)]
            return {'director': director,
                    'max_return_title': self._df_movies.iloc[index_var]["title"],
                    'max_return': self._df_movies.iloc[index_var]["return"].round(1),
                    'movies': m_list,
                    'year': d_list,
                    'return_movie': ret_list,
                    'budget_movie': c_list,
                    'revenue_movie': rev_list}

        return {'message': f'Director `{director}` not found'}
