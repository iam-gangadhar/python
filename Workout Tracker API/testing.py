from datetime import datetime
#
date = datetime.today()
print(date)
new_date = date.strftime('%d/%m/%Y')
print(new_date)

time = datetime.now()
print(time)
now = time.strftime('%H:%M')
print(now)
import os
print(os.environ)



# data = {
#   'exercises': [
#     {
#       'tag_id': 317,
#       'user_input': 'run',
#       'duration_min': 30,
#       'met': 9.8,
#       'nf_calories': 463.05,
#       'photo': {
#         'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
#         'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
#         'is_user_uploaded': False
#       },
#       'compendium_code': 12050,
#       'name': 'running',
#       'description': None,
#       'benefits': None
#     },
#     {
#       'tag_id': 766,
#       'user_input': 'strength',
#       'duration_min': 30,
#       'met': 3.5,
#       'nf_calories': 165.38,
#       'photo': {
#         'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_highres.jpg',
#         'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/766_thumb.jpg',
#         'is_user_uploaded': False
#       },
#       'compendium_code': 2054,
#       'name': 'weight lifting',
#       'description': None,
#       'benefits': None
#     },
#     {
#       'tag_id': 774,
#       'user_input': 'workout',
#       'duration_min': 45,
#       'met': 4,
#       'nf_calories': 283.5,
#       'photo': {
#         'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/774_highres.jpg',
#         'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/774_thumb.jpg',
#         'is_user_uploaded': False
#       },
#       'compendium_code': 2143,
#       'name': 'General Workout',
#       'description': None,
#       'benefits': None
#     }
#   ]
# }
#
# Exercise = data['exercises'][0]['name']
# duration = data['exercises'][0]['duration_min']
# calories = round(data['exercises'][0]['nf_calories'])
#
# print(Exercise)
# print(duration)
# print(calories)