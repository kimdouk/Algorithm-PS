SELECT B.FLAVOR
FROM FIRST_HALF A JOIN JULY B ON A.FLAVOR = B.FLAVOR
GROUP BY B.FLAVOR
ORDER BY SUM(B.TOTAL_ORDER)+A.TOTAL_ORDER DESC
LIMIT 3
