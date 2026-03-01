---
type: zitat
speaker: "[[Joachim Paul]]"
date: 2024-02-14
topic: Sonstiges
page_bfv: 836
source: 'Instagram'
status: Unbewertet
---

# Zitat: [[Joachim Paul]] vom 14.2.2024 veröffentlicht auf: 'Instagram'
> [!quote] Aussage
>Ja, liebe JA! Wie man so hört, hat der Verfassungsschutz euch zu Extremisten erklärt. Mitglieder der JA sind auf allen Ebenen mittlerweile in der parlamentarischen oder in der kommunalpolitischen Arbeit eingebunden. Sie stellen jeden Tag, jede Woche, jeden Monat Anträge und Anfragen, um das Leben der Bürger in ihrem Alltag zu verbessern. Warum sollten Extremisten sich diese Mühe und diese Arbeit machen? Auf diese Frage gibt es offenkundig keine Antwort. Wenn man hier, am Deutschen Eck, in Richtung Rhein schaut, an die Quelle des Rheins, dort gibt es eine Demokratie, die viel älter ist als die Bundesrepublik: die Schweiz. Und in der Schweiz gibt es auch Institutionen, und sie sagen ganz klar: Ins Visier kann nur der geraten, der seine politischen Ziele mit Gewalt durchsetzen will. Alles andere sei nicht extremistisch, alles andere ginge diese Behörden nichts an. Nicht nur in Sachen "direkte Demokratie" kann die Schweiz ein Vorbild sein, sondern auch in dieser Angelegenheit. Und deswegen heißt es für uns und für viele Funktionäre: Wir stehen hinter der JA! Das ist so und das wird auch so bleiben!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 836

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