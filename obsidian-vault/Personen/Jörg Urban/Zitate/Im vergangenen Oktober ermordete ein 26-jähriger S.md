---
type: zitat
speaker: "[[Jörg Urban]]"
date: 2023-09-21
topic: Menschenwürde
page_bfv: 332
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Jörg Urban]] vom 21.9.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Im vergangenen Oktober ermordete ein 26-jähriger Somalier im rheinland-pfälzischen Ludwigshafen zwei deutsche Männer im Alter von 20 und 35 Jahren. Der Stadtrat beschloss nun, dass eine Gedenkstelle für die beiden Opfer von importierter Gewalt errichte werden soll. Ich begrüße diese Entscheidung: Ein offener Umgang mit den politisch vermeidbaren Gewalttaten, die mittlerweile in ganz Deutschland zu beklagen sind, ist wichtig. Doch an viel zu vielen Orten können sich Bürger und Angehörige der Opfer nicht gegen die Altparteien-Vertreter durchsetzen, die die Konsequenzen ihrer Migrationspolitik verschleiern wollen. Mit der AfD ist klar: Die Opfer des Gesellschaftsexperiments der offenen Grenzen dürfen nicht vergessen werden. Es muss ein würdiges Andenken an sie geschaffen werden. Genauso wichtig ist es aber, aus den vielen tragischen Fällen die richtigen politischen Schlüsse zu ziehen: Remigration, Festung Europa und sichere Grenzen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 332

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