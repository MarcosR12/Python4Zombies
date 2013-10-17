# urllib2_proxy_handler.py
#
# Author: Wayne Koorts
# Date:   27/10/2008
#
# Example for using urllib2.urlopen() with a proxy server requiring authentication
import urllib2
uri = "http://www.python.org"
http_proxy_server = "someproxyserver.com"
http_proxy_port = "3128"
http_proxy_realm = http_proxy_server # Worked in my (limited) testing environment.
http_proxy_user = "username"
http_proxy_passwd = "password"
# Next line = "http://username:password@someproxyserver.com:3128"
http_proxy_full_auth_string = "http://%s:%s@%s:%s" % (http_proxy_user,
                            http_proxy_passwd,
                            http_proxy_server,
                            http_proxy_port)
def open_url_no_proxy():
  urllib2.urlopen(uri)
  print "Apparent success without proxy server!"
def open_url_installed_opener():
  proxy_handler = urllib2.ProxyHandler({"http": http_proxy_full_auth_string})
  opener = urllib2.build_opener(proxy_handler)
  urllib2.install_opener(opener)
  urllib2.urlopen(uri)
  print "Apparent success through proxy server!"
if __name__ == "__main__":
  open_url_no_proxy()
  open_url_installed_opener()


