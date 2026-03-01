---
type: zitat
speaker: "[[Kevin Michalzik]]"
date: 2022-11-25
topic: Menschenwürde
page_bfv: 198
source: 'X (ehemals Twitter)'
status: Unbewertet
---

# Zitat: [[Kevin Michalzik]] vom 25.11.2022 veröffentlicht auf: 'X (ehemals Twitter)'
> [!quote] Aussage
>Der Bevölkerungsaustausch ist keine rechtsextreme Verschwörungstheorie, er ist längst eine systematisch von den Altparteien, den MSM [Anm.: Mainstream-Medien] und staatsnahen NGOs vorangetriebene Realität! Die autochthonen Deutschen sollen zur Minderheit im eigenen Land gemacht werden!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 198

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