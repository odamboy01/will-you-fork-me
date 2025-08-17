import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random

from pressywinki import main as menu
import pressywinki as t
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    first = message.from_user.first_name  # faqat ismi olinadi

    await message.answer(
        f"AI psixologga xush kelibsiz, {first}! 👋\n"
        "Quyidagi tugmalardan birini tanlang 👇",
        reply_markup=menu
    )


motivation_responses = [
    "✨ Harakat qil, orzularing sari yaqinlashasan!",
    "🚀 Qattiq mehnat qilgan odam hech qachon yutqazmaydi.",
    "🔥 Har kuni oz bo‘lsa ham qadam tashla.",
    "🌱 Vaqt o‘tishi bilan mehnating meva beradi.",
    "💪 Mashaqqatli yo‘llar buyuk natijaga olib keladi.",
    "🏆 Kichik g‘alabalar katta muvaffaqiyatlarga olib boradi.",
    "⚡ O‘zingga ishonsang, hamma narsa mumkin.",
    "🌟 Harakat qilmasang, hech narsa o‘zgarmaydi.",
    "📈 Bugun qilgan ishing ertangi kunga ta’sir qiladi.",
    "🌍 Sen o‘z hayoting muallifisan.",
    "⏳ Sabr va izchillik – muvaffaqiyat kaliti.",
    "🔥 Mehnat qilsang, natija o‘zi keladi.",
    "💡 Xatolar – bu saboqlar.",
    "🌞 Har tong – yangi imkoniyat.",
    "💥 O‘tmish xatolaring seni to‘xtatmasin.",
    "🕊️ Tinimsiz harakat barqarorlikni beradi.",
    "🚴 Sekin bo‘lsa ham, oldinga yur!",
    "🌄 Yaxshi narsalar vaqt talab qiladi.",
    "👊 Senga hammasi qo‘lidan keladi!",
    "🎯 Maqsadingdan chalg‘ima."
]
depression_responses = [
    "💙 Sen yolg‘iz emassan.",
    "🤝 Yaqinlaring bilan gaplash, ular seni qo‘llab-quvvatlaydi.",
    "🌤 Qorong‘i tun ham oxir-oqibat tongga aylanadi.",
    "🙏 O‘zingni ayblama, hamma odam qiynaladi.",
    "💡 Yaxshi kunlar oldinda kutmoqda.",
    "📖 O‘zingni yaxshi narsalar bilan chalg‘itishga harakat qil.",
    "🕊 Nafas ol, bosqichma-bosqich oldinga yur.",
    "🌱 Vaqt bilan hamma og‘irlik yengillashadi.",
    "💬 Ichingdagini yozib qo‘y – yengil tortasan.",
    "☀️ Har tong yangi imkoniyat olib keladi.",
    "❤️ O‘zingni qadrlashni unutmang.",
    "🚶 Bir oz sayr qil – kayfiyating o‘zgaradi.",
    "🎶 Sevimli musiqangni eshit.",
    "🌸 Sen muhim va qadrli odamsan.",
    "💤 Yetarli dam ol.",
    "🍵 Bir piyola issiq choy ham ruhni yengillashtiradi.",
    "🌍 Sen dunyoga kerakli odamsan.",
    "🖊 Fikrlaringni qog‘ozga yoz.",
    "👂 Yaqiningga dardini aytishdan qo‘rqma.",
    "✨ O‘ziga mehribon bo‘l."
]
funfacts_responses = [
    "🤯 Asalarilar inson yuzini taniy oladi.",
    "🐢 Ba’zi toshbaqalar dumlari orqali nafas oladi.",
    "🌍 Dunyo okeanlarining 80% hali o‘rganilmagan.",
    "🐨 Koalalar kuniga 20 soat uxlaydi.",
    "🍍 Ananas pishishi uchun 2 yil kerak bo‘ladi.",
    "🐙 Ahtapotlarning 3 ta yuragi bor.",
    "🌌 Osmonda qumdan ko‘p yulduzlar bor.",
    "🦒 Jirafaning tilining uzunligi 50 sm dan oshadi.",
    "🦋 Kapalaklar oyoqlari bilan ta’m sezadi.",
    "🦘 Kengurular orqaga yurisholmaydi.",
    "🐶 Itlarning burun izi inson barmoq izi kabi noyob.",
    "🐦 Qarg‘alar odam yuzini eslab qoladi.",
    "🍌 Banan rezavor, lekin qulupnay emas.",
    "🐟 Ko‘plab baliqlar uxlamaydi.",
    "🐄 Sigirlarning eng yaqin do‘stlari bo‘ladi.",
    "🚀 Saturn va Yupiterda olmos yog‘adi.",
    "🌋 Vezuviy vulqoni milodiy 79 yilda Portseyni ko‘mgan.",
    "🦦 Dengiz otlari bir-birining qo‘lini ushlab uxlaydi.",
    "🐌 Ba’zi salyangozlar 3 yil uxlaydi.",
    "🧊 Antarktida Yer yuzidagi eng quruq joy."
]
health_responses = [
    "🥦 Ko‘proq sabzavot iste’mol qiling.",
    "💧 Har kuni kamida 2 litr suv iching.",
    "🚶‍♂️ Har kuni 30 daqiqa piyoda yuring.",
    "😴 7-8 soat uxlang.",
    "🍎 Har kuni meva yeyishga odatlaning.",
    "🏃‍♂️ Jismoniy mashq stressni kamaytiradi.",
    "🧘‍♀️ Nafas mashqlari tinchlantiradi.",
    "🚭 Chekishdan saqlaning.",
    "🥗 Qovurilgan ovqatni kamaytiring.",
    "🍵 Choy va suv – ichimliklar ichida eng foydalisi.",
    "🦷 Tishlaringni kuniga ikki marta yuv.",
    "📱 Uxlashdan oldin telefonni chetga qo‘ying.",
    "😃 Ko‘proq kuling – bu sog‘liq uchun foydali.",
    "🍋 Vitaminlarga boy ovqatlar iste’mol qiling.",
    "🛌 Uxlash rejimini tartibga soling.",
    "🚰 Sovuq suv ichish hazmni sekinlashtiradi.",
    "🍫 Shirinlikni me’yorida iste’mol qiling.",
    "🍽 Ovqatni tez emas, sekin yeying.",
    "🌳 Tabiatda sayr qilish asabni tinchlantiradi.",
    "🙌 Qo‘llaringizni tez-tez yuving."
]
randomtips_responses = [
    "💡 Katta ishni kichik qismlarga bo‘ling.",
    "📖 Har kuni 10 bet kitob o‘qing.",
    "🗒 Vazifalaringizni yozib boring.",
    "⏰ 25 daqiqa ishlang, 5 daqiqa tanaffus qiling (Pomodoro).",
    "🎧 O‘qiyotganda musiqani o‘chirib qo‘ying.",
    "📝 Maqsadlaringizni yozib qo‘ying.",
    "🙅 Kechiktirishni odat qilmang.",
    "🚶 Ish orasida bir oz yuring.",
    "📱 Keraksiz notifikatsiyalarni o‘chirib qo‘ying.",
    "🌐 Bir vaqtning o‘zida bitta ish qiling.",
    "🍀 Uchta narsaga minnatdorchilik yozing.",
    "👨‍🏫 Boshqalarga o‘rgatish – eng yaxshi o‘rganish yo‘li.",
    "📂 Fayllaringizni tartibga soling.",
    "🛑 Yo‘q deyishni o‘rganing.",
    "🧩 Yangi narsalarni sinab ko‘ring.",
    "📊 Har kuni qilgan ishlaringizni tahlil qiling.",
    "🌙 Kechasi uzoq ishlashdan saqlaning.",
    "📅 Haftalik reja tuzing.",
    "🧹 Ish joyingizni toza tuting.",
    "🔑 Intizom – muvaffaqiyat kaliti."
]


# 🌟 Motivatsiya
@dp.message(F.text == "🌟 Motivatsiya")
async def motivation(message: Message):
    await message.answer(random.choice(motivation_responses))

# 😔 Depressiya
@dp.message(F.text == "😔 Depressiya")
async def depression(message: Message):
    await message.answer(random.choice(depression_responses))

# 🤓 Fun Facts
@dp.message(F.text == "🤓 Qiziqarli faktlar")
async def funfacts(message: Message):
    await message.answer(random.choice(funfacts_responses))

# 💪 Health Tips
@dp.message(F.text == "💪 Sog'lomlik maslahatlari")
async def health(message: Message):
    await message.answer(random.choice(health_responses))

# 🎲 Random Tip
@dp.message(F.text == "🎲 Xar xil maslahatlar")
async def randomtip(message: Message):
    await message.answer(random.choice(randomtips_responses))
@dp.message(F.text == "Bot egasi")
async def owner(message: Message):
    await message.answer(
        "Bot egasi: Muhammadjon Iskandarov\n"
        "Telegram: @mkingboi\n"
        "instagram: @iskandarvx7\n")
# --- Run Bot ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
