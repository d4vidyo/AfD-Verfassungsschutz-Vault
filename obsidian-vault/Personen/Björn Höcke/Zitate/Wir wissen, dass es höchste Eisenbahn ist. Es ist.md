---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2023-09-07
topic: Menschenwürde
page_bfv: 188
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 7.9.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir wissen, dass es höchste Eisenbahn ist. Es ist nicht fünf vor zwölf, es ist eine Minute nach zwölf. Meine Vorredner haben darauf hingewiesen. Wir stehen in Gefahr, als Deutsche dieses Land zu verlieren. Wir stehen in Gefahr, heimatlos zu werden. In Erfurt haben ein Drittel der Grundschulen mittlerweile über dreißig Prozent Migrantenkinder. In Hamburg haben alle Grundschulen zusammengenommen mittlerweile über fünfzig Prozent Migrantenkinder. Schaut in die Schulen, schaut vor allen Dingen in die Kreißsäle oder in die Geburtsstationen Westdeutschlands, dann wisst ihr, wie die Zukunft dieses Landes nach dem Willen der Kartellparteien, nach dem Willen der Bunten aussehen soll. Das ist eine Zukunft, die eben eine andere Zukunft ist, aber keine deutsche Zukunft mehr. Es ist so, Demografie entscheidet über Demokratie. [...] Wenn wir die demografische Wende nicht schaffen und wenn wir die Einwanderung nicht stoppen, dann sind wir in wenigen Jahren Minderheit im eigenen Land. Dann, liebe Freunde, dann ist die deutsche Demokratie am Ende, weil dann logischerweise für die Minderheitsgesellschaft die deutsche Volkssouveränität am Ende ist. Und die müssen wir erhalten. Um die müssen wir jetzt kämpfen. Es geht um nichts weniger als unser Recht auf Heimat in der Mitte Europas. [...] Die Ampel-Regierung will das Staatsangehörigkeitsrecht reformieren. [...] Die Ampelkoalition, die Kartellparteien, sie schaffen sich gerade ein neues Volk

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 188

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