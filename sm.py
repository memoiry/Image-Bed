import requests
import sys
import os
import os.path

if (len(sys.argv[1])>3):

	url = 'https://sm.ms/api/upload';

	path = '/users/xuguodong/desktop/figure/';
	files = {'smfile' : open(path+sys.argv[1], 'rb')};

	r = requests.post(url, files = files);

	data1 = eval(r.text.encode('utf-8'));

	url1 = data1['data']['url'];
	print url1

else:
	dir = '/users/xuguodong/desktop/figure/'
	l = os.listdir(dir)
	l.sort(key = lambda fn: os.path.getmtime(dir+fn) if not os.path.isdir(dir+fn) else 0)
	l.reverse()
	url = 'https://sm.ms/api/upload';
	url1 = []
	for i in range(int(sys.argv[1])):
		files = {'smfile' : open(dir+l[i], 'rb')};

		r = requests.post(url, files = files);

		data1 = eval(r.text.encode('utf-8'));

		url1.append(data1['data']['url']);
	for i in url1:
		print i



