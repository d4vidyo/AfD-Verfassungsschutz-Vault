---
type: zitat
speaker: "[[Enrico Komning]]"
date: 2023-01-30
topic: Menschenwürde
page_bfv: 309
source: 'AUF1'
status: Unbewertet
---

# Zitat: [[Enrico Komning]] vom 30.1.2023 veröffentlicht auf: 'AUF1'
> [!quote] Aussage
>Die Ursache von Amokläufen, von Messerattacken, Angriffen auf Polizei oder eben auch Schutz- und Rettungskräfte: Das ist Gewalt durch Migranten. Das muss man auch ganz klar beim Namen nennen. Und da wird auch letztlich keine Einschränkung des Waffenrechtes helfen, diese Gewalt letztlich zu reduzieren. Stattdessen ist es aus meiner Ansicht besser, nicht nur an den Symptomen herumzudoktern, sondern der Ursache auf den Grund zu gehen. Und die Ursache ist eben die, dass wir hier gewalttätige Migranten in Deutschland haben, die schlichtweg nicht abgeschoben werden. [...] Einerseits haben wir nach wie vor einer Politik der offenen Grenzen, dass quasi jeder, der weltweit unterwegs ist, einfach zu uns kommen kann, hier die Hand heben muss und einfach nur 'Asyl' sagen muss, dann ein wahrscheinlich dauerhaftes Bleiberecht hier erhält. Da wird eben tatsächlich die Ursache dieser Migrantengewalt nicht nur nicht erkannt, sie wird auch nicht angesprochen und erst recht nicht verhindert. Wir müssen also dafür Sorge tragen, dass die Migranten, die hier nach Deutschland gekommen sind und die sich strafbar gemacht haben, und ich rede da nicht nur von Gewalttaten, sondern ich rede von Strafbarkeit jeglicher Art, wenn sie sich also gegen unser Rechtssystem wenden, dann müssen diese Täter unverzüglich abgeschoben werden. [...] Ja, zum zweiten kommt, wie gesagt, dann die Entwaffnung der Bürger dazu. Also offensichtlich geht es der Innenministerin darum, dass man die Deutschen, das deutsche Volk, das angestammte Volk hier in Deutschland in eine Art Wehrlosigkeit gegenüber Gewaltmigranten treiben will.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 309

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