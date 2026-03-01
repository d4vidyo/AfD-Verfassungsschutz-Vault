---
type: zitat
speaker: "[[Elisabeth Mengel-Stähle]]"
date: 2024-09-26
topic: Sonstiges
page_bfv: 734
source: 'TV-Beitrag'
status: Unbewertet
---

# Zitat: [[Elisabeth Mengel-Stähle]] vom 26.9.2024 veröffentlicht auf: 'TV-Beitrag'
> [!quote] Aussage
>Es wird einfach mal direkt angepackt wo es unterm Nagel brennt. Ich warte schon regelrecht abends drauf, ich schalte ein, gucke und sage, ja genau, das wollte ich jetzt hören, das sehe ich ganz genauso und sitze dann auf der Couch und sage, jawoll, wo kann ich unterschreiben? Ich liebe die Zeitung, Sie treffen einfach den Nagel auf den Kopf! Sie gehen rein, da wo es anderen wehtut und holen raus, was wirklich gesprochen werden muss und das ist das, wo ich sage Mut zur Wahrheit ist nicht nur der Slogan von der AfD, sondern tatsächlich, COMPACT hilft uns diesen Mut zur Wahrheit in der Bevölkerung wirklich ankommen zu lassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 734

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