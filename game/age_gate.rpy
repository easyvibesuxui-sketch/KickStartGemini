## 18+ შემოწმება და კონტენტის გაფრთხილება. ჩნდება მთავარ მენიუმდე და
## ერთხელ, დადასტურების შემდეგ, აღარ მეორდება.

default persistent.age_confirmed = False

screen age_gate():

    modal True

    add Solid("#07040b")

    vbox:
        align (0.5, 0.5)
        xmaximum 1300
        spacing 45

        text _("Shadows & Silk"):
            xalign 0.5
            size 96
            color gui.accent_color

        text _("This game is intended for adults aged 18 or older."):
            xalign 0.5
            size 42

        text _("Content warnings: dark romance, emotional manipulation, a missing family member, violence, mild blood and suggestive scenes. There is no explicit sexual content."):
            xalign 0.5
            text_align 0.5
            color "#bbaec6"

        hbox:
            xalign 0.5
            spacing 120

            textbutton _("I am 18 or older"):
                text_size 44
                action Return(True)

            textbutton _("Leave"):
                text_size 44
                action Return(False)


label splashscreen:

    if not persistent.age_confirmed:

        call screen age_gate

        if not _return:
            $ renpy.quit()

        $ persistent.age_confirmed = True

    return
