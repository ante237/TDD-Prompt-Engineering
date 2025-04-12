"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from datetime import datetime
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()
        
        self.all_concerts = get_all_concerts()
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """Some artists may have no concerts on the list. In that case, that should be indicated in the itinerary."""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        allArtists = []
        listedArtists = []

        for i in range(len(self.all_concerts)):
            if(self.all_concerts[i].artist not in allArtists):
                allArtists.append(self.all_concerts[i].artist)
        
        for j in range(len(itinerary)):
            if(itinerary[j].artist not in listedArtists):
                listedArtists.append(itinerary[j].artist)

        sortedAllArtists = sorted(allArtists)
        sortedListedArtists = sorted(listedArtists)

        self.assertTrue(itinerary)
        self.assertEqual(sortedAllArtists, sortedListedArtists)
        

    def test_manual_2(self):
        """The itinerary should return a list of concerts sorted in chronological order (by date from earliest to latest)"""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        for it in itinerary:
            it.print_class()
        dateList = []

        for i in range(len(itinerary)):
            dateList.append(datetime.fromisoformat(itinerary[i].date))

        self.assertTrue(itinerary)
        self.assertTrue(dateList == sorted(dateList))

    def test_manual_3(self):
        """An artist has at most one concert in the itinerary. If an artist has more than one concert in the list, the itinerary should only include the one with the earliest start date."""
        itinerary = self.builder.build_itinerary(self.all_concerts)
        foundArtists = []
        foundDupe = False
        onlyFirstDate = True
        concertDates = {}

        for c in self.all_concerts:
            if(c.artist not in concertDates):
                concertDates[c.artist] = [datetime.fromisoformat(c.date)]
            else:
                tmp = concertDates[c.artist]
                tmp.append(datetime.fromisoformat(c.date))
                concertDates[c.artist] = tmp

        for key in concertDates:
            concertDates[key] = sorted(concertDates[key])

        for i in range(len(itinerary)):
            if(itinerary[i].artist in foundArtists):
                foundDupe = True
                break
            date = datetime.fromisoformat(itinerary[i].date)
            if(date != concertDates[itinerary[i].artist][0]):
                onlyFirstDate = False
                break
            foundArtists.append(itinerary[i])

        self.assertTrue(itinerary)
        self.assertTrue(onlyFirstDate)
        self.assertFalse(foundDupe)


    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.


if __name__ == "__main__":
    unittest.main()