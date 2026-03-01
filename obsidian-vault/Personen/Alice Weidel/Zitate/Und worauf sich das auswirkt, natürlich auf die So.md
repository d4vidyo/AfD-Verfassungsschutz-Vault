---
type: zitat
speaker: "[[Alice Weidel]]"
date: 2022-12-04
topic: Menschenwürde
page_bfv: 259
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Alice Weidel]] vom 4.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Und worauf sich das auswirkt, natürlich auf die Sozialstatistiken, [...] auch auf die polizeiliche Kriminalstatistik, denn sind diese Leute einmal eingebürgert, dann tauchen sie als ausländische Staatsbürger gar nicht mehr auf. Obwohl genau diese Leute aus dem afghanischen, irakischen, syrischen Kontext eine hohe Kriminalitätsbelastung aufweisen. Ein Vielfaches von einem deutschen Staatsbürger im Übrigen. Dadurch wird auch die Kriminalstatistik verfälscht.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 259

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