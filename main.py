import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from hh import keep_alive
from gates import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
stopuser = {}
token = '6788433246:AAEyjRFC23VnSWHq3qfu4dwJ3E_Qgrk7jt4'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin= 7166322352
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
			keyboard.add(contact_button)
			random_number = random.randint(1, 92)
			photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	random_number = random.randint(1, 92)
	photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
	bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b> 
𝗧𝗛𝗘𝗦𝗘 𝗔𝗥𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 
━━━━━━━━━━━━
𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 > <code>/chk number|mm|yy|cvc</code>
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━
3𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 > <code>/vbv number|mm|yy|cvc</code>
𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━
𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 > <code>/str number|mm|yy|cvc</code>
𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━
𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 > <code>/au number|mm|yy|cvc</code>
𝗢𝗡𝗟𝗜𝗡𝗘 ✅
━━━━━━━━━━━━
/redeem
𝗪𝗘 𝗪𝗜𝗟𝗟 𝗕𝗘 𝗔𝗗𝗗𝗜𝗡𝗚 𝗦𝗢𝗠𝗘 𝗚𝗔𝗧𝗘𝗪𝗔𝗬𝗦 𝗔𝗡𝗗 𝗧𝗢𝗢𝗟𝗦 𝗦𝗢𝗢𝗡</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/y_vclub_own8r")
			keyboard.add(contact_button)
			random_number = random.randint(1, 92)
			photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 𝑾𝑬𝑬𝑲 > 300𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 950𝑬𝑮

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 𝑾𝑬𝑬𝑲 ➜  8
1 𝑴𝑶𝑵𝑻𝑯 ➜  30

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
			keyboard.add(contact_button)
			random_number = random.randint(1, 92)
			photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 𝑾𝑬𝑬𝑲 > 300𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 950𝑬𝑮

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 𝑾𝑬𝑬𝑲 ➜  8 
1 𝑴𝑶𝑵𝑻𝑯 ➜  30

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
			keyboard.add(contact_button)
			random_number = random.randint(1, 92)
			photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🏴‍☠️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 🏴‍☠️",callback_data='br')
		sw = types.InlineKeyboardButton(text=f" 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 🪽",callback_data='str')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @vclub_own8r')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Donation Confirmation' in last or 'This page doesn t seem to exist' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 🇪🇬🇵🇸 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @vclub_own8r''', reply_markup=mes)
					
					msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					if  'Donation Confirmation'  in last or  'This page doesn t seem to exist'  in last:
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last or 'Card Issuer Declined CVV' in last or '' in last or 'cvc was incorrect' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(15)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @vclub_own8r')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @vclub_own8r')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 🇪🇬🇵🇸 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @vclub_own8r''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {cc[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @vclub_own8r</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @vclub_own8r')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.au') or message.text.lower().startswith('/au'))
def respond_to_vbv(message):
	gate='stripe Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 3:
			bot.reply_to(message, f"<b>Try again after {3-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(scc(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='Braintree Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 3:
			bot.reply_to(message, f"<b>Try again after {3-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	gate='stripe charge'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 3:
			bot.reply_to(message, f"<b>Try again after {3-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(st(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "Card Issuer Declined CVV" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𝗘𝗕𝗡𝗘𝗟𝗡𝗘𝗚𝗠 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='EBNELNEGM-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3D Lookup'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 
𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗜𝗧, 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗔 𝗪𝗘𝗘𝗞𝗟𝗬 𝗢𝗥 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 

𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗝𝗢𝗕 𝗜𝗦 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 𝗖𝗔𝗥𝗗𝗦

𝗕𝗢𝗧 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗣𝗥𝗜𝗖𝗘𝗦:
 
𝙓ًَِِ 𝙐ًٍَََِِ 𝙎ًََٕٓ 𝘼 𓂀
━━━━━━━━━━━━
𝗪𝗢𝗥𝗟𝗗𝗪𝗜𝗗𝗘 » 𝗨𝗦𝗗𝗧 🌍
1 𝗪𝗘𝗘𝗞 » 10$ 
1 𝗠𝗢𝗡𝗧𝗛 » 30$
━━━━━━━━━━━━

𝗖𝗟𝗜𝗖𝗞 /cmds 𝗧𝗢 𝗩𝗜𝗘𝗪 𝗧𝗛𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

𝗬𝗢𝗨𝗥 𝗣𝗟𝗔𝗡 𝗡𝗢𝗪 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/vclub_own8r")
		keyboard.add(contact_button)
		random_number = random.randint(1, 92)
		photo_url = f'https://t.me/EBNELNEGM10/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url,
caption='''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		response = requests.post(
		f'https://rimuruchkbot.alwaysdata.net/vbv.php?bin={cc}')
		last=(response.json()['result'])
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
CC -> <code>{cc}</code>
Gateway -> {gate}
Response -> {last}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {card_type} - {brand}
Bank -> {bank}
Counrty -> {country} - {country_flag} 
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @vclub_own8r
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
keep_alive()
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
