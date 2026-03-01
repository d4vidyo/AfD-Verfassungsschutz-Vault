---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2024-09-22
topic: Sonstiges
page_bfv: 718
source: 'COMPACTTV'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 22.9.2024 veröffentlicht auf: 'COMPACTTV'
> [!quote] Aussage
>[Jeder] soll seine Meinung sagen dürfen. Das ist in unserer Verfassung, im Grundgesetz, verankert und darum bin ich so froh – bestellen Sie Jürgen Elsässer und seiner Frau viele liebe Grüße – [...], dass Sie wieder auf Sendung sind. So, das einfach mal vorab zu sagen: es ist exzellent.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 718

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