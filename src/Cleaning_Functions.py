import pandas as pd

import regex as re

def limpieza(data):

    columns = ['neighbourhood_group_cleansed', 'bathrooms', 'calendar_updated', 'listing_url', 'scrape_id', 'last_scraped',
            'picture_url', 'host_id', 'host_url', 'host_thumbnail_url', 'host_picture_url', 'calendar_last_scraped', 'license']

    data.drop(columns, axis=1, inplace=True)

    columns = ['name', 'description', 'neighborhood_overview', 'host_name', 'host_location', 'host_about', 'host_listings_count',
            'neighbourhood', 'property_type', 'maximum_nights', 'minimum_minimum_nights', 'maximum_minimum_nights',
            'minimum_maximum_nights', 'maximum_maximum_nights', 'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm',
            'has_availability', 'availability_30', 'availability_60', 'availability_90', 'availability_365',
            'number_of_reviews_ltm', 'number_of_reviews_l30d', 'review_scores_accuracy', 'review_scores_cleanliness',
            'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value',
            'calculated_host_listings_count', 'calculated_host_listings_count_entire_homes',
            'calculated_host_listings_count_private_rooms', 'calculated_host_listings_count_shared_rooms']

    cleaning = data.drop(columns, axis=1)

    cleaning.host_since = cleaning.host_since.apply(lambda x: int(x[:4]))

    cleaning.drop('host_response_time', axis=1, inplace=True)
    cleaning.drop('host_response_rate', axis=1, inplace=True)
    cleaning.drop('host_acceptance_rate', axis=1, inplace=True)

    cleaning.host_is_superhost = cleaning.host_is_superhost.replace(['f', 't'], [0, 1])

    cleaning.drop('host_neighbourhood', axis=1, inplace=True)

    def limpieza_lista(x):
        x = x.lstrip("['")
        x = x.rstrip("']")
        x = x.split("', '")
        return len(x)

    cleaning.host_verifications = cleaning.host_verifications.apply(limpieza_lista)

    cleaning.drop('host_has_profile_pic', axis=1, inplace=True)

    cleaning.host_identity_verified = cleaning.host_identity_verified.replace(['f', 't'], [0, 1])

    barrio = pd.get_dummies(cleaning.neighbourhood_cleansed)

    cleaning = pd.concat([cleaning, barrio], axis=1)

    cleaning.drop('neighbourhood_cleansed', axis=1, inplace=True)

    room_type = pd.get_dummies(cleaning.room_type)

    cleaning = pd.concat([cleaning, room_type], axis=1)

    cleaning.drop('room_type', axis=1, inplace=True)

    cleaning.bathrooms_text.fillna('0.0', inplace=True)

    def baños_digit (x):
        try:
            digit = re.findall('\d.?\d?', x)
            return float(digit[0])
        except:
            return 0.5 
        
    cleaning.bathrooms_text = cleaning.bathrooms_text.apply(baños_digit)

    def limpieza_lista2 (x):
        x = x.lstrip('''["''')
        x = x.rstrip('''"]''')
        x = x.split('''", "''')
        return len(x)

    cleaning.amenities = cleaning.amenities.apply(limpieza_lista2)

    def reviews_date(x):
        try:
            x = int(x[:4])
            return x
        except:
            x = 0     
            return x
            
    cleaning.first_review = cleaning.first_review.apply(reviews_date)

    cleaning.last_review = cleaning.last_review.apply(reviews_date)

    cleaning.review_scores_rating.fillna(0, inplace=True)

    cleaning.instant_bookable = cleaning.instant_bookable.replace(['f', 't'], [0, 1])

    cleaning.reviews_per_month.fillna(0, inplace=True)

    cleaning.drop('id', axis=1, inplace=True)
    cleaning.drop(['last_review', 'first_review', 'bedrooms', 'beds'] , axis=1, inplace=True)
    
    return cleaning