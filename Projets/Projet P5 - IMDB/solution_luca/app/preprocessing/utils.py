columns_to_keep = ['num_critic_for_reviews', 'duration', 'cast_total_fb_likes', 'color', \
                   'actor_1_fb_likes', 'actor_2_fb_likes', 'actor_3_fb_likes', 'gross',\
                     'num_voted_users',	'facenumber_in_poster',	'num_user_for_reviews',\
                      'budget',	'title_year', 'genres', \
                        'language', 'country', 'content_rating']

columns_to_fillna = ['num_critic_for_reviews', 'cast_total_fb_likes', \
                   'actor_1_fb_likes', 'actor_2_fb_likes', 'actor_3_fb_likes', \
                     'num_voted_users',	'facenumber_in_poster',	'num_user_for_reviews']

genre_columns = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', \
                 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Romance', \
                    'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']

content_rating_columns = ['NC-17', 'PG', 'PG-13', 'R', 'UR']

country_columns = ['North America', 'Other countries']

language_columns = ['European', 'Other languages']

color_columns = ['Color']

dummy_columns_dict = {'content_rating': content_rating_columns,\
                        'language': language_columns,\
                        'country': country_columns,\
                        'color': color_columns}

def replace_rating(row):
    if row['content_rating'] in ['Passed', 'Approved', 'M', 'GP']:
        return 'PG'
    elif row['content_rating'] in ['Not Rated', 'Unrated']:
        return 'UR'
    elif row['content_rating'] == 'X':
        return 'NC-17'
    elif row['content_rating'] == 'TV-14':
        return 'PG-13'
    else:
        return row['content_rating']
    
def replace_language(row):
    if row['language'] in ['French', 'Spanish', 'German', 'Italian', 'Portuguese', 'Norwegian', 'Dutch',
                           'Danish', 'Romanian', 'Bosnian', 'Czech', 'Hungarian', 'Swedish']:
        return 'European'
    elif row['language'] == 'English':
        return 'English'
    else:
        return 'Other languages'
  
def replace_country(row):
    if row['country'] in ['UK', 'France', 'Spain', 'Germany', 'West Germany', 'Italy', 'Portugal', 'Norway', 'Netherlands',
                        'Denmark', 'Ireland', 'Romania', 'Iceland', 'Czech', 'Hungary', 'Sweden', 'Belgium', 'Greece',
                        'Bulgaria', 'Switzerland', 'Poland', 'Finland']:
        return 'Europe'
    elif row['country'] in ['USA', 'Canada']:
        return 'North America'
    else:
        return 'Other countries'