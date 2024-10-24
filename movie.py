#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:36:26 2024

@author: avntrainee
"""
import pandas as pd

movie_info = pd.read_csv("/home/avntrainee/project_1/movie_dataset.csv")

movie_info.info()

df = pd.DataFrame(movie_info)
df1 = pd.DataFrame(movie_info)

df.dropna(inplace=True, axis=0)

#dropping empty rows


df.columns.str.replace(" ", "") 

#removing spaces



df.drop_duplicates(inplace=True)

#removing duplicates


df.info()

#to get highest rated movie

max_rating=df["Rating"].max()

print(max_rating)

ans = df["Rating"] == max_rating

print(df[ans])

# mean revenue

mean_revenue = df["Revenue (Millions)"].mean()

print(f"the mean revenue of all movies is {mean_revenue:.2f} million ")

# movies between 2015 and 2017

filtered_movies = df[(df["Year"] >=2015) & (df["Year"] <= 2017)]

average_revenues_2015_2017 = filtered_movies["Revenue (Millions)"].mean()

print(f"The average revenue of movies from 2015 to 2017 is:{average_revenues_2015_2017:.2f} million")

start_year = 2015

end_year = 2017

sliced_Years = df[(df["Year"]>= start_year) & (df["Year"]<=end_year)]

print(sliced_Years)


# slicinsing years for 2016

start_year2 = 2016

end_year2 = 2016


sliced_Years2 = df1[(df1["Year"]>= start_year2) & (df1["Year"]<=end_year2)]

print(sliced_Years2)

CN_movies = df["Director"]== "Christopher Nolan"

print(CN_movies)

print(df[CN_movies])

print(len(df[CN_movies]))

# rating greater than 8

ans3 = df["Rating"] >= 8.0

print(df[ans3])

# framing code for median

print(df[CN_movies]["Rating"].mean())

# Finding higest rated year

print(df.groupby("Year")["Rating"].mean())

# percentage increase in movies

start_year4 = 2006

end_year4 = 2016

sliced_year4 = df[(df["Year"]==start_year4)] #&(df["Year"]==end_year4)]

sliced_years5 = df[(df["Year"]==start_year4)] #&(df["Year"]==end_year4)]

print(len(sliced_year4))  

perc_inc = ((len(sliced_years5)-len(sliced_year4))/len(sliced_year4))*100

print(perc_inc)   

#common actor

actors= str(df["Actors"]).split(',')

actors_list= list(actors)

print(actors_list)

actors_df = pd.DataFrame(actors_list,columns=["actors"])

most_common = actors_df["actors"].value_counts().idxmax()

print(most_common)


#

print(df["Genre"])

genre= str(df["Genre"]).split(',')

genre_list= list(genre)

print(genre_list)

genre_df = pd.DataFrame(genre_list,columns=["genre"])

most_common2 = genre_df["genre"].value_counts().idxmi

print(most_common2)

print(len(most_common2))                                                   
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
                                                             
