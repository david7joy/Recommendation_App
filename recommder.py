import pandas as pd
corr_mat = pd.read_csv('/Users/davidjoy/PycharmProjects/Recommendation_Systems/corr_mat.csv')
X = corr_mat.values
movie_names = pd.read_csv('/Users/davidjoy/PycharmProjects/Recommendation_Systems/movie_names.csv')
movie_n = movie_names.T.index.values.tolist()
del movie_n[0]
print(movie_n.index('My Left Foot (1989)'))