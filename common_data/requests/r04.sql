-- students51
-- закрыть заявку

IF NOT EXISTS (
    SELECT *
    FROM (
        SELECT name
        FROM _techsup_left.task_state
        INNER JOIN (
            SELECT state_id
            FROM _techsup_left.task_operation
            WHERE task_id = $1 AND datetime = (
                SELECT max_date
                FROM (
                    SELECT task_id, MAX( datetime ) AS max_date
                    FROM _techsup_left.task_operation
                    GROUP BY task_id
                ) AS tmp_date
                WHERE tmp_date.task_id = $1
            )
        ) AS tmp
        ON task_state.id = tmp.state_id 
    ) AS t
    WHERE LOWER( t.name ) = 'закрыта'
)
THEN
  INSERT INTO _techsup_left.task_operation( datetime, task_id, technic_id, state_id )
    VALUES(
      $4,
      in_task_id,
      (
        SELECT id
        FROM _techsup_left.v_employee
        WHERE v_employee.login    LIKE $2 AND
              v_employee.password LIKE $3
      ),
      (
        SELECT id
        FROM _techsup_left.task_state
        WHERE LOWER( task_state.name ) LIKE 'закрыта'
      )
    );
    RETURN 0;
ELSE
  RETURN 1;
END IF;

END;
$$ LANGUAGE plpgsql;

