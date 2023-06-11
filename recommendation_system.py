import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Recommendation():
    """Recommendation class"""
    def __init__(self):
        """Class constructor to initialize component"""
        url='https://drive.google.com/file/d/1cW_pujQGUR2WqwbqiJU3knd8KNlh_z5p/view?usp=sharing'
        url='https://drive.google.com/uc?id=' + url.split('/')[-2]
        self._df_movies = pd.read_csv(url)
        features = ['genres', 'vote_average', 'overview']
        for feature in features:
            self._df_movies[feature] = self._df_movies[feature].fillna('')
        self._df_movies["combined_features"] = self._df_movies['genres'].str.lower() + ' ' \
                                               + str(self._df_movies['vote_average']) + ' ' \
                                               + self._df_movies['overview'].str.lower()
        self._tfidf = TfidfVectorizer()
        self._tfidf_matrix = self._tfidf.fit_transform(self._df_movies['combined_features'])


    def recommendation(self, title=''):
        """Get a movie recommendation based on a movie title.

        Args:
            title (str): Movie title.

        Returns:
            str: Dictionary with the movies recommended.
        """
        movie_index = self._df_movies[self._df_movies['title'].str.lower() == title].index.values
        if len(movie_index) > 0:
            similarity_scores = cosine_similarity(self._tfidf_matrix[movie_index],
                                                  self._tfidf_matrix)
            similar_movies_index = similarity_scores.argsort()[0][-5:][::-1]
            similar_movies = self._df_movies.iloc[similar_movies_index][['title', 'vote_average']]
            similar_movies.sort_values(by='vote_average', ascending=False, inplace=True)
            movie_list_str = '' 
            for _, element in similar_movies.iterrows():
                movie_list_str += element['title'] + ' ' + str(element['vote_average']) + '\r\n'
            return {'lista recomendada': movie_list_str}
        return {'lista recomendada': f'No title were found for {title}'}
