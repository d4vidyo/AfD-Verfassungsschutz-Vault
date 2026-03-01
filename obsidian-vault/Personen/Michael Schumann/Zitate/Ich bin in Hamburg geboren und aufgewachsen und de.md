---
type: zitat
speaker: "[[Michael Schumann]]"
date: 2023-08-05
topic: Menschenwürde
page_bfv: 424
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Michael Schumann]] vom 5.8.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Ich bin in Hamburg geboren und aufgewachsen und deshalb können Sie mir ruhig vertrauen wenn ich von deutschen Minderheiten spreche. Wir haben Stadtteile, in denen der Migrationsanteil an Schulen bei über 90% liegt. Kein Wochenende vergeht oder Schießerei, Messerstecherei oder Vergewaltigung. Und ich brauche Ihnen gar nicht zu erklären, welche Bevölkerungsgruppen hier überproportional vertreten sind, das wissen Sie genauso gut wie ich. Das ist Folge einer fatalen, desaströsen Einwanderungspolitik, deswegen sage ich, solange es noch möglich ist, und ich betone: noch möglich ist, müssen wir diese Masseneinwanderung stoppen und die Remigration starten. Und ich muss zugeben, ich finde es etwas erstaunlich, dass manche Vertreter der deutschen Wirtschaft noch nicht ganz verstanden haben, in welche Richtung der Wind weht. Denn Unternehmen wie etwa Airbus sollten nicht beim CDU-Parteitag mit sponsern, sondern sie sollten hier sein und uns ihre Pläne für die dringend notwendige Remigrations-Flotte vorstellen!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 424. Bewerbungsrede auf der Europawahlversammlung der AfD

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