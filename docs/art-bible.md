# Shadows & Silk: Art Bible

## ფაილების სახელები და ზომები

თამაში სურათებს ქვემოთ მოცემული გზებით ეძებს (`game/images.rpy`). ფაილს
ზუსტად ამ სახელით თუ ჩააგდებ, placeholder ავტომატურად ჩანაცვლდება.

| ტიპი | საქაღალდე | ზომა | ფორმატი |
| :--- | :--- | :--- | :--- |
| ფონი | `game/images/bg/bg_<სახელი>.png` | 1920×1080 | PNG/WEBP |
| Sprite | `game/images/sprites/<პერსონაჟი>_<ემოცია>.png` | სიმაღლე ≈1000–1080px, გამჭვირვალე ფონი | PNG |
| CG | `game/images/cg/cg_<სახელი>.png` | 1920×1080 | PNG/WEBP |
| მუსიკა | `game/audio/music/<სახელი>.ogg` | — | OGG |

**პროლოგისთვის საჭიროა:**

- ფონები: `bg_weaver_shop`, `bg_castle_gate`, `bg_castle_hall`, `bg_castle_bedroom`
- Valerius: `neutral`, `smirk`, `cold`, `surprised`, `soft`
- Cassian: `neutral`, `smile`, `serious`
- CG: `cg_prologue_shadow`, `cg_prologue_close`
- მუსიკა: `theme_night.ogg`

## Midjourney-ის სამუშაო პროცესი

1. **ვერსიის არჩევა.** აირჩიე ერთი, მაგალითად `--niji 6`, და მთელ პროექტში არ
   შეცვალო. `--cref` მუშაობს V6/Niji 6-ზე. V7-ში მის ნაცვლად Omni Reference-ია
   (`--oref <URL> --ow 100`).
2. **Character sheet.** ჯერ შექმენი, საუკეთესო ვარიანტი აირჩიე და მისი URL
   შეინახე. ეს არის პერსონაჟის „კანონი“.
3. **საბაზო sprite.** ერთი პოზა, სრული ტანი ან წელამდე, ნეიტრალური ფონი.
4. **ემოციები.** იგივე სურათზე **Vary Region / Editor**-ით მხოლოდ სახე შეცვალე.
   ასე სხეული, ტანსაცმელი და განათება იდენტური რჩება.
5. **დამუშავება.** ფონის მოჭრა (Photopea → Remove BG), ფერის გათანაბრება, ხელით
   კორექცია.
6. **Stealth.** სიუჟეტური CG-ები საჯარო გალერეაში ჩანს, თუ stealth რეჟიმი
   (Pro გეგმა) ჩართული არ გაქვს.

**წესი:** ყველა პრომპტი SFW უნდა იყოს. სენსუალურობა გადმოეცი განათებით,
სიახლოვით, მზერითა და ხელებით, შიშველი სხეულის გარეშე.

## სტილის საერთო ბოლოსართი

ყველა პრომპტს ბოლოში დაურთე, რომ სტილი ერთიანი იყოს:

```text
dark fantasy otome visual novel art, painterly anime style, soft rim light, deep violet and gold palette, cinematic lighting
```

## პრომპტები

### Valerius: character sheet
```text
character concept sheet of a handsome adult dark fantasy prince, 29 years old, long straight silver hair, piercing violet eyes, sharp jawline, black velvet doublet with gold embroidery, high collar, front view and three-quarter view, plain grey background, dark fantasy otome visual novel art, painterly anime style, deep violet and gold palette --ar 16:9 --niji 6
```

### Valerius: საბაზო sprite
```text
waist-up portrait of a handsome adult dark fantasy prince, long silver hair, violet eyes, black velvet doublet with gold embroidery, standing, facing the viewer, neutral expression, plain flat grey background, dark fantasy otome visual novel sprite, painterly anime style --cref [VALERIUS_SHEET_URL] --cw 100 --ar 2:3 --niji 6
```

ემოციები Vary Region-ით, მხოლოდ სახის მონიშვნით:
- `smirk`: `confident smirk, one eyebrow slightly raised`
- `cold`: `cold distant stare, lips pressed thin`
- `surprised`: `eyes widened, lips slightly parted, surprised`
- `soft`: `gentle tired smile, softened eyes`

### Cassian: character sheet
```text
character concept sheet of a handsome adult royal guard captain, 31 years old, short dark brown hair, small scar through left eyebrow, warm grey eyes, black and silver guard uniform with captain's chain, front view and three-quarter view, plain grey background, dark fantasy otome visual novel art, painterly anime style, deep violet and gold palette --ar 16:9 --niji 6
```

### ფონები
```text
# bg_castle_gate
gothic castle gate on a stone bridge at midnight, towers burning with cold blue fire, mist, snow, no people, dark fantasy otome visual novel background, painterly anime style --ar 16:9 --niji 6

# bg_castle_bedroom
luxurious gothic royal bedchamber at night, dozens of candles, open balcony doors with wind-blown curtains, moonlight, black and gold decor, no people, dark fantasy otome visual novel background, painterly anime style --ar 16:9 --niji 6

# bg_weaver_shop
small cosy weaver's workshop at night, wooden loom, spools of silver thread, a single oil lamp, frost on the window, no people, dark fantasy otome visual novel background, painterly anime style --ar 16:9 --niji 6

# bg_castle_hall
vast gothic castle hall at night, moonlight through tall stained glass windows, long shadows, no people, dark fantasy otome visual novel background, painterly anime style --ar 16:9 --niji 6
```

### CG-ები
```text
# cg_prologue_shadow
close-up of a young woman's wrist wrapped by a living tendril of black shadow, a black silk ribbon glowing silver in her sleeve, candlelit gothic chamber, tense atmosphere, dark fantasy otome visual novel CG, painterly anime style --ar 16:9 --niji 6

# cg_prologue_close
an adult silver-haired prince leaning close to whisper into a young woman's ear, candlelight, intimate tension, dramatic shadows, fully clothed, dark fantasy otome visual novel CG, painterly anime style --cref [VALERIUS_SHEET_URL] --cw 60 --ar 16:9 --niji 6
```

## გმირი

გმირის სახე CG-ებში ნაწილობრივ ჩანს: ზურგიდან, პროფილში, ჩრდილში. ეს ჟანრის
კონვენციაა და მოთამაშეს თავის მასში დანახვაში ეხმარება. Sprite გმირს არ სჭირდება.
