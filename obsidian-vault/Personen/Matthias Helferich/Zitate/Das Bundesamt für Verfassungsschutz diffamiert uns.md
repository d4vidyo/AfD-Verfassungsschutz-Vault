---
type: zitat
speaker: "[[Matthias Helferich]]"
date: 2025-02-08
topic: Menschenwürde
page_bfv: 879
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Matthias Helferich]] vom 8.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Das Bundesamt für Verfassungsschutz diffamiert uns ja als rechtsextremistischen Verdachtsfall. Und wisst ihr, was man uns vorwirft? Dass wir den Erhalt des deutschen Staatsvolkes und Deutschlands als Land der Deutschen betreiben. Ja, wenn der Vorwurf ist, dass wir wollen, dass es auch in hundert Jahren noch ein deutsches Volk gibt, dann sind wir schuldig im Sinne der Anklage. Und das treibt uns heute auf die Straße. Wir wollen, dass unser Deutschland auch in hundert Jahren noch besteht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 879

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