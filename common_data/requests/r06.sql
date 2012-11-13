-- students51
-- добавить куратора новой заявки

UPDATE _techsup_left.task
  SET owner_id = (
    SELECT id
    FROM _techsup_left.v_employee
    WHERE v_employee.login    LIKE 'anastas.sanina' AND
          v_employee.password LIKE 'e0fb2a62faafc09122d2e613b8a8118d'
  )
  WHERE task.id = 40379;

INSERT INTO _techsup_left.task_operation( datetime, task_id, technic_id, state_id )
  VALUES(
    (SELECT current_timestamp),
    40379,
    (
      SELECT id
      FROM _techsup_left.v_employee
      WHERE v_employee.login    LIKE 'anastas.sanina' AND
            v_employee.password LIKE 'e0fb2a62faafc09122d2e613b8a8118d'
    ),
    (
      SELECT id
      FROM _techsup_left.task_state
      WHERE LOWER( task_state.name ) LIKE 'выполняется'
    )
  );

