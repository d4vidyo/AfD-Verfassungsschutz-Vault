---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-09-25
topic: Demokratieprinzip
page_bfv: 642
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 25.9.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Das Machtkartell befindet sich seit den Wahltriumphen der AfD in Thüringen, Sachsen und Brandenburg im Ausnahmezustand. Und Ausnahmezustände erlauben Ausnahmemaßnahmen. So jedenfalls die offizielle Rechtfertigung für bizarre AfD-Verhinderung-Koalitionen und parlamentarische Regelbrüche. Das läßt zwar immer mehr die demokratische Ordnung zerbröseln, aber wer den "Faschismus" in Land und Ländle verhindern will, darf nicht zimperlich mit Gesetz und Ordnung sein. Morgen bekommen die Bürger ein konkretes Beispiel im Erfurter Landtag geboten. [...] Es steht zu vermuten, daß ein womöglich angerufenes Verfassungsgericht dem unheilvollen Treiben kaum Einhalt gebieten wird. In der Corona-Zeit folgten die Urteile der Verfassungsgerichtsbarkeit der Macht und nicht dem Recht. Letztlich verdanken die Verfassungsrichter ihre Position den Parteibüchern, die sie selbst besitzen - ein Schlag ins Gesicht der vielbeschworenen Gewaltenteilung. Der bedeutende Staatsrechtler Carl Schmitt sah für Ausnahmezustände die Möglichkeit von Ausnahmemaßnahmen vor. Er band allerdings diese "Souveränität" an das Staats- und Gemeinwohlinteresse, nicht an Partikular- und Einzelinteressen. Was gegen die Thüringer AfD jetzt in Stellung gebracht wird, ist das Partikularinteresse einer Beutegemeinschaft samt dem Egointeresse zweier eitler Personen: einem Wahlverlierer, der aus Machtambitionen doch noch Ministerpräsident werden möchte, und einer Talkshow-Diva, die aus dem fernen Saarland die Thüringischen belange zu gestalten gedenkt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 642

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