import reflex as rx
from link_bio.components.link_button import link_button

def links_maquetas() -> rx.Component:
    return rx.vstack(
        link_button("TBM-3 Avenger 1/48 Academy (ex Accurate Miniatures)", "https://imgur.com/gallery/tbm-3-avenger-1-48-academy-ex-accurate-1qcYWbs"),
        link_button("Dewoitine D.520 1/48 Tamiya", "https://imgur.com/gallery/tamiya-1-48-dewoitine-d-520-S0IPNEW"),
        link_button("Macchi C.202 Folgore 1/48 Hasegawa", "https://imgur.com/gallery/1-48-macchi-m-c-202-hasegawa-BDcRvQI"),
        link_button("SPAD XIII 1/48 Eduard","https://imgur.com/gallery/eduard-1-48-spad-xiii-gFAYOqp"),
        align = "center",
        width = "100%",
        text_align = "center"
    )
    