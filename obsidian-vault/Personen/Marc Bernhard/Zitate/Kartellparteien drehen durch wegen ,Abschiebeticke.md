---
type: zitat
speaker: "[[Marc Bernhard]]"
date: 2025-01-13
topic: Menschenwürde
page_bfv: 932
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marc Bernhard]] vom 13.1.2025 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Kartellparteien drehen durch wegen ,Abschiebeticket‘ Weil unser Kreisverband in Karlsruhe über einen Wahlwerbeflyer die Durchsetzung geltenden Rechts fordert, nämlich die umgehende Abschiebung von Illegalen, scheinen einige Vertreter der Altparteien völlig die Contenance zu verlieren. In diesem Zusammenhang wird wie üblich mit billigen Tricks agiert, indem bestimmte Inhalte weggelassen bzw. aus dem Zusammenhang gerissen werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 932

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