---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2022-09-29
topic: Menschenwürde
page_bfv: 330
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 29.9.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Heute vor fünf Jahren wurde \<xxx\> getötet, er wurde 30 Jahre alt. Er ist Tod, weil ein Syrer, dessen Alter nie festgestellt wurde mehrfach auf ihn eingeprügelt hat. [...] Solche Taten sind im Jahre 2022 alltäglich und sind, wenn überhaupt eine Meldung im Lokalteil wert. Die Täter, oft illegale und kulturfremde Flüchtlinge haben in Deutschland eines sehr schnell gelernt: Taten, für die sie in ihren Herkunftsländern viele Jahre oder lebenslang in die finstersten Gefängnislöcher eingesperrt würden, schützen sie sogar vor der Abschiebung. [...] Szenen von Straftätern, die lachend und feiernd mit Freunden und Familie den Gerichtsaal verlassen, während die Angehörigen der Opfer noch gebrochen im Saal sitzen, haben sich in unser Gedächtnis eingebrannt. Heute, am Todestag von \<xxx\> gedenken wir der oft namenlosen Opfer von Vergewaltigungen und tätlichen Angriffen. Ihnen wurde ihre Zukunft, ihre Leben, ihre Kindheit genommen. Justitia trägt in Deutschland keine Augenbinde mehr. Justitia schaut sich die Angeklagten vorher genau an. Kommt der Täter aus einem Land mit einer archaischen und Kultur, dann erhalten die Täter mit hoher Sicherheit einen Migrantenbonus. Heute am Todestag vom \<xxx\> dürfen wir nie vergessen: Mitverantwortlich für die Taten sind die Befürworter der tödlichen Politik der offenen Grenzen. Ohne ihre tödliche Toleranz würde Marcus noch leben! Ohne ihre tödliche Toleranz hätten alle Opfer eine Zukunft, ein Leben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 330. Der im Original erwähnte Name wurde durch den SPIEGEL mit \<xxx\> ersetzt.

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