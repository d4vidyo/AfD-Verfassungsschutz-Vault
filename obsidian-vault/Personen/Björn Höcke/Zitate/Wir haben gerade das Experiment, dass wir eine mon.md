---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-08-13
topic: Menschenwürde
page_bfv: 229
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 13.8.2024 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Wir haben gerade das Experiment, dass wir eine monoethnische, monokulturelle Gesellschaft, also das deutsche Volk, in eine multiethnische, multikulturelle Gesellschaft transformieren. Aha. Wir sind also Teilnehmer eines Experimentes, an dessen Ende das Ende des deutschen Volkes steht. An dessen Ende das steht, was Thilo Sarrazin in seinem epochalen Werk 2010 schon mal formuliert hat. Deutschland schafft sich ab. Und ich frage, sind wir Thüringer, sind wir Deutschen jemals gefragt worden, ob wir uns abschaffen lassen wollen? Sind wir jemals gefragt worden? Und ich sage euch, wie dieses Experiment ausgeht, Freunde. Es ist ganz klar, wie dieses Experiment ausgeht. Jetzt ist es schon zu erkennen, schaut bitte nach England, was dort passiert. Schaut nach Frankreich in den letzten Jahren, immer wieder aufstehende Banlieues von nicht integrierten Migrantengruppen. Diese Zustände werden wir auch haben. Und es wird so sein, wenn wir jetzt nicht gegensteuern, dass unsere fragmentierte Gesellschaft, und im Westen ist sie schon stark fragmentiert, da sind wir in einigen Städten schon in der Minderheit, Freunde. Dass diese stark fragmentierte Gesellschaft auseinanderstrebt, die Fliehkräfte werden immer größer werden, weil das gemeinsame Wertefundament, das wir in Jahrhunderten uns erarbeitet haben, beziehungsweise unsere Vorfahren sich erarbeitet haben, auf dem unser Staat steht, erodiert. Und was macht dann die Regierung in ihrer Not? Sie wird zu autoritären Maßnahmen greifen, um diese auseinanderdriftende fragmentierte Gesellschaft irgendwie zu disziplinieren. Und wenn das auch nicht mehr hilft, dann wird im letzten Schritt das Ganze in einem Bürgerkrieg auseinanderfallen. Das ist der Weg, den die Kartellparteien offenkundig für uns vorgesehen haben. Anders kann ich das nicht einordnen. Denn wer eins und eins zusammenzählen kann; der weiß, dass es gar nicht anders sein wird, und es gar nicht anders sein kann, gerade wenn wir weiter deindustrialisieren, unser Wohlstand schwindet und wir gar nichts mehr zum Verteilen haben. Dann werden auf einmal alle wach und dann fahren sie die Ellenbogen aus. Und dann werden wir die Konflikte genau an den ethnischen Trennlinien haben. So schlimm das ist, weil ich den Menschen nicht nach Ethnien bewerte. Aber als kluger Politiker muss ich einfach einsehen, dass es ein Maß an Migration gibt, dass das Maß an Integrationsfähigkeit der aufnehmenden Bevölkerung überschreitet. Davor hat schon Helmut Schmidt gewarnt. Und an dem Punkt stehen wir gerade. Deswegen ist die Wahl am 1. September nicht nur eine Wahl für Thüringen. Es ist nicht nur eine Landtagswahl. Wir haben dieses Motto nicht umsonst gewählt, Freunde. Der Osten macht's. Weil ihr wacher seid, weil ihr demokratieverliebter seid, weil ihr freiheitsliebender seid. Wir müssen aus dem Osten das Zeichen setzen. Wir müssen aus dem Osten den Impuls groß machen. Hier muss die politische Sonne aufgehen, damit sie auch im Westen sichtbar bleibt. Freunde, wir müssen das Ruder rumreißen für ganz Deutschland.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 229

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