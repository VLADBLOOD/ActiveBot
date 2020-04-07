import random
import vk_api

from new_meetup import create_meetup
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='22131dd1d466179b244ce42c5288fabfe4e116fbf5eea1a459eb29d12457b9bc30bb2be7bbc4ab75583a6')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

        if event.text == 'Начать' or event.text == 'Старт' or event.text == 'Привет':
            vk.messages.send(user_id=event.user_id,
                             message='Привет, я БОТ Актива Двора! Я помогу тебе создавать встречи!',
                             keyboard=open("keyboards/default.json", "r", encoding="UTF-8").read(),
                             random_id=random.randint(1, 2147483647))

        elif event.text == 'Оставить заявку':
            vk.messages.send(user_id=event.user_id,
                             message='Заполните, пожалуйста, заявку!',
                             keyboard=open("keyboards/meetup.json", "r", encoding="UTF-8").read(),
                             random_id=random.randint(1, 2147483647))
            create_meetup()

        #else:
        #    vk.messages.send(user_id=event.user_id,
        #                     message='Извини, я тебя не понял!',
        #                     random_id=random.randint(1, 2147483647))
