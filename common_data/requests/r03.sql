-- students51
-- добавить новую заявку

INSERT INTO _techsup_left.task ( name, datetime, priority_id, client_id )
    VALUES( 'test', 
            (SELECT current_timestamp),
            1, 
            (
                SELECT id
                FROM _techsup_left.v_employee
                WHERE v_employee.login    LIKE 'anastas.sanina' AND
                      v_employee.password LIKE 'e0fb2a62faafc09122d2e613b8a8118d'
            )            
           );

INSERT INTO _techsup_left.task_equipment ( task_id, equipment_id )
    VALUES( 
           (
                SELECT id
                FROM _techsup_left.task
                WHERE task.datetime = ( 
                    SELECT MAX( datetime )
                    FROM _techsup_left.task
                )  
           ),
           (
                SELECT id
                FROM _techsup_left.equipment
                WHERE LOWER( equipment.serial_number ) LIKE 'adm-999-9999-99-pc'
           )
          );


CREATE OR REPLACE FUNCTION _techsup_left.close_task (
                              in_task_id   INTEGER,
                              in_login     CHARACTER VARYING(64),
                              in_password  CHARACTER VARYING(128),
                              in_datetime  TIMESTAMP WITH TIME ZONE  
                           )
RETURNS INTEGER
AS $$
BEGIN

-- BEGIN TRANSACTION;

