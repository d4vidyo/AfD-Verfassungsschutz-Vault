---
type: zitat
speaker: "[[Eugen Schmidt]]"
date: 2022-08-04
topic: Menschenwürde
page_bfv: 272
source: 'Telegram'
status: Unbewertet
---

# Zitat: [[Eugen Schmidt]] vom 4.8.2022 veröffentlicht auf: 'Telegram'
> [!quote] Aussage
>Die Deutschen werden zur Minderheit im eigenen Land. In den Grundschulen unseres Landes zeichnet sich ein erschreckendes Bild: In 994 der insgesamt 2787 Grundschulen in NRW sind Kinder mit Migrationshintergrund in der Mehrheit! [...] Diese Entwicklung ist die Folge einer völlig fehlgeleiteten Migrations- und Demographiepolitik, schulen, die eigentlich zur Förderung von Bildung da sind, werden immer mehr zu Orten, an denen kulturelle Konflikte ausgetragen werden und Gewalt den Alltag prägt. Sie werden zu Keimzellen von Kriminalität und Islamismus. [...] Was es nun braucht ist eine entschiedene Kehrtwende in der Migrationspolitik. Illegal eingereiste Sozialmigranten müssen abgeschoben oder an der Einreise nach Deutschland gehindert werden. Zudem muss sich die Bundesregierung für eine familienfreundliche Politik einsetzen, um die Geburtenraten wieder auf ein erforderliches Niveau zu heben. Erst dann kann das Gleichgewicht wiederhergestellt und die nationale Identität auf Dauer bewahrt werden.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 272

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