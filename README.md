# Goulash Touch — kutatásalapú magyar politikai nyelvi skill

**Cél:** Ellenőrizhető, forrásokra épülő magyar politikai és közéleti nyelvi elemzés, amelyből másodlagosan szövegszerkesztés és kreatív szövegalkotás vezethető le. Nem kizárólag Kampánykörút-skill: a játékhoz tartozó kiegészítők opcionális integrációként szerepelnek.

## Fő képességek

- **Forráskritikus elemzés:** forrás és szöveghely → megfigyelés → annotáció → értelmezés → alternatív olvasat → korlátok.
- **Retorikai és nyelvi vizsgálat:** nyolc történeti és kortárs beszélő forrásolt példáin keresztül, beszélő- és korszakfüggetlen módszertannal.
- **Kérdés–válasz értelmezés:** előfeltevések, kérdéskeretezés, átkeretezés, állítások és vállalások megkülönböztetése.
- **Szakmai alkalmazások:** újságírói, politológusi, közéleti szövegírói és fikciós munkafolyamatok.
- **Átlátható minőségellenőrzés:** annotációs kódkönyv, bizonyítéklap, kézi tesztesetek és forrásjegyzék.
- **Opcionális Kampánykörút-integráció:** narráció, kérdés, válaszopció és dokumentált játékmechanikai következmény külön elemzése.

A korpusz nem reprezentatív és a skill nem finomhangolt nyelvmodell. Az elemzési szabályokat, a források teljességét és a következtetések bizonytalanságát minden feladatnál külön ellenőrizni kell.

## Könyvtárstruktúra

```text
goulash-touch/
├── SKILL.md
├── README.md
├── references/
│   ├── professional-context.md  # Újságíró/elemző/szövegíró/játékíró munkamódok
│   ├── speech-analyses.md        # Nyolc beszélő részletes, forrásalapú profilja
│   ├── source-register.md        # Dátum, médium, URL, forrástípus, korlát
│   ├── rhetorical-techniques.md  # Átvihető nyelvi mechanizmusok
│   ├── registers.md              # Műfajok és beszédhelyzetek
│   ├── hungarian-style.md        # Magyarosítás, szóhasználat, ritmus
│   ├── era-and-fact-check.md     # Korhűség és tényellenőrzés
│   ├── question-framing.md       # Kérdések keretezése és előfeltevései
│   ├── answer-interpretation.md  # Válasz, ígéret, feltétel, kitérés
│   ├── corpus-method.md          # Kutatási/annotációs módszer
│   ├── examples.md               # Eredeti, semleges stíluspéldák
│   └── quality-and-tests.md      # Értékelési rubrika és tesztek
├── workflows/
│   ├── journalism.md            # Szerkesztőségi, interjú- és címaudit
│   ├── political-analysis.md    # Retorikai kutatási, korpusz- és kódolási workflow
│   └── public-affairs-writing.md # Közéleti szöveg és nyilvános beszéd szerkesztése
├── integrations/
│   ├── kampanykorut.md           # Opcionális játékspecifikus szabályok
│   └── kampanykorut-context.md   # Kontextus- és döntési szövegaudit
└── tests/
    └── question-answer-fixtures.md # Regressziós esetek
```

## Használat

A skillt támogató agentben a `goulash-touch` könyvtárat telepítsd / importáld a környezet dokumentációja szerint, úgy, hogy az agent a `SKILL.md` és a relatív `references/` hivatkozások fájljait is olvashassa.

Példafeladatok:

- „Elemezd ezt az 1992-es politikai beszédet: nevezd meg a retorikai szerkezetét, és különítsd el az állításokat a tényektől.”
- „Szerkeszd természetes magyar hírnyelvre ezt a sajtóközleményt, az eredeti jelentés megőrzésével.”
- „Írj történeti fikcióhoz egy 1990-es parlamenti párbeszédet; legyen korhű, de ne valós személyeknek tulajdonított idézet.”
- „Mutasd meg ugyanazt a semleges közéleti információt egy helyi riport, egy jogi tájékoztató és egy civil fórum szövegeként.”

## Kérdés–válasz használati példa

„Elemezd ezt a leíró politikai helyzetet és a válaszopciókat. Különítsd el a kérdés előfeltevéseit, a válaszok explicit vállalását és a lehetséges kontextus-ellentmondásokat. Az opciók cselekvését és azonosítóit ne változtasd meg.”

A nyelvi auditot a `references/question-framing.md` és `references/answer-interpretation.md` fájl adja. Ha a kérdés a Kampánykörútban szerepel, aktiváld az `integrations/kampanykorut-context.md` modult is. **Konkrét repo/JSON-részlet nélkül a mezőnevek és események csak modellező példák.**

## Bizonyíték és korlát

A profilok **válogatott nyilvános források kvalitatív közeli olvasásán** alapulnak, nem nagymintás stilometriai kutatáson. A legjobban alátámasztott példák közvetlenül olvasható, dátumozott teljes szövegből készültek; Magyar Péternél a most vizsgált anyag nagyrészt sajtóban közölt részlet, ezért nem állítható, hogy a teljes beszédminta ismert. Csurka 1992-es írása újraközlésekből érhető el; a szövegkritikai egyeztetés további munkát igényel. Bármelyik beszélő későbbi vagy más műfajú nyelvi jellemzését új forrás alapján kell felülvizsgálni.

A Goulash Touch nem tartalmazza más skill szerzői jogilag védett szövegét; a `hungarian-humanizer` és `interpreting-hungarian` ihlető munkafolyamatként szolgálnak, nem másolt függőségek.

**Státusz:** kutatási workflow-ként használható, de sem empirikusan validált tudományos modell, sem reprezentatív beszédkorpusz; a teljes forrásellenőrzés és emberi értelmező kontroll szükséges.


## Ajánlott kipróbálás

1. **Újságírás:** „Elemezd ezt az interjúkérdést: milyen előfeltevést tartalmaz, és hogyan lehet az állítást nem torzító módon megfogalmazni?”
2. **Politológia:** „Készíts annotációs táblázatot az alábbi két, pontosan hivatkozott beszédből; kódold a kérdés-átkeretezést és a feltételes vállalást.”
3. **Szövegírás:** „Szerkeszd közérthetővé ezt a nyilvános tájékoztatót úgy, hogy a bizonytalanságok és vállalások változatlanok maradjanak.”
4. **Kampánykörút:** „Az alábbi jelenetnél auditáld a narrációt, a kérdést és a válaszopciókat a megadott korábbi döntések figyelembevételével; a mechanikát ne módosítsd.”

Az olvasónak és a modelleknek mindig adják át az **eredeti forrást és a kívánt kimenetet**; a skill önmagában nem tölti le a kapcsolódó beszédeket és nem validálja a játékadatokat.

## Alapértelmezett kimenet

Az elemző mód **nem írja át** a szöveget automatikusan. Először megadja a forrásadatokat, ellenőrizhető nyelvi megfigyeléseket, kódokat, értelmezési lehetőségeket, korlátokat és nyitott kérdéseket. Szövegváltozatot csak kifejezett kérésre készít. A forráshiányt nem fedi el általános stílusjelzőkkel.
