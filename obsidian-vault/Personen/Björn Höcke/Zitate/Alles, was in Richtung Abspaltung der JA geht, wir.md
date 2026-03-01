---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2024-02-20
topic: Sonstiges
page_bfv: 855
source: 'Podiumsdiskussion YouTube'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 20.2.2024 veröffentlicht auf: 'Podiumsdiskussion YouTube'
> [!quote] Aussage
>Alles, was in Richtung Abspaltung der JA geht, wird von mir den entschlossensten Widerstand erleben. Das kann ich an der Stelle sehr, sehr deutlich sagen. Jede Panikmache und das muss ich auch mal so deutlich hier und heute sagen, die es in einigen Gremien und Spitzengremien der Partei gibt, ist abzulehnen und muss der Rationalität weichen. Keinen Jota zurück vor den kruden, absurden realitätsfremden Interpretationen, ja vor den Irrsinnsinterpretationen der Bundesregierung, der Landesregierung, des Verfassungsschutzes bezüglich der Realität. Keinen Jota zurückweichen. Das muss unsere klare Verortung sein. Die JA ist die Jugendorganisation unserer Partei. Sie ist nicht integriert in die Partei. Das hat Vorteile, das hat Nachteile. Man kann und ich bin ein Freund davon, über die Totalintegration der JA sprechen. Das wäre dann das Juso-Modell, das heißt jeder junge Mensch ist dann bis zu seinem 35. Lebensjahr gleichzeitig nicht nur, wenn er Parteimitglied ist, Parteimitglied, sondern auch Mitglied der Jungen Alternative. Das bedeutet ein wenig weniger Bedeutung, weil man dann nur noch auf dem, auf der Ebene der Arbeitsgemeinschaften unterwegs ist, aber den Schutz der Mutterpartei. Eine Abgliederung, eine Abstoßung der JA, wie sie auch von einigen Protagonisten der Partei diskutiert wird, wäre der Beginn einer Salamitaktik, an dessen Ende ganz logischerweise der Verbots-, das Verbotsbegehren, der Verbotsantrag gegen die Mutterpartei stände. Und selbst wenn die AfD jetzt abgestoßen würde von der Mutterpartei und wenn die AfD, die JA dann relativ schnell verboten werden kann als Verein, das ist ja dann mit der Verordnung eines Innenministers möglich, bedeutet das ja nicht nur für die JA massive Nachteile, nämlich: Hausdurchsuchungen, Vermögenseinzug, etc. pp, sondern das wird immer die verbotene Jugendorganisation der Mutterpartei sein. Wir werden immer damit dann negativ kontextualisiert werden. Die JA werden wir niemals loswerden, das wird immer das Narrativ gespielt werden, das ist die ehemalige, jetzt verbotene Jugendorganisation der AfD. Zusätzlich kommen noch juristische Fragestellungen, die mit hineinspielen. Nach der, mit Verlaub, etwas kruden Logik der Unvereinbarkeitsliste der AfD, die ich immer wieder herzhaft kritisiert habe, müssten ja dann ehemalige JA-Funktionäre, und da sind einige prominente mittlerweile dabei, die Mitgliedsrechte entzogen werden. Das wäre die logische Konsequenz. Also die JA-Funktionäre oder die JA, würde auf die Unvereinbarkeitsliste gesetzt werden müssen nach der parteiinternen Logik und die ehemaligen Funktionäre der JA könnten nicht mehr Mitglied der, der der Mutterpartei sein. Also solche Auswirkungen muss man wirklich vor Augen haben und deswegen müssen wir der einsetzenden Salamitaktik Widerstand entgegenbringen und deswegen sage ich, auch weil ich vor dem Hintergrund, dass jetzt einige Landesparteitage in wichtigen Westländern stattfinden, von dem ein oder anderen Engagement, von der ein oder anderen Aktivität gehört habe, bitte ich auch, dass wir, dass wir uns uns solidarisch erklären, dass wir auch Landesparteitage nutzen mit einschlägigen Resolutionen. Ich weiß, dass in NRW sowas jetzt geplant ist, um zu zeigen: Wir stehen vor unserer Jugendorganisation. Wir lassen uns nicht spalten. Und ich wünsche solchen Aktivitäten, solchen Antragsaktivitäten jetzt in NRW oder vielleicht auch in Baden-Württemberg maximale Erfolge. Also: Ja zur JA und unbedingte Solidarität.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 855

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