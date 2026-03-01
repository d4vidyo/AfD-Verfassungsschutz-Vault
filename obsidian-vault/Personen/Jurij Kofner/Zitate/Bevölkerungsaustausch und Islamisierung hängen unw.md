---
type: zitat
speaker: "[[Jurij Kofner]]"
date: 2022-11-22
topic: Menschenwürde
page_bfv: 201
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jurij Kofner]] vom 22.11.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Bevölkerungsaustausch und Islamisierung hängen unweigerlich zusammen. [...] Insgesamt stellen Muslime aktuell knapp 6,6 Prozent der deutschen und 8,3 Prozent der österreichischen Bevölkerung. Der Anteil ist den letzten Jahren stark gewachsen, wozu nicht nur die anhaltende Einwanderung, sondern auch die durchschnittlich höhere Fertilitätsräte muslimischer Frauen beiträgt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 201

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