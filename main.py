"""
Concert Itinerary Builder

This module provides functionality to build an itinerary of upcoming concerts.
"""

import math
from datetime import datetime

class Concert:
    """
    Represents a concert event.
    
    Attributes:
        artist (str): The name of the artist performing.
        date (str): The date of the concert in 'YYYY-MM-DD' format.
        location (str): The location where the concert will take place.
        latitude (float): Latitude coordinate of the concert location.
        longitude (float): Longitude coordinate of the concert location.
    """
    
    def __init__(self, artist, date, location, latitude, longitude):
        self.artist = artist
        self.date = date
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

    def print_class(self):
        print(f"[\nartist: {self.artist}\ndate: {self.date}\nlocation: {self.location}\nlat: {self.latitude}\nlong: {self.longitude}")

class ItineraryBuilder:
    """
    A class to build concert itineraries. 
    """
    
    def quicksort(self, lst):

        less = []
        eq = []
        greater = []

        if(len(lst) > 1):
            pivot = datetime.fromisoformat(lst[0].date)
            for x in lst:
                if(datetime.fromisoformat(x.date) < pivot):
                    less.append(x)
                elif(datetime.fromisoformat(x.date) == pivot):
                    eq.append(x)
                else:
                    greater.append(x)
            return self.quicksort(less)+eq+self.quicksort(greater)
        else:
            return lst

    def calc_distance(self, prev, concert):
        if(prev == None):
            return 0
        R = 6371 # Earth radius in kilometers

        cur_lat = concert.latitude
        cur_long = concert.longitude
        prev_lat = prev.latitude
        prev_long = prev.longitude

        #Use Haversine formula to calculate distance in km
        phi1 = math.radians(prev_lat)
        phi2 = math.radians(cur_lat)
        delta_phi = math.radians(cur_lat - prev_lat)
        delta_lambda = math.radians(cur_long - prev_long)

        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c



    def build_itinerary(self, concerts):
        itinerary = []
        allArtists = []
        oneConcertArtists = []
        modConcerts = []

        concertCount = {}
        concertDict = {}

        for c in concerts:
            #List to track all artist
            if(c.artist not in allArtists):
                allArtists.append(c.artist)
            #Dict for tracking number of concerts for each artist
            if(c.artist not in concertCount):
                concertCount[c.artist] = 1
            else:
                concertCount[c.artist] += 1
            #Dict for tracking which artists have clashing concerts
            if(datetime.fromisoformat(c.date) not in concertDict):
                concertDict[datetime.fromisoformat(c.date)] = [c]
            else:
                concertDict[datetime.fromisoformat(c.date)].append(c)

        #Find which artists only has one concert
        for artist in concertCount:
            if(concertCount[artist] == 1):
                oneConcertArtists.append(artist)

        #Ensure concerts are sorted by date
        tmp = dict(sorted(concertDict.items()))
        concertDict = tmp

        prev = None

        for date in concertDict:
            #If there are more than one concert on the day, check distance and if it's the only concert
            #of an artist
            if(len(concertDict[date]) > 1):
                #Arbitrary large number to ensure first distance is always shorter
                dist = 100000000
                closest = concertDict[date][0]
                #Go through all concerts on the given day
                for c in concertDict[date]:
                    #Calculate distance between previous and current concert
                    tmpDist = self.calc_distance(prev, c)
                    #If current is the artists only concert, and current closest has more,
                    #select current
                    if(closest.artist not in oneConcertArtists and c.artist in oneConcertArtists):
                        closest = c
                    #If current closest is the artists only concert, and current artist has more, 
                    #disregard current
                    elif(closest.artist in oneConcertArtists and c.artist not in oneConcertArtists):
                        pass
                    #If both artists only have one or both have more than one concert, use distance
                    #to determine which concert to add.
                    else:
                        if (tmpDist < dist):
                            dist = tmpDist
                            closest = c
                #Set prev for calulating distance for next iteration
                prev = closest
                modConcerts.append(closest)
            #If it's the only concert of the day, add the concert
            else:
                prev = concertDict[date][0]
                modConcerts.append(prev)

        #Loop through concerts to add them to itinerary
        for c in modConcerts:
            index = -1
            for i in range(len(itinerary)):
                #If artist is already in itinerary, save index of entry
                if(c.artist == itinerary[i].artist):
                    index = i
                    break
            #If artist is not in itinerary, add concert
            if(index == -1):
                itinerary.append(c)
            #If artist is in itinerary, compare dates and add the earliest
            else:
                newDate = datetime.fromisoformat(c.date)
                currentDate = datetime.fromisoformat(itinerary[index].date)
                if(newDate < currentDate):
                    itinerary[index] = c

        #Sort the itinerary by dates
        itinerary = self.quicksort(itinerary)

        #Check if all artists are included. If they're not in the itinerary, enter them with no concerts
        for a in allArtists:
            artistFound = False
            for c in itinerary:
                if(c.artist == a):
                    artistFound = True
                    break
            if(not artistFound):
                tmp = Concert(a, "No Concerts", "-", "-", "-")
                itinerary.append(tmp)
        return itinerary

if __name__ == "__main__":
    from concerts_data import get_all_concerts
    
    all_concerts = get_all_concerts()