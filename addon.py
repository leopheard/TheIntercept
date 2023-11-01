from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theinterceptpodcasts

plugin = Plugin()

url0 = "http://api.spokenlayer.com/feed/channel/v1-intercept-news2-ext/3c9929b72538c12bd92ac6762f8d798b9d4e8cdca7692ea74f466061d01816cb"
url1 = "https://rss.prod.firstlook.media/deconstructed/podcast.rss"
url2 = "https://feeds.feedburner.com/InterceptedWithJeremyScahill"
url3 = "https://rss.prod.firstlook.media/murderville/podcast.rss"
url4 = "https://feeds.megaphone.fm/somebody"
url5 = "https://rss.art19.com/american-isis"

@plugin.route('/')
def main_menu():
    items = [
#        {
#            'label': plugin.get_string(30000), 
#            'path': plugin.url_for('spoken_edition'),
#            'thumbnail': "https://github.com/leopheard/thedeprogram/blob/master/resources/media/icon.jpg?raw=true"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_deconstructed'),
            'thumbnail': "https://github.com/leopheard/thedeprogram/blob/master/resources/media/2.jpg?raw=true"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_intercepted'),
            'thumbnail': "https://github.com/leopheard/thedeprogram/blob/master/resources/media/1.jpg?raw=true"},
{
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('all_murderGA'),
            'thumbnail': "https://github.com/leopheard/thedeprogram/blob/master/resources/media/3.jpg?raw=true"},
{
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('all_somebody'),
            'thumbnail': "https://github.com/leopheard/thedeprogram/blob/master/resources/media/4.jpg?raw=true"},
{
            'label': plugin.get_string(30005), 
            'path': plugin.url_for('all_americanisis'),
            'thumbnail': "https://content.production.cdn.art19.com/images/a3/dc/6f/f7/a3dc6ff7-5f36-445f-a563-f8adaf8d35e3/ae4e3bdb54d33f6bd9f9825359c3ff897014a2e903d12922f92e1b55ec934f9e2a285e3afff5ef27748f0517095f69683c8bac4ee1e4498b5913b5b880ab4897.jpeg"},
    ]
    return items

#@plugin.route('/spoken_edition/')
#def spoken_edition():
#    soup0 = theinterceptpodcasts.get_soup0(url0)
#    playable_podcast0 = theinterceptpodcasts.get_playable_podcast0(soup0)
#    items = theinterceptpodcasts.compile_playable_podcast0(playable_podcast0)
#    return items
@plugin.route('/all_deconstucted/')
def all_deconstructed():
    soup1 = theinterceptpodcasts.get_soup1(url1)
    playable_deconstructed = theinterceptpodcasts.get_playable_deconstructed(soup1)
    items = theinterceptpodcasts.compile_playable_deconstructed(playable_deconstructed)
    return items
@plugin.route('/all_intercepted/')
def all_intercepted():
    soup2 = theinterceptpodcasts.get_soup2(url2)
    playable_intercepted = theinterceptpodcasts.get_playable_intercepted(soup2)
    items = theinterceptpodcasts.compile_playable_intercepted(playable_intercepted)
    return items
@plugin.route('/all_murderGA/')
def all_murderGA():
    soup3 = theinterceptpodcasts.get_soup3(url3)
    playable_murderGA = theinterceptpodcasts.get_playable_murderGA(soup3)
    items = theinterceptpodcasts.compile_playable_murderGA(playable_murderGA)
    return items
@plugin.route('/all_somebody/')
def all_somebody():
    soup4 = theinterceptpodcasts.get_soup4(url4)
    playable_somebody = theinterceptpodcasts.get_playable_somebody(soup4)
    items = theinterceptpodcasts.compile_playable_somebody(playable_somebody)
    return items
@plugin.route('/all_americanisis/')
def all_americanisis():
    soup5 = theinterceptpodcasts.get_soup5(url5)
    playable_americanisis = theinterceptpodcasts.get_playable_americanisis(soup5)
    items = theinterceptpodcasts.compile_playable_americanisis(playable_americanisis)
    return items
if __name__ == '__main__':
    plugin.run()
