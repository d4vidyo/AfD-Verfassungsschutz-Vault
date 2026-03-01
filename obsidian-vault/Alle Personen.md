
>[!info] Alle Personen
>```dataview
>TABLE state AS "Bundesland", relevance AS "Relevanz", choice(is_still_member, "Ja", "Nein") AS "Noch Mitglied?"
>FROM "Personen"
>WHERE type = "person"
>SORT is_still_member DESC, relevance ASC, state ASC, speaker ASC
