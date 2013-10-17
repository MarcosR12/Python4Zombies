# urllib2_proxy_handler.py
#
# Author: Wayne Koorts
# Date:   27/10/2008
#
# Example for using urllib2.urlopen() with a proxy server requiring authentication
'''
17/10/2013 - ubb3rsith
Conversion of python2 to python3
First, try connect without proxy...if raise some Exception, call proxy authentication function
Json Killer mode on ;]
'''
import urllib.request #substitution for the urllib2 lib of python2
import json

uri = "http://api.icndb.com/jokes/random?limitTo=[nerdy]" #Chuck Norris jokes... ;]
http_proxy_server = "someproxyserver"
http_proxy_port = "port"
http_proxy_realm = http_proxy_server # Worked in my (limited) testing environment.
http_proxy_user = "user"
http_proxy_passwd = "passwd"
# Next line = "http://username:password@someproxyserver.com:3128"
http_proxy_full_auth_string = "http://%s:%s@%s:%s" % (http_proxy_user,
                            http_proxy_passwd,
                            http_proxy_server,
                            http_proxy_port)
def open_url_no_proxy():
  try:
    urllib.request.urlopen(uri)
    print ("Apparent success without proxy server!")
  except Exception:
    #try open url with proxy authentication
    open_url_installed_opener()
  finally:
    pass
  
def open_url_installed_opener():
  proxy_handler = urllib.request.ProxyHandler({"http": http_proxy_full_auth_string})
  opener = urllib.request.build_opener(proxy_handler)
  urllib.request.install_opener(opener)
  resp = urllib.request.urlopen(uri).read()
  data = data = json.loads(resp.decode('utf-8'))
  print(data['value']['joke'])

if __name__ == "__main__":
  open_url_no_proxy()
