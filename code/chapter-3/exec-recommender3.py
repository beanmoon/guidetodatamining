from recommender3 import *
r = recommender(0)
r.loadMovieLens('/Users/bean/Downloads/ml-100k/')
r.computeDeviations()
r.slopeOneRecommendations(r.data['25'])
