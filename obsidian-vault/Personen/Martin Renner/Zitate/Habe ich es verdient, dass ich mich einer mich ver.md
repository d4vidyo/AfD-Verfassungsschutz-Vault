---
type: zitat
speaker: "[[Martin Renner]]"
date: 2023-03-23
topic: Menschenwürde
page_bfv: 443
source: 'YouTube'
status: Unbewertet
---

# Zitat: [[Martin Renner]] vom 23.3.2023 veröffentlicht auf: 'YouTube'
> [!quote] Aussage
>Habe ich es verdient, dass ich mich einer mich verachtenden, mittelalterlichen Religion unterwerfen soll? [...] Ist das Multikulti wirklich bunt? Dieses Multikulti ist Burka-Schwarz, meine Damen und Herren. Die Freiheit des Individuums, das Grundprinzip des Christentums, kann niemals schiedlich-friedlich in einer Gesellschaft sich organisieren mit einem Islam-orientierten Menschenbild, die die totale Unterwerfung des Menschen unter den Willen Allahs fordert. Da gibt es keine Freiheit des Individuums. Da gibt es nur entweder du machst das, was sie im Koran steht oder in den Hadithen, oder du bist ein Apostat. Und dann musst du [Anm.: zeigt Kopf-Abtrenn-Geste]. Das kann nicht zusammen funktionieren. Das funktioniert momentan, weil wir, die hier immer schon leben, so bequem und so idiotisch tolerant geworden sind und gar nicht merken, wie hochgefährlich diese Entwicklung ist.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 443

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