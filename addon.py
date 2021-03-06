from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theinterceptpodcasts

plugin = Plugin()

url0 = "http://api.spokenlayer.com/feed/channel/v1-intercept-news2-ext/3c9929b72538c12bd92ac6762f8d798b9d4e8cdca7692ea74f466061d01816cb"
url1 = "https://feeds.megaphone.fm/deconstructed"
url2 = "https://feeds.megaphone.fm/intercepted"
url3 = "https://rss.prod.firstlook.media/murderville/podcast.rss"
url4 = "https://feeds.megaphone.fm/somebody"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('spoken_edition'),
            'thumbnail': "http://media.spokenlayer.com/cover-art/2016/10/01/the-intercept-v2-10-1-1400x1400.png"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_deconstructed'),
            'thumbnail': "https://static.megaphone.fm/podcasts/fcf98d00-1c11-11e8-bf47-4b460462a564/image/uploads_2F1544117246770-vb6r1xfm1ib-4762e5a8199166b03554b9b67a5d7bb2_2FDeconstructed_COVER-with-logo.png"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_intercepted'),
            'thumbnail': "https://static.megaphone.fm/podcasts/d5735a50-d904-11e6-8532-73c7de466ea6/image/uploads_2F1544117316918-ix7o6i7vnto-6a6e5ad7be02dd89be56d2081ae5e859_2FIntercepted_COVER-with-logo.png"},
{
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('all_murderGA'),
            'thumbnail': "https://theintercept-static.imgix.net/usq/490edc26-8485-4094-a20c-dc4ce70207b1/1dcfad38-a2d0-4e29-a86b-4420b3980e4b.jpeg?auto=compress,format&cs=srgb&dpr=2&h=440&w=440&fit=crop&crop=faces%2Cedges&_=7f3dc1b866c965bc3eee2890e79e85c3"},
{
            'label': plugin.get_string(30004), 
            'path': plugin.url_for('all_somebody'),
            'thumbnail': "https://theintercept-static.imgix.net/usq/0358703b-24aa-419c-984b-0aac81374882/0358703b-24aa-419c-984b-0aac81374882.jpeg?auto=compress,format&cs=srgb&dpr=2&h=440&w=440&fit=crop&crop=faces%2Cedges&_=e934a62b34025675868e4fd8713eb29e"},
    ]
    return items

@plugin.route('/spoken_edition/')
def spoken_edition():
    soup0 = theinterceptpodcasts.get_soup0(url0)
    playable_podcast0 = theinterceptpodcasts.get_playable_podcast0(soup0)
    items = theinterceptpodcasts.compile_playable_podcast0(playable_podcast0)
    return items
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
if __name__ == '__main__':
    plugin.run()
