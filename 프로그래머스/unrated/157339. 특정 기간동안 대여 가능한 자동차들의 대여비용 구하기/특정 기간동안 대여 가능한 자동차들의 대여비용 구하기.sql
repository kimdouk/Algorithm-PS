SELECT A.CAR_ID, A.CAR_TYPE, TRUNCATE( (A.DAILY_FEE*((100-B.DISCOUNT_RATE)/100)*30),0) AS FEE
FROM (SELECT *
FROM CAR_RENTAL_COMPANY_CAR 
WHERE CAR_ID NOT IN (SELECT CAR_ID
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                WHERE (START_DATE BETWEEN '2022-11-01' AND '2022-11-30') OR (END_DATE BETWEEN '2022-11-01' AND '2022-11-30') OR (START_DATE <='2022-11-01' AND END_DATE>= '2022-11-30')
                    GROUP BY CAR_ID) AND CAR_TYPE IN ('세단','SUV')) A
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN B ON A.CAR_TYPE = B.CAR_TYPE
WHERE B.DURATION_TYPE = '30일 이상' 
GROUP BY A.CAR_ID, A.CAR_TYPE, FEE
HAVING FEE BETWEEN 500000 AND 2000000
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC