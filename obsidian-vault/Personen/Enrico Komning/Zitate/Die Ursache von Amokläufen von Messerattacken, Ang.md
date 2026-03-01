---
type: zitat
speaker: "[[Enrico Komning]]"
date: 2023-01-30
topic: Rechtsstaatsprinzip
page_bfv: 654
source: 'https;//auf1.tv'
status: Unbewertet
---

# Zitat: [[Enrico Komning]] vom 30.1.2023 veröffentlicht auf: 'https;//auf1.tv'
> [!quote] Aussage
>Die Ursache von Amokläufen von Messerattacken, Angriffe auf Polizei oder eben auch Schutz- und Rettungskräfte: Das ist Gewalt durch Migranten. [...] Wir als AfD und insbesondere auch ich stehe eher für eine Liberalisierung des Waffenrechts. Ich denke, dass gerade vor dem Hintergrund, dass der Staat offensichtlich unsere Bürger nicht mehr mit dem alleinigen Gewaltmonopol schützen kann, dass dann die Bürger durchaus die Möglichkeit haben müssen, sich selbst zu schützen. Und das eben auch durch Waffen. Insofern meine ich, ist es eher Zeit für eine Liberalisierung des Waffenrechts als für eine Einschränkung. [...] Da wird eben tatsächlich die Ursache dieser Migrantengewalt nicht nur nicht erkannt, sie wird auch nicht angesprochen und erst recht nicht verhindert. Wir müssen also dafür Sorge tragen, dass die Migranten, die nach Deutschland gekommen sind, die sich strafbar gemacht haben und ich rede da nicht nur von Gewalttaten, sondern ich rede von Strafbarkeit jeglicher Art, wenn sie sich also gegen unser Rechtssystem wenden, dann müssen diese Täter unverzüglich abgeschoben werden. [...] Ja und zum zweiten kommt wie gesagt dann die Entwaffnung der Bürger dazu. Also offensichtlich geht es der Innenministerin darum, dass man die Deutschen, das deutsche Volk, das angestammte Volk hier in Deutschland in eine Art Wehrlosigkeit gegenüber Gewaltmigranten treiben will. Anders kann ich mir das letztlich nicht vorstellen. Diese Politik können wir auf keinen Fall mittragen.Wir können auch diese Innenministerin nicht mittragen. Wenn Sie mich also fragen, ob die Sicherheit in Deutschland durch das Handeln der Innenministerin gefährdet ist, dann kann ich das nur bejahen.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 654

**Verfassungsschutz Kategorisierung:** Verstoß gegen das Rechtsstaatsprinzip.

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