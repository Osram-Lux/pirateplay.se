from ..rerequest import TemplateRequest
from common import redirect_handler

init_req = TemplateRequest( re = r'(?P<req_url>(http://)?(www\.)?dr\.dk/.+)' )

stream_re = r'"Uri":"(?P<req_url>%s[^"]+\.%s[^"]*)"'


#Request chains

rtmp = { 'title': 'DR-TV', 'url': 'http://dr.dk/tv',
				'items': [init_req,
						TemplateRequest(
							re = r'videoData:\s+{.+?resource:\s+"(?P<req_url>[^"]+)"',
							handlerchain = redirect_handler()),
						TemplateRequest( re = r'Location: (?P<req_url>.*?)\n' ),
						TemplateRequest(
							re = r'"uri":"(?P<rtmp_base>rtmpe?:\\/\\/vod\.dr\.dk\\/cms\\/)(?P<rtmp_path>[^"]+).*?"bitrateKbps":(?P<bitrate>\d+)',
							encode_vars = lambda v: { 'final_url': ('%(rtmp_base)s playpath=%(rtmp_path)s swfVfy=1 swfUrl=http://www.dr.dk/assets/swf/program-player.swf' % v).replace('\\', ''),
														'quality': '%(bitrate)s kbps' % v,
														'suffix-hint': 'flv' })] }

hls = { 'items': [init_req,
						TemplateRequest(
							re = r'data-resource="(?P<req_url>[^"]+)"',
							handlerchain = redirect_handler()),
						TemplateRequest( re = r'Location: (?P<req_url>.*?)\n' ),
						TemplateRequest(
							re = r'"MimeType":"text/vtt;charset=utf-8",.*?"Uri":"(?P<subtitles>http?://[^"]+)'),
						TemplateRequest(
							re = r'"Uri":"(?P<url>http?://[^"]+).*?"FileFormat":"(?P<format>[^"]+).*?"Bitrate":(?P<bitrate>\d+)',
							encode_vars = lambda v: { 'final_url': '%(url)s' % v,
														'quality': '%s kbps' % (str(int(v['bitrate']))),
														'suffix-hint': v['format'] })] }
hls2 = { 'items': [init_req,
						TemplateRequest(
							re = r'data-resource="(?P<req_url>[^"]+)"',
							handlerchain = redirect_handler()),
						TemplateRequest( re = r'Location: (?P<req_url>.*?)\n' ),
						TemplateRequest(
							re = r'"MimeType":"text/vtt;charset=utf-8",.*?"Uri":"(?P<subtitles>http?://[^"]+)'),
						TemplateRequest(
							re = stream_re % ('http://', 'm3u8')),
						TemplateRequest(
							re = r'BANDWIDTH=(?P<bitrate>\d+).*?RESOLUTION=(?P<resolution>\d+x\d+).*?(?P<url>https?://[^\n]+)',
							encode_vars = lambda v: { 'final_url': '%(url)s' % v,
														'quality': '%s kbps' % (str(int(v['bitrate'])/1000)),
														'suffix-hint': 'mp4' })] }

services = [rtmp,
			hls,
			hls2]