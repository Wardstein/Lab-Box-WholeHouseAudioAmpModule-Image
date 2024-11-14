import urllib.request
import json

# Few constants needed, central in case the JSON strings change at some point
SYSTEM_32BIT_STRING = "32-bit"
SYSTEM_64BIT_STRING = "64-bit"
TITLE_FILTER_STRING = "Lite"
TITLE_FILTER_NOT_STRING = "Legacy"

# Results
url32bitInfo = ""
url64bitInfo = ""

with urllib.request.urlopen("http://downloads.raspberrypi.org/operating-systems-categories.json") as url:
	jsonData = json.load(url)
# print(jsonData)

for entry in jsonData:
	# print(entry)
	for image in entry['images']:
		# print(image)
		if (TITLE_FILTER_STRING in image['title']) and (TITLE_FILTER_NOT_STRING not in image['title']):
			# print(image)
			if image['system'] == SYSTEM_32BIT_STRING:
				url32bitInfo = image
				break
			elif image['system'] == SYSTEM_64BIT_STRING:
				url64bitInfo = image
				break

# print(url32bitInfo)
# print(url64bitInfo)

output = { }
output['x32'] = url32bitInfo
output['x64'] = url64bitInfo
print(json.dumps(output))
