## თამაშის შესასვლელი წერტილი. ეპიზოდები ცალკე ფაილებშია: game/episodes/

label start:

    scene black

    $ mc_name = renpy.input(_("What is your name?"), default="Elara", length=16, exclude="{}[]%").strip() or "Elara"

    jump prologue
