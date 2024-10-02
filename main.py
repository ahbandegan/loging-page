from flet import *


def main(page: Page):
    page.window.height = 460
    page.window.width = 440
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'dark'

    text_login = Container(
        Text(
            value="login",
            size=40,
            weight='bold',
        ),
        margin=margin.only(left=140)
    )

    login_input = Container(
        TextField(
            hint_text='login',
            width=300,
            border_color='white'
        ),
        margin=margin.only(left=50)
    )

    senha_input = Container(
        TextField(
            hint_text='password',
            password=True,
            can_reveal_password=True,
            width=300,
            border_color='white'
        ),
        margin=margin.only(left=50)
    )
    btn = Container(
        ElevatedButton(
            text='Enter',
            width=200,
            height=50,
            style=ButtonStyle(
                bgcolor={
                    MaterialState.HOVERED:colors.WHITE,
                    MaterialState.DEFAULT:colors.BLUE_GREY_300
                },
                side={
                    MaterialState.DEFAULT:BorderSide(color='withe', width=2)
                },
                color={
                    MaterialState.DEFAULT:colors.WHITE,
                    MaterialState.HOVERED:colors.BLUE_GREY
                }
            )
        ),
        margin=margin.only(left=100)
    )

    layout = Container(
        width=400,
        height=400,
        border_radius=20,
        shadow=BoxShadow(
            blur_radius=5,
            color='white54'
        ),
        gradient=LinearGradient(
            begin=alignment.top_left,
            end=alignment.bottom_right,
            colors=[
                colors.WHITE38,
                colors.BLUE_GREY,
                colors.BLUE_GREY_300
            ],
            stops=[0,0.5,1]
        ),
        content=Column(
            spacing=30,
            alignment='center',
            controls=[
                text_login,
                login_input,
                senha_input,
                btn
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    app(main)