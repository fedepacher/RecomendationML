import pandas as pd


class Movies():

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

        if month.lower() not in valid_months:
            return {'message': f'Month not exists: {month}'}
        else:
            condition = self._df_movies['release_date'].dt.strftime('%m') == valid_months.get(month.lower())
            return {'message': f'{self._df_movies[condition]["title"].count()} movies were released on ' \
                               f'{month}'}


    def get_count_movies_day(self, day=''):
        """Get the amount of movies released in the requested day.

        Args:
            day (str, optional): Released day. Defaults to ''.

        Returns:
            dict: Message with the information requested.
        """
        valid_days = {'lunes': 0, 'martes': 1, 'miercoles': 2, 'jueves': 3,
                      'viernes': 4, 'sabado': 5, 'domingo': 6}

        if day.lower() not in valid_days:
            return {'message': f'Mes no existente: {day}'}
        else:
            variable = valid_days.get(day.lower())
            condition = self._df_movies['release_date'].dt.dayofweek == valid_days.get(day.lower())
            return {'message': f'{self._df_movies[condition]["title"].count()} movies were released on '\
                               f'{day}'}


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
            return {'message': f'The movie {df_aux["title"].values[0]} was released on ' \
                    f'{df_aux["release_year"].values[0]} with a popularity ' \
                    f'of {df_aux["popularity"].values[0].round(1)}'}
        else:
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
                return {'message': f'The movie {df_aux["title"].values[0]} was released on ' \
                        f'{df_aux["release_year"].values[0]} with {int(df_aux["vote_count"].values[0])} ' \
                        f'votes and {df_aux["vote_average"].values[0].round(1)} of votes averages'}
            else:
                return {'message': f'Movie `{title}` has not enough votes'}
        else:
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
            return {'message': f'The actor {actor} has starred in {movies_count} films and has got '\
                               f'a maximun return of {self._df_movies.iloc[index_max_return]["return"].round(1)} '\
                               f'with an average of {ret_mean} per film.'}
        else:
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
            text = ''
            for m, d, ret, rev, c in zip(m_list, d_list, ret_list, rev_list, c_list):
                text += f'Movie: {m}, date: {d}, return: {ret.round(1)}, revenue: {rev}, cost: {c}\n'
            return {'message': f'The success of {director} was `{self._df_movies.iloc[index_var]["title"]}` ' \
                               f'with a return of {self._df_movies.iloc[index_var]["return"].round(1)}.\n'\
                               f'The movie list is:\n{text}'}
        else:
            return {'message': f'Director `{director}` not found'}
