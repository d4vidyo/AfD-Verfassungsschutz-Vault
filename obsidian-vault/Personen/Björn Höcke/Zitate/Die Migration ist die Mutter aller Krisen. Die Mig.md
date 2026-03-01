---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Menschenwürde
page_bfv: 382
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Die Migration ist die Mutter aller Krisen. Die Migration bedeutet Zerfall der inneren Sicherheit, bedeutet Gruppenvergewaltigung und bedeutet Messermorde. Die Migration bedeutet die Plünderung der Sozialversicherungssysteme. 50 Prozent der Bürgergeldempfänger sind mittlerweile Ausländer. Migration bedeutet den Kollaps unserer Bildungssysteme. Auch das hat was mit Migration zu tun. Bedeutet Überlastung des Wohnungsmarktes. Wir hätten keine Wohnungsnot, wenn die Kartellparteien nicht Millionen in den letzten zehn Jahren illegal über die Grenze gelassen hätten.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 382

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