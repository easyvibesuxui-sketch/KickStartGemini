## დემოს ფინალური ეკრანი: მადლობა და ბმულები. ცარიელი ბმული ღილაკს მალავს.

define LINKS = [
    (_("Support on Patreon"), ""),
    (_("Join the Discord"), ""),
    (_("Follow on itch.io"), ""),
]

screen demo_end():

    add Solid("#07040b")

    vbox:
        align (0.5, 0.45)
        xmaximum 1300
        spacing 40

        text _("End of the Prologue"):
            xalign 0.5
            size 80
            color gui.accent_color

        text _("Thank you for playing. Episode 1, \"Seven Nights\", is coming soon.\nYour choices in the Prologue will carry over."):
            xalign 0.5
            text_align 0.5

        vbox:
            xalign 0.5
            spacing 15

            for link_text, url in LINKS:
                if url:
                    textbutton link_text:
                        xalign 0.5
                        text_size 42
                        action OpenURL(url)

            null height 20

            textbutton _("Return to Main Menu"):
                xalign 0.5
                text_size 42
                action Return()


label demo_end:

    window hide

    call screen demo_end

    return
