---
type: zitat
speaker: "[[Uwe Schulz]]"
date: 2025-02-20
topic: Demokratieprinzip
page_bfv: 966
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Uwe Schulz]] vom 20.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Der Fisch stinkt vom Kopf. Und daher ist es so wichtig, die Köpfe zu ändern. Anstelle von Schwachköpfen brauchen wir Schlauköpfe, auch wenn sie blonde Zöpfchen tragen. Anstelle von Deutschland-Vernichtern brauchen wir Deutschland-Retter. Anstelle von globalisierten bunten Vasallen brauchen wir Ritter des Grundgesetzes. Wir brauchen Kämpfer, die unsere Farben Schwarz-Rot-Gold ganz offen und voller Stolz tragen und tapfer unser Heimatland Deutschland zurückerobern. Gehen Sie daher zur Wahl, bringen Sie noch ein paar Kumpels mit und beobachten Sie ab 18 Uhr die Leute, die ihre Wählerstimmen auszählen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 966

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