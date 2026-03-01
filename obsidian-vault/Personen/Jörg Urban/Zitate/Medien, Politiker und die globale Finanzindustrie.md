---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-06-17
topic: Menschenwürde
page_bfv: 513
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 17.6.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Medien, Politiker und die globale Finanzindustrie haben inzwischen eine unheilige Allianz gebildet. Und ich sage euch noch etwas: Jede Form von Sozialismus braucht ihre Sklaven. Die roten Sozialisten benutzten die Menschen damals als Arbeitssklaven, um ihrer kommunistischen Träume umzusetzen und nebenbei als kleine Pseudo-Elite in Saus und Braus zu leben. [...] Liebe Freunde, der grüne Kommunismus klopft an der Tür, getragen von allen Altparteien, getragen von den meisten Mainstream-Medien, getragen und gelenkt von anglo-amerikanischen Globalisten und Milliardären.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 513

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