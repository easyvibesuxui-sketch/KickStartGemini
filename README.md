# Shadows & Silk

ინტერაქტიული Dark Romance ვიზუალური ნოველა (18+) Ren'Py 8-ზე.

## სტრუქტურა

```
game/
  script.rpy           თამაშის დასაწყისი: სახელის არჩევა → პროლოგი
  age_gate.rpy         18+ ეკრანი და კონტენტის გაფრთხილება
  characters.rpy       პერსონაჟები და მათი ფერები
  variables.rpy        სიმპათია, სიუჟეტური flag-ები, დამხმარე ფუნქციები
  images.rpy           ყველა სურათი; placeholder-ები, სანამ არტი არ არის
  episodes/            ეპიზოდები (prologue.rpy, …)
  demo_end.rpy         დემოს ფინალური ეკრანი Patreon/Discord/itch ბმულებით
  gui.rpy, screens.rpy, options.rpy, gui/   Ren'Py-ის სტანდარტული GUI
  images/{bg,sprites,cg}/  აქ ჩააგდე არტი (სახელები: docs/art-bible.md)
  audio/music/         მუსიკა (.ogg)
docs/
  plan-review.md       ბიზნეს გეგმის ანალიზი, რისკები და განახლებული გეგმა
  story-bible.md       სამყარო, პერსონაჟები, ეპიზოდების მონახაზი
  art-bible.md         Midjourney-ის პრომპტები, ფაილების სახელები და ზომები
tools/
  make_gui.py          GUI-ს ფერების/გრაფიკის ხელახალი გენერაცია
```

## გაშვება

1. გადმოწერე [Ren'Py SDK](https://www.renpy.org/latest.html) (8.x).
2. Ren'Py Launcher → **Preferences → Projects Directory**: აირჩიე საქაღალდე,
   რომელშიც ეს რეპოა.
3. სიაში გამოჩნდება `KickStartGemini`. დააჭირე **Launch Project**-ს.
4. სანამ არტი არ გაქვს, თამაში placeholder-ებს აჩვენებს, ასე რომ პროლოგი უკვე
   ბოლომდე ითამაშება.
5. პირველ გაშვებამდე **Check Script (Lint)** გაუშვი.

## არტის დამატება

ფაილი ჩააგდე `game/images/...`-ში ზუსტად იმ სახელით, რომელიც `game/images.rpy`-ში
წერია (მაგ. `game/images/sprites/valerius_smirk.png`). კოდის შეცვლა საჭირო არ არის.

## ბილდები

Launcher → **Build Distributions**: Windows, macOS, Linux. Android-ისთვის:
Launcher → **Android** (პირველად SDK-ს გადმოწერას ითხოვს).

## ახალი ეპიზოდი

1. ახალი ფაილი `game/episodes/episode1.rpy`, `label episode1:`-ით.
2. `demo_end.rpy`-ში ფინალის ნაცვლად `jump episode1`.
3. Claude-ს სცენარის დაწერისას კონტექსტად მიეცი `docs/story-bible.md`.
