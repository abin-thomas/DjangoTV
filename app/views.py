"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from app import fetch
import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    stuff = fetch.fetch.fetch_popular_toprated()
    
    popShowName = stuff[0]
    popShowID = stuff[1]
    popShowPoster = stuff[2]


    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'popularShowDetails' : zip(popShowName,popShowID,popShowPoster),  
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Welcome to Django TV Project',
            'year':datetime.now().year,
        }
    )

def tv_Show_Details(request,show_ID):
    """Renders the episode page."""
    assert isinstance(request, HttpRequest)

    stuff = fetch.fetch.fetch_season_info(show_ID)
    seasonPosters = stuff[0]
    seasonTitles = stuff[1]
    seasonNums = stuff[2]
    seasonOverview = stuff[3]
    return render(
        request,
        'app/seasons.html',
        {
            'title':'Seasons',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'seasonDetails': zip(seasonPosters,seasonTitles,seasonNums,seasonOverview),
        }
    )

def singleTvShow_Details(request):
    assert isinstance(request, HttpRequest)

    creatorStuffs,tvShowDetails,tvShowPoster,castDetails,imagesPaths = fetch.fetch.fetch_Oneseason_info()
      
    
    creators = creatorStuffs[0]
    creatorPics = creatorStuffs[1]
    
    if castDetails==[]:
        casts = ""
        castPics=""
        castIDs=""
    else:    
        casts = castDetails[0]
        castPics = castDetails[1]
        castIDs= castDetails[2]

    

    return render(
        request,
        'app/tvshow_masterdetails.html',
        {
            'title':'Seasons',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'showCreators': zip(creators,creatorPics),
            'showCasts': zip(casts,castPics,castIDs),
            'extraImages': imagesPaths,
            'tvShowPoster': tvShowPoster,
            'tvShowID': tvShowDetails[0],
            'tvShowName': tvShowDetails[1],
            'tvShowOverview': tvShowDetails[2],
            'tvShowRating': tvShowDetails[3],
            'tvShowTotalSeasons': tvShowDetails[4],
            'tvShowTotalEpisodes':tvShowDetails[5],

        }
    )

def showsOfPerson(request,id):
    assert isinstance(request, HttpRequest)

    stuff = fetch.fetch.fetch_person_tvshows(id)         
    personShowPosters =stuff[0]
    personShowIDs = stuff[1]
    personShowTitle = stuff[2]

    return render(
        request,
        'app/searchResults.html',
        {
            'title':'TV Shows',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'showDetails': zip(personShowPosters,personShowIDs,personShowTitle),
        }
    )
    

def searchQuery(request):
    assert isinstance(request, HttpRequest)

    queryTerm = request.POST.get('searchTerm')
    if queryTerm =="":
        queryTerm=" "
    
    searchByPerson = request.POST.get('searchByPerson')
    
    if searchByPerson !="yes":
        stuff = fetch.fetch.fetch_all_tvshows(queryTerm)         
        tvShowPosters =stuff[0]
        tvShowIDs = stuff[1]
        tvShowTitle = stuff[2]

        return render(
            request,
            'app/searchResults.html',
            {
                'title':'TV Shows',
                'message':'Your application description page.',
                'year':datetime.now().year,
                'showDetails': zip(tvShowPosters,tvShowIDs,tvShowTitle),
            }
        )
    else:
        stuff = fetch.fetch.fetch_all_persons(queryTerm)         
        personPosters =stuff[0]
        personIDs = stuff[1]
        personTitle = stuff[2]

        return render(
            request,
            'app/searchPersonResults.html',
            {
                'title':'TV Shows',
                'message':'Your application description page.',
                'year':datetime.now().year,
                'personDetails': zip(personPosters,personIDs,personTitle),
            }
        )

def season_Show_Details(request, season_num):
    
    assert isinstance(request, HttpRequest)
    
    stuff = fetch.fetch.getEpisodes(season_num)
    ep_Names = stuff[0]
    ep_IDs = stuff[1]
    ep_Posters = stuff[2]
    
    return render(
        request,
        'app/episodes.html',
        {
            'title': 'Episodes',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'ep_details': zip(ep_Names,ep_IDs,ep_Posters),
        }
    )


def episode_Show_Details(request, episode_num):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    
    stuff,guestDetails,epImagesDetails = fetch.fetch.getEpisodeDetails(episode_num)
    ep_Name = stuff[0]
    ep_Overview = stuff[1]
    ep_Poster = stuff[2]
    
    guestNames = guestDetails[0]
    guestPosters = guestDetails[1]
    guestCharIDs = guestDetails[2]
    
    return render(
        request,
        'app/episodeDetails.html',
        {
            'title': 'Episode',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'currEp_Name': ep_Name,
            'currEp_Overview': ep_Overview,
            'currEp_Poster': ep_Poster,
            'episodeImages': epImagesDetails,
            'showGuests': zip(guestNames,guestPosters,guestCharIDs),
        }
    )