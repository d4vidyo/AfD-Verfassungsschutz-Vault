---
type: zitat
speaker: "[[Marc Jongen]]"
date: 2024-01-22
topic: Menschenwürde
page_bfv: 425
source: 'Facebook'
status: Unbewertet
---

# Zitat: [[Marc Jongen]] vom 22.1.2024 veröffentlicht auf: 'Facebook'
> [!quote] Aussage
>In der vergangenen Woche ist eine zwischen den Regierungsparteien und den staatsnahen Medien konzertierte Diffamierungskampagne über die AfD hereingebrochen, wie sie in der Geschichte der Bundesrepublik beispiellos ist. [...] Aus dem Begriff 'Remigration', der in einem der Gastvorträge am Rande eine Rolle spielte, wurde in lügenhafter Verzerrung der Tatsachen das Schauermärchen abgeleitet, die AfD wolle Menschen mit Migrationshintergrund massenhaft 'deportieren' und das Treffen habe dem Zweck gedient, einen entsprechenden 'Ge heimplan' auszuhecken. Dass sich die öffentlich-rechtlichen Medien und weite Teile der sogenannten Leitmedien für eine Kolportage dieser Räuberpistole hergegeben haben, welche die Stasi-Abteilung für Zersetzung nicht besser hätte erfinden können, ist ein Medienskandal ohnegleichen. [...] Vor diesem Hintergrund ist eine Klarstellung angebracht, was die AfD unter 'Remigration' versteht, wie es aus ihren Wahlprogrammen und den Aussagen ihrer führenden Vertreter bereits unmissverständlich hervorgeht: Die AfD macht keinen Unterschied zwischen deutschen Staatsangehörigen mit und ohne Migrationshintergrund. Alle Deutschen sind ohne Ansehen von Herkunft, Abstammung, Weltanschauung oder Religionszugehörigkeit Teil unseres Staatsvolkes. Remigration ist unsere politische Antwort, um das Asylchaos zu beenden und die Folgen der unkontrollierten Masseneinwanderung nachhaltig anzugehen. In diesem Sinne steht das Konzept der Remigration für ein umfassendes Maßnahmenpaket zur Wiederherstellung rechtskonformer Verhältnisse wie auch der Integrationsfähigkeit unserer Gesellschaft. [...] Deutsche Staatsbürger mit Migrationshintergrund wie auch Ausländer, die sich legal in Deutschland aufhalten und sich gesetzestreu verhalten, hier arbeiten, Steuern zahlen und sich in das gesellschaftliche Leben einbringen, sind uns willkommen und so wenig Teil eines Remigrationskonzepts wie Deutsche ohne Migrationshintergrund. Die gegenteilige Behauptung ist eine infame, durch nichts belegte Unterstellung der politischen Gegner, die damit von ihren eigenen Rechtsbrüchen im Rahmen der desaströsen Migrationspolitik abzulenken versuchen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 425. veröffentlicht vom AfD-Bundesverband

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