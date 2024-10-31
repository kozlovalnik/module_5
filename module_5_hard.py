from operator import index
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password  = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.time_now = 0
        self.duration = duration
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in users:
            if user.nickname == nickname and self.password == hash(password):
                self.current_user = user
                break

    def register(self, nickname, password, age):
        user_found = False
        for user in self.users:
            if user.nickname == nickname:
                user_found = True
                print(f'Пользователь {nickname} уже существует')
                break
        if not user_found:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)

    def log_out(self):
        current_user = None

    def add(self, *args):
        for i in range(len(args)):
            video_found = False
            for j in range(len(self.videos)):
                if self.videos[j].title == args[i].title:
                    video_found = True
            if not video_found:
                self.videos.append(args[i])

    def get_videos(self, _str = ''):
        video_list = []
        for i in range(len(self.videos)):
            if self.videos[i].title.lower().find(_str.lower()) != -1:
                video_list.append(self.videos[i].title)
        return video_list

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in range(len(self.videos)):
            if self.videos[i].title == title:
                if self.videos[i].adult_mode:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return

                    for j in range(self.videos[i].duration):
                        sleep(1)
                        print(j+1, end = ' ')
                    print('Конец видео')
                    break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
