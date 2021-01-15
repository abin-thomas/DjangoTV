
import requests
import datetime
import json


masterTvID =""
master_season_num=""

api_key = "eda2c7d3f3cec9d78106def269a4a6a4"

class fetch():
    """description of class"""


    def fetch_all_tvshows(queryTerm):
        url = "https://api.themoviedb.org/3/search/tv?api_key="+ api_key+"&language=en-US&query="+queryTerm
        response = requests.get(url)
        stuff = []

        if(response.ok):
            jData = json.loads(response.content)
            data = jData['results']
            posters = []
            ids = []
            titles =[]
            for idx in range(len(data)):
                posterPath = data[idx]['poster_path']
                posters.append(posterPath)
                showID = data[idx]['id']
                ids.append(showID)
                title = data[idx]['name']
                titles.append(title)


            stuff.append(posters)
            stuff.append(ids)
            stuff.append(titles)
            
        else:
            stuff = None

        return stuff

#*******************************************************************#
    def fetch_person_tvshows(id):
       
        url = "https://api.themoviedb.org/3/person/"+id+"/tv_credits?api_key="+ api_key+"&language=en-US"
        response = requests.get(url)
        stuff = []

        if(response.ok):
            jData = json.loads(response.content)
            data = jData['cast']
            posters = []
            ids = []
            titles =[]
            for idx in range(len(data)):
                showID = data[idx]['id']
                if ids.count(showID)<1:
                    ids.append(showID)
                    posterPath = data[idx]['poster_path']
                    posters.append(posterPath)
                    title = data[idx]['original_name']
                    titles.append(title)


            stuff.append(posters)
            stuff.append(ids)
            stuff.append(titles)
            
        else:
            stuff = None

        return stuff

#*******************************************************************#
    def fetch_all_persons(queryTerm):
        url = "https://api.themoviedb.org/3/search/person?api_key="+ api_key+"&language=en-US&query="+queryTerm
        response = requests.get(url)
        stuff = []

        if(response.ok):
            jData = json.loads(response.content)
            data = jData['results']
            
            posters = []
            ids = []
            titles =[]
            
            for idx in range(len(data)):
                tempData = data[idx]['known_for']
                for tempIdx in range(len(tempData)): # this code is just to show                                        the tv related persons only
                    tempMedia = tempData[tempIdx]['media_type']
                    if tempMedia == 'tv':
                        posterPath = data[idx]['profile_path']
                        posters.append(posterPath)
                        showID = data[idx]['id']
                        ids.append(showID)
                        title = data[idx]['name']
                        titles.append(title)
                        break


            stuff.append(posters)
            stuff.append(ids)
            stuff.append(titles)
            
        else:
            stuff = None

        return stuff

#*******************************************************************#

    def fetch_season_info(showID):        
        url = "https://api.themoviedb.org/3/tv/" + showID + "?api_key=" + api_key
        response = requests.get(url)
        stuff = []
        
        global masterTvID
        masterTvID = showID
        
        if(response.ok):
            jData = json.loads(response.content)
            data = jData['seasons']
            
            images = []
            titles = []
            seasonNums =[]
            overviews = []
            for idx in range(len(data)):
                title = data[idx]['name']
                titles.append(title)
                image = data[idx]['poster_path']
                images.append(image)
                snum = data[idx]['season_number']
                seasonNums.append(snum)
                overview = data[idx]['overview']
                overviews.append(overview)

            stuff.append(images)
            stuff.append(titles)
            stuff.append(seasonNums)
            stuff.append(overviews)
        else:
            stuff = None

        return stuff
#*******************************************************************#
    def fetch_Oneseason_info():
        seasonUrl = "https://api.themoviedb.org/3/tv/" + masterTvID + "?api_key=" + api_key
        
        response = requests.get(seasonUrl)
        creatorStuff = []
        tvShowDetails = []
        
        tvShowPoster =""
        tvShowDetailsRequests = ["id","original_name","overview","vote_average",                                      "number_of_seasons","number_of_episodes"]
        if(response.ok):
            jData = json.loads(response.content)

            tvShowPoster =jData['poster_path']

            creatorsData = jData['created_by']
            
            creatorNames = []
            creatorPosters =[]           
            

            for idx in range(len(creatorsData)):
                cName = creatorsData[idx]['name']
                creatorNames.append(cName)
                cProfilePic = creatorsData[idx]['profile_path']
                creatorPosters.append(cProfilePic)
                
            for items in tvShowDetailsRequests:
                value = jData[items]
                tvShowDetails.append(value)

            creatorStuff.append(creatorNames)
            creatorStuff.append(creatorPosters)
            
            
            
        else:
            creatorStuff = None

        creditsUrl = "https://api.themoviedb.org/3/tv/" + masterTvID + "/credits?api_key=" + api_key
        
        response = requests.get(creditsUrl)
        creditDetails = []
        if(response.ok):
            jData = json.loads(response.content)

            castDetails =jData['cast']

            castNames = []
            castPosters =[]
            castIDs = []
            for idx in range(len(castDetails)):
                name = castDetails[idx]['name']
                castNames.append(name)
                profilePic = castDetails[idx]['profile_path']
                castPosters.append(profilePic)
                ids = castDetails[idx]['id']
                castIDs.append(ids)

                creditDetails.append(castNames)
                creditDetails.append(castPosters)
                creditDetails.append(castIDs)
        else:
            creditDetails = None
        

        imagesUrl = "https://api.themoviedb.org/3/tv/" + masterTvID + "/images?api_key=" + api_key
        
        response = requests.get(imagesUrl)
        imagesDetails = []
        if(response.ok):
            jData = json.loads(response.content)

            backdropDetails =jData['backdrops']

            imagePaths =[]
            
            for idx in range(len(backdropDetails)):
                image = backdropDetails[idx]['file_path']
                imagesDetails.append(image)
                
        else:
            imagesDetails = None

        return creatorStuff,tvShowDetails,tvShowPoster,creditDetails,imagesDetails
   
#*******************************************************************#   
    def getEpisodes(season_num):
        
        global master_season_num
        master_season_num = season_num

        url = "https://api.themoviedb.org/3/tv/" + masterTvID +"/season/"+season_num +"?api_key=" + api_key
        response = requests.get(url)
        stuff = []
        

        if(response.ok):
            jData = json.loads(response.content)
            data = jData['episodes']
            titles = []
            epNums = []
            posters = []
            for idx in range(len(data)):
                title = data[idx]['name']
                titles.append(title)
                epNum = data[idx]['episode_number']
                epNums.append(epNum)
                poster = data[idx]['still_path']
                posters.append(poster)

            stuff.append(titles)
            stuff.append(epNums)
            stuff.append(posters)
        else:
            stuff = None

        return stuff
#*******************************************************************#
    def fetch_popular_toprated():

        popularUrl = "https://api.themoviedb.org/3/tv/popular?api_key=" + api_key + "&language=en-US&page=1"
        response = requests.get(popularUrl)
        stuff = []

        if(response.ok):
            jData = json.loads(response.content)

            data = jData['results']
            tvtitles = []
            tvIds = []
            tvPosters = []
            for idx in range(0,12):  #just taking the first 12 shows
                title = data[idx]['name']
                tvtitles.append(title)
                showID = data[idx]['id']
                tvIds.append(showID)
                poster = data[idx]['poster_path']
                tvPosters.append(poster)

            stuff.append(tvtitles)
            stuff.append(tvIds)
            stuff.append(tvPosters)
        else:
            stuff = None

        return stuff

#*******************************************************************#
    def getEpisodeDetails(episode_num):
       
        url = "https://api.themoviedb.org/3/tv/" + masterTvID +"/season/"+master_season_num +"/episode/" + episode_num +"?api_key=" + api_key
        response = requests.get(url)
        
        stuff = []
        showGuestStars = []

        if(response.ok):
            jData = json.loads(response.content)
            
            showGuest = jData['guest_stars']

            guestNames = []
            guestPosters = []
            guestCharIDs = []



            title = jData['name']
            overview = jData['overview']
            posterPath = jData['still_path']
            
            for idx in range(len(showGuest)):
                gName = showGuest[idx]['name']
                guestNames.append(gName)
                gProfilePic = showGuest[idx]['profile_path']
                guestPosters.append(gProfilePic)
                gCharID = showGuest[idx]['id']
                guestCharIDs.append(gCharID)


            stuff.append(title)
            stuff.append(overview)
            stuff.append(posterPath)

            showGuestStars.append(guestNames)
            showGuestStars.append(guestPosters)
            showGuestStars.append(guestCharIDs)
        else:
            stuff = None
            showGuestStars = None


        imagesUrl = "https://api.themoviedb.org/3/tv/" + masterTvID + "/season/"+ master_season_num +"/episode/"+ episode_num +"/images?api_key=" + api_key
        
        response = requests.get(imagesUrl)
        episodeImagesDetails = []
        if(response.ok):
            jData = json.loads(response.content)

            stillsDetails =jData['stills']

            imagePaths =[]
            
            for idx in range(len(stillsDetails)):
                image = stillsDetails[idx]['file_path']
                episodeImagesDetails.append(image)
                
        else:
            episodeImagesDetails = None


        return stuff, showGuestStars, episodeImagesDetails
#*******************************************************************#