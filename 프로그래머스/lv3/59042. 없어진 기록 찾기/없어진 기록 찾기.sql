# -- 코드를 입력하세요
# SELECT B.ANIMAL_ID, B.NAME
# FROM ANIMAL_INS A RIGHT OUTER JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
# WHERE B.ANIMAL_ID IS NULL
# ORDER BY B.ANIMAL_ID\

SELECT ANIMAL_ID,NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                      FROM ANIMAL_INS)
ORDER BY ANIMAL_ID