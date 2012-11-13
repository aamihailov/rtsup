-- students51
-- получить информацию о всех операциях 
-- с конкретным оборудованием

SELECT equipment_operation.id AS oper_id, 
       equipment_operation_type.name AS oper_name,
       tmp_repair.repair_id,
       datetime
FROM _techsup_left.equipment_operation
INNER JOIN (
    SELECT id AS equipment_id
    FROM _techsup_left.equipment
    WHERE LOWER( equipment.serial_number ) = 'issl-675-8635-84-pc' 
) AS t
ON equipment_operation.equipment_id = t.equipment_id
LEFT JOIN _techsup_left.equipment_operation_type
ON eq_oper_type_id = equipment_operation_type.id
LEFT JOIN (
    SELECT repair.equipment_operation_id AS repair_id
    FROM _techsup_left.repair
    WHERE repair.equipment_operation_id IN (
        SELECT id
        FROM _techsup_left.equipment_operation
        WHERE equipment_operation.equipment_id = (
            SELECT equipment.id
            FROM _techsup_left.equipment
            WHERE LOWER( equipment.serial_number ) LIKE 'issl-675-8635-84-pc'
        ) AND equipment_operation.eq_oper_type_id = ( 
            SELECT equipment_operation_type.id
            FROM _techsup_left.equipment_operation_type
            WHERE LOWER( equipment_operation_type.name ) = 'ремонт' )
    )
) AS tmp_repair
ON equipment_operation.id = tmp_repair.repair_id;

