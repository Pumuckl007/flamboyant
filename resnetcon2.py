#!/usr/bin/python

import time
import subprocess

def group_by_header(items, head_filter, head_mapper = None):
    retval = {}
    cur_item = []
    cur_key = None
    for itm in items:
        if head_filter(itm):
            if cur_key is not None:
                retval[cur_key] = cur_item
            cur_item = []
            cur_key = itm if head_mapper is None else head_mapper(itm)
        cur_item.append(itm)
    if len(cur_item) > 0:
        retval[cur_key] = cur_item
    return retval

def get_mac():
    raw_output = subprocess.check_output(['ip', 'addr'])
    info = group_by_header(raw_output.split('\n'), lambda row: (not row.startswith(' ') and len(row) > 0), head_mapper = lambda header: header.split(' ')[1].strip(' :'))
    wifi_key = [k for k in info.keys() if k.startswith('w')][0]
    wifi_data = info[wifi_key]
    ether_row = [r.strip() for r in wifi_data if 'ether' in r]
    ether_mac = [r.split(' ')[1] for r in ether_row]
    return ether_mac[0]

def get_redirect_url():
    try:
        socket_handle = make_get('http://1.1.1.1')
        web_data = socket_handle.read()
        socket_handle.close()

        parts = web_data.split(' ')
        kv = dict([itm.split('=', 1) for itm in parts if '=' in itm])
        url = kv['URL'].split('"')[0]
        return url 
    except:
        return None


def check_default_count():
    output = subprocess.check_output("ip route", shell=True)
    lines = output.split('\n')
    defaults = [d for d in lines if d.startswith('default')]
    return len(defaults)

def clear_most_defaults():
    if check_default_count() <= 1:
        return 
    output = subprocess.check_output("ip route del default", shell=True)
    return output

def mylog(msg):
    #print(msg)
    pass

def auth_guest():
    USER = 'autoguest'
    PASS = 'autoguest'
    url = 'https://guest-login.ucsd.edu/login.html'

    mylog('Getting redirect URL.')

    redirect_url = get_redirect_url()
    if redirect_url is None: 
        mylog('Seems like we already authenticated.')
        return
    mylog('Generating form data.')
    action = dict([itm.split('=') for itm in redirect_url.split('?', 1)[1].split('&')]).get('switch_url') or url

    data = {
        'username':USER, 
        'password':PASS, 
        'redirect_url' : '8.8.8.8',
        'err_flag' : '-1',
        'buttonClicked' : '4',
        'action' : action
    }
    headers = {
        "Host":"guest-login.ucsd.edu", 
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
        "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding":"gzip, deflate, br",
        "Referer": redirect_url,
        "Content-Type":"application/x-www-form-urlencoded",
        "DNT":"1",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1",
        "Pragma":"no-cache", 
        "Cache-Control": "no-cache",
    }
    delay = 0 #seconds
    mylog('Making post.')
    return make_post(url=url, headers=headers, data=url_encode(data))

def make_post(*args, **kwargs):
    url = kwargs['url']
    headers = kwargs.get('headers') or {}
    data = kwargs.get('data') or ''
    try: 
        import urllib2 
        req = urllib2.Request(url, headers = headers, data = data)
    except ImportError:
        import urllib.request 
        req = urllib.request.Request(url, headers = headers, data = data)
    assert(req.get_method().upper() == 'POST')
    return urllib2.urlopen(req)

def make_get(*args, **kwargs):
    try:
        import urllib2
        return urllib2.urlopen(*args, **kwargs)
    except ImportError:
        import urllib.request
        return urllib.request.urlopen(*args, **kwargs)
def url_encode(data):
    try: 
        import urllib.parse
        return urllib.parse.urlencode(data)
    except ImportError:
        import urllib
        return urllib.urlencode(data)

clear_most_defaults()
auth_guest()
