import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Create a user-item matrix
user_item_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# Calculate the cosine similarity between movies based on user ratings
cosine_sim_item = cosine_similarity(user_item_matrix.T)
cosine_sim_df = pd.DataFrame(cosine_sim_item, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Function to get movie recommendations based on a given movie title using Collaborative Filtering
def get_recommendations(title, cosine_sim=cosine_sim_df):
    try:
        # Get the movie ID based on the title the user entered
        movie_id = movies[movies['title'] == title].iloc[0]['movieId']
        
        # Grab the similarity scores for that movie
        sim_scores = cosine_sim[movie_id]
        
        # Sort them in descending order to get the most similar movies at the top
        sim_scores = sim_scores.sort_values(ascending=False)
        
        # Remove the movie itself from the recommendations list
        sim_scores = sim_scores[sim_scores.index != movie_id]
        
        # Get the top 10 most similar movie IDs
        recommended_movie_ids = sim_scores.head(10).index
        
        # Get the movie titles for the recommended movie IDs
        recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]
        
        # Return the titles of the recommended movies
        return recommended_movies['title'].tolist()
    
    except IndexError:
        return ["Oops! I couldn't find that movie. Please double-check the title and try again."]

# Example usage: Get recommendations for "Toy Story (1995)"
recommendations_toy_story = get_recommendations("Toy Story (1995)")
print("Recommended Movies for 'Toy Story (1995)':")
print(recommendations_toy_story)

# Example usage: Get recommendations for "Jumanji (1995)"
recommendations_jumanji = get_recommendations("Jumanji (1995)")
print("\nRecommended Movies for 'Jumanji (1995)':")
print(recommendations_jumanji)

