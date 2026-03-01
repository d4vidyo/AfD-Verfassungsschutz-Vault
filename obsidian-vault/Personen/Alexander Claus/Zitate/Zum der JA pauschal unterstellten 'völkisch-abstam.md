---
type: zitat
speaker: "[[Alexander Claus]]"
date: 2024-02-07
topic: Menschenwürde
page_bfv: 158
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Alexander Claus]] vom 7.2.2024 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Zum der JA pauschal unterstellten 'völkisch-abstammungsmäßigen #Volksbegriff': Ich finde sehr wohl, dass Menschen fremder Abstammung im deutschen Volk aufgehen können (Assimilation/Akkulturation). Ich toleriere aber auch restriktivere Auffassungen. Das nennt man Meinungsfreiheit!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 158

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