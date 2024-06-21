from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theintercept

plugin = Plugin()

url1 = "https://feeds.acast.com/public/shows/1d1223a2-9d05-473b-9e79-c2b65b71d676" #DECONSTRUCTED#
url2 = "https://feeds.acast.com/public/shows/f5b64019-68c3-57d4-b70b-043e63e5cbf6" #INTERCEPTED#
url3 = "https://feeds.acast.com/public/shows/c66d3932-72a5-49e9-bc88-ca2080d23735" #MURDER GA#
url4 = "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/5a115af8-776f-41c9-bf1b-ae300188d281/d3d0764f-3b72-4554-b783-ae300188d28f/podcast.rss" #SOMEBODY#

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_deconstructed'),
            'thumbnail': "https://github.com/leopheard/TheIntercept/blob/master/resources/media/1.jpg?raw=true"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_intercepted'),
            'thumbnail': "https://github.com/leopheard/TheIntercept/blob/master/resources/media/2.jpg?raw=true"},
{
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('all_murderGA'),
            'thumbnail': "https://github.com/leopheard/TheIntercept/blob/master/resources/media/3.jpg?raw=true"},
{
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('all_somebody'),
            'thumbnail': "https://github.com/leopheard/TheIntercept/blob/master/resources/media/4.jpg?raw=true"},
    ]
    return items

@plugin.route('/all_deconstucted/')
def all_deconstructed():
    soup1 = theintercept.get_soup1(url1)
    playable_deconstructed = theintercept.get_playable_deconstructed(soup1)
    items = theintercept.compile_playable_deconstructed(playable_deconstructed)
    return items
@plugin.route('/all_intercepted/')
def all_intercepted():
    soup2 = theintercept.get_soup2(url2)
    playable_intercepted = theintercept.get_playable_intercepted(soup2)
    items = theintercept.compile_playable_intercepted(playable_intercepted)
    return items
@plugin.route('/all_murderGA/')
def all_murderGA():
    soup3 = theintercept.get_soup3(url3)
    playable_murderGA = theintercept.get_playable_murderGA(soup3)
    items = theintercept.compile_playable_murderGA(playable_murderGA)
    return items
@plugin.route('/all_somebody/')
def all_somebody():
    soup4 = theintercept.get_soup4(url4)
    playable_somebody = theintercept.get_playable_somebody(soup4)
    items = theintercept.compile_playable_somebody(playable_somebody)
    return items
if __name__ == '__main__':
    plugin.run()
