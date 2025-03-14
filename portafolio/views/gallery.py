import reflex as rx

from portafolio.components.heading import heading
from portafolio.data import GalleryImage
from portafolio.styles.styles import Size

def gallery(data: list[GalleryImage]) -> rx.Component:
    return rx.vstack(
        heading("Photo Gallery"),
        rx.grid(
            *[
                rx.image(
                    src=image.image, 
                    alt="Gallery Image", 
                    width="100%",
                    height="auto",
                    object_fit="cover",
                    border_radius="10px",
                    box_shadow="lg"
                ) for image in data
            ],
            grid_template_columns="repeat(auto-fit, minmax(250px, 1fr))",
            spacing=Size.DEFAULT.value,
            gap=Size.DEFAULT.value,
            width="100%"
        ),
        spacing=Size.DEFAULT.value,
        width="100%"
    )