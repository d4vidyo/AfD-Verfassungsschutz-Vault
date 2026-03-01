
>[!todo] Unbewertete Aussagen
>```dataview
>TABLE speaker AS "Person", date AS "Datum", topic AS "Thema", choice(speaker.is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>FROM "Personen"
>WHERE type = "zitat" and status = "Unbewertet"
>SORT speaker.is_still_member DESC, speaker.relevance ASC, speaker ASC, date ASC
>```
