---
type: zitat
speaker: "[[Guido Reil]]"
date: 2024-02-17
topic: Sonstiges
page_bfv: 833
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Guido Reil]] vom 17.2.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Aber was ich finde, was nicht geht: Dass sich ein Kreisvorstand hinstellt und sich von unserer Jugendorganisation distanziert und die auffordert, aus der Partei auszutreten. Also ich möchte mal daran erinnern, dass die Landesverbände Thüringen, Sachsen, Sachsen-Anhalt und wahrscheinlich auch bald Brandenburg auch als gesichert rechtsextrem eingestuft sind. Sollen wir uns von denen auch trennen? Das sind unsere stärksten Landesverbände. Das sind unsere Speerspitzen. Also wir dürfen uns nicht weiter vorführen lassen und wir dürfen uns vor allem nicht spalten lassen. Das haben – das haben in der Vergangenheit schon viele versucht. Auch viele Bundessprecher. Und alle sind damit gescheitert. Und alle Versuche, die AfD und die JA auseinanderzureden, werden scheitern. Wir brauchen unsere Jugendorganisation und wir stehen hinter der JA, liebe Freunde!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 833

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