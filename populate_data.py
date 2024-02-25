"""
HOW TO USE:
* directly running this file will result in an error
* you should instead type
*   python manage.py shell
* and copy everything in this file into it
"""

from explorexp.models import Place, Category, Challenge, Post
from django.contrib.auth.models import User
from datetime import date

def populate_categories():
    categories = ['Study Spaces', 'Lounges', 'Café', 'Libraries', 'Museums', 'Gyms', 'Parks', 'Arcades', 'Restaurants', 'Night Life']
    for category in categories:
        Category.objects.create(name=category)

def populate_places():
    Place.objects.create(lat=38.03521267616765, long=-78.50043159071825, name='1515', name_slug='1515')
    Place.objects.create(lat=40.44614167722916, long=-79.94873133149169, name='Crêpes Parisiennes', name_slug='crêpes_parisiennes')
    Place.objects.create(lat=40.760799382692824, long=-73.97720105984551, name='New York City Public Library', name_slug='new_york_city_public_library')
    Place.objects.create(lat=40.781338639190814, long=-73.97399671761092, name='American Museum of Natural History', name_slug='american_museum_of_natural_history')
    Place.objects.create(lat=38.03289080184863, long=-78.51357280426573, name='Aquatic Fitness Center', name_slug='aquatic_fitness_center')
    Place.objects.create(lat=40.43510922356903, long=-79.9417576917797, name='Schenley Park', name_slug='schenley_park')
    Place.objects.create(lat=38.02984964576892, long=-78.47885264979851, name='Decades Arcade', name_slug='decades_arcade')
    Place.objects.create(lat=40.42785065391026, long=-79.70121367133262, name='Burgatory', name_slug='burgatory')
    Place.objects.create(lat=38.90847883310629, long=-77.04243919577, name='Cafe Citron', name_slug='cafe_citron')

def populate_challenges():
    Challenge.objects.create(name='Study for the exam that stresses you out the most', category=Category.objects.get(name='Study Spaces'), description='Bring your laptop and textbooks over! Study for at least one hour.', place=Place.objects.get(name='1515'), points=10)
    Challenge.objects.create(name="Chill with friends", category=Category.objects.get(name='Lounges'), description="Invite some of your friends to 1515 where you can sit and chat in their cozy basement.", place=Place.objects.get(name='1515'), points=10)
    Challenge.objects.create(name="Play Galaga", category=Category.objects.get(name='Arcades'), description="Go down to the corner and try defending your planet from extraterrestrial invaders.", place=Place.objects.get(name='1515'), points=10)
    Challenge.objects.create(name="Grab a pastry", category=Category.objects.get(name='Café'), description="Eat a delicious authentic French crêpe.", place=Place.objects.get(name='Crêpes Parisiennes'), points=30)
    Challenge.objects.create(name="Get caffeinated", category=Category.objects.get(name='Café'), description="Drink an invigorating espresso, coffee, or cup of tea.", place=Place.objects.get(name='Crêpes Parisiennes'), points=30)
    Challenge.objects.create(name="Read a book", category=Category.objects.get(name='Libraries'), description="Cozy up to a book written by an author you have not heard of.", place=Place.objects.get(name='New York City Public Library'), points=40)
    Challenge.objects.create(name="Find something shiny", category=Category.objects.get(name='Museums'), description="Tour the Hall of Geology, Gems, and Minerals.", place=Place.objects.get(name='American Museum of Natural History'), points=20)
    Challenge.objects.create(name="Timetravel to the Age of Dinosaurs", category=Category.objects.get(name='Museums'), description="Tour the Hall of Fossils. Make sure to take a picture with the T. Rex.", place=Place.objects.get(name='American Museum of Natural History'), points=20)
    Challenge.objects.create(name="Boost your cardio", category=Category.objects.get(name='Gyms'), description="Sprint a mile along the indoor track.", place=Place.objects.get(name='Aquatic Fitness Center'), points=10)
    Challenge.objects.create(name="Swim like a mermaid", category=Category.objects.get(name='Gyms'), description="Swim a mile in the Olympic-sized indoor pool", place=Place.objects.get(name='Aquatic Fitness Center'), points=10)
    Challenge.objects.create(name="Meditate", category=Category.objects.get(name='Parks'), description="Walk for an hour in this park. Bring your pret, friend, significant other, children along! Or, just bring yourself. Whatever relaxes you the most.", place=Place.objects.get(name='Schenley Park'), points=30)
    Challenge.objects.create(name="Play pinball", category=Category.objects.get(name='Arcades'), description="Go downtown and practice your physics skill with a pinball machine.", place=Place.objects.get(name='Decades Arcade'), points=10)
    Challenge.objects.create(name="Eat an authentic burger", category=Category.objects.get(name='Restaurants'), description="Enjoy a hearty dinner while looking at the Monongahela River.", place=Place.objects.get(name='Burgatory'), points=30)
    Challenge.objects.create(name="Combine food with dance", category=Category.objects.get(name='Restaurants'), description="Enjoy authentic Latin cuisine and take a free salsa class.", place=Place.objects.get(name='Cafe Citron'), points=20)
    Challenge.objects.create(name="Explore a DC club at night", category=Category.objects.get(name='Night Life'), description="Dance the night away at Dupont Circle.", place=Place.objects.get(name='Cafe Citron'), points=20)

def populate_posts():
    Post.objects.create(challenge=Challenge.objects.get(name='Study for the exam that stresses you out the most'),
                        place=Place.objects.get(name='1515'),
                        user=User.objects.get(username='emilychang'),
                        comment='Studying at 1515 has been awesome!',
                        date=date(2024, 2, 24))
    Post.objects.create(challenge=Challenge.objects.get(name='Chill with friends'),
                        place=Place.objects.get(name='1515'),
                        user=User.objects.get(username='emilychang'),
                        comment='Hanouts here leave an indelible memory.',
                        date=date(2024, 2, 2))
    Post.objects.create(challenge=Challenge.objects.get(name="Play Galaga"),
                        place=Place.objects.get(name='1515'),
                        user=User.objects.get(username='emilychang'),
                        comment='Playing Galaga at 1515 brought back nostalgic vibes.',
                        date=date(2024, 1, 2))
    Post.objects.create(challenge=Challenge.objects.get(name="Grab a pastry"),
                        place=Place.objects.get(name='Crêpes Parisiennes'),
                        user=User.objects.get(username='emilychang'),
                        comment='I dug into this amazing crêpe that was just divine. It was like a taste of heaven in every bite!',
                        date=date(2023, 12, 2))
    Post.objects.create(challenge=Challenge.objects.get(name="Get caffeinated"),
                        place=Place.objects.get(name='Crêpes Parisiennes'),
                        user=User.objects.get(username='emilychang'),
                        comment='Sipping on their rich espresso felt like a warm hug on a chilly day.',
                        date=date(2023, 12, 1))
    Post.objects.create(challenge=Challenge.objects.get(name="Read a book"),
                        place=Place.objects.get(name='New York City Public Library'),
                        user=User.objects.get(username='emilychang'),
                        comment='Surrounded by books, it felt like I was exploring the heart of the city\'s literary scene.',
                        date=date(2023, 11, 1))
    Post.objects.create(challenge=Challenge.objects.get(name="Find something shiny"),
                        place=Place.objects.get(name='American Museum of Natural History'),
                        user=User.objects.get(username='emilychang'),
                        comment='It was like embarking on a treasure hunt through time and space.',
                        date=date(2022, 11, 1))
    Post.objects.create(challenge=Challenge.objects.get(name="Timetravel to the Age of Dinosaurs"),
                        place=Place.objects.get(name='American Museum of Natural History'),
                        user=User.objects.get(username='emilychang'),
                        comment='I was filled with awe and wonder as I marveled at the scale and majesty of these long-extinct giants.',
                        date=date(2022, 10, 30))
    Post.objects.create(challenge=Challenge.objects.get(name="Boost your cardio"),
                        place=Place.objects.get(name='Aquatic Fitness Center'),
                        user=User.objects.get(username='emilychang'),
                        comment='Pounding the track left me feeling refreshed, ready to tackle whatever the day had in store.',
                        date=date(2021, 10, 30))
    Post.objects.create(challenge=Challenge.objects.get(name="Swim like a mermaid"),
                        place=Place.objects.get(name='Aquatic Fitness Center'),
                        user=User.objects.get(username='emilychang'),
                        comment='It was like tapping into an inner tranquility while getting in a solid workout.',
                        date=date(2021, 10, 29))
    Post.objects.create(challenge=Challenge.objects.get(name="Meditate"),
                        place=Place.objects.get(name='Schenley Park'),
                        user=User.objects.get(username='emilychang'),
                        comment='Schenley Park was a peaceful escape from the hustle and bustle of city life.',
                        date=date(2021, 9, 29))
    Post.objects.create(challenge=Challenge.objects.get(name="Play pinball"),
                        place=Place.objects.get(name='Decades Arcade'),
                        user=User.objects.get(username='emilychang'),
                        comment='Playing pinball at Decades Arcade was an absolute blast!',
                        date=date(2020, 9, 29))
    Post.objects.create(challenge=Challenge.objects.get(name="Eat an authentic burger"),
                        user=User.objects.get(username='emilychang'),
                        place=Place.objects.get(name='Burgatory'),
                        comment='Devouring a burger at Burgatory was a mouthwatering experience!',
                        date=date(2020, 9, 28))
    Post.objects.create(challenge=Challenge.objects.get(name="Combine food with dance"),
                        place=Place.objects.get(name='Cafe Citron'),
                        user=User.objects.get(username='emilychang'),
                        comment='A vibrant atmosphere made every visit to Cafe Citron a lively and memorable affair.',
                        date=date(2020, 8, 28))
    Post.objects.create(challenge=Challenge.objects.get(name="Explore a DC club at night"),
                        place=Place.objects.get(name='Cafe Citron'),
                        user=User.objects.get(username='emilychang'),
                        comment='Dancing under the neon lights...it was a euphoric escape where worries faded.',
                        date=date(2019, 8, 28))

populate_challenges()
populate_categories()
populate_places()
populate_posts()