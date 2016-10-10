#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib
import json
import eventlet
import uuid
import sys
import requests
import urllib
import urllib2
from flup.server.fcgi import WSGIServer


# from simpleauth.signature import AccessToken


def _process_data(method, url, headers, host, body=None):
    conn = httplib.HTTPConnection(host)
    # conn.set_debuglevel(1)
    conn.request(method, url, body, headers)
    try:
        response = conn.getresponse()
        data = response.read()
        return data
    except httplib.BadStatusLine as exc:
        exc_info = sys.exc_info()
        print exc_info[1]
    finally:
        conn.close()


        # urllib
        # url = 'http://%s%s' % (HOST, url)
        # req = urllib2.Request(url, body, headers)
        # response = urllib2.urlopen(req)
        # page = response.read()
        # return page

        # requests
        # url = 'http://%s%s' % (HOST, url)
        # r = requests.post(url, headers=headers, data=body)
        # return r.text


def process(host, port, url, method, body=None, token=None):
    headers = {"Content-Type": "application/json", "User-Agent": "python-novaclient", "Accept": "application/json"}
    if token is not None:
        headers.update({"X-Auth-Token": token})

    if body:
        body = json.dumps(body)

    host = '%s:%s' % (host, port)
    data = _process_data(method, url, headers, host, body)
    return data


