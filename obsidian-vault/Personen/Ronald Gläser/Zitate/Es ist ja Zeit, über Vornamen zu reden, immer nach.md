---
type: zitat
speaker: "[[Ronald Gläser]]"
date: 2025-01-08
topic: Menschenwürde
page_bfv: 884
source: 'Rede'
status: Unbewertet
---

# Zitat: [[Ronald Gläser]] vom 8.1.2025 veröffentlicht auf: 'Rede'
> [!quote] Aussage
>Es ist ja Zeit, über Vornamen zu reden, immer nach einer Silvesternacht reden wir über Vornamen. [...] Wir wollen niemanden bloßstellen, nur, weil er Hakan oder Yusuf heißt. Wir haben es ja schon gerade gehört. Viele von den abgefragten Namen, viele von den Tatverdächtigen heißen ja so. Aber es gibt auch viele, die Hakan oder Yusuf heißen, die führen ein normales Leben. Aber wir stellen fest in der Kriminalitätsstatistik, dass da halt sehr viele Ausländer drin sind und über diese Dinge soll nicht gesprochen werden und wir wollen das ändern. [...] Und warum müssen wir nach Vornamen fragen? Weil der Berliner Senat vor drei Jahren der Polizei verboten hat, dieses Kriterium Migrationshintergrund bei jugendlichen Strafverdächtigen überhaupt zu erfassen. [...] Inzwischen sind schon wieder neue Festnahmen dazugekommen, die noch nachgemeldet wurden. Aber ein Teil der Vornamen sind bekannt. Und sie decken sich natürlich genau mit dem, was unsere Befürchtung ist. Da ist auch mal ein Martin oder ein Benjamin dabei. Aber weit überwiegend sind diese [Anm.: anhand einer Geste in Anführungsstriche gesetzt] "deutschen" Straftäter oder Tatverdächtigen, haben halt einen ausländisch klingenden Namen, so dass wir insgesamt von 80% Tätern reden können bei den Silvester-typischen Verbrechen als Tatverdächtige. Das kann doch nicht sein, dass wir in unserem Land nicht mehr wie 1980 oder im Jahr 2000 ein normales Silvester feiern können, weil wir so viele illegale Masseneinwanderung haben.

**Parser-Notiz:** Keine

**SPIEGEL-Notiz:** Gutachten Seite: 884

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