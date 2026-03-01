---
type: zitat
speaker: "[[Hansjörg Schrade]]"
date: 2024-08-26
topic: Menschenwürde
page_bfv: 222
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Hansjörg Schrade]] vom 26.8.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Frau Esken (und die ganze SPD) [ist] [...] schon längst nicht mehr dem deutschen Volk, dessen Frieden, Sicherheit und Wohlstand verpflichtet, sondern [...] ihren perfiden Plan der Umvolkung, des großen Austauschs.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 222

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