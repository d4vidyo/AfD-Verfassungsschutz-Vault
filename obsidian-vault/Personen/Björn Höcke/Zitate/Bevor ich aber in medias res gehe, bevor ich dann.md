---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2022-12-02
topic: Sonstiges
page_bfv: 749
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 2.12.2022 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Bevor ich aber in medias res gehe, bevor ich dann auch zur schlimmen Lage in diesem Lande komme und die Schuldigen klar benenne, möchte ich auch noch einmal Danke sagen. Danke, an die treuen Mitstreiter des Vorfeldes, die heute hier sind. Ich hab das COMPACT-Magazin gesehen, ich hab die Kehre gesehen, ich hab Ein Prozent gesehen. Liebe Freunde, das ist toll, dass ihr hier seid und gemeinsam mit uns, der AfD, dieses Zeichen für Einigkeit und Recht und Freiheit setzt. Ja, wir sind die Partei aber ohne Vorfeld sind wir nichts, liebe Freunde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 749

**Verfassungsschutz Kategorisierung:** Sonstiges.

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