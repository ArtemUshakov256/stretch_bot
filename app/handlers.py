import asyncio
import logging

import app.keyboards as kb
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()

#---------------------Main menue starts---------------------
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Приветственный текст (заменить).",
        reply_markup=kb.main_menue
    )

@router.message(F.text == "Назад в главное меню")
async def back_to_main_menue(message: Message):
    await message.answer(
        "Вы вернулись в гравное меню.",
        reply_markup=kb.main_menue
    )
#---------------------Main menue ends---------------------

#---------------------Exercises block starts---------------------
@router.message(F.text == "Тренировки🤸")
@router.message(F.text == "Назад к выбору недели")
async def choose_exercise_week(message: Message):
    await message.answer(
        "Выберите неделю.",
        reply_markup=kb.exercises
    )

@router.message(F.text == "Тренировки 1 неделя")
async def choose_exercise_week1(message: Message):
    await message.answer(
        "Выберите тренировку.",
        reply_markup=kb.exercises_week1
    )

@router.message(F.text == "Тренировки 2 неделя")
async def choose_exercise_week2(message: Message):
    await message.answer(
        "Выберите тренировку.",
        reply_markup=kb.exercises_week2
    )

@router.message(F.text == "Тренировки 3 неделя")
async def choose_exercise_week3(message: Message):
    await message.answer(
        "Выберите тренировку.",
        reply_markup=kb.exercises_week3
    )

@router.message(F.text == "1 неделя - тренировка 1")
async def send_exercise1_week1(message: Message):
    await message.answer("Твоя тренировка №1")
    await message.answer("https://youtu.be/4IziwJSKxrg?si=Q9EZV3ddbQNqtCF6")

@router.message(F.text == "1 неделя - тренировка 2")
async def send_exercise2_week1(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "1 неделя - тренировка 3")
async def send_exercise3_week1(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "1 неделя - тренировка 4")
async def send_exercise4_week1(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "2 неделя - тренировка 1")
async def send_exercise1_week2(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "2 неделя - тренировка 2")
async def send_exercise2_week2(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "2 неделя - тренировка 3")
async def send_exercise3_week2(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "2 неделя - тренировка 4")
async def send_exercise4_week2(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "3 неделя - тренировка 1")
async def send_exercise1_week3(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "3 неделя - тренировка 2")
async def send_exercise2_week3(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "3 неделя - тренировка 3")
async def send_exercise3_week3(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "3 неделя - тренировка 4")
async def send_exercise4_week3(message: Message):
    await message.reply(
        "Пусто"
    )
#---------------------Exercises block ends---------------------

#---------------------Nutrition block starts---------------------
@router.message(F.text == "Питание🍴")
async def choose_nutrition_week(message: Message):
    await message.answer(
        "Выберете необходимый рацион.",
        reply_markup=kb.nutrition
    )

@router.message(F.text == "Рекомендации по питанию")
async def send_nutrition_recommendation(message: Message):
    await message.reply(
        "Вот рекомендация по питанию."
    )

@router.message(F.text == "Питание 1-я неделя")
async def send_nutrition_week1(message: Message):
    await message.reply(
        "Вот питание на 1 неделю"
    )

@router.message(F.text == "Питание 2-я неделя")
async def send_nutrition_week2(message: Message):
    await message.reply(
        "Вот питание на 2 неделю"
    )

@router.message(F.text == "Питание 3-я неделя")
async def send_nutrition_week3(message: Message):
    await message.reply(
        "Вот питание на 3 неделю"
    )
#---------------------Nutrition block ends---------------------

#---------------------Bonuses block starts---------------------
@router.message(F.text == "Бонусы🎁")
@router.message(F.text == "Назад к выбору зарядки")
async def choose_bonus(message: Message):
    await message.answer(
        "Выберете бонус.",
        reply_markup=kb.bonuses
    )

@router.message(F.text == "15 минут зарядки")
async def choose_jerk(message: Message):
    await message.answer(
        "Выберете зарядку.",
        reply_markup=kb.jerks_bonus
    )

@router.message(F.text == "Зарядка от отеков")
async def send_anti_ederma_jerk(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "Зарядка на расслабление мышц шеи")
async def send_neck_relaxation_jerk(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "Зарядка в кровати")
async def send_bed_jerk(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "Гайд по пищевым добавкам")
async def send_supplement_guide(message: Message):
    await message.reply(
        "Пусто"
    )

@router.message(F.text == "МФР")
async def send_yoga(message: Message):
    await message.reply(
        "Пусто"
    )
#---------------------Bonuses block ends---------------------

@router.message(F.text == "Поддержка👩🏼‍💻")
async def exercises(message: Message):
    await message.answer(
        "Напишите ваш запрос и мы рассмотрим его."
    )