import asyncio
import random
import uuid
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from aiogram.filters import CommandStart

# ======================
# Вставь сюда свой токен
# ======================
TOKEN = "8904746605:AAEW1yledAfEmIjaQ4DNcqki-Hzv1sGsP4c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список онигири
ONIGIRI = [
("-1487%", "Хитлер -- абсолютное зло."),
("-677%", "Хаменеи."),
("-666%", "Сатана."),
("-148%", "Ганс Ланда -- Вы укрываете у себя врагов рейха?."),
("-100%", "Путин -- я не подддерживаю политику ...."),
("-89.3%", "Аллах -- Акбар."),
("-14.87%", "Тамаев -- Ракетка."),
("-1%", "Иван Золо -- ыыы."),
("0%", "Дотер -- первый скилл и третий."),
("0.01%", "Я пришел со своим стулом."),
("1%", "Соловьев -- Просроченный еврей ."),
("2%", "Борат -- я в еврейском логове."),
("5%", "Человек-Паук 🕷️."),
("6.7%", "Мистер Бист."),
("10%", "Месси."),
("14.8%", "Меллстрой."),
("19.45%", "Сын свошника."),
("19.84%", "#Грр понедельник."),
("20.31%", "Годжу Сатору."),
("22.2%", "Это вот так солдатскую кашу клевать."),
("25%", "Моггед."),
("31%", "Эль Примо."),
("42%", "Глубина -- Мое ж плечо."),
("45%", "Ванзай -- начинается паника."),
("48.8%", "Остап Бендер -- Сын турецкоподданного."),
("50%", "Кадыров."),
("52%", "Панда По -- 451 км/ч."),
("66.6%", "Исраэль Йегуда -- 666."),
("67.67%", "Израильлендер -- Прыгай."),
("69%", "Пантера."),
("75%", "Роман Абрамович -- я куплю тебя."),
("88%", "Досс Десмонд -- пока рядовой Досс за нс помолится сэр."),
("91%", "Сергей Брин -- почему не яндекс?"),
("99%", "Зеленский -- чуть-чуть не хватило."),
("99.99%", "Иешуа."),
("100%", "Зигмунд Фрейд -- 💬🗨️💬🗨️"),
("100%", "Эйнштейн -- 🧠🧠🧠🧠🧠"),
("101%", "Нетаньяху -- ✊🇮🇱✊🇮🇱✊🇮🇱✊🇮🇱✊"),
("LitEnergy%", "Литвин -- экстримальчик да ты дорогой?"),
("ЦАХАЛ%", "Эяль Замир -- к вам летит ракета."),
("1000%", "Моисей."),
("1489%", "Иисус Христос."),

]

def make_result():
    name, desc = random.choice(ONIGIRI)
    text = f"🇮🇱 <b>Ты сегодня — {name}</b>\n\n{desc}"
    return name, text

@dp.message(CommandStart())
async def start(message: Message):
    me = await bot.get_me()
    await message.answer(
        f"Привет! 🇮🇱\n\n"
        f"Чтобы использовать бота, напиши в любом чате:\n"
        f"<code>@{me.username}</code>\n\n"
        f"И выбери результат.",
        parse_mode="HTML"
    )

@dp.inline_query()
async def inline_handler(query: InlineQuery):
    results = []

    # Генерируем 5 разных вариантов
    for _ in range(5):
        name, text = make_result()
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=f"🇮🇱           {name}",
                description="Нажми, чтобы отправить",
                input_message_content=InputTextMessageContent(
                    message_text=text,
                    parse_mode="HTML"
                )
            )
        )

    await query.answer(results, cache_time=1, is_personal=True)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
