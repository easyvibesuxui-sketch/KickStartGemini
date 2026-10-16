## პროლოგი: "The Price of Answers" (უფასო დემო)
## გეგმა სცენებად: docs/story-bible.md → "პროლოგი"

label prologue:

    $ play_music("audio/music/theme_night.ogg")

    scene bg weaver_shop with fade

    "One year ago tonight, my sister walked into the Midwinter masquerade at Castle Noctis."

    "She wore a gown I wove for her myself, moonsilk the colour of frost. She never walked out."

    "The Queen's guard called it an accident. The city called it the Prince's curse. Nobody called it murder, so nobody looked for her."

    "Except me."

    "Tonight a ribbon was waiting on my doorstep. Black moonsilk, my family's weave, the same as the trim on Lyra's mask."

    "Three words were stitched into it in silver thread."

    thought "Castle Noctis. Midnight."

    "I didn't wait for dawn."

    ## Scene 1: the gate ######################################################

    scene bg castle_gate with dissolve

    "Castle Noctis doesn't sleep. Its towers burned with cold blue fire, and its gate stood open like a mouth."

    "I had taken three steps across the bridge when a gloved hand caught my arm."

    show cassian serious at center with dissolve

    c "The castle is closed to the city after dark. Turn around."

    "He wore the black and silver of the royal guard, and a captain's chain. His grip was firm, but it didn't hurt."

    c "I won't ask twice. What business does a weaver have here at midnight?"

    thought "He knew what I was from the thread calluses on my fingers. He was the kind of man who noticed things."

    menu:
        "Lie: \"I'm delivering silk the Prince ordered.\"":
            $ flags.add("lied_to_cassian")

            m "Silk for His Highness. He asked for it tonight."

            show cassian neutral

            c "The Prince hasn't ordered anything in a year. He doesn't receive visitors either."

            c "You're a poor liar. That's almost a compliment."

        "Truth: \"I'm looking for my sister.\"":
            $ add_affinity("cassian")

            m "My sister disappeared here a year ago. Her name was Lyra. Someone wants me to come inside."

            show cassian neutral

            "Something moved behind his eyes. It might have been guilt."

            c "Lyra Vane. I was on duty that night."

            c "I'm sorry. I mean that."

    c "Listen to me. Whatever brought you here, it isn't a friend."

    "He looked up at the highest tower. A single window was lit, gold instead of blue."

    c "If you go up there, you'll find the Prince. If he speaks, answer. If he offers you anything, refuse."

    c "And whatever happens, don't let his shadow touch you."

    m "His shadow?"

    show cassian smile

    c "Call it a captain's superstition."

    "He stepped aside. He didn't let go of the gate."

    c "I'm Cassian. If you scream, I'll hear it."

    hide cassian with dissolve

    ## Scene 2: the chamber ####################################################

    scene bg castle_bedroom with fade

    "The candles in the chamber flickered as the cold wind pushed through the balcony doors."

    show valerius neutral at center with dissolve

    "He was standing at the window with his back to me. Silver hair, black velvet, gold thread at the cuffs."

    "My hands knew that embroidery before my mind did. My mother stitched it, twelve years ago, for a boy prince's coronation coat."

    v "You shouldn't have come here tonight."

    m "I needed answers, Valerius. And I wasn't going to wait until dawn."

    "He turned. His eyes were violet, and very tired."

    show valerius smirk with dissolve

    v "Answers come with a price in this castle."

    menu:
        "Step closer to him":
            $ add_affinity("valerius")
            $ flags.add("stepped_closer")

            "I took a slow step forward, refusing to let him intimidate me."

            v "Brave. Or foolish. We shall see which one you are."

        "Demand the truth immediately":
            $ flags.add("demanded_truth")

            m "Tell me what happened that night. No more games."

            show valerius neutral

            v "Direct. I can respect that."

    "He drew something from inside his coat and held it out on his open palm."

    "It was a scrap of a mask, frost-white moonsilk with a black ribbon trim. The edges were singed."

    m "That's Lyra's."

    v "She came to this room a year ago and stood where you're standing. She asked the same question."

    show valerius cold

    v "I gave her the same warning. She didn't listen either."

    m "What did you do to her?"

    v "Nothing she didn't ask for."

    "The candles leaned all at once, as though someone had sighed."

    "On the wall behind him his shadow stretched, longer than it should have been. It wasn't moving the way he moved."

    "It was reaching for me."

    ## Scene 3: the shadow #####################################################

    scene cg prologue_shadow with dissolve

    "The darkness slid across the floor and coiled around my wrist, cold as river water."

    "For a heartbeat I couldn't breathe."

    "Then the ribbon in my sleeve began to glow. The moonsilk burned silver, and the shadow went still."

    v "Don't move."

    "He was beside me. I hadn't heard him cross the room. His voice was rough."

    v "In twelve years it has never stopped for anyone. Not for priests, not for mages."

    v "It is listening to you."

    menu:
        "Pull your hand away":
            $ flags.add("pulled_away")

            "I tore my wrist free. The shadow fell back like a scolded hound and melted into the floor."

            v "Wise. Most people aren't, the first time."

        "Hold still and let it settle":
            $ add_affinity("valerius")

            "I made myself breathe. Slowly the cold faded until it felt like a hand resting on mine, nothing more."

            "When I looked up, he was watching me as if I were something he'd stopped believing in."

            v "...Remarkable."

        "Touch the shadow back":
            $ add_affinity("valerius", 2)
            $ flags.add("touched_shadow")

            "I didn't know why I did it. I turned my hand and closed my fingers around the darkness, the way I'd hold a loose thread."

            "It shivered. Across from me, so did he."

            v "{i}Careful.{/i} You have no idea what you're holding."

            m "Then tell me."

    scene bg castle_bedroom
    show valerius soft at center
    with dissolve

    v "Seven nights from now the Queen Regent holds the Midwinter masquerade again. Exactly as she did the night your sister vanished."

    v "Weave me a mask from that silk of yours. One that can hold this..."

    "He glanced at his shadow. It was standing very politely behind him now."

    v "...and I'll tell you everything I know about Lyra."

    m "And if I refuse?"

    show valerius smirk

    v "Then you'll walk back across that bridge and spend another year wondering."

    v "You'll stay in the castle as my seamstress. Nobody questions a seamstress."

    menu:
        "\"One truth now, or there's no bargain.\"":
            $ flags.add("bargained_hard")
            $ add_affinity("valerius")

            m "One truth now, as a deposit. Or there's no bargain."

            show valerius neutral

            "For a long moment he said nothing. Then, unexpectedly, he smiled. It changed his whole face."

            v "Very well, weaver. One truth."

        "\"Seven nights. Not one more.\"":
            m "Seven nights. Not one more."

            v "Seven nights."

            "He offered his hand. When I took it, his shadow brushed my fingers like a promise."

            v "And because I'd like you to come back tomorrow, I'll pay a small advance."

    scene cg prologue_close with dissolve

    "He leaned in until his voice was barely more than breath against my ear."

    v "Your sister isn't dead."

    "The candles went out."

    scene black with Dissolve(1.5)

    "In the dark, beneath the howl of the wind, someone whispered my name."

    "It was Lyra's voice."

    $ renpy.pause(1.5, hard=True)

    jump demo_end
