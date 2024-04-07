from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menue = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тренировки🤸"), KeyboardButton(text="Питание🍴")],
        [KeyboardButton(text="Бонусы🎁"), KeyboardButton(text="Поддержка👩🏼‍💻")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

exercises = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Тренировки 1 неделя"), KeyboardButton(text="Тренировки 2 неделя")],
        [KeyboardButton(text="Тренировки 3 неделя"), KeyboardButton(text="Назад в главное меню")],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите неделю"
)

exercises_week1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 неделя - тренировка 1"), 
            KeyboardButton(text="1 неделя - тренировка 2")
        ],
        [
            KeyboardButton(text="1 неделя - тренировка 3"),
            KeyboardButton(text="1 неделя - тренировка 4")
        ],
        [KeyboardButton(text="Назад к выбору недели")],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите тренировку"
)

exercises_week2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2 неделя - тренировка 1"), 
            KeyboardButton(text="2 неделя - тренировка 2")
        ],
        [
            KeyboardButton(text="2 неделя - тренировка 3"),
            KeyboardButton(text="2 неделя - тренировка 4")
        ],
        [KeyboardButton(text="Назад к выбору недели")],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите тренировку"
)

exercises_week3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="3 неделя - тренировка 1"), 
            KeyboardButton(text="3 неделя - тренировка 2")
        ],
        [
            KeyboardButton(text="3 неделя - тренировка 3"),
            KeyboardButton(text="3 неделя - тренировка 4")
        ],
        [KeyboardButton(text="Назад к выбору недели")],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите тренировку"
)

nutrition = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рекомендации по питанию")],
        [
            KeyboardButton(text="Питание 1-я неделя"), 
            KeyboardButton(text="Питание 2-я неделя"), 
            KeyboardButton(text="Питание 3-я неделя")
        ],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите неделю"
)

bonuses = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="15 минут зарядки"), KeyboardButton(text="МФР")],
        [KeyboardButton(text="Гайд по пищевым добавкам")],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите ваш бонус"
)

jerks_bonus = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зарядка от отеков"), KeyboardButton(text="Зарядка на расслабление мышц шеи")],
        [KeyboardButton(text="Зарядка в кровати"), KeyboardButton(text="Назад к выбору зарядки")],
        [KeyboardButton(text="Назад в главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите зарядку"
)