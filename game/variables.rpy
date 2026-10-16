## თამაშის მდგომარეობა. ყველა ცვლადი default-ით არის აღწერილი, რომ
## save/load-მა და rollback-მა სწორად იმუშაოს.

default mc_name = "Elara"

## სიმპათია თითოეული სასიყვარულო ხაზისთვის. ეპიზოდების ფინალები და
## ექსკლუზიური სცენები ამ ქულებზეა დამოკიდებული.
default affinity = {"valerius": 0, "cassian": 0}

## სიუჟეტური არჩევანები, რომლებსაც შემდეგი ეპიზოდები იხსენებს.
default flags = set()

init python:

    AFFINITY_NOTES = {
        "valerius": _("Valerius will remember that."),
        "cassian": _("Cassian will remember that."),
    }

    def add_affinity(who, amount=1):
        """
        ზრდის სიმპათიას და აჩვენებს Telltale-ის სტილის შეტყობინებას.
        """

        affinity[who] = affinity.get(who, 0) + amount

        if amount > 0:
            renpy.notify(AFFINITY_NOTES[who])

    def play_music(path, fadein=2.0):
        """
        უკრავს მუსიკას, თუ ფაილი არსებობს, ასე რომ თამაში აუდიოს გარეშეც ეშვება.
        """

        if renpy.loadable(path):
            renpy.music.play(path, channel="music", fadein=fadein, loop=True)
