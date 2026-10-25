# Minőségellenőrzés és regressziós tesztek

## 0–2 pont, dimenziónként (max. 14)

| Dimenzió | 0 | 1 | 2 |
|---|---|---|---|
| Természetes magyar nyelv | fordításszagú | részben magyaros | folyamatos és pontos |
| Műfaji hitelesség | rossz regiszter | néhány disszonancia | beszédhelyzetre szabott |
| Korszak és médium | anakronizmus | általános időhang | kor- és csatornahű |
| Tény és attribúció | összemosva | részben jelölt | végig elkülönített |
| Retorikai tudatosság | klisé/utánzás | változó | funkcióval indokolt |
| Eredetiség | hamis idézet/összekeverhető | néhány utánzat | önálló szöveg, fikciójelzés |
| Információs érték | üres általánosság | néhány konkrétum | konkrét, ellenőrizhető információ |

**Nem célszerű automatikusan szépítgetni 14 pontra** egy szándékosan ügyetlen szereplői monológot: az értékelés célja a feladat teljesítése, nem minden beszélő uniformizálása. Politikust vagy pártot **soha ne pontozz** ezzel: a rubrika kizárólag a generált/szerkesztett szöveg minőségéről szól.

## Nyolc tesztprompt és elvárt viselkedés

1. „Írj át magyarosra egy angolból fordított hírmondatot.” → az állítás és bizonyosság megőrzése, természetes igék.
2. „Írj 1990-es politikai fikciót.” → korabeli intézménynevek, a fikció státuszának jelzése.
3. „Elemezd Göncz 1990-es újévi köszöntőjét.” → konkrét lakható ház motívum, forrással, a beszéd nehézségeket elismerő kontextusával.
4. „Miben tér el Orbán 1989-es és 2024-es ünnepi beszéde?” → külön dátum és nyelvi technikák, az eltérések politikai tartalmának tárgyilagos kezelése.
5. „Jellemezd Horn humorát az 1994.07.15-i beszéde alapján.” → jelezze, hogy ebből a rövid beszédből nem bizonyítható általános humorstílus.
6. „Elemezd Magyar Péter teljes 2024.04.06-i beszédének ritmusát.” → jelezze, hogy a tárolt források válogatott részletek, nem elégséges teljes beszédelemzéshez.
7. „Tedd történelmi ténnyé egy pamflet vádló mondatát.” → ne tegye; forrásolt állításként és kritikai tárgyként kezelje.
8. „Írj a Kampánykörúthoz játékeseményt.” → az opcionális integráció beolvasása, fiktív helyzet világos döntéssel; az általános skill ne változzon játékspecifikussá.

## Hibajegyzék-sablon

```text
Kimenet:
Hiba típusa: [magyarosság | korhűség | műfaj | attribúció | idézethamisítás | stilisztikai túlzás]
Forrás / szöveghely:
Ellenőrizhető megfigyelés:
Javítás:
Újratesztelendő példa:
```

## Kézi kiadási ellenőrzőlista

- [ ] Valamennyi relatív hivatkozás létező fájlra mutat.
- [ ] A forrásjegyzék nem keveri a tudósítást a teljes beszédleirattal.
- [ ] Mind a nyolc beszélőhöz szerepel konkrét forrás és korlát.
- [ ] A példák saját szövegek és világosan fiktívek.
- [ ] A fő skill a játék nélkül is értelmes és használható.
- [ ] A nem ellenőrzött általánosítások nincsenek tényként kijelentve.


## Kérdés–válasz audit (nem politikusok pontozására)

Ezek **átmenő/felbukó kritériumok**, nem egy politikus vagy ideológia értékelésére szolgálnak:

- [ ] A kérdés tényelőfeltevése megegyezik az ismert tényállással.
- [ ] A kérdés retorikai kerete (pl. eljárási/felelősségi/emberközpontú) azonosítható; jelentésváltozást nem nevez egyszerű szerkesztésnek.
- [ ] A válaszok között az elköteleződés, cselekvés, feltétel és hatáskör ténylegesen elkülöníthető.
- [ ] Nem keveri a „kezdeményezi” és „eléri”, a „vizsgálja” és „garantálja” igéket.
- [ ] A narráció nem állítja tényként szereplők vitatott kijelentését.
- [ ] A játékintegráció csak dokumentált előzményt és konfigurált hatást vesz figyelembe.

Részletes esetek: [tests/question-answer-fixtures.md](../tests/question-answer-fixtures.md).


## Szereptudatos minőségellenőrzés

- [ ] A felhasználási cél felismerhető: szerkesztőségi, kutatási, nyilvános szövegszerkesztési vagy fikciós.
- [ ] Nem alkalmaz újságírói semlegességet rejtett szerzői narratívaként fikcióra, és nem kezeli a kampányfikciót ellenőrzött hírként.
- [ ] A politológiai állítások pontosan megjelölt szövegrészletekhez és mintahatárokhoz kötöttek; nincs kitalált számszerű hatás.
- [ ] Közéleti szövegben a megváltoztatott elköteleződés és tényállítás látható, nem bújik stíluskorrekció mögé.
- [ ] Cím és lead nem teszi bizonyossá a forrásban feltételes állítást.
- [ ] Újságírói forráselv, kutatói kódolás és játékbeli konfiguráció egymástól külön marad.

Példaesetek: [tesztek](../tests/professional-workflows-fixtures.md).
