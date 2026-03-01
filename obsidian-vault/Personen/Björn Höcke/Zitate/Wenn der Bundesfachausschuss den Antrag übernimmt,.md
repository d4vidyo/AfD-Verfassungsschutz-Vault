---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-11
topic: Demokratieprinzip
page_bfv: 950
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 11.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wenn der Bundesfachausschuss den Antrag übernimmt, freut uns das natürlich. Es ist ja letztlich nur ‘ne Petitesse, aber doch ‘ne bedeutende. Weil wir ja im Augenblick - und das ist der Status quo - ja tatsächlich Objekt fremder Interessen jetzt schon sind. Und die Aufgabe der AfD ist es eben, dass Deutschland wieder frei und souverän und selbstbestimmt wird. Das ist unser Auftrag. Und deswegen müssen wir das ,sein‘ einfügen und sind dann auch glattgezogen im Bundestagsprogramm.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 950

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