from ..rerequest import TemplateRequest

def get_playerinfo_url(v):
	import urllib

	quoted_path = urllib.quote_plus(v['req_url'])
	return { 'req_url': 'http://sverigesradio.se/sida/ajax/getplayerinfo?url=%s&isios=false&playertype=flash' % quoted_path }

sr = { 'title': 'SR', 'url': 'http://sr.se/', 'feed_url': 'http://sverigesradio.se/api/rss/broadcast/516',
				'items': [ TemplateRequest(
							re = r'(http://)?(www\.)?sverigesradio\.se/(?P<req_url>.+)',
							encode_vars = lambda v: { 'req_url': 'http://sverigesradio.se/%(req_url)s' % v } ),
						TemplateRequest(
							re = r'<ref href="(?P<final_url>[^"]+)"')] }

sr2014 = { 'items': [ TemplateRequest(
							re = r'(http://)?(www\.)?sverigesradio\.se(?P<req_url>.+)',
							encode_vars = get_playerinfo_url ),
						TemplateRequest(
							re = r'"Quality":(?P<bitrate>[0-9]+),"Url":"(?P<url>https?://[^"]+)"',
							encode_vars = lambda v: { 'final_url': '%(url)s' % v,
												'quality': '%s kbps' % (str(int(v['bitrate'])/1000)),
												'suffix-hint': 'm4a' })] }

services = [sr,
			sr2014]