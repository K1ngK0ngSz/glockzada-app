from kivy.app import App from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition from kivy.uix.boxlayout import BoxLayout from kivy.uix.label import Label from kivy.uix.button import Button from kivy.uix.textinput import TextInput from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)

Estilo visual hacker

GREEN = (0, 1, 0, 1)

Admin login

ADMIN_USER = "Glock" ADMIN_PASS = "MenuFelipe"

class LoginScreen(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

layout.add_widget(Label(text='[b]Painel Glockzada[/b]', markup=True, font_size=28, color=GREEN))

    self.username = TextInput(hint_text='Usuário', multiline=False)
    self.password = TextInput(hint_text='Senha', multiline=False, password=True)

    layout.add_widget(self.username)
    layout.add_widget(self.password)

    login_btn = Button(text='Entrar', background_color=GREEN)
    login_btn.bind(on_press=self.check_login)
    layout.add_widget(login_btn)

    user_btn = Button(text='Entrar como Usuário Comum')
    user_btn.bind(on_press=self.goto_nick)
    layout.add_widget(user_btn)

    self.add_widget(layout)

def check_login(self, instance):
    if self.username.text == ADMIN_USER and self.password.text == ADMIN_PASS:
        self.manager.current = 'admin'
    else:
        self.manager.current = 'user'

def goto_nick(self, instance):
    self.manager.current = 'nick'

class NickScreen(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation='vertical', padding=20, spacing=10) layout.add_widget(Label(text='Escolha seu Nick:', color=GREEN)) self.nick_input = TextInput(hint_text='Digite seu nick', multiline=False) layout.add_widget(self.nick_input) enter_btn = Button(text='Entrar no Painel', background_color=GREEN) enter_btn.bind(on_press=self.enter_panel) layout.add_widget(enter_btn) self.add_widget(layout)

def enter_panel(self, instance):
    self.manager.get_screen('user').nickname = self.nick_input.text
    self.manager.current = 'user'

class UserPanel(Screen): def init(self, **kwargs): super().init(**kwargs) self.nickname = "" self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10) self.label = Label(text='Bem-vindo!', color=GREEN) self.layout.add_widget(self.label) self.layout.add_widget(Button(text='Ferramenta: Scan de IP', background_color=GREEN)) self.layout.add_widget(Button(text='Ferramenta: Gerador de Senha', background_color=GREEN)) self.layout.add_widget(Button(text='Chat com outros usuários', background_color=GREEN)) self.layout.add_widget(Button(text='Sair', on_press=self.logout)) self.add_widget(self.layout)

def on_pre_enter(self):
    self.label.text = f"Bem-vindo, {self.nickname}!"

def logout(self, instance):
    self.manager.current = 'login'

class AdminPanel(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation='vertical', padding=20, spacing=10) layout.add_widget(Label(text='[b]Painel Admin - Glockzada[/b]', markup=True, font_size=24, color=GREEN)) layout.add_widget(Button(text='Ver usuários conectados', background_color=GREEN)) layout.add_widget(Button(text='Enviar notificação', background_color=GREEN)) layout.add_widget(Button(text='Ativar ferramentas privadas', background_color=GREEN)) layout.add_widget(Button(text='Testar vulnerabilidades (SQLi, XSS, LFI)', background_color=GREEN)) layout.add_widget(Button(text='Interface estilo Lucky Patcher', background_color=GREEN)) layout.add_widget(Button(text='Sair', on_press=self.logout)) self.add_widget(layout)

def logout(self, instance):
    self.manager.current = 'login'

class GlockzadaApp(App): def build(self): sm = ScreenManager(transition=FadeTransition()) sm.add_widget(LoginScreen(name='login')) sm.add_widget(NickScreen(name='nick')) sm.add_widget(UserPanel(name='user')) sm.add_widget(AdminPanel(name='admin')) return sm

if name == 'main': GlockzadaApp().run()

