---
type: zitat
speaker: "[[Miguel Klauß]]"
date: 2023-02-12
topic: Menschenwürde
page_bfv: 221
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Miguel Klauß]] vom 12.2.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Sie zerstören mit Absicht unser Land. Selbstverständlich wird niemand nach Ablauf des Visums von 3 Monaten zurück gehen. Genauso wie Ausreisepflichtige, illegale und abgelehnte Asylbewerber nie das Land verlassen. Was von den Altparteien von Anfang an geplant war. Die umvolkung findet statt auf kosten unseres Landes. Es wird noch viel schlimmer. Nur die #AfD kann diese wahnsinnigen Politiker stoppen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 221

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