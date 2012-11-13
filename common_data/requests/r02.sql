-- students51
-- просмотреть очередь заявок с последним
-- изменённым статусом для пользователя

SELECT *
FROM (
    SELECT tmp.task_id, 
           task_priority.name AS priority,
           task.name AS task,
           tmp.name AS technic,
           tmp.state, tmp.datetime
    FROM (
        SELECT task_operation.task_id, 
               v_employee.name,
               task_state.name AS state, task_operation.datetime 
        FROM _techsup_left.task_operation
        INNER JOIN (
            SELECT task_operation.task_id, MAX( task_operation.datetime ) AS date
            FROM _techsup_left.task_operation
            GROUP BY task_operation.task_id
        ) AS temp
        ON task_operation.task_id = temp.task_id AND
           task_operation.datetime = temp.date
        LEFT JOIN _techsup_left.v_employee
        ON technic_id = v_employee.id
        INNER JOIN _techsup_left.task_state 
        ON state_id = task_state.id
    ) tmp
    INNER JOIN _techsup_left.task
    ON tmp.task_id = task.id
    INNER JOIN _techsup_left.task_priority
    ON priority_id = task_priority.id
) AS t
WHERE t.datetime >= '2012-01-01' AND datetime <= ( SELECT current_timestamp )
ORDER BY t.datetime DESC
LIMIT 20;

