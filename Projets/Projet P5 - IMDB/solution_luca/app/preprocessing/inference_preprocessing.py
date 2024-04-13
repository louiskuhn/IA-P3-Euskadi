import pandas as pd
from preprocessing import utils

# C'est ici qu'on va appliquer les mêmes étapes de preprocessing qu'on a appliquées pour l'entrainement du modèle.
def prepare_data(df_json, scaler):

  df = pd.read_json(df_json)

  df = df[utils.columns_to_keep]

  df[utils.columns_to_fillna] = df[utils.columns_to_fillna].fillna(0)

  # print(df.iloc[4])

  df.dropna(inplace=True)


  df['other_actors_fb_likes'] = df.cast_total_fb_likes - df.actor_1_fb_likes
  df.drop(['cast_total_fb_likes', 'actor_2_fb_likes', 'actor_3_fb_likes'], axis=1, inplace=True)

  df['content_rating'] = df.apply(utils.replace_rating, axis=1)


  # Créer toutes les colonnes de genre et les remplir avec des 0
  df[utils.genre_columns] = 0

  genre_dummy_columns = df.genres.str.get_dummies('|').columns
  genre_dummies = df.genres.str.get_dummies('|')

  # les remplir avec des 1 aux bons endroits
  df[genre_dummy_columns] = genre_dummies
  df.drop(['genres'], axis=1, inplace=True)

  df['language'] = df.apply(utils.replace_language, axis=1)

  df['country'] = df.apply(utils.replace_country, axis=1)

  # pareil qu'au dessus avec les genres, mais pour toutes les autres colonnes de catégorie
  for varcat in df.select_dtypes(include="object").columns :
    df[utils.dummy_columns_dict[varcat]] = 0

    dummies = pd.get_dummies(df[varcat], drop_first=True)
    dummy_columns = dummies.columns
    df[dummy_columns] = dummies

    df.drop([varcat], axis=1, inplace=True)


  df_normalized = pd.DataFrame(scaler.transform(df), columns = df.columns, index = df.index)


  return df_normalized
