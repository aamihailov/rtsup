-- students51
-- выдать список топ-10 сотрудников, на ремонт
-- чьего оборудования потрачено больше всего денег :)

SELECT *
FROM (
    SELECT v_employee.snils,
           v_employee.name,
           tmp_summ.work_price,
           tmp_summ.detail_price,
           ( SELECT work_price + detail_price) AS summ
    FROM (
      SELECT tmp.client_id,
             SUM( tmp.work_price ) AS work_price,
             SUM( tmp.detail_price ) AS detail_price
      FROM (
          SELECT task_equipment.task_id, 
                 task_equipment.equipment_id,
                 task.client_id,       
                 tmp_task.work_price,
                 equipment_operation.detail_price
          FROM _techsup_left.task_equipment
          LEFT JOIN _techsup_left.task
          ON task_id = task.id
          LEFT JOIN (
              SELECT task_operation.task_id, work_price, task_operation.datetime
              FROM _techsup_left.task_operation
              RIGHT JOIN (
                 SELECT task_id, MAX( datetime ) AS datetime
                 FROM _techsup_left.task_operation
                 GROUP BY task_id, work_price
              ) t
              ON task_operation.datetime = t.datetime AND
                 task_operation.task_id = t.task_id
          ) AS tmp_task
          ON task_equipment.task_id = tmp_task.task_id
          LEFT JOIN _techsup_left.repair
          ON task_equipment.task_id = repair.task_id
          LEFT JOIN _techsup_left.equipment_operation
          ON repair.equipment_operation_id = equipment_operation.id
       ) AS tmp
      GROUP BY tmp.client_id
    ) AS tmp_summ
    LEFT JOIN _techsup_left.v_employee
    ON client_id = v_employee.id
    ) AS t_summ
WHERE t_summ.summ > 0
ORDER BY summ DESC
LIMIT 10;