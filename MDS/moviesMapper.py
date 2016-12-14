#!/usr/bin/env python
import sys

# Mapper to return local top 10 cars by weight
# Data source: https://archive.ics.uci.edu/ml/datasets/Auto+MPG
# Data header:"color" "director_name" "num_critic_for_reviews"	"duration" "director_facebook_likes" "actor_3_facebook_likes" "actor_2_name" "actor_1_facebook_likes" "gross" "genres" "actor_1_name" "movie_title"	"num_voted_users" "cast_total_facebook_likes" "actor_3_name" "facenumber_in_poster"	"plot_keywords"	"movie_imdb_link" "num_user_for_reviews" "language"	"country" "content_rating" "budget"	"title_year" "actor_2_facebook_likes" "imdb_score" "aspect_ratio" "movie_facebook_likes"

myList = []
n = 10	# Number of top N records

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split data values into list
	data = line.split("\t")

# add (weight, record) touple to list
myList.append(("hello", line))
# sort list in reverse order
myList.sort(reverse=True)
	
# keep only first N records
if len(myList) > n:
		myList = myList[:n]
		
# Print top N records
for (k,v) in myList:
	print(v)