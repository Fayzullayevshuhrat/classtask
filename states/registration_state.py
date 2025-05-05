from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    name = State()
    age = State()
    phone = State()