WITH channel_stats AS (
    SELECT contact,
           COUNT(*) AS n_records,
           COUNT(CASE WHEN y = 'yes' THEN 1 END) AS n_subscribed,
           AVG(CASE WHEN y = 'yes' THEN 1.0 ELSE 0.0 END) AS subscription_rate
    FROM campaign_train
    GROUP BY contact
)
SELECT channel_stats.*,
       RANK() OVER (ORDER BY subscription_rate DESC) AS channel_rank
FROM channel_stats
ORDER BY channel_rank, contact;
