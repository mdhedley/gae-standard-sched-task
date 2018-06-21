import webapp2
from pyweatherscraper.scraper import WeatherScraper

class MainPage(webapp2.RequestHandler):
    def get(self):
        print('test')
        WeatherScraper().storeWeather()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Complete!')


app = webapp2.WSGIApplication([('/scraper',MainPage)], debug=True)
