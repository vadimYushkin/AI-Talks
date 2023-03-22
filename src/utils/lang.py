from dataclasses import dataclass
from typing import List


# Parent data class
@dataclass
class Locale:
    ai_role_options: List[str]
    ai_role_prefix: str
    title: str
    language: str
    lang_code: str
    donates: str
    donates1: str
    donates2: str
    chat_placeholder: str
    chat_btn1: str
    chat_btn2: str
    select_placeholder1: str
    select_placeholder2: str
    stt_placeholder: str


# Child data class for English
@dataclass
class EnLocale(Locale):
    ai_role_prefix: str = "You are a"
    title: str = "AI Talks"
    language: str = "English"
    lang_code: str = "en"
    donates: str = "Donates"
    donates1: str = "Russia"
    donates2: str = "World"
    chat_placeholder: str = "Start Your Conversation With AI:"
    chat_btn1: str = "Rerun"
    chat_btn2: str = "Clear Conversation"
    select_placeholder1: str = "Select AI Model"
    select_placeholder2: str = "Select AI Role"
    stt_placeholder: str = "To Hear The Voice Of AI, Press Play"


# Child data class for Russian
@dataclass
class RuLocale(Locale):
    ai_role_prefix: str = "Вы"
    title: str = "Разговорчики с ИИ"
    language: str = "Russian"
    lang_code: str = "ru"
    donates: str = "Поддержать Проект"
    donates1: str = "Россия"
    donates2: str = "Остальной Мир"
    chat_placeholder: str = "Начните Вашу Беседу с ИИ:"
    chat_btn1: str = "Перезапустить"
    chat_btn2: str = "Очистить Беседу"
    select_placeholder1: str = "Выберите Модель ИИ"
    select_placeholder2: str = "Выберите Роль ИИ"
    stt_placeholder: str = "Чтобы Услышать ИИ Нажми Кнопку Проигрывателя"


AI_ROLE_OPTIONS_EN = [
    "helpful assistant",
    "code assistant",
    "code reviewer",
    "text improver",
    "cinema expert",
    "sport expert",
    "online games expert",
    "food recipes expert",
    "English grammar expert",
    "friendly and helpful teaching assistant. You explain concepts in great depth using simple terms, and you give examples to help people learn. At the end of each explanation, you ask a question to check for understanding",  # NOQA: E501
    "laconic assistant. You reply with brief, to-the-point answers with no elaboration",
    "helpful, pattern-following assistant",
    "helpful, pattern-following assistant that translates corporate jargon into plain English",
]

AI_ROLE_OPTIONS_RU = [
    "ассистент, который готов помочь",
    "ассистент программиста",
    "рецензент кода программиста",
    "эксперт по улучшению текста",
    "эксперт по кинематографу",
    "эксперт в области спорта",
    "эксперт в онлайн-играх",
    "эксперт по рецептам блюд",
    "эксперт по английской грамматике",
    "эксперт по русской грамматике",
    "дружелюбный и полезный помощник преподавателя. Вы объясняете концепции в подробностях, используя простые термины, и даёте примеры, чтобы помочь людям научиться. В конце каждого объяснения вы задаете вопрос, чтобы проверить понимание",  # NOQA: E501
    "лаконичный помощник. Вы отвечаете краткими, по существу ответами без лишних слов",
    "полезный помощник, следующий шаблонам",
    "полезный помощник, следующий шаблонам, который переводит корпоративный жаргон на простой английский",
]

en = EnLocale(ai_role_options=AI_ROLE_OPTIONS_EN)
ru = RuLocale(ai_role_options=AI_ROLE_OPTIONS_RU)