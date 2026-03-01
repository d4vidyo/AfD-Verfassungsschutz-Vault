---
type: zitat
speaker: "[[Marvin Weber]]"
date: 2022-07-19
topic: Menschenwürde
page_bfv: 341
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Marvin Weber]] vom 19.7.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Wie viele deutsche Frauen sollen noch vergewaltigt und ermordet, wie viele deutsche Männer noch gemessert werden, bis die #ichbinhier-Weltverbesserer merken, dass sie hierdurch ihre bunte Willkommenspolitik für die barbarischsten und kriminellsten Regionen der Erde, dem Brandherden aus Islamismus, Terrorismus, Gewaltkriminalität und Feindschaft zu Freiheit und Demokratie, in denen ein Menschenleben kaum etwas zählt sondern nur das Recht des Stärkeren, dass jeder einzelne, der hier illegal über 100 sichere Länder ins Sozialstaatsparadies mit ewigem historischen Nazikomplex und Bücklingssyndrom der falschen Toleranz eingewandert ist, so schnell wie möglich abgeschoben gehören? Wie viel tickende Zeitbomben wollen Sie in der Nachbarschaft denn erdulden? Dürfen wir Deutschen nicht mehr in Frieden, Sicherheit und Wohlstand leben? Sind wir das ewige schuldige Volk, das aus historischer Rachegelüste einiger Weniger nun jeden Tag aufs Neue bereichert und demnächst fremd im eigenen Land werden soll? [...] Selten habe ich solche verfassungsfeindliche Entscheidungen dieser gekauften Deutschenfeinde an der Spitze gesehen wie 2015, aber die bunte Resettlement-Regierung, setzt noch einen drauf und macht Deutschland zur weltweiten Beutekolonie Germanistan. Selten, habe ich in der Nachkriegszeit eine schändlichere, staats- und kulturzersetzendere Politik gegen das eigene Volk gesehen als heutzutage.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 341

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