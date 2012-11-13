-- student52
-- удалить администратора

DELETE FROM _techsup_right.admins 
WHERE admins.employee_id =
    (
        SELECT id
        FROM _techsup_right.employee
        WHERE LOWER( employee.snils )  LIKE in_snils
    );

CREATE OR REPLACE FUNCTION _techsup_right.delete_equipment_owner(
                                        in_snils         CHARACTER VARYING( 16 ),
                                        in_serial_number CHARACTER VARYING( 128 ),
                                        in_datetime      TIMESTAMP WITH TIME ZONE                               
                                       )
RETURNS INTEGER
AS $$
BEGIN

-- START TRANSACTION;

