#!/usr/bin/env python

import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Stimulate an HTTPS server vulnerable to Heartbleed')
    parser.add_argument('-a', action = 'store', default = '127.0.0.1',
        type = str,
        help = 'Address of server to be fed with data. Default is 127.0.0.1.')
    parser.add_argument('-u', action = 'store', default = 'admin',
        type = str,
        help = 'Username. Default is admin.')
    parser.add_argument('-p', action = 'store', default = 'letmein',
        type = str,
        help = 'Password. Default is letmein.')
    args = parser.parse_args()
    print(args.a)
    user = args.u
    password = args.p
    print('Calling server. User:%s, password:%s' % (user, password))
    subprocess.call([
    	'curl',
        '--insecure',
        '-d',
        'user=%s&password=%s' % (user, password),
        '-A',
        'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;)',
        '-w',
        '%{http_code} %{url_effective} %{size_request}\n',
        'https://%s' % args.a,
        '-o',
        '/dev/null',
    ])
    print("DONE!")