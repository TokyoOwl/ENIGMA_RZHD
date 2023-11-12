import flet as ft
from flet import *
from flet_core import TextButton
from end import *
logo = Image(src="img/image_3.png", width=200, height=100)
google_image = Image(src="img/image_4.png", width=70, height=70)
telegram_image = Image(src="img/image_5.png", width=70, height=70)
vk_image = Image(src="img/image_6.png", width=70, height=70)
BG='#292929'
FG='#D71E1E'
class Message():
    def __init__(self, text: str, message_type: str):
        self.text = text
        self.message_type = message_type
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment="start"
        self.alignment="end"
        self.controls=[
                Column(
                    [
                        ft.Text(message.text, selectable=True),
                    ],
                    tight=True,
                    spacing=5,
                ),
            ]
def Page(page: ft.Page):
    page.window_width = 400
    page.window_height = 900
    def increase_try(e):
        send_message_click(e)
        txt_number.value = str(int(txt_number.value) + 1)
        percent_number.value = str(int(rigth_answers.value)/int(txt_number.value)*100)
    def send_message_click(e):
        if new_message.value != "":
            chat.controls.append(Text(new_message.value))
            chat.controls.append(Text(f_inp(new_message.value)))
            if f_inp(new_message.value)=="Верно" or f_inp(new_message.value)[:7]=="Неверно":
                chat.controls.append(Text(g_q()))
            if f_inp(new_message.value) == "Верно":
                rigth_answers.value = str(int(rigth_answers.value) + 1)
            new_message.value = ""
            new_message.focus()
            page.update()
    def start_dialog_click(e):
        chat.controls.append(Text(g_q()))
        new_message.value = ""
        new_message.focus()
        page.update()
    chat = ListView(
        expand=True,
        spacing=10,
        auto_scroll=True
    )
    chat_container = Container(
        width=360,
        height=700,
        content=chat,
        border=border.all(1, ft.colors.OUTLINE),
        border_radius=15,
        padding=10,
        expand=True,
    )
    new_message = TextField(
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=2,
        filled=True,
        expand=True,
    )
    def create_new_dialog(e):
        page.go('/chat')
        chat.clean()
        page.update()
    send_button = IconButton(icon=ft.icons.SEND, on_click=increase_try, height=60, width=70)
    message_func = Container(
        content=Row([new_message, send_button], vertical_alignment="end")
    )
    new_dialog_button = ElevatedButton(text="Создать новый диалог",  color='White', on_click=create_new_dialog, bgcolor=FG, height=70, width=350)
    rigth_answers = TextField(value="0")
    percent_number = TextField(value="0", text_align="center", width=100, height=70, bgcolor=BG, color='White',suffix_icon=ft.icons.PERCENT_OUTLINED)
    txt_number = TextField(value="0", text_align="center", width=70, height=70, bgcolor=BG, color='White')
    settings_button = IconButton(icon=ft.icons.SETTINGS)
    start_button = ElevatedButton(text="Начать", color='White', on_click=start_dialog_click, bgcolor=FG)
    menu_button = IconButton(icon=ft.icons.MENU, on_click=lambda _: page.go('/menu'))
    google_button = IconButton(content=google_image, on_click=lambda _: page.go('/chat'))
    has_account_button = TextButton(text="Уже есть аккаунт? Войдите", on_click=lambda _: page.go('/'))
    telegram_button = IconButton(content=telegram_image, on_click=lambda _: page.go('/chat'))
    vk_button = IconButton(content=vk_image, on_click=lambda _: page.go('/chat'))
    or_divider = Row([ft.Divider(), Text("or"), ft.Divider()], alignment="center")
    name_field = TextField(label="Имя", color=None, keyboard_type=ft.KeyboardType.NAME, bgcolor=BG, prefix_icon=ft.icons.ACCOUNT_CIRCLE)
    email_field = TextField(label="Почта", keyboard_type=ft.KeyboardType.EMAIL, bgcolor=BG, prefix_icon=ft.icons.MAIL)
    password_field = TextField(label="Пароль", color='white', password=True, bgcolor=BG, prefix_icon=ft.icons.LOCK)
    login_button = ElevatedButton(text="Войти", color='white', on_click=lambda _: page.go('/chat'), bgcolor=FG)
    signup_button = ElevatedButton(text="Зарегистрироваться", color='white', on_click=lambda _: page.go('/chat'), bgcolor=FG)
    no_account_button = TextButton(text="Нет аккаунта? Зарегистрируйтесь", on_click=lambda _: page.go('/register'))
    forgot_password = Text("Забыли пароль?", style="subtitle1")
    back_button = IconButton(icon=ft.icons.ARROW_BACK,on_click=lambda _: page.go('/chat'))
    menu = Container(
        content=Row([menu_button, start_button, settings_button], alignment="center", spacing=100),
    )

    page_1 = Container(
       content = Column(
           controls=[
           Row([logo], alignment="center"),
           Row([google_button, telegram_button, vk_button], alignment="center"),
           or_divider,
           email_field,
           password_field,
           forgot_password,
           Row([login_button],alignment="center"),
           no_account_button,
           ],
           spacing=10,
        alignment = "center",
       )
    )
    page_2 = Container(
        content = Column(
            controls=[
                Row([logo], alignment="center"),
                Row([google_button, telegram_button, vk_button], alignment="center"),
                or_divider,
                name_field,
                email_field,
                password_field,
                Row([signup_button],alignment="center"),
                has_account_button,
            ],
            alignment="center",
            spacing=10
        )
    )
    page_3 = Container(
        content= Column(
            controls=[
                menu,
                Stack(
                   controls= [
                        chat_container
                    ]
                ),
                message_func,
            ],
        )
    )
    page_4 = Container(
        content= Column(
            controls=[
                Row([back_button, settings_button], spacing=270, alignment="center"),
                Text("Количество попыток"),
                txt_number,
                Text("Процент правильных ответов"),
                percent_number,
                Container(
                    height=400,
                ),
                Text("Новый диалог"),
                Row([new_dialog_button], alignment="center", vertical_alignment="end"),
            ]
        )
    )
    container = Container(
    content = Column(
        controls=
            [
                page_1,
            ],
        alignment="center",
        )
    )
    pages = {
        '/': View(
            "/",
            [
                container
            ],
        ),
        '/register': View(
            "/register",
            [
                page_2
            ],
        ),
        '/chat': View(
            "/chat",
            [
                page_3
            ],
        ),
        '/menu': View(
            "/menu",
            [
                page_4,
            ],
        ),
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    page.add(container)
    page.on_route_change = route_change
    page.go(page.route)
    page.update()

app(target=Page)
