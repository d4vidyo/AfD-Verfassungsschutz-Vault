---
type: zitat
speaker: "[[Thomas Dietz]]"
date: 2021-11-15
topic: Menschenwürde
page_bfv: 371
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Thomas Dietz]] vom 15.11.2021 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Humitätsgerede fehl am Platz [...] Frau Käßmann weiß, dass in der ersten Etappe Frauen und Kinder vorgeschickt werden. Mit ihnen produzieren Menschenhändlerbanden die Bilder, die man zur Grenzöffnung braucht, damit muslimische Migrantenarmeen in Deutschland einmarschieren können. Bilder des Mitleids produzieren diejenigen, die im Orient Massaker an Frauen, Kindern und Alten verüben Es sind Bilder, die diejenigen produzieren, die in den Herkunftsländern der illegalen Migranten grausame Massaker an Frauen, Kindern und Alten im Namen Allahs verüben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 371

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