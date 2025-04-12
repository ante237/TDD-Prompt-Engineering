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

    def build_itinerary(self, concerts):
        itinerary = []

        for c in concerts:
            index = -1
            for i in range(len(itinerary)):
                if(c.artist == itinerary[i].artist):
                    index = i
                    break
            if(index == -1):
                itinerary.append(c)
            else:
                currentDate = datetime.fromisoformat(c.date)
                newDate = datetime.fromisoformat(itinerary[index].date)
                if(newDate > currentDate):
                    itinerary[index] = c


        itinerary = self.quicksort(itinerary)
        return itinerary

if __name__ == "__main__":
    from concerts_data import get_all_concerts
    
    all_concerts = get_all_concerts()