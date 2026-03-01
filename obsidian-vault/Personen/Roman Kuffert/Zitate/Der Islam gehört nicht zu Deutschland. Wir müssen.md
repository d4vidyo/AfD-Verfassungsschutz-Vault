---
type: zitat
speaker: "[[Roman Kuffert]]"
date: 2021-09-03
topic: Menschenwürde
page_bfv: 465
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Roman Kuffert]] vom 3.9.2021 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Der Islam gehört nicht zu Deutschland. Wir müssen Deutschland vor der Islamierung schützen, Freunde. [...] Die aktuell in Deutschland lebenden Afghanen bereiten uns täglich, täglich massive Probleme mit Kriminalität, v.a. mit Gruppenvergewaltigungen, zwei an einem Tag, Messerstraftaten, Ehrenmorde usw. Das ist nur die Spitze. [...] Politiker mit Kopftuch, tausendfach auf Plakaten, gerade in den alten Bundesländern, welche oft den politischen Islam okay finden, ja. Na klar finden sie ihn okay. In den Großstädten Deutschlands haben schon heute deutlich mehr als 50% Kinder einen Migrationshintergrund, im Alter von bis zu 7 Jahren. Auf vielen Grundschulen dominiert Arabisch auf den Schulhöfen, das ist eine Tatsache. In den Großstädten und in den mittleren Städten geht’s auch schon los. Eine fremde Kultur breitet sich kontinuierlich an den Schulen und Institutionen aus. Die deutsche Mehrheitsgesellschaft wird Stück für Stück verändert und zurückgedrängt. Wenn die Deutschland-hassende Politik so weitermacht, dann sind wir Deutsche spätestens 2050 definitiv die Minderheit in Deutschland. Ist das kein Genozid an uns Deutsche?

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 465

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