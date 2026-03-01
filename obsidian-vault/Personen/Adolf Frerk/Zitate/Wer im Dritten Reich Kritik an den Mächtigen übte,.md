---
type: zitat
speaker: "[[Adolf Frerk]]"
date: 2022-06-16
topic: Menschenwürde
page_bfv: 302
source: 'www.afd-kleve.de'
status: Unbewertet
---

# Zitat: [[Adolf Frerk]] vom 16.6.2022 veröffentlicht auf: 'www.afd-kleve.de'
> [!quote] Aussage
>Wer im Dritten Reich Kritik an den Mächtigen übte, wirkte 'zersetzend' und wurde aus dem Verkehr gezogen. Manchmal erhielt der 'Zersetzer' gnadenhalber einen Jagdschein', d. h. er wurde für unzurechnungsfähig erklärt und blieb unbehelligt. Diese Praxis gibt es heutzutage nur noch für migrantische Messerstecher.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 302

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