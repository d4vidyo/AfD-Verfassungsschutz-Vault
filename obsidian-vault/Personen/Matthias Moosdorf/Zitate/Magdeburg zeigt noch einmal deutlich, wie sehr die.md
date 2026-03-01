---
type: zitat
speaker: "[[Matthias Moosdorf]]"
date: 2024-12-22
topic: Demokratieprinzip
page_bfv: 962
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Matthias Moosdorf]] vom 22.12.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Magdeburg zeigt noch einmal deutlich, wie sehr diese Kartellparteien abgewirtschaftet haben. [...] Der ganze linke Verbrecherclan schaut weg. So lange bis sie ihre Krokodilstränen vergießen können. Diese gelten jedoch eher ihrem Kontroll- und damit Machtverlust als den Opfern ihrer Politik. Im Mittelalter hätte man Politiker mit diesem Karma nicht nur abgewählt. Einstweilen bleibt nur, die AfD zu wählen. Wir sind die einzige Partei, die die Verantwortlichen zur Rechenschaft ziehen wird - wenn wir dazu genügend Stimmen haben!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 962

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