# Kampánykörút – játékbeli szövegek

A játékban a narráció a játékos helyzetét világítsa meg, ne győzködje valós politikai nézetekről. A játékmechanika adatai elsőbbséget élveznek a stilisztikai finomítással szemben.

## Játékesemény szerkezete

1. **Cím:** rövid, felismerhető helyzet; kerüld az általános „Új lehetőség” típusú címet.
2. **Helyzet:** ki, hol, miért keresi meg a játékost? Mi most a probléma?
3. **Dilemma:** valódi választás két vagy több érthető szempont között. Nem szükséges minden opciót ugyanolyan hangnemben írni.
4. **Opciók:** cselekvő ige, kézzel fogható döntés, ne üres morális címke.
5. **Következmény:** mi változik a játék világában? A mechanikai hatás pontos maradjon.

## Játékbeli természetesség

- A stábtag nem tudja a választás végeredményét előre.
- Egy helyi konfliktus érződjön helyinek: valódi helyzet, szereplők, tét (de ne találj ki valós tényként helyi adatot).
- Ne használj ugyanazt az udvarias és emelkedett hangot minden szereplőre.
- Egyes karakterek lehetnek ügyetlenek, opportunisták vagy körülményesek; a jó szerkesztés nem teszi mindet szellemes szónokká.
- Az opcióban megjelölt költség, hatás és feltétel soha ne változzon pusztán stilisztikai javítás miatt.

## Fiktív példa

**Cím:** Ki fizeti a termet?

**Helyzet:** „A helyi csapat vitafórumot szervezne, de a bérelhető terem drágább a vártnál. A szervező szerint a kisebb hely is elég lenne. A többiek tartanak tőle, hogy sokan kívül rekednek.”

**Opció A:** „Béreljétek ki a nagyobb termet.”
**Opció B:** „Legyen kisebb, kötetlen beszélgetés.”

**Következmény:** „A rendezvény formája és költsége megváltozik. A játékmechanikai értékeket kizárólag az átadott konfiguráció alapján add hozzá.”

## Játékos és történeti fikció

Ha valós pártok vagy politikusok szerepelnek egy alternatív történetben, a megfogalmazásnak egyértelművé kell tennie, hol kezdődik a játék fikciója. Valós politikusnak ne tulajdoníts ellenőrizetlen valódi idézetet.

## Kérdés–válasz kontextusértelmezés

A játékban a **leíró narráció**, a **döntési kérdés**, a **válaszopció** és a **mechanikai következmény** külön elemzési egység. A teljes eljárás: [Kampánykörút kérdés–válasz kontextusértelmező](kampanykorut-context.md). Az általános, más műfajokban is használható háttér: [kérdéskeretezés](../references/question-framing.md) és [válaszértelmezés](../references/answer-interpretation.md).

Szerkesztéskor: (1) azonosítsd az eredeti narratív tényt, (2) elemezd a kérdés értelmezési keretét, (3) minden válaszból emeld ki a vállalt cselekvést és feltételt, (4) nézd meg az előző döntéseket, (5) **ne változtasd meg** az opcióazonosítókat, költségeket és hatásokat. A narratíva lehet drámai, de a szereplői vád ne váljon véletlenül narrátori ténnyé.

## Szöveghossz és olvasási terhelés — Kampánykörút-specifikus szabály

A játékban a kérdést és **az összes látható választ együtt** kell elolvasni, ráadásul sok egymást követő körben és mobilon is. A szebb fogalmazás **nem** indok a szöveg meghosszabbítására. A kérdés a teljes narrációt és a végső döntési kérdőmondatot is magában foglalja.

Az alábbi számok **kezdeti, tesztelhető szerkesztői küszöbök, nem tudományosan igazolt olvasási határok**. Kiindulás: a `2026_tisza_questions_v2.json` 32 kérdésének és 128 válaszának szószámai (kérdésmedián 38,5; válaszmedián 16; teljes döntésmedián 102; legnagyobb teljes döntés 120 szó). A szószám szóközzel elválasztott elemeket jelent; a mérés közelítés, a mobil elrendezést külön kell tesztelni.

| Egység | Ajánlott cél | Felső határ |
| --- | ---: | ---: |
| Cím | 3–6 szó | 8 szó |
| Helyzetleírás **és** kérdés összesen | 30–45 szó | **55 szó** |
| Egy válaszlehetőség | 10–18 szó | **25 szó** |
| A teljes kérdés és a négy válasz együtt | kb. 90–110 szó | **120 szó** |

**Prioritás:** 1. tény- és jelentéshűség; 2. válaszok közötti világos döntéskülönbség; 3. rövidség; 4. stilisztikai díszítés. Ha a hosszkorlát és a szükséges jelentés ütközik, **ne csonkítsd** a döntést: hagyd meg az eredetit, vagy jelöld szerkesztői felülvizsgálatra. Indokolt kivétel lehet, de ne legyen észrevétlen.

### Kötelező tömörítési eljárás

1. Előbb mérd meg az **eredeti** szavak számát. A szerkesztett változat lehetőleg ne legyen hosszabb. Ha a rövidség rontaná az érthetőséget, legfeljebb 3 szóval vagy kb. 10%-kal legyen hosszabb, amelyik több — és maradjon a felső határok alatt.
2. A felvezető részben csak azt tartsd meg, ami a döntéshez szükséges: helyzet, tét, korlát, majd az egyértelmű kérdés. Ne ismételd meg a címet; ne legyen hosszú történelmi bevezető, ha nem módosítja a döntést.
3. Egy opció lehetőleg **egy fő cselekvést** és a ténylegesen hozzá tartozó feltételt írja le. Ne adj hozzá megjósolt választói reakciót, új vállalást, költséget vagy propaganda-hangulatú tölteléket.
4. A legfontosabb különbség az opció **első néhány szavából** derüljön ki; a választ a játékos egyszeri átfutással is meg tudja különböztetni.
5. Nézd meg a teljes kérdés + válaszok szószámát. Ha meghaladja a 120-at, csökkentsd a megismételt kontextust és a redundanciát; ne a politikai jelentést.
6. Mobilos ellenőrzés: valódi UI-ban teszteld, látszik-e a dilemma, és könnyű-e végigolvasni, illetve összehasonlítani a négy választ. A szószám önmagában nem garantálja ezt; számít a betűméret, sortörés és képernyőmagasság.
7. Csak jóváhagyás után cseréld le az eredeti kampányszöveget, és mindig jelöld, ha a retorikai keretezés változott.

**Kimeneti forma:** átírás esetén röviden mutasd meg `eredeti → javasolt` szószámmal a kérdést és az opciókat; jelöld, ha a szöveg túllépte a küszöböt vagy megváltozott a keretezése. Nem szükséges minden egyes rövidítéshez hosszas indoklás.

**Helyes alapállás:** ha az eredeti szöveg már érthető és megfelelő hosszú, mondhatod azt, hogy **„Nem javaslok átírást.”** A skill nem terjedelmesítési automatizmus.

A repo aktuális JSON-sémájához igazított ellenőrző: `scripts/check_campaign_copy.py`. Alapértelmezésben a `title`, `question`, `possibleAnswers[].label` mezőkkel számol; a program csak a hosszúságot ellenőrzi, **nem** dönti el, hogy a politikai jelentés megmaradt-e.
