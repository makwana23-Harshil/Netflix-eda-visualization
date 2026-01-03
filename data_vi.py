import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("NetFlix.csv")
# print(df)

# cleaning the data
df=df.dropna(subset=["type","release_year","rating","duration","country"])

type_count = df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=["blue","orange"],edgecolor="black")
plt.title("Number of Movies vs Number of TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.grid(color="gray",linestyle=":",linewidth=1)
# plt.savefig("movie_vs_tv.png")
plt.show()

# percentage of content rating
rating_count= df["rating"].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct="%1.1f%%",startangle=90)
plt.title("% of content rating")
# plt.savefig("rating_percentage.png")
plt.show()

# filteing the movies
movie_df=df[df["type"]=="Movie"]
movie_df["duration"]=movie_df["duration"].replace('min',' ').astype(int)
plt.figure(figsize=(8,6))
plt.grid(color="lightblue",linestyle="--",linewidth=1)
plt.hist(movie_df["duration"],bins=30,color="lightgreen",edgecolor="black",label="Movie Duration (min)")
plt.title("Distrubation of Movie Duration")
plt.xlabel("Duration of Movie in Min")
plt.ylabel("Number of Movie")
plt.legend()
# plt.savefig("duration_movie.png")
plt.show()

# Relase year vs number of shows
release_count=df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.grid(color="lightblue",linestyle=":",linewidth=1)
plt.scatter(release_count.index,release_count.values,color="blue",marker="D",label="Total Shows")
plt.legend()
plt.title("Release Year of movie VS Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Movies")
plt.show()

# top 10 country
country_count=df["country"].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color="teal",edgecolor="black")
plt.xlabel("Number of shows")
plt.ylabel("Country names")
plt.title("TOP 10 country vs number of shows")
# plt.savefig("top_10_country.png")
plt.show()

# subplot of movies 
content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(10,5))
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='gold',marker='s')
ax[0].set_title("movie release per year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("No. of Movie")
ax[0].legend(["Movies"])
ax[0].grid(color="lightblue",linestyle="-",linewidth=1)

ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='blue', marker='o')
ax[1].set_title("TV shows release per year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("No. of TV shows")
ax[1].legend(["TV Shows"])
ax[1].grid(color="lightblue",linestyle="--",linewidth=1)
fig.suptitle("movie and TV shows related over year")
plt.tight_layout()
# plt.savefig()
plt.show()