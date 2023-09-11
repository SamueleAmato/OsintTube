import requests
import re

def youtube_subscriber_count(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	followers = (response.text[response.text.index("Subscribers</p></div><p class=")+30:response.text.index("Subscribers</p></div><p class=")+80])
	return (followers[followers.index(">", 2)+1:followers.index("</p>", 1)])

def youtube_video_views_count(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	views = (response.text[response.text.index('The total video views count and its change in the last 30 days'):response.text.index('The total video views count and its change in the last 30 days')+200])
	return (views[186:len(views)]).replace("</p><p", "")

def youtube_video_duration(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	duration = (response.text[response.text.index('The average duration of the last 15 videos'):response.text.index('The average duration of the last 15 videos')+200])
	return (duration[184:len(duration)]+" min.").replace("<!-- --> <!", "")

def youtube_estimate_earnings(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	earnings = (response.text[response.text.index('An estimated value based on a default category'):response.text.index('An estimated value based on a default category')+400])
	return ("$"+earnings[218:len(earnings)]).replace('</p><div class="mb-0 inline-flex items-center gap-2 text-xs text-[#FF4273]"><div><span class="content-[&quot; &quot;] block h-2 w-2 rounded-sm bg-[#F', "").replace("<!-- -->", "").replace("<!-- -->", "").replace(">", "").replace('</p<div class="mb-0 inline-flex items-center gap-2 text-xs text-[#07E092]"<div<span class="content-[&quot; &quot;] block h-2 w-2 rounded-sm bg-[#07E0', "").replace('F427', "")

def youtube_channel_location(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	location = (response.text[response.text.index('class="mb-0">Location</p></div><p class="mb-0 text-right text-white">'):response.text.index('class="mb-0">Location</p></div><p class="mb-0 text-right text-white">')+400])
	return (location[69:len(location)]).replace('</p></div><div class="flex items-center justify-between gap-4 text-sm font-medium"><div class="text-vidiq-body-gray inline-flex items-center gap-[6px]"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M10 3H4a1 1 0 0 0-1 1v6', "")

def youtube_channel_join_date(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	join_date = (response.text[response.text.index('-0">Joined</p></div><p class="mb-0 text-right text-white">'):response.text.index('-0">Joined</p></div><p class="mb-0 text-right text-white">')+400])
	return (join_date[58:len(join_date)]).replace('</p></div><div class="flex items-center justify-between gap-4 text-sm font-medium"><div class="text-vidiq-body-gray inline-flex items-center gap-[6px]"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M12 14c2.206 0 4-1.794 4-4s', "")

def youtube_channel_category(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	category = (response.text[response.text.index('Category</p></div><p class="mb-0 text-right text-white">'):response.text.index('Category</p></div><p class="mb-0 text-right text-white">')+400])
	return (category[56:len(category)]).replace('</p></div><div class="flex items-center justify-between gap-4 text-sm font-medium"><div class="text-vidiq-body-gray inline-flex items-center gap-[6px]"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M18 7c0-1.103-.897-2-2-2H4c-1.10', "").replace('</p></div><div class="flex items-center justify-between gap-4 text-sm font-medium"><div class="text-vidiq-body-gray inline-flex items-center gap-[6px]"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M18 7c0-1.103-.897-2-2-2H4c-', "")

def youtube_video_count(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	video_count = (response.text[response.text.index('mb-0">Videos</p></div><p class="mb-0 text-right text-white">'):response.text.index('mb-0">Videos</p></div><p class="mb-0 text-right text-white">')+400])
	return (video_count[60:len(video_count)]).replace('</p></div><div class="flex items-center justify-between gap-4 text-sm font-medium"><div class="text-vidiq-body-gray inline-flex items-center gap-[6px]"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="18" width="18" xmlns="http://www.w3.org/2000/svg"><pat', "")

def youtube_description(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	description = (response.text[response.text.index('ollbar-hide mb-4 h-full text-ellipsis text-sm font-medium text-white transition-all duration-150 ease-in-out line-clamp-3 max-h-20">'):response.text.index('ollbar-hide mb-4 h-full text-ellipsis text-sm font-medium text-white transition-all duration-150 ease-in-out line-clamp-3 max-h-20">')+600])
	return (description[132:len(description)]).replace('</p></div></div><style data-emotion="css b4e621">@media (min-width: 0px){.css-b4e621{border-radius:10px;background:var(--vidiq-dark-500);color:#fff;padding:1rem;border:1px solid var(--vidiq-dark-300);}@media (max-width: 768px){.css-b4e621{padding:0.75rem;}}}</style><', "").replace('</p></div></div><style data-emotion="css b4e621">@media (min-width: 0px){.css-b4e621{border-radius:10px;background:var(--vidiq-dark-500);color:#fff;padding:1rem;border:1px solid var(--vidi', "").replace("q-dark-300", "").replace("</p></div></div><style dat", "")

def youtube_username(id):
	response = requests.get(f'https://vidiq.com/youtube-stats/channel/{id}/')
	username = (response.text[response.text.index('<title>'):response.text.index('<title>')+60]).replace(''''s YouTube Stats and Insights - vidIQ YouTube Stats"''', "").replace("<title>", "").replace("q-dark-300", "").replace("'s YouTube Stats and Insights - vidIQ YouTube Stats</title><meta p", "").replace("'s YouTube Stats and Insights - vidIQ YouTube Stats</title><m", "").replace("'s", "").replace("YouTube Stats and Insights", "").replace("- vidIQ YouTube", "").replace("- vidIQ", "").replace("YouT", "").replace("Stats</title><meta", "")

	return username

