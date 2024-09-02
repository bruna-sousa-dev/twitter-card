import flet as ft

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = 'Twitter Card'
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.main()

    def main(self):
        
        style_body_normal = ft.TextStyle(size = 12, color = ft.colors.BLACK, weight = ft.FontWeight.NORMAL)
        style_body_fade = ft.TextStyle(size = 12, color = ft.colors.GREY_500, weight = ft.FontWeight.NORMAL)
        style_title = ft.TextStyle(size = 14, color = ft.colors.BLACK, weight = ft.FontWeight.BOLD)
        
        header = ft.Container(
                content = ft.ListTile(
                    title = ft.Text(
                        spans = [
                            ft.TextSpan(text = 'Elon Musk ', style = style_title), 
                            ft.TextSpan(text = '@elonmusk', style = style_body_fade)
                        ],
                    ),
                    subtitle = ft.Text(
                        value = 'Estamos cada vez mais próximos de chegar a Marte e 2024 será o ano que conseguiremos isso', 
                        style = style_body_normal
                    ),
                    leading = ft.CircleAvatar(
                        foreground_image_src = 'images/elon_musk.jpg',
                        radius = 30                  
                    ),
                ),
        )

        description = ft.Container(
            margin = ft.margin.only(left = 90, right = 20),
            content = ft.Text(
                value = 'A SpaceX fez avanços notáveis e agradeço a todo o time empenhado em fazer isso acontecer 👏👏👏', 
                style = style_body_normal
            )
        )

        media = ft.Container(
            margin = ft.margin.only(left = 90, right = 20),
            border = ft.border.all(width = 1, color = ft.colors.GREY_500),
            border_radius = ft.border_radius.all(10),
            content = ft.Column(
                controls = [
                    ft.Image(src = '/images/spacex.jpg', fit = ft.ImageFit.FIT_WIDTH, scale = ft.Scale(scale = 1.15)),
                    ft.ListTile(
                        title = ft.Text(
                            spans = [
                                ft.TextSpan(text = 'Elon Musk ', style = style_title), 
                                ft.TextSpan(text = '@elonmusk', style = style_body_fade)
                            ]
                        ),
                        subtitle = ft.Text(
                            value = 'Lançamento do Starship da SpaceX hoje às 11h', 
                            style = style_body_normal
                        ),
                    ),     
                ],
            ),
        )

        actions = ft.Container(
            margin = ft.margin.only(left = 90, right = 20),
            padding = ft.padding.only(bottom = 10),
            content = ft.ResponsiveRow(
                controls = [
                    ft.Icon(col = 1, name = ft.icons.CHAT, color = ft.colors.BLACK, scale = 0.8),
                    ft.Icon(col = 1, name = ft.icons.SHARE, color = ft.colors.BLACK, scale = 0.8),
                    ft.Icon(col = 1, name = ft.icons.FAVORITE, color = ft.colors.BLACK, scale = 0.8),
                    ft.Icon(col = 1, name = ft.icons.ANALYTICS, color = ft.colors.BLACK, scale = 0.8),
                ],            
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN    
            ),
        )
        
        layout = ft.Container(
            width = 450,
            bgcolor = ft.colors.WHITE,
            border_radius = ft.border_radius.all(5),
            shadow = ft.BoxShadow(
                blur_radius = 50, 
                color = ft.colors.BLUE_400, 
                blur_style = ft.ShadowBlurStyle.NORMAL
            ),
            content = ft.Column(
                controls = [
                    header,
                    description,
                    media,
                    actions
                ],
            ),
        )

        self.page.add(layout)

if __name__ == '__main__':
	ft.app(target = App, assets_dir = 'assets')
