---
type: zitat
speaker: "[[Martin Reichardt]]"
date: 2023-04-01
topic: Menschenwürde
page_bfv: 267
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Martin Reichardt]] vom 1.4.2023 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Einer handlungsunfähigen und migrationsgeilen Regierung haben wir es zu verdanken, dass mittlerweile sogar die Spielplätze unserer Kinder nicht mehr die sorglosen und friedvollen Orte sind, die sie eigentlich sein sollten. Migrantengewalt scheint genauso grenzenlos wie die Verantwortungslosigkeit derer, die die Grenzen Deutschlands nicht schützen wollen. Unsere Bürger und vor allem unsere Kinder werden schutzlos denen ausgesetzt, die unseren Rechtsstaat nicht respektieren und Integration verweigern. Sichere Grenzen bedeuten Rechtsstaatlichkeit, Ausgewogenheit und Sicherheit für unsere Bürger und unsere Kinder!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 267

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