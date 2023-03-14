## Reference to `robots.txt`

- [ ] Check `/robots.txt` <br>
	`It is too late now, but this is where I begun.`
	<br>
	![robots](https://user-images.githubusercontent.com/93029180/210171042-e723014c-26ad-427f-89cf-64469edc0c7e.png)

<br>

## Reference to Web Archive
- [ ] We see the format of a date - `20221225193927` and the intro told us about an internet archive. <br>
	Check the format used by the Web Archive: https://en.wikipedia.org/wiki/Template:Webarchive. <br><br>
	And form the final link: http://web.archive.org/web/20221225193927/http://165.227.164.122/robots.txt.
	![oldrobots](https://user-images.githubusercontent.com/93029180/210171146-47dbd930-26b2-4641-a2c7-6984825743dc.png)

<br>

## Now what?
- [ ] Once you get to the site archive, view the source code and, at the bottom, find a comment. <br>
- [ ] Decode recursively `base64` encoded string
	```bash
	dec="Vm0wd2QyVkhVWGhVYmxKV1YwZDRXRmxVUm5kVlJscHpXa2M1VjFKdGVGWlZNbmhQWVd4S2MxTnNX
	bGRTTTFKUVdWY3hTMUl4V25GVQpiR2hvVFZWd1ZWZFdaRFJUTWsxNFZHNU9hUXBTTUZwVVZtcEti
	MlZXV25KWk0yaFVUVlUxV0ZWdE5VdFpVWEJUWW10S1dWWnRNVFJXCmJWWkhWMWhvV0dKWVVsVlVW
	bHB6VGtaVmVVNVZaRmRrTTBKd1ZUQldTMlJzV2tkWk0yaHBDazFXV2xoWGExcHJWMGRLVmxkc1Zs
	VlcKTTAxNFZqRmFWMk15UmtsYVJuQldWMFZLVlZkWGVHdGlNV1JYV2tab2JGSXdXbFJEYXpGRlVX
	cFNXR0V4Y0haWlZFWktaREZrZFZGcwpjR2tLVW01Q2IxWnRjRWRWYlZaSFdraE9ZVkp0VWxOV01G
	WkxaREZhZEdWSFJtdE5WMUo2VmpKNGIySkdTWHBSYkVKRVlrVndWbFZ0CmVHOVdNa3BaWVVab1Yy
	RXlVa3hXTVZwSFl6Rktjd3BhUjJ0TFZqQmFTMVJXV25OVmEyUnFUV3hLV1ZVeGFIZFpWa3B6VTI1
	S1ZWWXoKUW5WVWJGcEdaVlpzTm1KR1JsWldlbWMxVVRKak9WQlJiejBLCg=="
	
	for i in {1..10}; do dec=$(<<<"$dec" base64 -d); echo $dec; echo; done
	```

<br><br>

## Flag:
`flag{robots_will_take_over}`
