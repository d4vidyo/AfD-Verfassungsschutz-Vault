---
type: zitat
speaker: "[[Heiko Scholz]]"
date: 2025-01-22
topic: Menschenwürde
page_bfv: 927
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Heiko Scholz]] vom 22.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Ich kann, ich will (!) es nicht mehr lesen! Deshalb #Remigration! Konsequente Remigration! ,Unser Gesindel haben wir im Land, wir brauchen keines aus dem Ausland zusätzlich importieren.' Otto Landsberg (1869-1957), deutsch-jüdischer Sozialdemokrat (#SPD) und Justizminister in der Weimarer Republik im Kabinett Scheidemann – #Aschaffenburg

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 927

**Verfassungsschutz Kategorisierung:** Verstoß gegen die Menschenwürde.

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