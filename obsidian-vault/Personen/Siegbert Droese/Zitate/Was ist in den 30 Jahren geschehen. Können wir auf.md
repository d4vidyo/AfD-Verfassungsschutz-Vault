---
type: zitat
speaker: "[[Siegbert Droese]]"
date: 2022-07-30
topic: Demokratieprinzip
page_bfv: 601
source: 'Artikel auf Website des AfD-Kreisverbands Leipzig'
status: Unbewertet
---

# Zitat: [[Siegbert Droese]] vom 30.7.2022 veröffentlicht auf: 'Artikel auf Website des AfD-Kreisverbands Leipzig'
> [!quote] Aussage
>Was ist in den 30 Jahren geschehen. Können wir aufatmen? Können wir sagen, dass wir den Opfern der SED-Diktatur gerecht geworden sind? Die Antwort lautet: Nein. [...] Aufruf zur Denunziation, Ausspionieren über das Telefon, Demonstranten wird mit Psychiatrie gedroht, Andersdenkenden die Konten gesperrt, die Medien gleichgeschaltet. Um dieses gegen den Bürger in Anschlag bringen zu können, hat man einen Katalog von Angstszenarien aus der linksideologischen Wunderlampe aufsteigen lassen, die keinen Widerspruch dulden. Wieder ist Deutschland zu einem Gefängnis umfunktioniert worden, psychisch wie physisch geht man jetzt auch an die Kinder. Nein, ein Großteil der Deutschen hat nichts gelernt und die Opfer der DDR Diktatur noch einmal zu Opfern gemacht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 601

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

---
## Meine Auswertung:

**Meine Bewertung:** `INPUT[inlineSelect(option(Unbewertet), option(Legitim), option(Fragwürdig), option(Nicht legitim), defaultValue(Unbewertet)):status]`

_Mein Kommentar:_ 


---
# Nächste Aussage:
```dataview
TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
FROM "Personen"
WHERE type = "zitat" and status = "Unbewertet" AND file.name != this.file.name
SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
LIMIT 10
```