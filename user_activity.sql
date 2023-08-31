SELECT
    activity_date,
    ROUND(
        (COUNT(DISTINCT CASE WHEN activity_type IS NOT NULL THEN user_id END) /
         COUNT(DISTINCT user_id)) * 100, 2
    ) AS engagement_rate
FROM user_activity
GROUP BY activity_date
ORDER BY activity_date;