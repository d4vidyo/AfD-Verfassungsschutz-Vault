---
type: zitat
speaker: "[[Björn Höcke]]"
date: 2025-01-18
topic: Menschenwürde
page_bfv: 915
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Björn Höcke]] vom 18.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Schluss mit der Ausplünderung unseres Sozialstaates. Schluss mit Gender-Gaga und Multi-Kulti-Dekadenz. Schluss mit identitätszerstörender Einwanderung. Schluss mit Kriegstreiberei. Aber ja zur Zukunft unseres Vaterlandes. [...] Die Migration ist die Mutter aller Krisen. Der Zerfall der inneren Sicherheit, der Zerfall unseres Sozialstaats bzw. die Plünderung unseres Sozialstaats, der Zerfall der schulischen Bildung in Deutschland, vor allen Dingen auch das Auflösen einer relativen Homogenität, ist bedingt durch eine unkontrollierte, millionenfache Zuwanderung aus kulturfremden Kontexten. Gerade der letzte Punkt ist so enorm wichtig, wenn man Demokratiefreund ist. Denn Demokratie braucht, um zu leben und zu funktionieren, einen Konsens. Sie braucht die Existenz einer Vertrauensgemeinschaft, die über Jahrhunderte gewachsen ist, die in einem konfliktträchtigen Prozess das miteinander ausgehandelt hat, was man gut findet und was man schlecht findet. Sie braucht ein Wertefundament, damit sie blühen kann. Nur wenn es ein gemeinsames Wertefundament gibt, können Kompromisse gefunden werden. Nur dann kann Demokratie überhaupt gelebt werden. Das bedeutet relative Homogenität. Und diese relative Homogenität ist in Deutschland, zumindest in den Ballungsgebieten, schon weitestgehend zerstört. Deswegen müssen wir jetzt unbedingt den Bremsklotz einlegen. Wir brauchen eine 180-Grad-Wende in der Migrationspolitik. Und dann kommen die Kartellparteienpolitiker und sagen, ja, das geht ja nicht. Wir leben in einer globalisierten Welt mit Reisefreiheit, mit Bewegungsfreiheit. Das sind doch alles Menschenrechte. Ja, sage ich dann. Das mag ja alles so sein. Aber das Heimatrecht, das Recht, nicht fremd im eigenen Land zu werden, ist auch Teil meiner Menschenwürde.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 915

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