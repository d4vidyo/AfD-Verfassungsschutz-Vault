---
type: zitat
speaker: "[[Uwe Schulz]]"
date: 2025-02-20
topic: Menschenwürde
page_bfv: 886
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Uwe Schulz]] vom 20.2.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Meine Damen und Herren, das Beispiel Karneval zeigt, wie wir schleichend entwöhnt werden von den Traditionen unserer Vorfahren. Auf der bunten Todesliste stehen ausnahmslos alle unsere Feste, unsere Riten, unsere Bräuche – die Entwöhnung von allem, was uns als Gesellschaft ausmacht, was uns heilig ist. Es geht rasend voran mit dem Umbau der Bevölkerung. Und mit jedem Weiteren, der hier hineingeflutet wird, steigt die Macht dieser Gruppe und steigt auch deren Unberechenbarkeit. [...] Auf jeden Fall sind es genau diese Menschen, die uns die Identität nehmen und das Feiern und Weitertragen unserer Bräuche schlicht und einfach auslöschen. [...] Wir schauen nicht zu, wie Deutschland jeden Tag ein wenig mehr verreckt, und wir lassen es nicht zu, dass unsere Werte in die Gosse getrieben werden, meine Damen und Herren. [...] Und wir werden tun, was unausweichlich ist. [...] Wir werden sie ausweiseh: die Illegalen, die Straftäter und solche, die hier nichts zum Wohle unserer Gesellschaft beitragen wollen. Nennen Sie es Abschiebung, nennen Sie es Ausweisung, nennen Sie es Remigration – es ist mir scheißegal! Mein österreichischer Mitarbeiter sagt dazu "Ausschaffung" und irgendwie gefällt mir dieses Wort am besten: Ausschaffung. Ausschaffung – auch für den eingeschleppten Familiennachzug, meine Damen und Herren. Wir werden es schaffen, solche Leute auszuschaffen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 886

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