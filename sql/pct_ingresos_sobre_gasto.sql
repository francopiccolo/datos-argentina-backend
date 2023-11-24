SELECT EXTRACT(year FROM indice_tiempo) AS year,
       SUM(CASE WHEN prestacion_l1 = 'ingresos' THEN gasto ELSE 0 END) / SUM(gasto) * 100 AS pct_ingresos
FROM fact.gasto_publico_anual_por_prestacion
WHERE EXTRACT(year FROM indice_tiempo) < 2022
GROUP BY 1
ORDER BY 1;