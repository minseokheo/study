-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
        IF (SEX_UPON_INTAKE LIKE "Neutered%" or SEX_UPON_INTAKE LIKE "Spayed%", "O", "X") AS "중성화"
FROM ANIMAL_INS