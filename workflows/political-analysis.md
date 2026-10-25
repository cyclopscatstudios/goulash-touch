# Politológusi / retorikai kutatói munkafolyamat

**Cél:** Magyar politikai nyelvi jelenségek **leíró, megismételhető** vizsgálata. A retorikai leírás nem választói szándékmérés, nem politikai teljesítményrangsor, és nem pszichológiai diagnózis.

## Négy elemzési szint

1. **Mikro:** szóválasztás, szóismétlés, metafora, megszólítás, névmás, igealak, tagadás, modalitás, mondatritmus.
2. **Mezo:** beszédaktus, érv, kérdés–válasz viszony, előfeltevés, átkeretezés, ellenfél állításának parafrázisa, narratív láncolat.
3. **Makro:** intézményi beszédhelyzet, év, médium, alkalom, párt-/kormányzati szerep, cél és forráskörnyezet.
4. **Időbeli:** hogyan változik egy kifejezés és funkciója ugyanannál vagy több beszélőnél — csak összemérhető minták alapján.

## Korpuszkezelési minimum

Minden szöveghez:
- `speaker`, `date`, `institutionalRole`, `genre`, `medium`, `audienceContext`;
- `sourceUrl`, `sourceType` (elsődleges átirat / másodközlés / tudósítás), `completeness` (teljes / kivonat / ismeretlen);
- `unitOfAnalysis` (mondat / kérdés-válasz pár / bekezdés / beszéd), `selectionRule` (hogyan került be);
- kódolási döntés, rövid bizonyíték, bizonytalanság.

A nyolc történeti retorikai inspirációt **nem** tekintheted reprezentatív népességi vagy teljes életműmintának. Válassz összehasonlítható helyzeteket, és tedd láthatóvá a forrástorlódást (pl. ünnepi beszédek túlreprezentáltsága).

## Elsődleges kódkönyv

| Kód | Kérdés | Példa (fiktív) |
|---|---|---|
| `HIST_CONTEXT` | Milyen történelmi keretbe helyezi az ügyet? | „Egy évtizede másként működött…” |
| `COLLECTIVE_WE` | Kik tartoznak bele a „mi”-be? | „Mi, a város lakói…” |
| `PRESUPPOSITION` | Mit vesz kész ténynek a kérdés? | „Miért halogatták a döntést?” |
| `REFRAME` | Elfogadja-e a válasz a kérdés keretét? | „Nem a bezárásról, hanem a nyitvatartásról van szó.” |
| `COMMITMENT` | Mit vállal ténylegesen a beszélő? | „Kezdeményezünk egy egyeztetést.” |
| `MODALITY` | Tény, lehetőség, feltétel, előrejelzés? | „Lehetséges, hogy…” |
| `ATTRIBUTION` | Kinek tulajdonítható az állítás? | „A helyi egyesület szerint…” |
| `METAPHOR` | Konkrét kép mely fogalmat magyarázza? | „A költségvetés szűk mozgástér.” |
| `OPPOSITION` | Milyen alternatívákat állít szembe? | „Nem gyors döntés, hanem alapos vita kell.” |
| `EVIDENCE` | Van-e konkrét ellenőrizhető adat? | jegyzőkönyv, dátum, nyilvános dokumentum |

**Ne csak jelenlétet kódolj:** jegyezd fel, milyen funkciója van az eszköznek az adott szövegben. A „mi” lehet inkluzív közösségteremtés, intézményi beszélő vagy egyszerű többes szám is. Ugyanaz a nyelvi forma nem bizonyít azonos szándékot vagy hatást.

## Elemzési menet

1. Határozd meg a kutatási kérdést és az elemzési egységet.
2. Ellenőrizd a korpusz eredetét; jegyezd fel a hiányt, csonkolást és médiumot.
3. Kódolj konkrét, visszakereshető szöveghelyekhez; közvetlen idézetet csak ellenőrzötten.
4. A kódokból következtess funkcióra, **külön** jelezve a lehetséges alternatív magyarázatot.
5. Összehasonlításnál csak indokolt esetben adj gyakoriságot; nevezd meg a nevezőt (beszédek száma / szavak / kérdés-párok).
6. A gyakoriságból ne következtess automatikusan hatásosságra, szavazói motivációra vagy választási eredményre.
7. Ha több annotátor dolgozik, dokumentáld a nézeteltérések rendezését; ne állíts intercoder-megbízhatóságot mérés nélkül.

## Ajánlott kimenet

```text
Kutatási kérdés és időszak:
Korpusz és kiválasztási szabály:
Elemzési egység:
Szöveghely / forrás:
Kódok és leíró megfigyelések:
Funkcióra vonatkozó értelmezés:
Alternatív értelmezés és korlát:
Mire NEM ad választ ez az adat:
```

Lásd még: `../references/corpus-method.md`, `../references/speech-analyses.md`, `../references/question-framing.md`, `../references/answer-interpretation.md`.
