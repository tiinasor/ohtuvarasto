from varasto import Varasto

def show_state(title, mehua=None, olutta=None):
    if title:
        print(title)
    if mehua is not None:
        print(f"Mehuvarasto: {mehua}")
    if olutta is not None:
        print(f"Olutvarasto: {olutta}")

def show_olut_getters(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def tee(kuvaus, fn, *args):
    print(kuvaus)
    res = fn(*args)
    if res is not None:
        print(f"saatiin {res}")
    return res

def mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    show_state("", mehua=mehua)
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    show_state("", mehua=mehua)

def virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    print(Varasto(-100.0))
    print("Varasto(100.0, -50.7)")
    print(Varasto(100.0, -50.7))

def _show_call_olut(before_msg, after_msg, obj, fn, amount):
    show_state(before_msg, olutta=obj)
    tee(fn.__name__ + f"({amount})", fn, amount)
    show_state(after_msg, olutta=obj)

def _show_call_mehu(before_msg, after_msg, obj, fn, amount):
    show_state(before_msg, mehua=obj)
    tee(fn.__name__ + f"({amount})", fn, amount)
    show_state(after_msg, mehua=obj)

def raja_arvot(mehua, olutta):
    _show_call_olut(
        "Olut ennen lisäystä:",
        "Olut lisäyksen jälkeen:",
        olutta,
        olutta.lisaa_varastoon,
        1000.0,
    )

    _show_call_mehu(
        "Mehu ennen lisäystä:",
        "Mehu lisäyksen jälkeen:",
        mehua,
        mehua.lisaa_varastoon,
        -666.0,
    )

    _show_call_olut(
        "Olut ennen ottoa:",
        "Olut oton jälkeen:",
        olutta,
        olutta.ota_varastosta,
        1000.0,
    )

    _show_call_mehu(
        "Mehu ennen negatiivista ottoa:",
        "Mehu oton jälkeen:",
        mehua,
        mehua.ota_varastosta,
        -32.9,
    )

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    show_state("Luonnin jälkeen:", mehua=mehua, olutta=olutta)
    show_olut_getters(olutta)
    mehu_setterit(mehua)
    virhetilanteet()
    raja_arvot(mehua, olutta)

if __name__ == "__main__":
    main()
