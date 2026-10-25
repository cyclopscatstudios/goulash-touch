# A Goulash Touch beszédkorpuszának fejlesztési módszere

## A jelenleg dokumentált forrásanyag

**Forrásvezérelt, kvalitatív beszédelemzés**: legalább egy ellenőrizhető nyelvi szakasz mind a nyolc választott beszélőtől, néhányuknál két időpont vagy műfaj összevetése. Nincs nyelvmodell-finomhangolás, hangfelvételek akusztikai elemzése, statisztikai stilometria vagy reprezentatív életműmintavétel. A forrásanyag korlátait külön dokumentáljuk, hogy az elemzés a későbbi bővítésekkel is összehasonlítható maradjon.

## Minden új szövegegység annotációja

```yaml
source_id: "G1"
speaker: "Göncz Árpád"
date: "1990-12-31"
genre: "államfői újévi köszöntő"
venue: "nyilvános országos köszöntő"
source_type: "MTI-ként jelölt teljes szöveg, alapítványi archívumban"
source_url: "https://www.gonczarpad.hu/goncz-arpad-koztarsasagi-elnok-ujevi-koszontoje"
verified_on: "2026-10-24"
scope: "a beszéd intézményi metaforát használó szakasza"
observation: "a demokrácia intézményét lakhatóság/metafora segítségével magyarázza"
function: "absztrakt alkotmányos fogalom konkretizálása"
limitation: "a nyelvi jelenség az adott beszédhelyzetre igazolt"
confidence: "magas — látható teljes szöveg"
```

A `confidence` a **megfigyelés forrásoldali bizonyossága**, nem annak a valószínűsége, hogy a beszélő általános stílusa ez.

## Annotációs dimenziók

1. **Beszédaktus:** kérés, köszöntés, jelentés, válasz, polémia, magyarázat, vita.
2. **Közönség és csatorna:** egyéni megszólítás / testület / országos nyilvánosság / helyszíni és online közönség.
3. **Szerkezet:** narratíva, tétel–indoklás, kérdés–válasz, probléma–teendő, történeti analógia.
4. **Nyelv:** tagmondathossz, alárendelés, fókusz, igeidő, névmáshasználat, névelők, igekötők, stilisztikai regiszter.
5. **Retorikai eszköz:** ismétlés, antitézis, metafora, irónia, felsorolás, metakommunikáció.
6. **Állítás típusa:** ellenőrzött tény / politikai állítás / vélemény / bizonytalan következtetés / retorikai kép.
7. **Ellenolvasat:** mi lehet műfaj- vagy alkalomhatás, nem személyes stílus?
8. **Transzfer:** névtelen, személytől függetlenül használható írástechnikai tanulság — vagy kritikai figyelmeztetés.

## Mintavétel későbbi, szélesebb korpuszhoz

- **Beszélőnként több különböző műfaj** és legalább két eltérő év, amennyiben van forrás; a teljes szöveg + hang/videó összevetése ideális.
- A történeti anyagban **eredeti lapszám, országgyűlési napló vagy levéltári forrás** előnyben az internetes újraközléssel szemben.
- Minden beszélőnél kell *ellenpélda*, amelyben a vélt sajátosság nem jelenik meg. Például egy hosszú szónoklat nem bizonyítja, hogy rövid interjúban is körmondatokban beszélt.
- Az egymáshoz közel álló korszakok azonos beszédműfajait is hasonlítsd össze, hogy a különbség ne pusztán a műfajból eredjen.
- Az összehasonlítást mindig **szövegen belüli** bizonyítékhoz kösd. Nem kell személyiséget, képességet vagy erkölcsi minőséget megítélni.
- A különböző pártállások és korok forrásai egyaránt bekerülhetnek; a reprezentativitás többet ér, mint a kedvenc idézet.

## Licenc, adat és szöveghűség

Ne tölts teljes beszédeket a skillbe azonosítatlan felhasználási joggal. Tárold a metaadatokat, linkeket, saját rövid megfigyeléseket és nagyon rövid, indokolt idézeteket. Saját példákat egyértelműen jelölj. Külső beszédszövegek, hangok és fordítások újrafelhasználási jogát külön ellenőrizd.

## Ellenőrzési protokoll

A profil csak akkor módosulhat határozott kijelentésre, ha (1) a beszédhely azonosítható, (2) a nyelvi jelenség ténylegesen látszik, (3) egy másik műfaj/korszak nem mond neki nyilvánvalóan ellent, (4) a korlát és a bizonyosság is szerepel.
