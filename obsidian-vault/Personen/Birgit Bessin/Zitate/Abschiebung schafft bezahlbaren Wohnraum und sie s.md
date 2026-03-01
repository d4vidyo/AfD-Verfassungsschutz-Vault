---
type: zitat
speaker: "[[Birgit Bessin]]"
date: 2023-09-05
topic: Menschenwürde
page_bfv: 397
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Birgit Bessin]] vom 5.9.2023 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Abschiebung schafft bezahlbaren Wohnraum und sie schafft vor allem wieder rechtsstaatliche Zustände in Deutschland! Und sie schafft vor allem auch Sicherheit, denn die Fachkräfte des Todes haben in Deutschland einfach nichts zu suchen und das muss man so deutlich auch aussprechen. [...] Deswegen, liebe Freunde wird es Zeit für einen AfD-Innenminister, es wird Zeit für ein Abschiebeministerium in Brandenburg und guten Flug nach Hause! [...] Migrantenrevolte arabischer Zuwanderer aus dem Maghreb, unintegriert, die unsere westlichen Werte ablehnen, die auch unseren Staat und unseren Rechtsstaat ablehnen. Das, was gerade in Frankreich passiert ist, ist nur eine Frage der Zeit, wann und wo damit in Deutschland zu rechnen ist, wo wir und wann wir das in Deutschland erleben werden, wenn dieser Politik nicht endlich schnell Einhalt geboten wird. Denn die Explosion zugewanderter Kriminalität, die haben wir auf jeden Fall an Silvester erlebt in Berlin. [...] Ich danke euch, dass ihr hier seid, dass ihr uns gemeinsam als letztes Bollwerk für Deutschland gegen diese Migration, gegen diese Massenmigration unterstützt.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 397

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