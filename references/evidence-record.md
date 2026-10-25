# Bizonyítéklap: elemzési rekord sablon

A mezők üresen hagyhatók, ha a forrás nem ad rájuk választ, de ilyenkor szerepeljen: `nincs adat`.

```yaml
research_question: ""
unit_id: ""
source_id: ""
speaker: ""
date: ""  # YYYY-MM-DD vagy ismert pontosság
context_and_genre: ""
source_url: ""
source_type: "primary_recording | official_transcript | full_press_reprint | excerpt | commentary | user_input | fiction"
source_verified_at: ""
verbatim_span: ""  # csak pontosan ellenőrzött, szükséges hosszúságú idézet
location_in_source: ""  # időbélyeg / bekezdés / lapszám / oldalszám
observable_features: []
codes: []
interpretation: ""
alternative_readings: []
confidence_basis: ""  # bizonyosság indoka, NEM numerikus kamu-pontszám
fact_status: "verified | speaker_claim | uncertain | fictional"
limitations: []
editorial_transformations: []
```

## Bizonyosság jelölése

- **Közvetlen megfigyelés**: szöveghelyből bárki visszaellenőrizheti a szóválasztást/szerkezetet.
- **Megalapozott értelmezés**: a megfigyelésből és kontextusból következik, de alternatív olvasatok lehetségesek.
- **Hipotézis**: további forrás vagy összehasonlítás szükséges.
- **Nem állapítható meg**: hiányzik a szó szerinti szöveg, kérdés, kontextus vagy beszélőazonosság.

**Ne használj százalékos bizonyossági értéket kalibráció nélkül.** A forrás ismertsége és a forrás tartalmának igazsága két külön probléma.

## Rövid kimenet újságíróknak

> Megfigyelhető elem → szó szerinti támpont → az előfeltevés vagy keret lehetséges szerepe → mi ellenőrizhető / mi nem → jelentésmegőrző szerkesztési opció (ha kérik).

## Korpusz-összevetéshez

Ha több szöveget elemzel, egységesíteni kell a műfajt, a szegmentálást, a transzkriptumkezelést és a forrásmegjelölést. Egy médiacikk idézetét ne számold úgy, mintha teljes beszéd lenne. A kódszámok csak a választott korpuszra és egységre vonatkoznak.
