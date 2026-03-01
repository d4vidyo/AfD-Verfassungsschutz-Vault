---
type: zitat
speaker: "[[Christina Baum]]"
date: 2024-04-22
topic: Menschenwürde
page_bfv: 456
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Christina Baum]] vom 22.4.2024 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Alles Lüge !! Es gibt sie nicht und wird sie nie geben - eine echte Integration von Muslimen in christliche Gesellschaften, mit wenigen Ausnahmen. Man musste wahrlich kein Prophet sein, um diese erschreckenden Zahlen vorherzusehen. Viele unserer muslimischen Mitbürger machten nämlich nie einen Hehl daraus, laut auszusprechen, was sie von uns Deutschen, unseren Gesetzen und Traditionen halten- nämlich nichts, gar nicht. Die meisten von ihnen verachten uns und betrachten uns Frauen als Freiwild. [...] Keine Gesellschaft kann ihre Traditionen und Regeln und damit ihre Sicherheit auf Dauer beibehalten, wenn solche Zuwanderer die Regel und nicht die Ausnahme sind.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 456

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