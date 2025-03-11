
API_KEY = "8159376088:AAEkKcKTiPTD9dmITlW6YJoErgLJNw0XNjQ"
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters, CommandHandler
import os
import time
import random
updater = Updater(token=API_KEY, use_context=True)

def fn_start(update, context):
    # 키보드 버튼
    keyboard = [
        [InlineKeyboardButton("button 1", callback_data=1)]
        ,[InlineKeyboardButton("button 2", callback_data=2)]
        ,[InlineKeyboardButton("button 3", callback_data=3)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('choose one option:', reply_markup=reply_markup)

def fn_button(update, context):
    query = update.callback_query
    query.answer()
    i = 0
    text = ""
    while i < int(query.data):  # for i in range(cnt)
        lotto_num = set()
        while len(lotto_num) < 6:
            lotto_num.add(random.randint(1, 45))
        print(sorted(lotto_num))
        text +=str(sorted(lotto_num)) +"\n"
        i += 1
    user_id = update.effective_chat.id
    query.bot.send_message(chat_id=user_id, text=f'로또번호{query.data}개\n{text}')
    # query = update.callback_query
    # query.answer()
    # query.edit_message_text(text=f'selected option:{query.data}')

def echo(update, context) :
    user_id = update.effective_chat.id
    user_msg = update.message.text
    context.bot.send_message(chat_id=user_id, text=user_msg)

def diary(update, context):
    user_id = update.effective_chat.id
    user_msg = update.message.text
    with open('my_diary.txt', 'a', encoding='utf8') as f:
        f.write(user_msg.replace('/diary', '').strip())
        f.write('\n')
    context.bot.send_message(chat_id=user_id, text='다이어리 작성')

def save_photo(update, context):
    # 1. 폴더 체크
    img_dir = './myimg'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    # 2. 저장 이름
    filename = time.strftime('%Y%m%d%H%M%S') + '.png'
    img_path = os.path.join(img_dir, filename)
    # 3. 저장
    photo_id = update.message.photo[-1].file_id # 이미지 위치 가져오기
    photo_file = context.bot.getFile(photo_id)
    photo_file.download(img_path) # 저장
    update.message.reply_text('photo saved')

def get_photo(update, context):
    img_path = './test.png'
    user_id = update.effective_chat.id
    context.bot.send_photo(chat_id=user_id, photo=open(img_path, 'rb'))

# 사진 가져오기
updater.dispatcher.add_handler(CommandHandler('get', get_photo))
# 버튼
start_handler = CommandHandler('start', fn_start)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(fn_button))
# 사진저장 기능 추가
photo_handler = MessageHandler(Filters.photo, save_photo)
updater.dispatcher.add_handler(photo_handler)
# 다이어리 기능 추가
diary_handler = CommandHandler('diary', diary)
updater.dispatcher.add_handler(diary_handler)
# 응답 함수 등록
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)
print("bot 스타트")
updater.start_polling()
updater.idle()