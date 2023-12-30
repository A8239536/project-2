from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):

    def build(self):
        # 創建一個BoxLayout，設定方向為垂直
        layout = BoxLayout(orientation='vertical')

        # 創建六個按鈕，並添加到BoxLayout中
        for i in range(6):
            button_text = f'button {i + 1}'
            button = Button(text=button_text, on_press=self.on_button_press)
            layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # 當按鈕被按下時的事件處理
        button_text = instance.text
        print(f'{button_text} 被按下了！')

if __name__ == '__main__':
    MyApp().run()
