---
type: zitat
speaker: "[[Heiko Scholz]]"
date: 2025-02-20
topic: Demokratieprinzip
page_bfv: 953
source: 'Rede auf YouTube'
status: Unbewertet
---

# Zitat: [[Heiko Scholz]] vom 20.2.2025 veröffentlicht auf: 'Rede auf YouTube'
> [!quote] Aussage
>Abschiebungen, wie vorige Woche in Hessen, werden zu Wahlkampfzwecken vorgetäuscht. Wie dumm hält eigentlich diese Frau Faeser unseren deutschen Wähler? [...] Kein Land dieser Welt kann eine derartige unqualifizierte und unkontrollierbare Migrationsflut verkraften. Und sobald wir in Regierungsverantwortung sind, werden wir dem ein Ende bereiten. Wir, das Volk, sind der Souverän und nicht die Erfüllungsgehilfen eines skrupellosen, machtbesetzenden Altparteienkartells, liebe Freunde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 953

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