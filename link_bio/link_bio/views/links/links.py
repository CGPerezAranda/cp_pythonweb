import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("TBM-3 Avenger 1/48 Academy (ex Accurate Miniatures)", "https://lh3.googleusercontent.com/pw/AP1GczMjO0atXwRHiJCehdHSCMyi4YV0BlQqoKQgB7GONU0BT2bwoxy__Eim2EtxhvPEXdLJQU-_Ol0aUonFbiiL9Ut477wa7g7yxTUnVaJS6pnZzq10g2kRUYTYKHL6O8p8U8EdoE2MPbjRl5n0GBNtZFqqeQ=w2568-h1712-s-no?authuser=0"),
        link_button("Dewoitine D.520 1/48 Tamiya", "https://lh3.googleusercontent.com/pw/AP1GczNydCDR8tbKViU2yzdJNs-f-oR7IUyGqqd-vZ5pgXacizqIgOdBmd6P7XkWq9rN5sZ5JfSaDfCGgDmFU9DZSaiX3N0MI3dg-jYauRy-YewEmPq-MUNe4pFDoCHNIU5guZ0N0L9OhmilIcd8KOkbYjVVLw=w2568-h1712-s-no?authuser=0"),
        link_button("Macchi C.202 Folgore 1/48 Hasegawa", "https://lh3.googleusercontent.com/pw/AP1GczPvEeychKzHuYbbfz7dWzsii9R1deJelgbGnDJgzgt_5qRkdZkOKFzUYO-eEb-qcIVKdUFdzT5otUE0JnLfz0duFerEY2juRCTReUM0oFO0Ji75pmhUqzXBV3I7Q4HsjtDJYKybCCUsVf1zOCals184BA=w2568-h1712-s-no?authuser=0"),
        link_button("SPAD XIII 1/48 Eduard","https://lh3.googleusercontent.com/pw/AP1GczNcClkeT8yKs7Xz7XF5KL0Qe2k1GefIBnQPen6TScB-E_XXRoYt9AX6-AgJdLEjajPyDyOZljJmFMGFaUeU3l2ZAbgRauapFLSeMEbyao1FHLy1BTlAZ0vUkrN_8r5BqNQpgL68NM0RfZcKA9cDYazydA=w2568-h1712-s-no?authuser=0"),
        align = "center",
        width = "100%",
        text_align = "center"
    )
    