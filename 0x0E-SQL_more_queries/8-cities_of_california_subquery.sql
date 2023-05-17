-- lists all the cities of California that can be found in the database
SELECT `id`, `name`
	FROM `cities`
WHERE `state_id` IN
	(SELECT `id` IN
		FROM `states`
	WHERE `name` = "California")
ORDER BY `id`;
