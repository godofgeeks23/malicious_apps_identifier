from tkinter import N
from google_play_scraper import app
from google_play_scraper import search
from google_play_scraper import permissions


def search_apps(query):

    result = search(query, country="in", n_hits=100)
    return result


def get_permissions(app_id):

    result = permissions(app_id)
    return result


def filter_currency_developer(orglist):

    result = []
    for app in orglist:
        # if(app['currency'] == 'INR'):
            # if(app['developerEmail'] == '' or app['developerEmail'].endswith('@gmail.com') or app['developerEmail'].endswith('@hotmail.com') or app['developerEmail'].endswith('@yahoo.com')):
        if(app['developerEmail'].endswith('@gmail.com') or app['developerEmail'].endswith('@hotmail.com') or app['developerEmail'].endswith('@yahoo.com')):
            result.append(app)
    return result

def filter_permissions(orglist):

    # result = []
    for app in orglist:
        # print(app['appId'])
        # print(type(app['appId']))
        get_permissions(app['appId'])

        # if(perms):
            # print(perms)
        # result.append(perms)
    # return result

def truncate(str, max_len):
    if len(str) > max_len:
        return str[:max_len] + '...'
    return str

keywords_file = open("keywords.txt", "r")
terms = keywords_file.read().splitlines()
appslist = []
for term in terms:
    for tempapp in search_apps(term):
        app_details = app(tempapp['appId'])
        appslist.append(app_details)

# filter_permissions(appslist)

# print(get_permissions("com.google.android.apps.translate"))


filtered_list = filter_currency_developer(appslist)


code_start = """
<html>
<head>
<title>Test</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<h1>Suspected Apps</h1>
<div class="mainParent">
"""

code_end = """
</div>
</body>
</html>
"""
 
# dynamic_content = f"<img src='{appslist[0]['icon']}' alt='Italian Trulli' >"
dynamic_content = ""

for apps in filtered_list:
    dynamic_content += f"""
        <div class="app">
            <div class="section1">
                <div class="icon_box">
                    <img
                        src="{apps['icon']}">
                </div>
                <p class="fieldheading">Title
                <p class="fieldvalue">{apps['title']}</p></p>
                <p class="fieldheading">Package Name
                <p class="fieldvalue">{apps['appId']}</p></p>
                <p class="fieldheading">Installs
                <p class="fieldvalue">{apps['installs']}</p></p>
            </div>
            <div class="section2">
                <p class="fieldheading">Release Date
                <p class="fieldvalue">{apps['released']}</p>
                </p>
                <p class="fieldheading">Genre
                <p class="fieldvalue">{apps['genre']}</p></p>
                <p class="fieldheading">Summary
                <p class="fieldvalue">{apps['summary']}</p></p>
                <p class="fieldheading">Developer
                <p class="fieldvalue">{apps['developer']}</p></p>
                <p class="fieldheading">Developer ID
                <p class="fieldvalue">{apps['developerId']}</p></p>
                <p class="fieldheading">Developer EMail
                <p class="fieldvalue">{apps['developerEmail']}</p></p>
                <p class="fieldheading">Developer Website
                <p class="fieldvalue">{apps['developerWebsite']}</p></p>
                <p class="fieldheading">Developer Address
                <p class="fieldvalue">{apps['developerAddress']}</p></p>
                <p class="fieldheading">Ratings
                <p class="fieldvalue">{apps['ratings']}</p></p>
                <p class="fieldheading">Reviews
                <p class="fieldvalue">{apps['reviews']}</p></p>
            </div>
            <div class="section3">
                <p class="fieldheading">Description:
                <p class="fieldvalue">{truncate(apps['description'], 500)}</p></p>
            </div>
        </div>
"""

code = code_start + dynamic_content + code_end

file = open("test.html","w", encoding="utf-8")
file.write(code)
file.close()