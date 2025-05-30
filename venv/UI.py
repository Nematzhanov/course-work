import flet as ui
import threading
import pyperclip
import re
from chat_api import get_bot_response 

def main(page: ui.Page):
    page.title = "My chat"
    page.theme_mode = ui.ThemeMode.DARK
    
    # цветовая схема
    user_message_color = ui.Colors.INDIGO_700
    bot_message_color = ui.Colors.TEAL_700
    code_block_color = ui.Colors.GREY_900
    text_color = ui.Colors.GREY_200
    accent_color = ui.Colors.BLUE_400
    
    chat_column = ui.Column(
        expand=True,
        scroll="auto",
        spacing=10
    )

    input_field = ui.TextField(
        text_align=ui.TextAlign.LEFT,
        hint_text="Введите сообщение...",
        expand=True,
        autofocus=True,
        color=text_color
    )

    send_button = ui.IconButton(icon=ui.Icons.SEND, icon_color=accent_color)

    def create_message_controls(message_text):
        """Создаёт кнопку копирования для всего сообщения."""
        return ui.Row(
            controls=[
                ui.IconButton(
                    icon=ui.Icons.CONTENT_COPY,
                    icon_size=18,
                    tooltip="Копировать всё",
                    icon_color=accent_color,
                    on_click=lambda e, text=message_text: copy_message(text)
                ),
            ],
            spacing=5,
            alignment=ui.MainAxisAlignment.END
        )

    def copy_message(text):
        """Копирует текст в буфер обмена и показывает уведомление."""
        pyperclip.copy(text)
        page.snack_bar = ui.SnackBar(ui.Text("Текст скопирован!"))
        page.snack_bar.open = True
        page.update()

    def parse_response(response):
        """Разделяет ответ бота на текст и блоки кода."""
        code_block_pattern = r'```(\w+)?\n(.*?)```'
        matches = list(re.finditer(code_block_pattern, response, re.DOTALL))
        parts = []
        last_end = 0
        for match in matches:
            start, end = match.span()
            if last_end < start:
                parts.append({'type': 'text', 'content': response[last_end:start]})
            language = match.group(1) or 'text'
            code = match.group(2)
            parts.append({'type': 'code', 'language': language, 'content': code})
            last_end = end
        if last_end < len(response):
            parts.append({'type': 'text', 'content': response[last_end:]})
        return parts

    def send_message(e):
        user_input = input_field.value.strip()
        if not user_input:
            return
            
    
        chat_column.controls.append(
            ui.Container(
                content=ui.Text(user_input, color=text_color),
                alignment=ui.alignment.center_right,
                bgcolor=user_message_color,
                padding=10,
                border_radius=10,
                margin=ui.margin.only(left=60, right=5, top=5, bottom=5)
            )
        )
        
        # Индикатор загрузки
        loading_indicator = ui.Container(
            content=ui.Row([
                ui.ProgressRing(width=20, height=20, stroke_width=2, color=accent_color),
                ui.Text("Обработка...", color=text_color)
            ]),
            alignment=ui.alignment.center_left,
            bgcolor=ui.Colors.GREY_700,
            padding=10,
            border_radius=10,
            margin=ui.margin.only(left=5, right=60, top=5, bottom=5)
        )
        chat_column.controls.append(loading_indicator)
        
        input_field.value = ""
        page.update()
        
        def api_request():
            try:
                bot_response = get_bot_response(user_input)
                
                # Удалит индикатор загрузки
                if loading_indicator in chat_column.controls:
                    chat_column.controls.remove(loading_indicator)
                
        
                parts = parse_response(bot_response)
                
               
                parts_column = ui.Column(spacing=5)
                
                for part in parts:
                    if part['type'] == 'text':
                        parts_column.controls.append(ui.Text(part['content'], color=text_color))
                    elif part['type'] == 'code':
                        code_text = ui.Text(part['content'], font_family="monospace", color=text_color)
                        copy_button = ui.IconButton(
                            icon=ui.Icons.CONTENT_COPY,
                            icon_size=18,
                            tooltip="Копировать код",
                            icon_color=accent_color,
                            on_click=lambda e, text=part['content']: copy_message(text)
                        )
                        #"Язык" пр
                        header_row = ui.Row([
                            ui.Text(f"Язык: {part['language']}", size=12, color=text_color),
                            copy_button
                        ], alignment=ui.MainAxisAlignment.SPACE_BETWEEN)
                        code_container = ui.Container(
                            content=ui.Column([
                                header_row,
                                code_text
                            ]),
                            bgcolor=code_block_color,
                            padding=5,
                            border_radius=5
                        )
                        parts_column.controls.append(code_container)
                
                # кнопку копирования
                controls_row = create_message_controls(bot_response)
                
                #Копировать всё
                bot_message_container = ui.Container(
                    content=ui.Column([
                        parts_column,
                        ui.Container(controls_row, alignment=ui.alignment.bottom_right)
                    ], spacing=5),
                    alignment=ui.alignment.center_left,
                    bgcolor=bot_message_color,
                    padding=10,
                    border_radius=10,
                    margin=ui.margin.only(left=5, right=60, top=5, bottom=5)
                )
                chat_column.controls.append(bot_message_container)
            except Exception as e:
                chat_column.controls.append(
                    ui.Container(
                        content=ui.Text(f"Ошибка: {e}", color=text_color),
                        alignment=ui.alignment.center_left,
                        bgcolor=ui.Colors.RED_800,
                        padding=10,
                        border_radius=10,
                        margin=ui.margin.only(left=5, right=60, top=5, bottom=5)
                    )
                )
            finally:
                page.update()
        
        threading.Thread(target=api_request, daemon=True).start()

    #Enter
    send_button.on_click = send_message
    input_field.on_submit = send_message

    #интерфейс
    page.add(
        ui.Column([
            ui.Container(content=chat_column, expand=True, padding=10),
            ui.Container(
                content=ui.Row([
                    input_field,
                    send_button
                ], expand=True, vertical_alignment="center"),
                padding=10
            )
        ], expand=True)
    )

ui.app(target=main)