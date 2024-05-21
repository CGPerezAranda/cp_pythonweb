import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("TBM-3 Avenger 1/48 Academy (ex Accurate Miniatures)"),
        link_button("Dewoitine D.520 1/48 Tamiya"),
        link_button("Macchi C.202 Folgore 1/48 Hasegawa"),
        link_button("SPAD XIII 1/48 Eduard"),
    )
    