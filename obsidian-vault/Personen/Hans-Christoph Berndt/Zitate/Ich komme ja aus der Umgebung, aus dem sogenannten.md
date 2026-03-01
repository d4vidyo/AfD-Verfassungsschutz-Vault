---
type: zitat
speaker: "[[Hans-Christoph Berndt]]"
date: 2024-02-20
topic: Sonstiges
page_bfv: 767
source: 'Podiumsdiskussion'
status: Unbewertet
---

# Zitat: [[Hans-Christoph Berndt]] vom 20.2.2024 veröffentlicht auf: 'Podiumsdiskussion'
> [!quote] Aussage
>Ich komme ja aus der Umgebung, aus dem sogenannten Vorfeld. Und wir sollten uns auch in Erinnerung rufen, dass die AfD, wie wir sie jetzt haben, die AfD, die seit Sommer 22/23 ja diesen, doch diese wachsende Zustimmung erhalten hat, nicht die AfD wäre, ohne dass sie sozusagen, die Gedanken, den Impulse und auch wichtige Vertreter dieser ganzen Protestbewegungen der letzten zehn Jahre aufgenommen hätte. Nämlich der Protestbewegung gegen die Grenzöffnung seit 2015, die anhält, der Protestbewegung gegen die Corona-Zwangsmaßnahmen, der Protestbewegung gegen die Kriegs- und Embargopolitik und jetzt der Bürger- und Bauernprotest. All das haben wir aufgenommen. Da haben wir wichtige Leute, die zu uns gekommen sind und wir haben es inhaltlich aufgenommen und deswegen ist die AfD so stark. Und das ist ja ganz klar, was Björn sagte, jetzt ist es die Junge Alternative, aber wir wissen doch auch, dass die Corona-Proteste als Delegitimierung des Staates schon beim Verfassungsschutz registriert werden. Dass jetzt die Verächtlichmachung des Staates nach diesem 13-Punkte-Papier bereits ein Grund ist zur Beobachtung oder zum Verbot oder zur Verfolgung. Da ist keine Grenze in Sicht und deswegen kommt es für uns überhaupt nicht in Frage uns von irgendjemanden zu distanzieren. Kommt überhaupt nicht in Frage, wir haben gar keinen Grund. Die einzigen, von denen wir uns distanzieren, das sind die Ampelleute und die CDU, die unser Land ruiniert haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 767

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