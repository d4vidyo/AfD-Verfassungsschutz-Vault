---
type: zitat
speaker: "[[Anna Leisten]]"
date: 2025-01-08
topic: Sonstiges
page_bfv: 863
source: 'YouTube; Interview mit COMPACTTV'
status: Unbewertet
---

# Zitat: [[Anna Leisten]] vom 8.1.2025 veröffentlicht auf: 'YouTube; Interview mit COMPACTTV'
> [!quote] Aussage
>Die AfD wollte eigentlich immer eine Jugendorganisation, die sie auch stückweise kontrollieren können. Und das war all die Jahre immer zu merken und auch zu spüren. Man hat uns versucht kleinzuhalten. [...] Es geht im Kern darum, dass hier versucht wird, die Stimmen stillzubekommen, die man sich eben von der Parteispitze nicht mehr wünscht. Und das steckt dahinter und das hat auch Frau Weidel deutlich gemacht. Sie hätte sich ja auch hinstellen können und sagen können, ich stehe voll und ganz zu unserer Jugendorganisation und ich möchte diese schützen vor einem drohenden Verbot. Das hat sie nicht getan [...]. Aber es war ganz eindeutig, was sie gesagt hat. Ihr geht es um die Kontrolle und Ihnen geht es darum, dass die Junge Alternative nicht mehr so besteht, wie wir sie kennen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 863

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