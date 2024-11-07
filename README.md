# RiotApp

## backend

API キーは 24 時間で有効期限が消える
ホストのポートは 8005 番にフォワード
コンテナ内で

```
export RIOT_API_KEY={生成されたKEY}
```

```
pip3 install -r requirements.txt
```

### envfile

.docker.local.env

- RIOT_API_KEY="RIOT_API_KEY"

サーバー起動
gunicorn -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:8000" --log-level debug main:app --reload

## frontend

npx create-react-app で作成
ホストのポートは 3005 番にフォワード

## RiotAPI

### MatchV5

["info"]["gameDuration"]は["info"]["gameEndTimestamp"]があれば秒として扱いなければミリ秒として扱う

ユーザーごとにとれる試合のデータ

```json
{
  "allInPings": 0, //オールインのピンの数
  "assistMePings": 3, //アシストピンの数
  "assists": 4, //アシスト数
  "baronKills": 0, //バロンのキル数
  "basicPings": 0, //べーシックピン？の数
  "bountyLevel": 3, //賞金レベル？
  "challenges": { //チャレンジ
    "12AssistStreakCount": 0,
    "HealFromMapSources": 0,
    "InfernalScalePickup": 0,
    "SWARM_DefeatAatrox": 0,
    "SWARM_DefeatBriar": 0,
    "SWARM_DefeatMiniBosses": 0,
    "SWARM_EvolveWeapon": 0,
    "SWARM_Have3Passives": 0,
    "SWARM_KillEnemy": 0,
    "SWARM_PickupGold": 0,
    "SWARM_ReachLevel50": 0,
    "SWARM_Survive15Min": 0,
    "SWARM_WinWith5EvolvedWeapons": 0,
    "abilityUses": 466,
    "acesBefore15Minutes": 0,
    "alliedJungleMonsterKills": 0,
    "baronBuffGoldAdvantageOverThreshold": 1,
    "baronTakedowns": 1,
    "blastConeOppositeOpponentCount": 0,
    "bountyGold": 0,
    "buffsStolen": 0,
    "completeSupportQuestInTime": 0,
    "controlWardTimeCoverageInRiverOrEnemyHalf": 0.7798394520081874,
    "controlWardsPlaced": 7,
    "damagePerMinute": 634.0355183740703,
    "damageTakenOnTeamPercentage": 0.1326297976263452,
    "dancedWithRiftHerald": 0,
    "deathsByEnemyChamps": 1,
    "dodgeSkillShotsSmallWindow": 0,
    "doubleAces": 0,
    "dragonTakedowns": 3,
    "earliestBaron": 1588.936843382,
    "earliestDragonTakedown": 839.161298824,
    "earlyLaningPhaseGoldExpAdvantage": 0,
    "effectiveHealAndShielding": 0,
    "elderDragonKillsWithOpposingSoul": 0,
    "elderDragonMultikills": 0,
    "enemyChampionImmobilizations": 7,
    "enemyJungleMonsterKills": 0,
    "epicMonsterKillsNearEnemyJungler": 0,
    "epicMonsterKillsWithin30SecondsOfSpawn": 0,
    "epicMonsterSteals": 0,
    "epicMonsterStolenWithoutSmite": 0,
    "firstTurretKilled": 1,
    "firstTurretKilledTime": 759.264970608,
    "fistBumpParticipation": 0,
    "flawlessAces": 0,
    "fullTeamTakedown": 0,
    "gameLength": 1744.8609060570002,
    "getTakedownsInAllLanesEarlyJungleAsLaner": 0,
    "goldPerMinute": 434.7370503634689,
    "hadOpenNexus": 0,
    "immobilizeAndKillWithAlly": 2,
    "initialBuffCount": 0,
    "initialCrabCount": 0,
    "jungleCsBefore10Minutes": 0,
    "junglerTakedownsNearDamagedEpicMonster": 1,
    "kTurretsDestroyedBeforePlatesFall": 0,
    "kda": 7,
    "killAfterHiddenWithAlly": 0,
    "killParticipation": 0.30434782608695654,
    "killedChampTookFullTeamDamageSurvived": 0,
    "killingSprees": 1,
    "killsNearEnemyTurret": 1,
    "killsOnOtherLanesEarlyJungleAsLaner": 0,
    "killsOnRecentlyHealedByAramPack": 0,
    "killsUnderOwnTurret": 0,
    "killsWithHelpFromEpicMonster": 1,
    "knockEnemyIntoTeamAndKill": 0,
    "landSkillShotsEarlyGame": 4,
    "laneMinionsFirst10Minutes": 84,
    "laningPhaseGoldExpAdvantage": 0,
    "legendaryCount": 0,
    "legendaryItemUsed": [6657, 3003, 3040],
    "lostAnInhibitor": 0,
    "maxCsAdvantageOnLaneOpponent": 34,
    "maxKillDeficit": 2,
    "maxLevelLeadLaneOpponent": 1,
    "mejaisFullStackInTime": 0,
    "moreEnemyJungleThanOpponent": 0,
    "multiKillOneSpell": 0,
    "multiTurretRiftHeraldCount": 0,
    "multikills": 0,
    "multikillsAfterAggressiveFlash": 0,
    "outerTurretExecutesBefore10Minutes": 0,
    "outnumberedKills": 1,
    "outnumberedNexusKill": 0,
    "perfectDragonSoulsTaken": 0,
    "perfectGame": 0,
    "pickKillWithAlly": 6,
    "playedChampSelectPosition": 1,
    "poroExplosions": 0,
    "quickCleanse": 0,
    "quickFirstTurret": 0,
    "quickSoloKills": 0,
    "riftHeraldTakedowns": 0,
    "saveAllyFromDeath": 0,
    "scuttleCrabKills": 0,
    "skillshotsDodged": 4,
    "skillshotsHit": 30,
    "snowballsHit": 0,
    "soloBaronKills": 0,
    "soloKills": 0,
    "stealthWardsPlaced": 5,
    "survivedSingleDigitHpCount": 0,
    "survivedThreeImmobilizesInFight": 4,
    "takedownOnFirstTurret": 0,
    "takedowns": 7,
    "takedownsAfterGainingLevelAdvantage": 0,
    "takedownsBeforeJungleMinionSpawn": 0,
    "takedownsFirstXMinutes": 3,
    "takedownsInAlcove": 0,
    "takedownsInEnemyFountain": 0,
    "teamBaronKills": 1,
    "teamDamagePercentage": 0.1772918443763536,
    "teamElderDragonKills": 0,
    "teamRiftHeraldKills": 0,
    "tookLargeDamageSurvived": 0,
    "turretPlatesTaken": 2,
    "turretTakedowns": 3,
    "turretsTakenWithRiftHerald": 0,
    "twentyMinionsIn3SecondsCount": 0,
    "twoWardsOneSweeperCount": 0,
    "unseenRecalls": 0,
    "visionScoreAdvantageLaneOpponent": 0.4300612211227417,
    "visionScorePerMinute": 0.992800059744817,
    "voidMonsterKill": 4,
    "wardTakedowns": 5,
    "wardTakedownsBefore20M": 2,
    "wardsGuarded": 0
  },
  "champExperience": 18060, //経験値？
  "champLevel": 17, //チャンピオンレベル
  "championId": 13, //チャンピオンID
  "championName": "Ryze", //チャンピオン名
  "championTransform": 0, //このフィールドは現在、ケインの変身にのみ使用されています。（有効な値: 0 - なし、1 - スレイヤー、2 - アサシン）
  "commandPings": 5, //コマンドピン？
  "consumablesPurchased": 10, //試合中に購入された消耗品アイテムの数を表します。これには、ポーションやワードなど、使用後に消費されるアイテムが含まれます。
  "damageDealtToBuildings": 6667, //試合中にプレイヤーが建物（タワー、インヒビターなど）に与えた総ダメージ量を表します。
  "damageDealtToObjectives": 19338, //試合中にプレイヤーがゲーム内の目標（オブジェクト）に与えた総ダメージ量を表します。対象となるオブジェクト:タワー, インヒビター, エピックモンスター（ドラゴン、バロン、リフトヘラルドなど）, ジャングルモンスター（青バフ、赤バフなど）, ネクサス
  "damageDealtToTurrets": 6667, //試合中にプレイヤーがタレット（タワー）に与えた総ダメージ量を表します。
  "damageSelfMitigated": 12546, //試合中にプレイヤーが自分で軽減したダメージの総量を表します。軽減ダメージの要素:防御力（Armor）や魔法防御力（Magic Resist） によるダメージ軽減, シールド効果（アイテムやスキルによるもの）, ダメージ軽減スキル（例: モルデカイザーのパッシブやマルファイトのスキルなど）
  "dangerPings": 0, //危険ピンの数
  "deaths": 1, //デス数
  "detectorWardsPlaced": 7, //試合中にプレイヤーが設置した コントロールワード（旧称: ピンクワード）の数を表します。
  "doubleKills": 0, //ダブルキルの数
  "dragonKills": 0, //ドラゴンのキル数
  "eligibleForProgression": true, //プレイヤーが試合後に進行状況（例: ランクポイント、イベントミッション、経験値など）を獲得できるかどうかを示すブール値 (true または false) です。
  /*
  主な用途:
    true: プレイヤーが試合結果に基づいて進行状況の報酬を受け取れることを意味します。
    false: プレイヤーが試合結果に基づく進行状況の報酬を受け取れないことを意味します（例: カスタムゲームや無効試合など）。
    想定される状況:
    通常の試合
    プレイヤーが公式モード（ランク、ノーマル、イベントモードなど）でプレイした場合、eligibleForProgression は通常 true になります。

    カスタムゲームや非公式試合
    カスタムマッチなど、進行状況に影響を与えないモードの場合、eligibleForProgression は false になります。

    試合の途中退出や不正行為
    ペナルティが発生する条件（AFKや不正行為）が発生した場合、eligibleForProgression が false になることがあります。
  */
  "enemyMissingPings": 5, //ハテナピンの数
  "enemyVisionPings": 5, //ワードピンの数
  "firstBloodAssist": false,　//ファーストブラッドのアシストをしたか
  "firstBloodKill": false, //ファーストブラッドをとったか
  "firstTowerAssist": false, //ファーストタワーのアシストをしたか
  "firstTowerKill": false, //ファーストタワーを壊したか
  "gameEndedInEarlySurrender": false, //試合が早期サレンダー(10分以上15分未満)によって終了したかどうかを示すブール値 (true または false) です。
  "gameEndedInSurrender": false, //、試合がサレンダーによって終了したかどうかを示すブール値 (true または false) です。
  "getBackPings": 0, //プレイヤーが試合中に使用した「戻れピン（Back Ping）」の回数を表します。
  "goldEarned": 12642, //獲得したゴールド量
  "goldSpent": 10050, //試合中にプレイヤーがアイテム購入に費やしたゴールドの総量を表します。
  "holdPings": 0, //プレイヤーが試合中に使用した「ホールドピン（Hold Ping）」の回数を表します。その場を維持する指示を出すとき。
  "individualPosition": "MIDDLE", //ポジション
  "inhibitorKills": 0, //インヒビターの破壊数(ラストヒット)
  "inhibitorTakedowns": 1, //試合中にプレイヤーが破壊した インヒビター の数を表します。
  "inhibitorsLost": 0, //インヒビターを失った数
  "item0": 3040, //アイテムスロットに何があるか。アイテム一覧を別途参照。
  "item1": 1058,
  "item2": 2055,
  "item3": 3111,
  "item4": 1058,
  "item5": 6657,
  "item6": 3363, //トリンケット
  "itemsPurchased": 25, //試合中にプレイヤーが購入したアイテムの総数を表します。
  "killingSprees": 1, //キリングスプリーの数
  "kills": 3, //　キル数
  "lane": "MIDDLE", //レーン
  "largestCriticalStrike": 0, //試合中にプレイヤーが一度のクリティカルヒットで与えた最大ダメージを表します。
  "largestKillingSpree": 3, //最大キリングスプリー
  "largestMultiKill": 1, //最大マルチキル数
  "longestTimeSpentLiving": 1294, //試合中にプレイヤーが一度も死亡せずに生存し続けた最長時間を表します。この値は秒単位で記録されます。
  "magicDamageDealt": 197371, //魔法ダメージ
  "magicDamageDealtToChampions": 17681, //チャンピオンに対する魔法ダメージ
  "magicDamageTaken": 6180, //受けた魔法ダメージ
  "missions": {
    "playerScore0": 0,
    "playerScore1": 0,
    "playerScore2": 0,
    "playerScore3": 0,
    "playerScore4": 0,
    "playerScore5": 0,
    "playerScore6": 0,
    "playerScore7": 0,
    "playerScore8": 0,
    "playerScore9": 0,
    "playerScore10": 0,
    "playerScore11": 0
  },
  "needVisionPings": 0, //視界が必要ピンの数
  "neutralMinionsKilled": 0, //試合中にプレイヤーが倒した中立モンスター（Neutral Minions）の数を表します。中立モンスターは、ジャングル内に存在する敵・味方どちらにも属さないモンスターのことです。
  "nexusKills": 0, //ネクサスキル(ラストヒット)
  "nexusLost": 0, //ネクサスロスト
  "nexusTakedowns": 1, //ネクサス破壊に関与
  "objectivesStolen": 0, //オブジェクトのスティール数
  "objectivesStolenAssists": 0, //オブジェクトのスティールにアシストした回数
  "onMyWayPings": 10, //向かうピン数
  "participantId": 8, //試合における参加者ID
  "pentaKills": 0, //ペンタキル数
  "perks": {
    "statPerks": { //シャード
      "defense": 5001,
      "flex": 5008,
      "offense": 5005
    },
    /*
    statPerks には、3つのカテゴリーでプレイヤーの基本ステータスに影響を与える補正値が含まれています。

    defense（防御ステータス）

    プレイヤーが防御関連のルーンを選択した際の補正値を表します。
    選択肢:
    5001: Armor（防御力）
    5002: Magic Resist（魔法防御力）
    5003: Health Scaling（成長体力）
    flex（フレックスステータス）

    攻撃や防御、魔力など、柔軟な補正を提供する選択肢を表します。
    選択肢:
    5008: Adaptive Force（適応型ステータス: 攻撃力または魔力）
    5002: Magic Resist（魔法防御力）
    5003: Health Scaling（成長体力）
    offense（攻撃ステータス）

    攻撃関連のルーンを選択した際の補正値を表します。
    選択肢:
    5005: Attack Speed（攻撃速度）
    5007: Ability Haste（スキルヘイスト）
    5008: Adaptive Force（適応型ステータス: 攻撃力または魔力）
    */
    "styles": [ //ルーン
      {
        "description": "primaryStyle",
        "selections": [
          {
            "perk": 8230,
            "var1": 12,
            "var2": 0,
            "var3": 0
          },
          {
            "perk": 8226,
            "var1": 250,
            "var2": 906,
            "var3": 0
          },
          {
            "perk": 8210,
            "var1": 2,
            "var2": 0,
            "var3": 0
          },
          {
            "perk": 8236,
            "var1": 24,
            "var2": 0,
            "var3": 0
          }
        ],
        "style": 8200
      },
      {
        "description": "subStyle",
        "selections": [
          {
            "perk": 8451,
            "var1": 250,
            "var2": 0,
            "var3": 0
          },
          {
            "perk": 8473,
            "var1": 400,
            "var2": 0,
            "var3": 0
          }
        ],
        "style": 8400
      }
    ]
  },
  /*
  メインルーン（Primary Style）: 魔道（Sorcery）
    ルーン系統ID 8200（魔道）を選択。

    perk: 8230 – ウォーターワーキング（Waterwalking）

    効果: 川にいる間、移動速度とアダプティブダメージが増加。
    var1: 12 → 川で得た移動速度のボーナス。
    perk: 8226 – マナフローバンド（Manaflow Band）

    効果: 敵にスキルを命中させると最大マナが増加。
    var1: 250 → 獲得した最大マナ。
    var2: 906 → 試合全体で使用したスキル回数。
    perk: 8210 – 追い風（Celerity）

    効果: ボーナス移動速度を強化。
    var1: 2 → 増加した移動速度の割合。
    perk: 8236 – ガーディアンのオーブ（Gathering Storm）

    効果: 時間経過でアダプティブフォースを増加。
    var1: 24 → 獲得した追加アダプティブフォース。
  */
  "physicalDamageDealt": 14417, //物理ダメージ量
  "physicalDamageDealtToChampions": 756, //チャンピオンに対する物理ダメージ量
  "physicalDamageTaken": 7949,//受けた物理ダメージ量
  "placement": 0, //通常、試合中の順位や位置を表す数値を指します。このフィールドは特に**チームファイトタクティクス（TFT）**などのモードで使用され、プレイヤーがその試合で何位だったかを示します。
  "playerAugment1": 0, //プレイヤーが試合中に選択した**最初のオーグメント（Augment）を表すフィールドです。オーグメントは主にチームファイトタクティクス（TFT）**で使用されるシステムで、試合中のプレイスタイルや戦術を強化する追加効果を提供します。
  "playerAugment2": 0,
  "playerAugment3": 0,
  "playerAugment4": 0,
  "playerAugment5": 0,
  "playerAugment6": 0,
  "playerSubteamId": 0,
  "profileIcon": 6696, //プレイヤーが使用しているプロフィールアイコンのIDを表します。プロフィールアイコンは、プレイヤーのアカウントの見た目をカスタマイズするために使用される画像で、サモナーズリフトやロビー画面で表示されます。
  "pushPings": 0, //プッシュピンの数
  "puuid": "QCCbUgKwomSanKMUNZQq5ui14SUmVUbFVeq6VLejUgVDFAuaOMnHbD9i2iMQzA0CFYpJyhboFRBE7g",
  "quadraKills": 0, //クアドラキル数
  "retreatPings": 6, //試合中にプレイヤーが使用した**「撤退ピン（Retreat Ping）」**の回数を表します。
  "riotIdGameName": "Mattya",
  "riotIdTagline": "JP2",
  "role": "SOLO", //midやtopだとソロレーン
  "sightWardsBoughtInGame": 0, //sightWardsBoughtInGame は、試合中に購入したサイツワード（Sight Wards）の数を表します。現在はコントロールワードに該当する。
  "spell1Casts": 203, //Qスキル使用回数
  "spell2Casts": 46, //Wスキル使用回数
  "spell3Casts": 212, //Eスキル使用回数
  "spell4Casts": 5, //Rスキル使用回数
  "subteamPlacement": 0, //試合中におけるチーム内での順位や、特定のサブグループにおけるプレイヤーの順位を表すフィールドです。このフィールドは特に、チームファイトタクティクス（TFT） や他の特殊なモードで使用される場合があります。
  "summoner1Casts": 3,//試合中にプレイヤーが使用した1番目のサモナースペル（Summoner Spell） の総使用回数を表します。
   /*
   一般的なサモナースペルとID
    サモナースペル	ID	説明
    フラッシュ	4	短距離の瞬間移動
    イグナイト	14	敵に継続ダメージを与え、回復を妨害
    ヒール	7	自身と味方の体力を回復
    バリア	21	一時的なシールドを生成
    スマイト	11	中立モンスターやミニオンに高ダメージ 
   */
  "summoner1Id": 12,
  "summoner2Casts": 1,
  "summoner2Id": 4,
  "summonerId": "cA9GsDIF7hjXIri7LoNeqfF1RtryOah2-k4W-BIwci8sNA", //サモナーID
  "summonerLevel": 754, //サモナーレベル
  "summonerName": "Mattya",
  "teamEarlySurrendered": false, //試合中にプレイヤーのチームが早期サレンダー（Early Surrender）を行ったかどうかを示すブール値 (true または false) です。
  "teamId": 200, //チームID 100だとブルー、200だとレッド
  "teamPosition": "MIDDLE",
  "timeCCingOthers": 14,//試合中にプレイヤーが敵チャンピオンに対して与えたCC（クラウドコントロール）効果の総時間を秒単位で表します。
  "timePlayed": 1744, //プレイ時間
  "totalAllyJungleMinionsKilled": 0,// レイヤーが試合中に味方側のジャングル内で倒した中立モンスター（ジャングルミニオン）の総数を表します。
  "totalDamageDealt": 213497,
  "totalDamageDealtToChampions": 18438,
  "totalDamageShieldedOnTeammates": 0,
  "totalDamageTaken": 14542,
  "totalEnemyJungleMinionsKilled": 0,
  "totalHeal": 3880,
  "totalHealsOnTeammates": 0,
  "totalMinionsKilled": 267,
  "totalTimeCCDealt": 51,
  "totalTimeSpentDead": 44,
  "totalUnitsHealed": 1,
  "tripleKills": 0,
  "trueDamageDealt": 1708,
  "trueDamageDealtToChampions": 0,
  "trueDamageTaken": 411,
  "turretKills": 2,
  "turretTakedowns": 3,
  "turretsLost": 3,
  "unrealKills": 0,
  "visionClearedPings": 0,
  "visionScore": 28,
  "visionWardsBoughtInGame": 8,
  "wardsKilled": 5,
  "wardsPlaced": 16,
  "win": true
}
```
