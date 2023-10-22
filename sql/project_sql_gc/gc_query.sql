-- Tabela com os jogos dos ultimos 30 dias
WITH tb_lobby AS
  (SELECT *
   FROM tb_lobby_stats_player
   WHERE dtCreatedAt < '2022-02-01'
     AND dtCreatedAt > date('2022-02-01', '-30 day') ), -- Tabela com as estatisticas dos jogadores, agrupada por id do jogador
tb_stats AS
  (SELECT idPlayer,
          count(DISTINCT idLobbyGame) AS qtd_partidas,
          count(DISTINCT date (dtCreatedAt)) AS qtd_dias,
          1.0 * count(DISTINCT idLobbyGame) / count(DISTINCT date(dtCreatedAt)) AS qtd_partida_dia,
          avg(qtKill) AS avg_qtKill,
          avg(qtAssist) AS avg_qtAssist,
          avg(qtDeath) AS avg_qtDeath,
          avg(qtHs) AS avg_qtHs,
          avg(qtBombeDefuse) AS avg_qtBombeDefuse,
          avg(qtBombePlant) AS avg_qtBombePlant,
          avg(qtTk) AS avg_qtTk,
          avg(qtTkAssist) AS avg_qtTkAssist,
          avg(qt1Kill) AS avg_qt1Kill,
          avg(qt2Kill) AS avg_qt2Kill,
          avg(qt3Kill) AS avg_qt3Kill,
          avg(qt4Kill) AS avg_qt4Kill,
          avg(qt5Kill) AS avg_qt5Kill,
          avg(qtPlusKill) AS avg_qtPlusKill,
          avg(qtFirstKill) AS avg_qtFirstKill,
          avg(vlDamage) AS avg_vlDamage,
          avg(qtHits) AS avg_qtHits,
          avg(qtShots) AS avg_qtShots,
          avg(qtLastAlive) AS avg_qtLastAlive,
          avg(qtClutchWon) AS avg_qtClutchWon,
          avg(qtRoundsPlayed) AS avg_qtRoundsPlayed,
          avg(descMapName) AS avg_descMapName,
          avg(vlLevel) AS avg_vlLevel,
          avg(qtSurvived) AS avg_qtSurvived,
          avg(qtTrade) AS avg_qtTrade,
          avg(qtFlashAssist) AS avg_qtFlashAssist,
          avg(qtHitHeadshot) AS avg_qtHitHeadshot,
          avg(qtHitChest) AS avg_qtHitChest,
          avg(qtHitStomach) AS avg_qtHitStomach,
          avg(qtHitLeftAtm) AS avg_qtHitLeftAtm,
          avg(qtHitRightArm) AS avg_qtHitRightArm,
          avg(qtHitLeftLeg) AS avg_qtHitLeftLeg,
          avg(qtHitRightLeg) AS avg_qtHitRightLeg,
          avg(flWinner) AS avg_flWinner,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_ancient' THEN idLobbyGame
                         END) AS qtd_de_ancient,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_ancient'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_ancient,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_dust2' THEN idLobbyGame
                         END) AS qtd_de_dust2,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_dust2'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_dust2,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_inferno' THEN idLobbyGame
                         END) AS qtd_de_inferno,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_inferno'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_inferno,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_mirage' THEN idLobbyGame
                         END) AS qtd_de_mirage,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_mirage'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_mirage,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_nuke' THEN idLobbyGame
                         END) AS qtd_de_nuke,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_nuke'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_nuke,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_overpass' THEN idLobbyGame
                         END) AS qtd_de_overpass,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_overpass'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_overpass,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_train' THEN idLobbyGame
                         END) AS qtd_de_train,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_train'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_train,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_vertigo' THEN idLobbyGame
                         END) AS qtd_de_vertigo,
          count(DISTINCT CASE
                             WHEN descMapName = 'de_vertigo'
                                  AND flWinner =1 THEN idLobbyGame
                         END) AS qtd_vitorias_de_vertigo,
          count(DISTINCT CASE
                             WHEN qtRoundsPlayed < 16 THEN idLobbyGame
                         END) AS qtd_partidas_menos_16rounds,
          1.0 * count(DISTINCT (qtKill + qtAssist) / qtDeath) AS avg_kda,
          1.0 * sum(qtKill + qtAssist) / sum(qtDeath) AS kda_geral,
          1.0 * count(DISTINCT (qtKill + qtAssist) / qtRoundsPlayed) AS avg_kar,
          1.0 * sum(qtKill + qtAssist) / sum(qtRoundsPlayed) AS kar_geral,
          1.0 * count(DISTINCT vlDamage / qtRoundsPlayed) AS avg_damage_x_round,
          1.0 * sum(vlDamage) / sum(qtRoundsPlayed) AS damage_x_round_geral,
          avg(qtHitHeadshot) AS avg_hs,
          avg(qtHitStomach) AS avg_hit_stomach,
          avg(qtHitChest) AS avg_hit_chest,
          avg(qtHitLeftAtm) AS avg_hit_left_arm,
          avg(qtHitLeftLeg) AS avg_hs_hit_lef_leg,
          avg(qtHitRightArm) AS avg_hs_hit_right_arm,
          avg(qtHitRightLeg) AS avg_hs_hit_rigth_leg
   FROM tb_lobby
   GROUP BY idPlayer), -- Tabela com o level atual do jogador conforme a ultima partida jogada
tb_level_atual AS
  (SELECT idPlayer,
          vlLevel
   FROM
     (SELECT idPlayer,
             idLobbyGame,
             vlLevel,
             dtCreatedAt,
             row_number() OVER(PARTITION BY idPlayer
                               ORDER BY dtCreatedAt DESC) AS ranking
      FROM tb_lobby)
   WHERE ranking = 1 ), -- Tabela com junçao dos dados da tb_stats e tb_level_atual
tb_book_lobby AS
  (SELECT ts.*,
          tla.vlLevel
   FROM tb_stats AS ts
   LEFT JOIN tb_level_atual AS tla ON ts.idPlayer = tla.idPlayer), -- Tabela que junta os dados das medalhas dos jogadores no período de corte
tb_medals AS
  (SELECT tpm.*,
          tm.*
   FROM tb_players_medalha AS tpm
   LEFT JOIN tb_medalha AS tm ON tpm.idMedal = tm.idMedal
   WHERE dtCreatedAt < dtExpiration
     AND dtCreatedAt < '2022-02-01'
     AND coalesce(dtRemove, dtExpiration) > date('2022-02-01', '-30 day') ), -- Tabela que agrupa as medalhas por player
tb_book_medals AS
  (SELECT idPlayer,
          count(DISTINCT idMedal) AS qtd_medalhas,
          count(DISTINCT CASE
                             WHEN dtCreatedAt > date('2022-02-01', '-30 day') THEN id
                         END) AS qtd_medalhas_adquiridas,
          sum(CASE
                  WHEN descMedal = 'Membro Premium' THEN 1
                  ELSE 0
              END) AS qtd_membros_premium,
          sum(CASE
                  WHEN descMedal = 'Membro Plus' THEN 1
                  ELSE 0
              END) AS qtd_membros_plus,
          max(CASE
                  WHEN descMedal in ('Membro Premium', 'Membro Plus')
                       AND coalesce(dtRemove, dtExpiration) >= '2022-02-01' THEN 1
                  ELSE 0
              END) AS assinatura_ativa
   FROM tb_medals
   GROUP BY idPlayer) -- Tabela que consolida as stats dos players e medalhas

INSERT INTO tb_book_players1
SELECT ts1.qtd_partidas,
       ts1.qtd_dias,
       ts1.qtd_partida_dia,
       ts1.avg_qtKill,
       ts1.avg_qtAssist,
       ts1.avg_qtDeath,
       ts1.avg_qtHs,
       ts1.avg_qtBombeDefuse,
       ts1.avg_qtBombePlant,
       ts1.avg_qtTk,
       ts1.avg_qtTkAssist,
       ts1.avg_qt1Kill,
       ts1.avg_qt2Kill,
       ts1.avg_qt3Kill,
       ts1.avg_qt4Kill,
       ts1.avg_qt5Kill,
       ts1.avg_qtPlusKill,
       ts1.avg_qtFirstKill,
       ts1.avg_vlDamage,
       ts1.avg_qtHits,
       ts1.avg_qtShots,
       ts1.avg_qtLastAlive,
       ts1.avg_qtClutchWon,
       ts1.avg_qtRoundsPlayed,
       ts1.avg_descMapName,
       ts1.avg_vlLevel,
       ts1.avg_qtSurvived,
       ts1.avg_qtTrade,
       ts1.avg_qtFlashAssist,
       ts1.avg_qtHitHeadshot,
       ts1.avg_qtHitChest,
       ts1.avg_qtHitStomach,
       ts1.avg_qtHitLeftAtm,
       ts1.avg_qtHitRightArm,
       ts1.avg_qtHitLeftLeg,
       ts1.avg_qtHitRightLeg,
       ts1.avg_flWinner,
       ts1.qtd_de_ancient,
       ts1.qtd_vitorias_de_ancient,
       ts1.qtd_de_dust2,
       ts1.qtd_vitorias_de_dust2,
       ts1.qtd_de_inferno,
       ts1.qtd_vitorias_de_inferno,
       ts1.qtd_de_mirage,
       ts1.qtd_vitorias_de_mirage,
       ts1.qtd_de_nuke,
       ts1.qtd_vitorias_de_nuke,
       ts1.qtd_de_overpass,
       ts1.qtd_vitorias_de_overpass,
       ts1.qtd_de_train,
       ts1.qtd_vitorias_de_train,
       ts1.qtd_de_vertigo,
       ts1.qtd_vitorias_de_vertigo,
       ts1.qtd_partidas_menos_16rounds,
       ts1.avg_kda,
       ts1.kda_geral,
       ts1.avg_kar,
       ts1.kar_geral,
       ts1.avg_damage_x_round,
       ts1.damage_x_round_geral,
       ts1.avg_hs,
       ts1.avg_hit_stomach,
       ts1.avg_hit_chest,
       ts1.avg_hit_left_arm,
       ts1.avg_hs_hit_lef_leg,
       ts1.avg_hs_hit_right_arm,
       ts1.avg_hs_hit_rigth_leg,
       tm1.qtd_medalhas,
       tm1.qtd_medalhas_adquiridas,
       tm1.qtd_membros_premium,
       tm1.qtd_membros_plus
FROM tb_stats AS ts1
LEFT JOIN tb_book_medals AS tm1 ON ts1.idPlayer = tm1.idPlayer
