---
type: zitat
speaker: "[[Emil Sänze]]"
date: 2024-09-19
topic: Menschenwürde
page_bfv: 290
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Emil Sänze]] vom 19.9.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>Der Deutsche wird aus dem öffentlichen Raum gestochen! - Emil Sänze Co- Landesvorsitzender Baden-Württemberg über den jüngsten Angriff in Althengstett [...],[...] Nirgends ist mehr Sicherheit, überall sind Messermänner. Das aufdringliche Diversitätsmarketing der Lebensmittelkrämer, Modisten oder BWegt-Mobilitäts-Dienstleister, ja staatlicher Stellen, sehe ich als gewissenlos, opportunistisch, bedrückend und verantwortungslos. Die Realität sehen wir doch. Das tägliche mediale Aufdrängen und brutale Vergewaltigen der Normalität erinnert mich fast schon an das 'Einheitlichkeitsmarketing‘ derjenigen Leute, die der Gesellschaft vor 90 Jahren, der Politik liebedienernd, in Geltungs-und Profitsucht einen vermeintlichen Norm-Typus aufgenötigt haben. [...] Anstatt friedlichen Andersdenkenden mit maskierten Polizisten und Geheimdienstschnüffelei Angst einjagen zu wollen, sollen sich Herrschaften Strobl, Faeser und Kollegen der erschütternden täglichen Gewaltorgie zuwenden. Sie sollen diesen Vorgang mit aller staatlichen Autorität beenden, der sich verblüffend schnell und buchstäblich zu einer Eroberung des öffentlichen Raumes durch migrantisch-stämmige junge Gewalttäter auswächst, unter aktivem Rückzug des einheimischen Elements, das von seinem Staat ganz einfach nicht mehr geschützt wird. Es wird zum verschüchterten Zuschauer und dann dem Faustrecht der Zuwanderer respektive -sprösslinge überlassen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 290

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