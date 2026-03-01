---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2022-12-15
topic: Menschenwürde
page_bfv: 362
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 2022-12-15 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Bestandserhaltungs-Migration = Volksaustausch? Dresden 2022. Heute kamen die ersten Sozialsystem-Migranten - alles junge Männer aus den bekannten und vorrangig islamischen Asylherkunftsländern - in der neuen ‚Asylunterkunft‘ [...] an. [...] Wir brauchen einen sofortigen Aufnahmestopp für unsere Landeshauptstadt und die klare Ansage an die Landesregierung, sofort mit massiven Abschiebungen zu beginnen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 362

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