# Annotációs kódkönyv — Goulash Touch

## Egységek és dimenziók

**Elemzési egység:** alapértelmezésben mondat vagy interjú-fordulópár; narratív játékban a teljes helyzet + kérdés + opciók együtt. Mindig rögzítsd a tényleges egységet. A kódok nem politikai „jó/rossz” minősítések.

| Kód | Mit jelöl? | Mikor használd? | Mikor ne? |
|---|---|---|---|
| `PRESUPPOSITION` | Állításként nem kimondott, de előfeltételezett tartalom | A kérdés egy vitatható eseményt adottnak vesz | Ha az állítás csak nyílt hipotézis |
| `AGENCY` | A cselekvő, felelős vagy döntéshozó nyelvi kijelölése/elfedése | „A miniszter döntött” vs. „döntés született” | Ha nincs felelősségi/kauzális tét |
| `FRAME` | Problémaértelmező keret | Ugyanaz a tény ellátási, költségvetési vagy jogi oldalról jelenik meg | Puszta témamegjelölésnél |
| `EVAL_LEXICON` | Értékelő szó vagy kifejezés | „Megmentés”, „megszorítás”, „árulás” megítélést sugall | Csak szakmai terminus bizonyíthatóan leíró használatakor |
| `METAPHOR` | Forrás- és céltartomány közötti képi átvetítés | „Vihart áll ki a rendszer” | Rögzült, már nem értelmezhető köznyelvi ige esetén: opcionális |
| `COLLECTIVE_ID` | Közösségi önazonosítás | „Mi, …” külön kijelölt csoporttal | Ha a „mi” csak két beszélgető fél |
| `QUESTION_DESIGN` | Kérdés alakja és elvárt válasza | Zárt/nyitott, kérdéselőtag, visszakérdezés, kettős kérdés | Nem kérdő funkciójú idézetnél |
| `ANSWER_RESP` | Válasz kapcsolata a kérdéssel | Teljes/részleges válasz, átkeretezés, kitérés, visszakérdezés | Ha a korábbi kérdés hiányzik: jelöld nem értékelhetőnek |
| `COMMITMENT` | Nyelvileg vállalt cselekvés ereje | Javaslat, szándék, ígéret, feltétel, kijelentett döntés | Ha puszta érzelmi értékelés |
| `EPISTEMIC` | Bizonyosság, forrásjelölés | „Állítólag”, „felmerült”, „biztosan” | Ha a következtetés csak az olvasó fejében van |
| `TEMPORAL` | Időbeli viszony | Terv, folyamat, bejelentés, visszatekintés | Ha nincs értelmezési jelentősége |
| `GENRE_SWITCH` | Regiszter vagy műfaj váltása | Parlamentáris → személyes történet / riport → vélemény | Pusztán tematikus váltásnál |

## Eljárási szabályok

- Kódold külön a **szó szerinti szerkezetet** és az **értelmezett funkciót**; egy kérdés lehet nyelvtanilag nyitott, de értékelő előfeltevést tartalmazó.
- Minden rekordban legyen `evidence_span`, `interpretation`, `alternative_reading`, `confidence_basis` és `source_id`.
- Egyetlen megfigyelés is indokolhat kódot; **általános tendenciára** csak megfelelő mintával következtess.
- A `COMMITMENT` szintjei nem automatikus rangsor: `nincs` / `felvetés` / `szándék` / `feltételes vállalás` / `egyértelmű vállalás` / `bejelentett döntés`. Az állított cselekvés megtörténtét külön ellenőrizd.
- A `ANSWER_RESP` címkék: `válaszol` / `részleges` / `átkeretez` / `kitér` / `visszakérdez` / `nem eldönthető`. Az `átkeretez` nem automatikusan `kitér`.
- Több lehetséges értelmezés esetén mindkettőt dokumentáld; *belső szándékot* ne kódolj bizonyíték nélkül.

## Fiktív mintakódolás

**Kérdés:** „Miért hagyták megszűnni a rendelő ügyeletét?”

- `PRESUPPOSITION`: az ügyelet megszűnt, valakik hagyták ezt megtörténni — *mindkettő ellenőrizendő*.
- `AGENCY`: a „hagyták” felelősként feltételez egy meg nem nevezett alanyt.
- `QUESTION_DESIGN`: nyelvtanilag okkérdés, de egy már megtörtént mulasztásból indul ki.

**Válasz:** „Az átszervezést még vizsgáljuk, döntés nincs.”

- `ANSWER_RESP`: a kérdés kiinduló feltételét vitatja/átkeretezi; ez önmagában nem válaszkerülés.
- `EPISTEMIC` és `TEMPORAL`: a „még”, „nincs” a folyamat aktuális állapotát jelöli.

A példa nem valós ügyet ír le, és semmilyen politikai félnek nem tulajdonítható.
