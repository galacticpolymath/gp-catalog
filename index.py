from os import listdir
from os.path import isfile, join
mypath = "./"
lessons = [f for f in listdir(mypath) if not isfile(join(mypath, f)) and f[0] != "."]

for lesson in lessons:
    # permalink??
    # crawl lesson-plans.json for Title, SponsoredBy, and Subtitle
    # add each to a string if present
    # add string into dictionary?
    # include entire lesson plan?
    # include pics?
    pass
