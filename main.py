import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# بيانات البوت الأساسية
TOKEN = "8746113101:AAHScaAiiIhbAPWAJzhmw9Lp-pGdwK3XqQA"
ADMIN_ID = 6665332515

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("🛒 شراء حسابات فري فاير", callback_data="buy_ff"),
        InlineKeyboardButton("💳 الدفع عبر Binance Pay ID", callback_data="pay_binance"),
        InlineKeyboardButton("📞 التواصل مع الدعم", callback_data="support")
    )
    bot.send_message(message.chat.id, "أهلاً بك في متجر @smoke73_store_bot لحسابات فري فاير! اختر ما يناسبك:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "buy_ff":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "اختر الحساب المطلوب أو تواصل مع الدعم لمعرفة الأسعار والتفاصيل الحالية.")
    elif call.data == "pay_binance":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "طريقة الدفع:\nقم بتحويل المبلغ على Binance Pay ID الخاص بالمتجر، ثم قم بإرسال صورة إيصال التحويل هنا في الشات ليتم مراجعته وتأكيده من قبل الإدارة.")
    elif call.data == "support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "للدعم والاستفسار، سيتم الرد عليك في أقرب وقت.")

@bot.message_handler(content_types=['photo'])
def handle_receipt(message):
    bot.reply_to(message, "تم استلام الإيصال بنجاح! جاري تحويله للإدارة للمراجعة وتأكيد الطلب.")
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(ADMIN_ID, f"🔔 إيصال جديد من المستخدم: {message.from_user.id} (@{message.from_user.username})")

if __name__ == "__main__":
    bot.infinity_polling()
