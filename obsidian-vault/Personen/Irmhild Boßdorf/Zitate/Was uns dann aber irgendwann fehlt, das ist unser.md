---
type: zitat
speaker: "[[Irmhild Boßdorf]]"
date: 2023-07-30
topic: Rechtsstaatsprinzip
page_bfv: 656
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Irmhild Boßdorf]] vom 30.7.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Was uns dann aber irgendwann fehlt, das ist unser Volk. Und dieses wird von Berlin und Brüssel der Auflösung preisgegeben. Es ist egal, wie die Frage lautet: Massenzuwanderung ist immer das Problem und niemals eine Lösung. Die Lösung lautet Remigration. Millionenfache Remigration. Deutschland leidet an einem noch nie dagewesenen Geburtenrückgang, und das mag die Endzeitapologeten der Grünen erfreuen. Schließlich bezeichnen sie Kinder als Klimaschädling Nummer eins. Man muss sich vorstellen, wie infam das ist, auszurechnen, wie viel CO₂ durch Kinder produziert wird. Aber was wir wirklich fürchten müssen, das ist nicht der menschengemachte Klimawandel. Nein, wir sollten uns viel eher fürchten vor dem menschengemachten Bevölkerungswandel, der das... der Bevölkerungswandel, der das alte Europa in eine Siedlungsregion für Millionen Afrikaner und Araber umwandeln soll. Das jüngst von den EU-Innenministern beschlossene ,gemeinsame europäische Asylsystem ist reine Makulatur, denn im Außengrenzverfahren werden überhaupt nur 20% aller Asylforderer betroffen... Äh, das betrifft nur 20% der Asylforderer. Aber die Somalier, die Iraker und die Afghanen, die kommen weiter ungehindert nach Europa. Was wir brauchen, das sind Pushbacks, egal was der Europäische Gerichtshof dazu sagt. Was wir brauchen, sind Grenzanlagen, egal wie laut linke NGOs schreien. Was wir auch brauchen, ist eine europäische Grenzschutzagentur, die die Festung Europa endlich verteidigt!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 656

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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