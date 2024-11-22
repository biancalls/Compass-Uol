WITH Decada AS (
    SELECT
        nome,
        total,
        FLOOR(ano / 10) * 10 AS decada
    FROM nomes
    WHERE ano >= 1950
),
RankingPorDecada AS (
    SELECT
        decada,
        nome,
        SUM(total) AS total_por_decada,
        ROW_NUMBER() OVER (PARTITION BY decada ORDER BY SUM(total) DESC) AS ranking
    FROM Decada
    GROUP BY decada,nome
)
SELECT
    decada,
    nome,
    total_por_decada
FROM RankingPorDecada
WHERE ranking <= 3
ORDER BY decada, ranking;