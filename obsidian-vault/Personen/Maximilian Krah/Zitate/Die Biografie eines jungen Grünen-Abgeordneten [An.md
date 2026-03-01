---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2022-05-15
topic: Menschenwürde
page_bfv: 492
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom 15.5.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Biografie eines jungen Grünen-Abgeordneten [Anm.: es sind die Abgeordneten des Europäischen Parlamentes gemeint] sieht so aus: Er kommt bereits aus einer Familie der oberen Mittelschicht, die bevorzugt beim Staat angestellt sind. Er studiert anschließend irgendwie was mit Politik. Ist dann schon Mitarbeiter bei einem Abgeordneten, dann geht er zu einer NGO, die ihn noch ins Ausland schickt und nochmal gut ausbildet. Diese NGO kommt in der Regel aus dem Umfeld von Soros. Und wenn er dort gut performt, kriegt er dann einen Listenplatz und zieht nach Brüssel. Das heißt diese Leute haben null Bindung an ihre Heimat und schon gar nicht an ihren Nationalstaat. Sondern sie verstehen sich als Teil einer globalen Elite und ihr Auftrag ist nicht dem deutschen Volk zu dienen, seinen Nutzen zu mehren, Schaden von ihm zu wenden, sondern ihr Auftrag ist es, so 'ne Art die Welt zu managen, wie die Filiale einer Weltregierung. Also sie fühlen sich nicht verantwortlich dem Wähler unten, sondern sie fühlen sich quasi so 'ner gewissen Weltregierung verantwortlich, die so verkörpert wird durch dieses NGO-Netzwerk, ‚Open Society' und wie es so weiter heißt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 492

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