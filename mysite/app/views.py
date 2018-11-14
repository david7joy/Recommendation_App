from django.shortcuts import render
import pandas as pd
import numpy as np

corr_mat = pd.read_csv('/Users/davidjoy/PycharmProjects/Recommendation_Systems/corr_mat.csv', header=None,index_col=False)
X = corr_mat.values
movie_names = pd.read_csv('/Users/davidjoy/PycharmProjects/Recommendation_Systems/movie_names.csv')
movie_names_l = movie_names.columns[1:]
movie_n = movie_names.T.index.values.tolist()
del movie_n[0]

def getval(value):
    locs = movie_n.index(value)
    return locs

def test(request):
    loc = movie_n
    if request.method == 'POST':
        value = request.POST.get('value')
        locs = getval(value)
        corr_val = X[locs]
        corr_movies = list(movie_names_l[(corr_val<1.0) & (corr_val>.95)])
        simi_rating = list(corr_val[(corr_val < 1.0) & (corr_val > .96)])
        v = zip(corr_movies, np.around(simi_rating, decimals=4))
        return render(request, 'app/test.html', {'iloc': loc, 'rloc': v, 'selected':value})

    return render(request, 'app/test.html', {'iloc': loc})



