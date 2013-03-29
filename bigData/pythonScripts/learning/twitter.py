import twitter
import oauth2 as oauth
import time
import json
from pprint import pprint

def oauth_req(url, key, secret, http_method="GET", post_body="",
        http_headers=None):
    consumer = oauth.Consumer(key="JhUqKJiU1OJG39epBzGT6g", secret="AD4QJWFXa8wc8CDVd2jbZ04bVuLrsMR4RROsNZA73zg")
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)

    resp, content = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers
    )
    return content

home_timeline = oauth_req(
  'http://search.twitter.com/search.json?q=blue%20angels',
  '144773310-19CfBxYWmLVGHYhe7xCSK42YnAAFrBd7zfFOIeXS',
  'NNZGyDgZjy1KqPK7z3pticOIhrCOKoSlSdZMdgg44LY'
)

print home_timeline

#data = json.load(home_timeline)
#pprint(data)


