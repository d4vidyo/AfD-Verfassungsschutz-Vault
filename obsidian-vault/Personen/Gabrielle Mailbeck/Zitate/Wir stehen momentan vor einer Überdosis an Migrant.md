---
type: zitat
speaker: "[[Gabrielle Mailbeck]]"
date: 2024-08-19
topic: Menschenwürde
page_bfv: 312
source: 'Vortrag'
status: Unbewertet
---

# Zitat: [[Gabrielle Mailbeck]] vom 19.8.2024 veröffentlicht auf: 'Vortrag'
> [!quote] Aussage
>Wir stehen momentan vor einer Überdosis an Migranten und Migration in diesem Land. Und wir alle wissen, dass eine Überdosis zum Tod führen kann. Wie viele Tote haben wir bereits zu beklagen? Wie viele Messerattacken haben wir erlebt? Wie viele Opfer haben sie nicht überlebt? Wir haben viel mehr Messermänner in unserem Land, als wir denken. Und traurigerweise sind sie überall da, wo wir sind, wo wir mit unseren Kindern sind. [...] Und wir haben eher, ich glaube, das Gefühl, dass wir etwas verlieren und wir letztendlich, das deutsche Volk uns eigentlich fremd im eigenen Land fühlen, oder? Weil ganz ehrlich, der Hans und der Dieter, wenn sie streiten, sie werden sich nicht gegenseitig abstechen. Das machen wir nicht. Sie werden vielleicht zu einem Biergarten gehen und das Ganze, ja, das Ganze dort diskutieren, ein Bierchen trinken. Das machen wir nicht. So etwas machen wir nicht, weil wir Anstand haben. [...] Und wir, liebe Freunde, wir sind diejenigen, die die Rechte, Gesetze und Pflichten hier in unserem Land bestimmen. Wir sind diejenigen, die darüber entscheiden, was passiert. Und hier sind wir. Wir sind die einzigen, die die Remigration vollziehen. [...] Eine neue veröffentlichte Statistik des Bundeskriminalamtes zeigt, dass speziell seit 2019 die Mordfälle durch Marokkaner um 110 Prozent und Tunesier um 67 Prozent gestiegen sind. Diese Gruppen begehen in Deutschland statistisch an jedem sechsten Tag einen Mord. [...] Wir wollen entweder gut integrierte Menschen aber sowas brauchen wir nicht und wir müssen darüber sprechen. Und wir als AfD sprechen es laut aus: Remigration schützt Leben und das ist keine Schande. Das müssen wir laut sagen. Remigration schützt Leben!

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 312

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