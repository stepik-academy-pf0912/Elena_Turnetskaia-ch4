all_videos = [
    { "videotitle": "Concrete Candle Holder How To Make", "video_id": "Z_8Ss94fgZ" },
    { "videotitle": "How To Make a Concrete Fire Bowl", "video_id": "uSSp3X07Vls" }, 
    { "videotitle": "Diy LED Desk Lamp With Concrete Base", "video_id":"a5yiMhJaGCo" },  
]

playlists = [
    {
        "playlist_title": "Поделки из бетона",
        "videos": [0],
    },
    {
        "playlist_title": "Поделки из дерева",
        "videos": [0,2],
    },
    {
        "playlist_title": "Изготовление мебели",
        "videos": [1],
    },
    {
        "playlist_title": "Новости сельской жизни",
        "videos": [0,1,2],
    },
]

def entry_point():
    """
    Начало ввода и проверка на правильность
    """
    while True:
        human_ans, fun = start()
        decision_switcher(human_ans, fun)
    

def start():
    """
    Стартовое сообщение пользователю о выборе между видео и плейлистом 
    """    
    return """Привет, это  портал по видео про строительстве.
Введите 1 чтобы посмотреть видео и 2 чтобы посмотреть плейлист. """, playlists_or_videos


def decision_switcher(output_msg, fun = None):
    """
    при подаче сообщения в output_msg выплюнет его на экран с последующим пользовательским вводом
    """

    if fun is None:
        print(output_msg)
        input("Приятного просмотра!")
        exit()
    else:
        try:
            human_ans = int(input(output_msg)) # вывод сообщения из output_msg и ожидание ввода пользователя
        except ValueError: # если пользователь ввел не цифру, то будет ошибка
            user_input_error()
        output_msg, fun = fun(human_ans) # выполнение переданной функции, результат которой снова кортеж
        decision_switcher(output_msg, fun) # тут еще и рекурсия( 

def playlists_or_videos(human_ans):
    """
     Выбор пользователя
    """
    if human_ans == 1:
        return videos_decision() # просмотр вcего списка видео
    elif human_ans == 2:
        return playlist_decision() # просмотр списка плейлистов
    else:
        user_input_error()


def playlist_decision():
    """
    Список плейлистов
    """
    print("Выберите плейлист")
    output = ""
    #сообщение со списком плейлистов
    for i, playlist in enumerate(playlists, start=1): # Перебор в циклах с функцией enumerate (подсказали, что есть)
        output += "{n}. {name}({pl_len} видео)\n".format(
            n = i,
            name = playlist["playlist_title"],
            pl_len = len(playlist["videos"]),
            )
    return output, videos_decision


def videos_decision(ans=None):
    """
    Функция для подготовки списка видео
    """
    # оказалось сложно для меня, помогли
    try:
        num_of_videos = range(len(all_videos)) if ans is None else playlists[ans-1]["videos"] 
        print("Название выбранных видео: ") # Сообщение о переходе на выбор видео
        output = ""
        # составление списка видео
        for i, video_num in enumerate(num_of_videos, start=1): 
            output += "{n}. {name}\n".format(
                n = i,
                name = all_videos[video_num]["videotitle"],
                )
    except IndexError:
        user_input_error()
    return output, concrete_video

            
def concrete_video(video_num):
    """
    Сообщение для пользователя с информацией о конкретном видео
    """
    try:
        output = "Title\n{video_title}\n{video_id}\n".format(
            video_title = all_videos[video_num-1]["videotitle"],
            video_id = all_videos[video_num-1]["video_id"],
            )
    except IndexError:
        user_input_error()
    return output, None        
    
def user_input_error():
    print("Ошибка ввода параметров. Программа будет закрыта") 
    exit() # выход из программы
    
if __name__ == "__main__":

    entry_point()
    exit()
# Сначала написала условными операторами. Потом переписывала. ушло почти четыре дня. Долго искала функции и решения. Задание сложное.