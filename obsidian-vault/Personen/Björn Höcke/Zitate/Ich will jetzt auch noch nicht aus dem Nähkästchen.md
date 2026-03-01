---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-31
topic: Demokratieprinzip
page_bfv: 646
source: 'YouTube Interview'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 31.8.2024 veröffentlicht auf: 'YouTube Interview'
> [!quote] Aussage
>Ich will jetzt auch noch nicht aus dem Nähkästchen plaudern, wir haben ja schon alles durchdekliniert und alles durchdacht, aber man muss in der Politik auch vielleicht das ein oder andere taktische Geheimnis wahren, ob wir zu einer schnellen MP-Wahl schreiten oder ob wir den Prozess eher mal begleiten, der relativ lange andauern wird, wenn man uns außen vor lässt. Nochmal, wir sind auf alles vorbereitet und wir werden genauso wie am 5. Februar 2020 eine sehr gute Rolle spielen, eine sehr dominante Rolle spielen. Alle Wähler, die uns wählen, können sicher sein, dass unsere Stimme unüberhörbar sein wird und dass wir auch in den nächsten Wochen und Monaten für Gesprächsstoff bundesweit sorgen werden, im positiven Sinne.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 646

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Demokratieprinzip.

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