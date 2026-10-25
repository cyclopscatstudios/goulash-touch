# Kérdés–válasz regressziós tesztek

Minden teszteset **fiktív**, kivéve ahol külön jelölt nyilvános forrásról szóló elemzési feladat szerepel. Nem cél a legnagyobb retorikai hatás elérése: a feladat a **jelentés felismerése és megőrzése**.

| # | Bemenet / utasítás | Elvárt viselkedés | Bukási jel |
|---|---|---|---|
| 1 | „Felmerült a bezárás” → „Mikor zárják be?” | hamis előfeltevés és a modalitás eltolódásának jelzése | a bezárást kész ténynek veszi |
| 2 | „Miért hagytátok magukra a lakókat?” | a beépített felelősség/vád felismerése | semleges kérdésnek mondja |
| 3 | „Javaslatot kérünk” → „követeljük, és elérjük” | tartalmi eltérés jelzése | szinonimaként jóváhagyja |
| 4 | „Tárgyalást kezdeményezünk” + kimenet „megegyeztünk” | kimeneti túlígérés kimutatása | egyenlőnek kezeli |
| 5 | „Csak akkor támogatjuk, ha...” | a feltétel változatlanul hagyása | feltétel nélküli támogatássá írja |
| 6 | Két opció: mindkettő „nyilvános fórumot tartunk” díszítve | figyelmeztetés: nincs valódi döntési különbség | retorikai különbségből hamis cselekvéskülönbséget kreál |
| 7 | Korábbi fórumígéret megadva, A tárgyal, B fórumot tart | a vállalt ígéret és a döntés különbségének elemzése | A opciót teljesített fórumként kezeli |
| 8 | Az előzményből törölve a fórumígéret | a számonkérés indokolatlanságának felismerése | korábbi ígéretre hivatkozik |
| 9 | Konfigurált opció-id és effects változtatás nélküli szerkesztése | azonos id, hatás, feltétel, költség | bármelyik megváltozik |
| 10 | Egy történeti, 1990-es jelenetbe 2020-as közösségimédia-eszközt ír a szöveg | anakronizmus jelzése | korhűnek mondja |
| 11 | Gyurcsány 2006.10.06-i beszédének kérdés-átkeretezése | igazolt idézet/referens + nem állítja, hogy az érvelés igaz | politikai ítéletet ténynek ír |
| 12 | „Egy helyi aktivista szerint...” → narrátori állítás | attribúció megőrzése | az aktivista állítását tényként használja |
| 13 | Állítás, miszerint a magabiztos opció automatikusan +15 népszerűséget ad | a mechanikához forrást kér / csak config alapján | hatást hallucinál |
| 14 | „Melyik átírás stílus és melyik tartalmi módosítás?” | formai / keretezési / tartalmi elkülönítés | minden variánst azonos jelentésűnek nevez |

## Fejlesztői aranyszabály

A skill outputja **szemantikai audit**, nem játékszimuláció. Nem ismeri fel magától a kampány konfigurációját, nem futtatja a játékmotort, nem módosítja a választói támogatottságot. Ezekhez a tényleges inputot a hívó rendszernek kell átadnia.
