SELECT job,
       COUNT(*) AS record_count,
       COUNT(CASE WHEN y = 'yes' THEN 1 END) AS subscriber_count,
       AVG(CASE WHEN y = 'yes' THEN 1.0 ELSE 0.0 END) AS subscription_rate
FROM campaign_train
GROUP BY job
HAVING COUNT(*) >= 100
ORDER BY subscription_rate DESC, job;
