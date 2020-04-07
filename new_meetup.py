import random
import vk_api
import time
from user_bot import bot_post
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='22131dd1d466179b244ce42c5288fabfe4e116fbf5eea1a459eb29d12457b9bc30bb2be7bbc4ab75583a6')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

keyboard = VkKeyboard()

meetup_message = ''
meetup_date = ''
meetup_time = ''
meetup_inventory = ''


def create_meetup():

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            # Текст встречи
            if event.text == 'Текст встречи':
                vk.messages.send(user_id=event.user_id,
                                 message='Отлично, укажи текст для вашей встречи!',
                                 random_id=random.randint(1, 2147483647))
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                        global meetup_message
                        meetup_message = event.text
                        vk.messages.send(user_id=event.user_id,
                                         message='Идём дальше!',
                                         keyboard=open("keyboards/meetup.json", "r", encoding="UTF-8").read(),
                                         random_id=random.randint(1, 2147483647))
                        break
            # День встречи
            elif event.text == 'День встречи':
                vk.messages.send(user_id=event.user_id,
                                 message='Укажите цифрой день месяца!',
                                 random_id=random.randint(1, 2147483647))
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                        global meetup_date
                        meetup_date = event.text
                        vk.messages.send(user_id=event.user_id,
                                         message='Отлично, еще пункт!',
                                         keyboard=open("keyboards/meetup.json", "r", encoding="UTF-8").read(),
                                         random_id=random.randint(1, 2147483647))
                        break
            # Время встречи
            elif event.text == 'Время встречи':
                vk.messages.send(user_id=event.user_id,
                                 message='Укажите время встречи в любом формате',
                                 random_id=random.randint(1, 2147483647))
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                        global meetup_time
                        meetup_time = event.text
                        vk.messages.send(user_id=event.user_id,
                                         message='Так держать, еще пункт!',
                                         keyboard=open("keyboards/meetup.json", "r", encoding="UTF-8").read(),
                                         random_id=random.randint(1, 2147483647))
                        break
            # Тип мяча
            elif event.text == 'Тип мяча':
                vk.messages.send(user_id=event.user_id,
                                 message='Выберите мячь!',
                                 keyboard=open("keyboards/inventory_type.json", "r", encoding="UTF-8").read(),
                                 random_id=random.randint(1, 2147483647))
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                        global meetup_inventory
                        meetup_inventory = event.text
                        vk.messages.send(user_id=event.user_id,
                                         message='Осталось опбликовать!',
                                         keyboard=open("keyboards/meetup.json", "r", encoding="UTF-8").read(),
                                         random_id=random.randint(1, 2147483647))
                        break
            # Опубликовать пост
            elif event.text == 'Опубликовать':
                vk.messages.send(user_id=event.user_id,
                                 message='Пост успешно опубликован!',
                                 keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read(),
                                 random_id=random.randint(1, 2147483647))

                bot_post(meetup_message, meetup_date, meetup_time, meetup_inventory)
                break
            # Отменить публикацию
            elif event.text == 'Отменить':
                vk.messages.send(user_id=event.user_id,
                                 message='Нет, так нет, приходи еще!',
                                 keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read(),
                                 random_id=random.randint(1, 2147483647))
                break
    #        else:
    #            vk.messages.send(user_id=event.user_id,
    #                             message='Я вас не понял! попробуйте еще раз',
    #                             keyboard=open("keyboards/meetup.json", "r", encoding="UTF-8").read(),
    #                             random_id=random.randint(1, 2147483647))
