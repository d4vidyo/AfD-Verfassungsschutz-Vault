---
type: zitat
speaker: "[[Alejandra Catalina Monzon]]"
date: 2025-02-08
topic: Menschenwürde
page_bfv: 907
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Alejandra Catalina Monzon]] vom 8.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Gerade weil ich als ehemalige Exil-Argentinierin und Tochter von politisch Verfolgten den Wert des Asylrechts sehr schätze, verurteile ich einen Missbrauch durch Asyl-Erschleicher und Flüchtlingssimulanten aufs Allerschärfste. Unsere Mütter und Großmütter haben für unser Recht auf sexuelle Selbstbestimmung ihre Röcke gegen Hosen getauscht und BHs verbrannt und diese Prädatoren kommen hierher, nehmen uns Frauen als ihre Beute, verhöhnen unsere friedvollen Männer als schwach, mobben unsere Kinder und stechen im Wahn wahllos jeden ab, der zufällig ihren Weg kreuzt. Darum bin ich für Remigration mit vollem Recht und Anspruch. Verbrecher gehören bestraft und Täterprofile klar benannt. Es sind keine Flüchtlinge und es sind auch keine politisch verfolgten Freiheitskämpfer. Das Erstaufnahmelager gehört geschlossen und ein Gewerbegebiet darauf erbaut.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 907

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