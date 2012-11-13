-- students51
-- получить информацию о всех ремонтах 
-- с конкретным оборудованием

SELECT repair.equipment_operation_id AS repair_id,
       detail_model.name AS detail_model,
       tmp_repair.detail_price,
       repair.comment,
       v_employee.name,
       v_employee.phone,
       repair.datetime
FROM _techsup_left.repair
RIGHT JOIN (
    SELECT id, detail_price
    FROM _techsup_left.equipment_operation
    WHERE equipment_operation.equipment_id = (
        SELECT equipment.id
        FROM _techsup_left.equipment
        WHERE LOWER( equipment.serial_number ) LIKE 'issl-675-8635-84-pc'
    ) AND equipment_operation.eq_oper_type_id = ( 
        SELECT equipment_operation_type.id
        FROM _techsup_left.equipment_operation_type
        WHERE LOWER( equipment_operation_type.name ) = 'ремонт'
    )
) AS tmp_repair
ON equipment_operation_id = tmp_repair.id
LEFT JOIN _techsup_left.detail_model
ON detail_model_id = detail_model.id
INNER JOIN _techsup_left.task_operation
ON repair.task_id = task_operation.task_id
LEFT JOIN _techsup_left.v_employee
ON technic_id = v_employee.id;

