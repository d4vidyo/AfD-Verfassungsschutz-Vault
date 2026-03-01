---
type: zitat
speaker: "[[René Springer]]"
date: 2024-09-23
topic: Menschenwürde
page_bfv: 408
source: 'Pressekonferenz'
status: Unbewertet
---

# Zitat: [[René Springer]] vom 23.9.2024 veröffentlicht auf: 'Pressekonferenz'
> [!quote] Aussage
>Also, dieser Abschiebesong, der gestern gespielt wurde, war Teil der Kampagne der JA Brandenburg, und das ist ja nicht unüblich in Parteien, dass die Jugend Grenzen austestet und dazu gehört das sicherlich auch. Was ich aber nie verstehen werde, ist, wie man sich über einen Song aufregen kann, während man die Forderung der Jusos, die vor einiger Zeit erhoben wurde, bis zum neunten Monat abzutreiben, einfach so dahin plätschert. Also, da verstehe ich auch die Prioritätensetzung der Journalisten nicht. Dagegen ist so ein Song harmlos und die JA hat eine großartige Arbeit im Wahlkampf geleistet und dann sei es ihr vergönnt, dass am Wahlkampfabend eben mal der Song gespielt wird.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 408

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