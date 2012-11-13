-- student51
-- получить всех владельцев конкретного оборудования
-- с последним изменением статуса (принят/уволен)

SELECT v_employee.id AS employee_id, v_employee.name,
       v_employee_role.name AS role,
       v_employee.phone, v_employee.login,
       tmp2.state, tmp2.date
FROM _techsup_left.v_employee
LEFT JOIN _techsup_left.v_employee_role
ON v_employee.role_id = v_employee_role.id
RIGHT JOIN (
    SELECT *
    FROM (
        -- id сотрудников  с последними изменёнными статусами
        SELECT v_employee_operation.employee_id, 
               v_employee_operation_type.name AS state,
               v_employee_operation.date
        FROM _techsup_left.v_employee_operation
        INNER JOIN (
            SELECT v_employee_operation.employee_id, MAX( v_employee_operation.date ) AS date
            FROM _techsup_left.v_employee_operation
            GROUP BY v_employee_operation.employee_id
        ) AS tmp1
        ON v_employee_operation.employee_id = tmp1.employee_id AND
           v_employee_operation.date = tmp1.date
        INNER JOIN _techsup_left.v_employee_operation_type
        ON type_id = v_employee_operation_type.id
    ) AS tmp
    WHERE tmp.employee_id IN (
        SELECT employee_id
        FROM _techsup_left.v_equipment_owner
        WHERE v_equipment_owner.equipment_id = (
            SELECT equipment.id
            FROM _techsup_left.equipment
            WHERE LOWER( equipment.serial_number ) LIKE 'comm-269-5195-31-proj'
        )
   )
) AS tmp2
ON v_employee.id = tmp2.employee_id
ORDER BY date, name;

