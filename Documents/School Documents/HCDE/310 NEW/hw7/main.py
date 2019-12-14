#!/usr/bin/env python
#
# this is a modified version of the Google App Engine Tutorial
import webapp2, os, urllib2, json, jinja2, logging, urllib, logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('hw7template.html')

        #this part will need to be re-written to accept user input
        tag = "tuxedo_cat"
        photos = [Photo(getPhotoInfo(pid)) for pid in getPhotoIDs("tuxedo_cat")]

        tvals = {'results': {}, 'tag': tag}
        # byviews
        tvals['results']['views'] = sorted(photos, key=lambda x: x.numViews, reverse=True)[:3]
        tvals['results']['tags'] = sorted(photos, key=lambda x: len(x.tags), reverse=True)[:3]
        tvals['results']['comments'] = sorted(photos, key=lambda x: x.commentcount, reverse=True)[:3]

        self.response.write(template.render(tvals))

class Photo():
    """A photo from Flickr"""
    def __init__(self,photoInfo):
        self.title = photoInfo["title"]["_content"]
        self.author = photoInfo["owner"]["username"]
        self.userid = photoInfo["owner"]["nsid"]
        self.tags = [tag["_content"] for tag in photoInfo["tags"]["tag"]]
        self.commentcount = int(photoInfo["comments"]["_content"])
        self.numViews = int(photoInfo["views"])
        self.url = photoInfo["urls"]["url"][0]["_content"]
       # self.thumbnailURL =

    def __str__(self):
        fmtstr = "\n~~~ {} ~~~\n author: {}\n number of tags: {}\n views: {}\n comments: {}\n"
        return fmtstr.format(self.title,self.author,str(len(self.tags)),self.numViews,self.commentcount)

### flickrREST from s10



def flickrREST(baseurl='https://api.flickr.com/services/rest',
               method='flickr.photos.search',
               api_key='#7a5d10e35788ab02875635c0a1417795',
               format='json',
               params={},
               printurl=False
               ):
    params['method'] = method
    params['api_key'] = api_key
    params['format'] = format
    if format == "json":
        params['nojsoncallback'] = True
    url = baseurl + "?" + urllib.urlencode(params)
    if printurl:
        logging.info(url)
    return safeGet(url)


### safeGet from last time
def safeGet(url):
    try:
        return urllib2.urlopen(url)
    except urllib2.URLError as e:
        if hasattr(e, "code"):
            logging.error("The server couldn't fulfill the request lol.")
            logging.error("Error code: ", e.code)
        elif hasattr(e, 'reason'):
            logging.error("We failed to reach a server")
            logging.error("Reason: ", e.reason)
        return None


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


def getPhotoIDs(tag, n = 100):
    params = {}
    params["tags"] = tag
    params["per_page"] = n
    result = json.load(flickrREST(params=params))

    return [item["id"] for item in result["photos"]["photo"]]


def makePhotoURL(pd):
    ## get a photo url, following documentation at https://www.flickr.com/services/api/misc.urls.html
    url = "https://farm%s.staticflickr.com/%s/%s_%s_q.jpg" % (pd['farm'], pd['server'], pd['id'], pd['secret'])
    return url


def getPhotoInfo(photoID):
    params = {}
    params["photo_id"] = photoID
    method = "flickr.photos.getInfo"

    return json.load(flickrREST(method=method,params=params))['photo']


application = webapp2.WSGIApplication([('/', MainHandler)], debug=True)