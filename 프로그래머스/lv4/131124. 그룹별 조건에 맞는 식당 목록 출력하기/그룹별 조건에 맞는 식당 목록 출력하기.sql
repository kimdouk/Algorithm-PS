SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE NATURAL JOIN REST_REVIEW
WHERE MEMBER_ID IN (SELECT MEMBER_ID
                   FROM REST_REVIEW
                   GROUP BY MEMBER_ID
                    HAVING COUNT(*) IN (SELECT MAX(CNT)
                                       FROM 
                                        (SELECT COUNT(*)AS CNT
                                         FROM REST_REVIEW
                                         GROUP BY MEMBER_ID) AS B
                    )
                    )
ORDER BY REVIEW_DATE,REVIEW_TEXT