## სურათები. თითოეული აღწერილია ცალკე ფაილის გზით; სანამ ფაილი არ
## არსებობს, თამაში placeholder-ს აჩვენებს. ასე პროლოგი არტის გარეშეც
## ბოლომდე ითამაშება. ზომები და სახელები: docs/art-bible.md

init python:

    def art(path, placeholder):
        if renpy.loadable(path):
            return path
        return placeholder

    def bg_placeholder(label, color="#120c18"):
        return Fixed(
            Solid(color),
            Text(label, size=40, color="#ffffff55", xalign=0.5, yalign=0.35),
        )

    def sprite_placeholder(label):
        return Placeholder("boy", text=label)


## ფონები (1920x1080) ##########################################################

image bg weaver_shop = art("images/bg/bg_weaver_shop.png",
    bg_placeholder("BG: the weaver's shop, night", "#1a1210"))
image bg castle_gate = art("images/bg/bg_castle_gate.png",
    bg_placeholder("BG: Castle Noctis gate, night", "#0d0a14"))
image bg castle_hall = art("images/bg/bg_castle_hall.png",
    bg_placeholder("BG: castle hall, moonlight", "#100c18"))
image bg castle_bedroom = art("images/bg/bg_castle_bedroom.png",
    bg_placeholder("BG: Valerius' chamber, candlelight", "#160d12"))


## Valerius ####################################################################

image valerius neutral = art("images/sprites/valerius_neutral.png", sprite_placeholder("Valerius: neutral"))
image valerius smirk = art("images/sprites/valerius_smirk.png", sprite_placeholder("Valerius: smirk"))
image valerius cold = art("images/sprites/valerius_cold.png", sprite_placeholder("Valerius: cold"))
image valerius surprised = art("images/sprites/valerius_surprised.png", sprite_placeholder("Valerius: surprised"))
image valerius soft = art("images/sprites/valerius_soft.png", sprite_placeholder("Valerius: soft"))


## Cassian #####################################################################

image cassian neutral = art("images/sprites/cassian_neutral.png", sprite_placeholder("Cassian: neutral"))
image cassian smile = art("images/sprites/cassian_smile.png", sprite_placeholder("Cassian: smile"))
image cassian serious = art("images/sprites/cassian_serious.png", sprite_placeholder("Cassian: serious"))


## CG ილუსტრაციები (1920x1080) #################################################

image cg prologue_shadow = art("images/cg/cg_prologue_shadow.png",
    bg_placeholder("CG: the shadow coils around her wrist", "#1b0f22"))
image cg prologue_close = art("images/cg/cg_prologue_close.png",
    bg_placeholder("CG: Valerius, a breath away", "#1f0f17"))
