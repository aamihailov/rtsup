-- student52
-- отписать владельца от оборудования

IF EXISTS (
  SELECT *
  FROM _techsup_right.equipment_owner
  WHERE equipment_owner.equipment_id = (
    SELECT id
    FROM _techsup_right.v_equipment
    WHERE LOWER( v_equipment.serial_number ) LIKE $2
  ) AND
  equipment_owner.employee_id = (
    SELECT id
    FROM _techsup_right.employee
    WHERE LOWER( employee.snils ) LIKE $1
  ) AND
  equipment_owner.finish_datetime IS NULL
)
THEN
  UPDATE _techsup_right.equipment_owner
    SET finish_datetime = $3
    WHERE equipment_owner.equipment_id = (
      SELECT id
      FROM _techsup_right.v_equipment
      WHERE LOWER( v_equipment.serial_number ) LIKE $2
    )  AND equipment_owner.employee_id = (
      SELECT id
      FROM _techsup_right.employee
      WHERE LOWER( employee.snils ) LIKE $1
    );
  RETURN 0;
ELSE
  RETURN 1;
END IF;

-- COMMIT;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION _techsup_right.add_equipment_owner(
                                     in_snils         CHARACTER VARYING( 16 ),
                                     in_serial_number CHARACTER VARYING( 128 ),
                                     in_datetime      TIMESTAMP WITH TIME ZONE   
                                    )
RETURNS INTEGER
AS $$
BEGIN

-- START TRANSACTION;

-- добавить пользователя оборудованием

IF NOT EXISTS (
  SELECT *
  FROM _techsup_right.equipment_owner
  WHERE equipment_owner.equipment_id = (
    SELECT id
    FROM _techsup_right.v_equipment
    WHERE LOWER( v_equipment.serial_number ) LIKE $2
  ) AND
  equipment_owner.employee_id = (
    SELECT id
    FROM _techsup_right.employee
    WHERE LOWER( employee.snils ) LIKE $1
  ) AND
  equipment_owner.finish_datetime IS NULL
)
THEN
  INSERT INTO _techsup_right.equipment_owner ( equipment_id, employee_id, start_datetime )
      VALUES (
          (
              SELECT id
              FROM _techsup_right.v_equipment
              WHERE LOWER( v_equipment.serial_number ) LIKE $2
          ),
          (
              SELECT id
              FROM _techsup_right.employee
              WHERE LOWER( employee.snils )  LIKE $1
          ),
          $3
      );
  RETURN 0;
ELSE
  RETURN 1;
END IF;

--COMMIT;

END;
$$ LANGUAGE plpgsql;


