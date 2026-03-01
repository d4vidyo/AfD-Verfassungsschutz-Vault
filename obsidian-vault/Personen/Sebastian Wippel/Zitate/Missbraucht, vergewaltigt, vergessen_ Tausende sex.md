---
type: zitat
speaker: "[[Sebastian Wippel]]"
date: 2024-01-15
topic: Menschenwürde
page_bfv: 347
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Sebastian Wippel]] vom 15.1.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Missbraucht, vergewaltigt, vergessen: Tausende sexuelle Übergriffe durch Migranten seit dem Jahre 2015! Wieder einmal schlägt die grauenhafte Gruppenvergewaltigung einer deutschen Frau hohe Wellen: Trotz der Versprechen des Berliner Senates, den Görlitzer Park sicherer werden zu lassen, vergingen sich hier erneut mehrere nichtdeutsche Männer an einer jungen Frau. Diesmal zur Silvesternacht. Bereits im Juni kam es hier zuletzt zu einer Gruppenvergewaltigung, die von Behördenseite - wohl aufgrund des politischen Drucks - über Wochen hinweg verschwiegen wurde, Eine Frau, ein trauriges Schicksal - und damit eine von vielen, die seit dem Jahre 2015 Opfer sexueller Gewalt durch Männer aus dem arabischen und afrikanischen Raum geworden ist. [...]Auch hier in Sachsen werden sexuelle Übergriffe beispielsweise in Schwimmhallen und Freibädern überwiegend von Ausländern begangen. [...] Und bei all diesen Zahlen gilt wie immer: Deutsche Staatsbürger mit Migrationshintergrund werden nicht extra kriminalstatistisch erfasst und kommen somit hierbei noch oben drauf, was das Bild der Überrepräsentation bei Sexualdelikten weiter nach oben schießen ließe. [...] Die Gründe für solche Zahlen sind vielfältig: Patriarchalische, frauenfeindliche Strukturen aus den Heimatländern, der Stellenwert von (auch sexueller) Gewalt, der in diesen Gesellschaften viel stärker ausgeprägt ist als in Deutschland, aber auch die ausbleibende Kontrolle darüber, wer durch unser deutsches Sozialsystem motiviert unsere Grenzen passiert. Die Jahre haben gezeigt: Massenmigration lockt in der Menge nicht hochgebildete, gut ausgebildete und gut situierte Individuen an, sondern überwiegend Glücksritter ohne Befähigung und Eignung, dieses Land voranzubringen. Dass sich hierunter dann auch Kriminelle mischen, überrascht nicht, macht die Einzelschicksale vieler tausender deutscher Frauen dadurch aber nicht weniger tragisch.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 347

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