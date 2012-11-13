-- students51
-- получить расходы по закупке деталей
-- для конкретного оборудования

SELECT tmp.sum_detail_price
FROM (
    SELECT equipment_id, SUM( detail_price ) AS sum_detail_price 
    FROM _techsup_left.equipment_operation
    GROUP BY equipment_id
) AS tmp
WHERE tmp.equipment_id = (
    SELECT id
    FROM _techsup_left.equipment
    WHERE LOWER( equipment.serial_number ) LIKE 'issl-675-8635-84-pc'
);

