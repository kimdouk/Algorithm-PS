-- 코드를 입력하세요
# SELECT A.PRODUCT_ID, A.PRODUCT_NAME, (A.PRICE * B.AMOUNT) AS TOTAL_SALES
# FROM (SELECT PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
#      FROM FOOD_ORDER
#      WHERE PRODUCE_DATE LIKE '2022-05%'
#      GROUP BY PRODUCT_ID) B JOIN FOOD_PRODUCT A ON A.PRODUCT_ID = B.PRODUCT_ID
# ORDER BY TOTAL_SALES DESC, PRODUCT_ID

# SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(A.PRICE * B.AMOUNT)AS TOTAL_SALES
# FROM (SELECT * FROM FOOD_ORDER WHERE PRODUCE_DATE LIKE '2022-05%') B JOIN FOOD_PRODUCT A ON A.PRODUCT_ID = B.PRODUCT_ID
# GROUP BY PRODUCT_ID
# ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID


# SELECT A.PRODUCT_ID, A.PRODUCT_NAME, (A.PRICE*B.TOTAL) AS TOTAL_SALES
# FROM FOOD_PRODUCT A JOIN (
#     SELECT PRODUCT_ID, SUM(AMOUNT) AS TOTAL
#     FROM FOOD_ORDER
#     WHERE PRODUCE_DATE REGEXP '^2022-05'
#     GROUP BY PRODUCT_ID
# ) B ON A.PRODUCT_ID = B.PRODUCT_ID
# ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID

# SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(A.PRICE*B.AMOUNT) AS TOTAL_SALES
# FROM (SELECT * FROM FOOD_ORDER WHERE PRODUCE_DATE LIKE '2022-05%') B JOIN FOOD_PRODUCT A ON A.PRODUCT_ID = B.PRODUCT_ID
# GROUP BY PRODUCT_ID
# ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID

SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(AMOUNT*PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT A JOIN FOOD_ORDER B ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE B.PRODUCE_DATE REGEXP '^2022-05'
GROUP BY A.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID