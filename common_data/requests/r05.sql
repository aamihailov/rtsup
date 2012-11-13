-- students51
-- изменить куратора заявки

UPDATE _techsup_left.task
    SET owner_id = (
            SELECT v_employee.id
            FROM _techsup_left.v_employee
            WHERE LOWER( v_employee.snils ) LIKE '275-985-770 30'
        )
    WHERE task.id = 40386;

