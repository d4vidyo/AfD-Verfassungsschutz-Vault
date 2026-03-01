---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2023-09-01
topic: Sonstiges
page_bfv: 789
source: 'TikTok'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 1.9.2023 veröffentlicht auf: 'TikTok'
> [!quote] Aussage
>Wir stehen auf jeden Fall zu euch, wenn ihr jetzt Unterstützung braucht, wir sind für euch da. Wir sammeln auf jeden Fall Spenden. Und ich rufe jetzt hiermit alle Abgeordneten der Partei, alle Abgeordneten im Landtag, im Bundestag und sonst wo auf, unterstützt die jungen Leute. [...] Und ansonsten nochmal der Aufruf: spendet, was das Zeug hält, und jeder Cent kommt an. Meine Spende ist auch grad rausgegangen, wir haben zwar alle nicht so viel, aber wir unter stützen uns trotzdem, wo wir nur können.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 789

**Verfassungsschutz Kategorisierung:** Sonstiges.

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