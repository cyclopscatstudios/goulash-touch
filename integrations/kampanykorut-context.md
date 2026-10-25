# Kampánykörút – kérdés–válasz kontextusértelmező

**Opcionális játékmodul.** A Goulash Touch általános politikai kérdés- és válaszértelmezését használja a Kampánykörút narratív eseményeinél. Nem módosítja a játék motorját, nem feltételez konkrét JSON-sémát vagy jelenleg létező mezőneveket. A projekt aktuális adatmodellje **mindig** elsőbbséget élvez.

## 1. Amit a játékszövegben külön kell választani

- **Leíró helyzet:** mi történt, kik érintettek, mit tudhat a játékos?
- **Feltett kérdés:** mit kér a játék a szereplőtől; milyen politikai dilemmaként keretezi?
- **Válaszopció:** mi az egyes döntések pontos cselekvése, elköteleződése és hangneme?
- **Következmény:** milyen előre deklarált játékállapot-változás követi a választ? (Nem következtethető ki puszta retorikából.)
- **Korábbi kontextus:** milyen korábbi döntés, viszony, erőforrás vagy megígért lépés tesz most valamelyik választ következetessé vagy ellentmondásossá?

Ne írj mindent beszélt dialógusként: a játék *leíró narrációja* és a játékosnak címzett döntési kérdés önálló szövegműfaj.

## 2. Minimális kontextuscsomag — leíró modell, nem konkrét repo-séma

A modell induljon az elérhető, bizonyított mezőkből; ismeretlen mezőt hagyjon `unknown` értéken. Például:

```json
{
  "campaignId": "fiktiv-pelda",
  "era": "1990-es évek (példa)",
  "playerRole": "helyi kampányvezető",
  "scene": "lakossági fórum előtti szervezői egyeztetés",
  "location": "fiktív város",
  "campaignStage": "kampány közepe",
  "knownFacts": ["a rendelő jövőjéről még nincs végleges döntés"],
  "sourceClaims": ["egy civil csoport szerint veszélybe kerülhet az ellátás"],
  "previousDecisions": ["a játékos korábban tárgyalást ígért"],
  "resources": {"campaignBudget": "unknown", "localOrganization": "unknown"},
  "question": "Hogyan léptek tovább?",
  "options": [
    {"id": "A", "text": "Kezdeményezzetek egyeztetést a döntéshozókkal."},
    {"id": "B", "text": "Szervezzetek nyilvános fórumot az érintettekkel."}
  ],
  "effects": "csak a játék tényleges konfigurációjából olvasható"
}
```

Az `era`, `previousDecisions` és `resources` **nem** származhat puszta fantáziából, amikor létező kampányadatot dolgozunk fel. Példában lehetnek fiktívek, a kimenetben jelöld ezt.

## 3. Feldolgozási pipeline

### A. Kontextus és tudásállapot

1. Azonosítsd, **mi ismert** és **mi csak szereplő állítása**. Vizsgáld a korszakot és a szerző által már megadott világállapotot.
2. Keress kapcsolatot az előzményekkel: beváltatlan ígéret, korábbi ellentmondás, nyitott konfliktus, meglevő helyi szervezet, költségkorlát, történeti fordulópont.
3. A narrátor nem ismerheti a jövő játékbeli kimenetét; csak a konfigurációból származó következményt mondhatja el megfelelő narratív formában.

### B. Kérdés auditja

1. `references/question-framing.md` szerint elemezd az explicit kérdést, az előfeltevést, a fókuszt, a polaritást és a nyitva hagyott cselekvéseket.
2. A narráció és a kérdés ugyanarról az állapotról beszéljen. „Felmerült” állapotból ne legyen „már bezártak” vagy „már eldöntötték”.
3. Ha a kérdés eleve véleményt sugall, a narrátor helyett **jelölt szereplői nézőpont** mondja (pl. „Az egyik aktivista szerint…”). A narráció lehet feszült, de nem lehet láthatatlanul pártos tényközlés.
4. Ellenőrizd, hogy a kérdés valóban a felkínált döntési lehetőségeket nyitja-e meg.

### C. Válaszopciók auditja

1. Minden válaszhoz rögzíts egy `coreAction` (mit tesz), egy `commitment` (mire kötelezi el magát), valamint opcionális `tone` (hogyan fogalmaz).
2. Különítsd el a **retorikai attitűdöt** a **mechanikai hatástól**. „Követeljük” önmagában nem garantál változást, „egyeztetünk” nem egyenlő a megállapodással.
3. `previousDecisions` tükrében vizsgáld a következetességet; a következetlenség lehet tudatos szereplői döntés, de nem történhet észrevétlen szerkesztési hibából.
4. A választási opciók legyenek világosan elkülöníthető **cselekvések vagy álláspontok**, ne ugyanannak a lépésnek három díszített változatai — hacsak a játék tényleg retorikai döntést kér.
5. Ne tüntesd el a kockázatot vagy a költséget, és ne változtasd meg az eredeti `id`-t, következményt vagy feltételt.

### D. Kimenet

- **Audit:** kérdés, előfeltevések, hiányzó kontextus, válaszok explicit/implicit jelentése, narratív ellentmondások, mechanikai eltérés.
- **Szerkesztés:** javított narráció + kérdés + opciók; rövid változásnaplóval; az eredeti azonosítók és mechanikai adatok változatlanok.
- **Történeti hitelesség:** csak a rendelkezésre bocsátott forrásanyag vagy ellenőrzött nyilvános tények alapján; eltérő történelmi korszakokhoz ne importálj későbbi fogalmakat automatikusan.

## 4. Végigvezetett fiktív példa — ugyanaz az opció, eltérő múlt

**Adott állapot:** nincs még végleges döntés a rendelőről. A szervezők előzőleg lakossági egyeztetést ígértek.

**Eredeti narráció:** „A rendelőt bezárják, és mindenki tőled várja, hogy megmentsd.”

**Probléma:** bizonyítatlanul véglegesnek állítja a még csak felvetett tervet; a „mindenki” kitalált egyetértést tételez, a „megmentés” kizárólagos hősszerepet sugall.

**Javított narráció:** „A város a rendelő nyitvatartásának csökkentését mérlegeli. A helyi szervezők emlékeztetnek rá, hogy korábban lakossági egyeztetést ígértetek. Most azt várják, mikor és hogyan kerül erre sor.”

**Javított kérdés:** „Hogyan folytatjátok az egyeztetést a javaslatról?”

**A opció:** „Kérjetek találkozót a döntéshozóktól, és szerezzétek meg a részletes tervet.”
- Beszédaktus: információszerzés és egyeztetés kezdeményezése.
- Elköteleződés: találkozó kérése; nem megállapodás.
- Előzmény: a korábbi lakossági egyeztetés ígéretét **önmagában nem teljesíti**.

**B opció:** „Tartsatok nyilvános fórumot, és gyűjtsétek össze az érintettek kérdéseit.”
- Beszédaktus: fórum szervezése, részvétel biztosítása.
- Elköteleződés: fórum megtartása; nem biztosítja a rendelő eredeti működését.
- Előzmény: a korábbi ígérethez közvetlenebbül kapcsolódó cselekvés.

**Kontextusváltozat:** ha *nem* történt előzetes fórumígéret, a narráció nem kérheti számon annak teljesítését. Ugyanaz a B opció így nem ígéret betartása, hanem **új részvételi kezdeményezés**. Ez a különbség nem puszta hangnem.

**Mechanikai hatás:** kizárólag az eredeti konfigurációból; itt nincs pontszám, választói reakció vagy népszerűségi következmény kitalálva.

## 5. Ugyanannak a döntésnek három eltérő kérdéskerete

Ugyanaz a *két cselekvés* (döntéshozói tárgyalás vagy nyilvános fórum), de eltérő hangsúly:

- Eljárási: „Milyen formában kértek tisztázást a javaslatról?”
- Felelősségi: „Ki előtt vállaltok elszámolást arról, hogyan képviselitek az érintetteket?”
- Közösségi: „Hogyan hallgatjátok meg azokat, akiket a változás érinthet?”

**Figyelmeztetés:** a három kérdés nem egyenértékű szinonima: tárgyalás/fórum választásnál más lesz hangsúlyos, és a „ki előtt vállaltok elszámolást?” már további felelősségi keretet vezet be. A narratíván belül legyen indokolt, melyiket választja a szerző.

## 6. A játékból érkező tartalomra ajánlott annotáció

A tényleges JSON-mezőket a fejlesztő térképezze rá erre az **elemzési sémára**; nem új játék-API.

```json
{
  "eventId": "example-01",
  "questionAudit": {
    "explicitAsk": "milyen lépést választ a játékos",
    "presuppositions": ["az ügy napirenden van"],
    "framing": "eljárási",
    "factStatus": "fiktív esemény, végleges döntés nincs"
  },
  "options": [
    {"id": "A", "coreAction": "tárgyalás kezdeményezése", "commitment": "találkozó kérése", "semanticRisk": "nem azonos a megállapodással"},
    {"id": "B", "coreAction": "lakossági fórum", "commitment": "fórum megszervezése", "semanticRisk": "nem azonos a rendelő megőrzésével"}
  ],
  "consistency": ["ellenőrizendő: a korábbi fórumígéret teljesül-e"],
  "mechanics": "ellenőrizetlen, változtatás tilos"
}
```

## 7. Kiadás előtti ellenőrzőlista

- [ ] A kérdésre valóban válaszolnak az opciók; nincs válasz nélküli dilemmaszöveg.
- [ ] A válasz cselekvését nem módosította a stílusjavítás.
- [ ] A szöveg külön kezeli a szereplő véleményét, a narrátor állítását és a játék biztos tényeit.
- [ ] A korábbi döntésekre és ígéretekre csak valós narratív kontextusból hivatkozik.
- [ ] A dátum, intézmény, technológia és médiacsatorna korhű.
- [ ] Egy opció nem árul el olyan mechanikai kimenetet, amelyet a játék nem közöl.
- [ ] Nincs hamis kettősség ott, ahol az alternatívák nem teljes körűek; ha szándékolt, jelölve van.
- [ ] A JSON-azonosítók, választási feltételek, költségek, hatások változatlanok.
- [ ] A szerkesztés nem a valódi választók politikai befolyásolására, hanem a fiktív játékhelyzet és a nyelvi jelentés pontosítására irányul.
