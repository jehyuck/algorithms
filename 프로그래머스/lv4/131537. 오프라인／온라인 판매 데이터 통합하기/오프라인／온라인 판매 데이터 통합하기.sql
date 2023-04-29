-- 코드를 입력하세요
SELECT * 
FROM (
    SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE
    , PRODUCT_ID
    , USER_ID
    , SALES_AMOUNT
    FROM ONLINE_SALE
    WHERE DATE_FORMAT(SALES_DATE, '%Y%m') = 202203
    UNION ALL
    SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE
    , PRODUCT_ID
    , NULL AS USER_ID
    , SALES_AMOUNT
    FROM OFFLINE_SALE 
    WHERE DATE_FORMAT(SALES_DATE, '%Y%m') = 202203
) AS UNION_TABLE
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC