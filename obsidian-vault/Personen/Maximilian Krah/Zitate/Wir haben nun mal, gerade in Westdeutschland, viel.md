---
type: zitat
speaker: "[[Maximilian Krah]]"
date: 2025-03-01
topic: Menschenwürde
page_bfv: 896
source: 'Interview im Compact-Magazin'
status: Unbewertet
---

# Zitat: [[Maximilian Krah]] vom März 2025 veröffentlicht auf: 'Interview im Compact-Magazin'
> [!quote] Aussage
>Wir haben nun mal, gerade in Westdeutschland, viele Menschen mit Migrationshintergrund. Es gibt Leute, die integriert sind, aber auch Gruppen, die ihre Eigenidentität bewahren und dennoch deutschfreundlich sind. Auch ihnen müssen wir sagen: Wir haben etwas für euch zu bieten, wir können gemeinsam Dinge klären, indem wir uns gegenseitig respektieren. Das Zauberwort heißt Respekt. Ich denke, dass diese Erweiterung notwendig ist, wenn wir wirklich Regierungspartei werden wollen. [...] Ich will jetzt auch keine große Verschmelzung, aber die Leute sind da, sie organisieren sich und stehen in fast allen politischen Fragen auf unserer Seite. [...] Denn eines muss klar sein: Remigration hin oder her - es ist offensichtlich, dass die Völkerwanderung, die hier im letzten Jahrzehnt stattgefunden hat, bleibende Folgen haben wird. [...] Was ich allerdings sage, ist, dass der Fehler sowohl der Linken als auch der Rechten in diesem Fall darin liegt, dass sie die Einwanderer alle über einen Kamm scheren — bei Muslimen sowieso. Wofür ich werbe, ist, dass man sich die Mühe macht, die einzelnen Gruppen, die wir hier haben, auseinanderzunehmen. [...] Wenn wir uns wirklich nur auf ein rein ethnisches Prinzip beschränken würden, das heißt, wir sagen, wir sind die Partei der rein ethnisch Deutschen und alle, die das nicht sind - selbst wenn sie uns inhaltlich zustimmen -, die vertreten wir nicht, dann werden wir scheitern. Dann werden sich alle Ausländer, auch diejenigen, die uns mögen, mit unseren linksliberalen Eliten zusammentun und uns plattmachen. Ohne neue Verbündete werden wir das Land nicht verändern können. Das heißt, wir sind in gewisser Weise gezwungen, über den sicheren Grund der eigenen ethnischen Gruppe hinauszugehen und zu sagen: Wer ist ein Partner, ohne dass er uns ins unserer ethnisch-kulturellen Identität infrage stellt, wer respektiert uns so, dass er uns das zugesteht, was unsere Tradition, unsere eigene Art zu leben, unser Deutschtum - um dieses Wort mal zu benutzen - betrifft. Ich möchte vor allem warnen: Ich halte das Remigrationsthema für wichtig, aber es ist nicht das Entscheidende und das Einzige.

**Parser-Notiz:** Es war nur Monat und Jahr des Datums vorhanden daher wurde es zur Darstellung auf den Ersten des Monats gesetzt. Original: März 2025

**SPIEGEL-Notiz:** Gutachten Seite: 896

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