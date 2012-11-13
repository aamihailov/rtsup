-- students51
-- получить информацию околичестве выполненных заявок
-- для конкретного работника по приоритетам заявок

SELECT id, name, priority, COUNT(*)
FROM (
    SELECT v_employee.id, v_employee.snils, v_employee.name,
           tmp.task_id, tmp.priority_id,
           task_priority.name AS priority
    FROM _techsup_left.v_employee
    RIGHT JOIN (
        SELECT owner_id, task.id AS task_id, task.priority_id
        FROM _techsup_left.task
        WHERE id IN (
            SELECT task_id
            FROM _techsup_left.task_operation
            WHERE task_operation.state_id = (
                SELECT id
                FROM _techsup_left.task_state
                WHERE LOWER( task_state.name ) = 'закрыта'
            )
        )
    ) AS tmp
    ON v_employee.id = tmp.owner_id
    RIGHT JOIN _techsup_left.task_priority
    ON priority_id = task_priority.id
) AS tmp1
WHERE priority_id > 0  AND snils LIKE %s
GROUP BY id, priority, name;