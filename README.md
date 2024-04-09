# MobileDogs

### Идея проекта:
Проект "Mobile Dogs" представляет собой систему для отслеживания бездомных собак с помощью носимых устройств (ошейников). 
Каждый пользователь может выбрать себе некоторое количество бездомных собак для отслеживания. 
Персонал устанавливает новые ошейники на бездомных собак. 
Пользователи могут наблюдать за собаками, давать задания другим пользователям, а также получать данные о собаках через приложение.
Персонал устанавливает новые ошейники на бездомных собак. 
Есть базовые станции LoRa для связи носимых устройств (ошейников). 
Есть регистрация пользователей и ошейников. Носимые устройства регистрирует только персонал.

### Сценарии:

1. Регистрация пользователей:
     * Пользователи могут зарегистрироваться, указав свои данные и получив уникальный идентификатор.
3. Регистрация ошейников:
     * Персонал может зарегистрировать новые ошейники, присваивая им уникальные идентификаторы и привязывая к конкретным собакам.
3. Привязка ошейников и пользователей:
     * Пользователи могут "привязывать" зарегистрированные ошейники к своему аккаунту для отслеживания конкретных собак.
4. Оповещение пользователей:
     * Пользователи получают данные о местоположении и состоянии собак через приложение.
5. Модерирование:
     * Персонал следит за состоянием ошейников, информацией о пользователях и собаках, и при необходимости, модерирует контент, а также решает возникающие проблемы и вопросы.
6. Задание от одних пользователям другим:
     * Пользователи могут давать задания другим пользователям по уходу за определенными собаками, кормлением или выполнению других действий.
7. Верификация выполнения заданий:
     * Пользователи отправляют фото или другие доказательства выполнения задания, а тот пользователь, который отправил задание, подтверждает достоверность и выполнение.

### Необходимые запросы для реализации сценариев:
1. POST request для регистрации пользователей
     * *id_user, login, password, email, gender, phone, birthday(?)*
3. POST request для регистрации ошейников
     * *id_collar, name_dog, temp, feeling_hungry(?), health_status*
5. POST request для привязки ошейников и пользователей
     * *id_user, id_collar*
7. GET request для отправки оповещений пользователям
     * *id_user, text_alert*
9. POST и DELETE request для модерации пользователей и данных
     * delete - *id_user/id_collar*
     * post(изменение состояния собаки) - *id_collar, temp, feeling_hungry, health_status*
11. POST request для создания заданий для пользователей
     * *id_user_1, id_user_2, id_task, text_task(?)*
13. GET request для проверки верификации выполненных заданий
     * *id_user_1, id_user_2, id_task, confirm(true/false)*

### Инструкции для установки зависимостей и запуска приложения:
   *в разработке*





