---
type: zitat
speaker: "[[Roland Ulbrich]]"
date: 2022-12-09
topic: Menschenwürde
page_bfv: 336
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Roland Ulbrich]] vom 9.12.2022 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Die Welt von Frauen ist enger geworden - auf der Straße, beim Joggen, beim Ausgehen, in der U-Bahn. Jetzt kann man Kinder offenbar nicht mal mehr gefahrlos zur Schule gehen lassen. Weil sich sogenannte Asylanten, deren illegales Eindringen in unser Land von den Systemparteien bejubelt und befördert wird, immer öfter als Zeitbombe entpuppen. Tausende Menschen wurden seit 2015 von vermeintlich ‚Schutzsuchenden‘ vergewaltigt, erschlagen, erstochen, zerstückelt, vor einen Zug gestoßen. Jetzt ist die 14jährige \<xxx\> aus Illerkirchberg tot, ihre 13jährige Freundin liegt schwerverletzt im Krankenhaus. Der Tatverdächtige: ein 27jähriger Asylbewerber aus Eritrea, der den Mädchen auf dem Schulweg auflauerte und mit einem Messer auf sie einstach. Und die Polizei hat nichts Eiligeres zu tun, als vor einem ‚Generalverdacht‘ gegenüber Asylanten zu warnen., Warum warnt sie nicht vor illegaler Einwanderung von Männern mit einem mittelalterlichen Frauen- und Menschenbild?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 336. Der im Original erwähnte Name wurde durch den SPIEGEL mit \<xxx\> ersetzt.

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