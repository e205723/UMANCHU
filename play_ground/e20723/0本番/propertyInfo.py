from gameObjects import Property

propertyInfo = [
["せんばるりょう", [52, 5], [Property("いっぱんとう", 2000, 100), Property("こんじゅうがたとう", 3000, 80), Property("しんこんじゅうがたとう", 5000, 50)]],
["ZEHじっけんとう", [49, 8], [Property("たいようこうパネル", 1000, 50), Property("コンクリートパネル", 1000, 50), Property("CTLのやね", 1000, 50)]],
["かがいかつどうきょうようしせつ", [55, 8], [Property("サークルかいかん", 5000, 50), Property("プレハブとう", 2000, 50), ]],
["ちそうそうごうけんきゅうとう", [49, 11], [Property("さんがくかんれんけいすいしんきこうフロア", 10000000, 1), Property("とうしょぼうさいけんきゅうセンターフロア", 10000000, 1), Property("こうがくぶフロア", 30000000, 3)]],
["さんがくかんれんけいとう", [52, 11], [Property("かきくけんきゅうじょ", 5000, 100), Property("さしすせソリューション", 10000, 25), ]],
["こうがくぶ1ごうかん", [55, 11], [Property("けんきゅうしつ", 100000000, 1), Property("しょうめいしょじどうはっこうき", 1000, 100), Property("321きょうしつ", 1000000000, 1)]],
["あねったいフィールド", [34, 14], [Property("ビニールハウス", 5000, 200), Property("はたけ", 5000, 200), Property("のうじょうきかいとうせいびしせつ", 10000, 10)]],
["のうがくぶ", [43, 14], [Property("けんきゅうしつ", 100000000, 1), Property("がくせいサポートルーム", 5000, 100), Property("コンピューターしつ", 10000, 50)]],
["あねったいせいぶつ", [40, 17], [Property("けんきゅうしつ", 100000000, 1), Property("じっけんしつ", 100000, 5), Property("ばいようしつ", 50000, 10)]],
["はくぶつかん", [43, 17], [Property("せいぶつひょうほん", 10000, 25), Property("こしりょう", 1000, 100), Property("のうぐ", 5000, 50)]],
["せいきょうきたしょくどうばいてん", [49, 17], [Property("しょくどう", 3000, 25), Property("てづくりパン", 1000, 100), Property("じかせいべんとう", 5000, 100)]],
["こうがくぶ2ごうかん", [55, 17], [Property("けんきゅうしつ", 100000000, 1), Property("こうエネルギーかこうじっけんしつ", 100000, 5), Property("みずこうがくじっけんしつ", 100000, 5)]],
["ちくさんしせつ", [31, 20], [Property("ぎゅうしゃ", 5000, 200), Property("けいしゃ", 5000, 200), Property("とんしゃ", 5000, 200)]],
["えんげいようガラスしつ", [34, 20], [Property("ガラスしつ1", 2000, 100), Property("ガラスしつ2", 2000, 100), Property("ガラスしつ3", 2000, 100)]],
["あねったいけんきゅうとう", [49, 20], [Property("けんきゅうきかくしつ", 10000, 50), Property("せんりゃくてきけんきゅうプロジェクトセンター", 10000, 50), Property("じっけんしつ", 100000, 5)]],
["きゅうどうじょう", [61, 20], [Property("しゃじょう", 5000, 50), Property("やみち", 1000, 50), Property("まとば", 5000, 50)]],
["かんきょうあんぜんしせつ", [31, 23], [Property("じっけんけいはいきぶつ", 100000, 5), Property("はいえきタンク", 10000, 50)]],
["きょくていおんしせつ", [49, 23], [Property("えきたいちっそ", 500000, 1), Property("えきたいヘリウム", 500000, 1)]],
["こうがくぶ3ごうかん", [52, 23], [Property("けんきゅうしつ", 100000000, 1), Property("じしゅうしつ1", 5000, 100), Property("じしゅうしつ2", 5000, 100)]],
["こうがくぶ4ごうかん", [55, 23], [Property("けんきゅうしつ", 100000000, 1), Property("ちゅうこうぎしつ", 2500, 50), Property("だいこうぎしつ", 5000, 50)]],
["テニスコート", [61, 23], [Property("テニスコート3めん", 3000, 50), Property("テニスコート3めん", 3000, 50), Property("テニスコート4めん", 4000, 50)]],
["やきゅうじょう", [64, 23], [Property("しょうめいせつび", 3000, 100), Property("ブルペン", 1000, 50), Property("やきゅうじょう1めん", 10000, 50)]],
["そうごうじょうほうしょりセンター", [52, 26], [Property("コミュニケーションルーム", 5000, 100), Property("かしだしiPad", 5000, 200), Property("がくせいじょうほう", 100000000, 1)]],
["RIしせつ", [55, 26], [Property("じっけんしつ", 100000, 5), Property("そくていしつ", 50000, 10), Property("おせんけんさしつ", 50000, 10)]],
["だい1たいいくかん", [61, 26], [Property("フロア3めん", 30000, 25), Property("ぶどうじょう", 3000, 100), Property("トレーニングルーム", 5000, 100)]],
["400Mトラック", [64, 26], [Property("しょうめいせつび", 3000, 100), Property("すもうじょう", 2000, 50), Property("400Mトラック", 4000, 50)]],
["いがくぶたいいくかん", [19, 29], [Property("フロア1めん", 10000, 50), Property("フロア1めん", 10000, 50)]],
["ほけんかんりセンター", [61, 29], [Property("けんこうしんだん", 1000, 100), Property("おうきゅうしょち", 1000, 200), Property("カウンセリング", 1000, 500)]],
["ぜんほれんステーション", [46, 32], [Property("にゅうしか", 50000, 10), Property("キャリアきょういくセンター", 50000, 10), Property("とくべつかいぎしつ", 10000, 50)]],
["りけいふくごうとう", [49, 32], [Property("けんきゅうしつ", 100000000, 1), Property("げんそぶんせきしつ", 100000, 5), Property("ほうしゃせんそくていしつ", 100000, 5)]],
["だい2たいいくかん", [61, 32], [Property("フロア1めん", 10000, 50), Property("フロア1めん", 10000, 50)]],
["プール", [64, 32], [Property("50M2コース", 5000, 50), Property("50M2コース", 5000, 50), Property("50M3コース", 7500, 50)]],
["シミュレーションセンター", [13, 35], [Property("シミュレーションきょういくのかいはつ", 100000, 10), Property("シミュレーションきょういくのじっせん", 100000, 100), Property("シミュレーションきょういくのけんきゅう", 300000, 20)]],
["さいせいいりょうセンター", [25, 35], [Property("けんきゅうしつ", 100000000, 1), Property("さいせいいりょうけんきゅうきかくぶ", 1000000, 5)]],
["ちゅうおうしょくどうばいてん", [46, 35], [Property("しょくどう", 30000, 25), Property("てづくりパンとべんとう", 6000, 200), Property("しょてん", 10000, 50)]],
["りがくぶ", [49, 35], [Property("Aとう", 100000, 5), Property("Bとう", 100000, 5), Property("Cとう", 100000, 5)]],
["がじゅまるかいかん", [19, 38], [Property("しょうめいしょじどうはっこうき", 1000, 100), Property("だんわしつ", 3000, 80), Property("がくせいじしゅうしつ", 5000, 100)]],
["ほけんがっかとう", [22, 38], [Property("けんきゅうしつ", 100000000, 1), Property("かんごがくコース", 100000, 5), Property("けんさぎじゅつがくコース", 100000, 5)]],
["かんりとう", [25, 38], [Property("かんりいんしつ", 5000, 100), Property("しゅうかいしつ", 5000, 100), Property("システムしつ", 10000, 50)]],
["だいがくほんぶとう", [43, 38], [Property("じむしえんセンター", 30000, 25), Property("こうほうしつ", 10000, 50), Property("かんさしつ", 50000, 10)]],
["ふぞくとしょかん", [46, 38], [Property("やく86まんさつのぞうしょ", 1000000, 20), Property("えつらんしつ", 5000, 100), Property("スタディルーム", 5000, 100)]],
["きょうつう1ごうかん", [49, 38], [Property("こくさいきょういくか", 10000, 50), Property("がくせいしえんか", 10000, 50), Property("きょういくしえんか", 10000, 50)]],
["かいぼうほういとう", [13, 41], [Property("けんきゅうしつ", 100000000, 1), Property("かいぼうしつ", 10000, 80), Property("こうぎしつ", 5000, 200)]],
["きそこうぎじっしゅうしつ", [16, 41], [Property("こうぎしつ1", 5000, 200), Property("こうぎしつ2", 5000, 200), Property("じっしゅうしつ", 10000, 50)]],
["ふぞくとしょかんいがくぶぶんかん", [22, 41], [Property("やく10まんさつのぞうしょ", 100000, 20), Property("しちょうかくしつ", 5000, 100), Property("ゼミしつ", 10000, 50)]],
["ぎじゅつきょういくとう", [40, 41], [Property("きんぞくかこうじっけんしつ", 100000, 20), Property("ざいりょうしけんしつ", 100000, 20), Property("きかいじっしゅうしつ", 100000, 20)]],
["ぶんけいそうごうけんきゅうとう", [43, 41], [Property("けんきゅうしつ", 100000000, 1), Property("こうぎしつ", 5000, 200), Property("しりょうしつ", 7500, 80)]],
["きょうつう4ごうかん", [49, 41], [Property("こうぎしつ", 5000, 200), Property("ごがくラボしつ", 2500, 100), Property("がいこくごセンター", 10000, 50)]],
["きょうつう2ごうかん", [52, 41], [Property("こうぎしつ", 5000, 200), Property("だいこうぎしつ", 10000, 100), Property("パソコンじしゅうしつ", 10000, 100)]],
["サッカーラグビーじょう", [64, 41], [Property("しょうめいせつび", 3000, 100), Property("サッカーコート", 10000, 50), Property("ラグビーコート", 10000, 50)]],
["きそけんきゅうとう", [16, 44], [Property("けんきゅうしつ", 100000000, 1), Property("こうぎしつ", 5000, 200), Property("じっけんしつ", 100000, 20)]],
["りゅうきゅうだいがくびょういん", [28, 44], [Property("りゅうきゅうだいがくびょういん", 500000000, 10)]],
["おんがくとう", [40, 44], [Property("けんきゅうしつ", 100000000, 1), Property("MLしつ", 10000, 50), Property("くうちょうきかいしつ", 50000, 10)]],
["きょういくじっせんとう", [43, 44], [Property("きょういくじっせんしどうA", 5000, 100), Property("きょういくじっせんしどう5", 5000, 100)]],
["きょうつう3ごうかん", [52, 44], [Property("こうぎしつ1", 5000, 200), Property("こうぎしつ2", 5000, 200), Property("ごがくラボしつ", 2500, 100)]],
["きそけんきゅうとう", [16, 47], [Property("けんきゅうしつ", 100000000, 1), Property("こうぎしつ", 5000, 200), Property("じっけんしつ", 100000, 20)]],
["りんしょうこうぎとう", [25, 47], [Property("こうぎしつ1", 5000, 200), Property("こうぎしつ2", 5000, 200), Property("こうぎしつ3", 5000, 200)]],
["ちりょうしせつ", [28, 47], [Property("ちりょうそうち", 1000000, 10), Property("しんりょうしつ", 10000, 100)]],
["ぶんけいこうぎとう", [46, 47], [Property("こうぎしつ1", 5000, 200), Property("こうぎしつ2", 5000, 200), Property("こうぎしつ3", 5000, 200)]],
["RIじっけんしせつとう", [16, 50], [Property("えきたいシンチレーションカウンタ", 500000, 20), Property("ほうしゃせんちゅうおうかんしそうち", 300000, 20), Property("ベータせんそくていしつ", 100000, 10)]],
["りんしょうけんきゅうとう", [19, 50], [Property("けんきゅうしつ", 100000000, 1), Property("こうぎしつ", 5000, 200), Property("じっけんしつ", 100000, 20)]],
["ちゅうおうせつびきしつ", [25, 50], [Property("ようぐしつ", 10000, 50), Property("かんりいんしつ", 5000, 100), Property("せいびきしつ", 100000, 10)]],
["リニアックしんりょうしせつとう", [28, 50], [Property("こうエネルギーほうしゃせんちりょうそうち", 1000000, 10), Property("しんりょうしつ", 1000, 100)]],
["きゅうきゅうさいがいいりょうとう", [31, 50], [Property("しょりょうしつ", 5000, 100), Property("かんさつしつ", 5000, 100), Property("カンファレンスしつ", 5000, 200)]],
["ふぞくどうぶつじっけんしせつとう", [19, 53], [Property("しいくそうち", 100000, 20), Property("マイクロマニュピレーター", 1000000, 10), Property("オートクレープ", 500000, 20)]],
["けんしゅうきょういくセンター", [28, 53], [Property("りんしょうけんしゅうセンター", 50000, 10), Property("キャリアけいせいしえんセンター", 10000, 100), Property("しかいしりんしょうけんしゅうしえんしつ", 100000, 10)]],
["ふぞくしょうがっこう", [40, 53], [Property("グラウンド", 10000, 100), Property("たいいくかん", 5000, 50), Property("こうしゃ", 10000, 100)]],
["ふぞくちゅうがっこう", [43, 53], [Property("グラウンド", 10000, 100), Property("たいいくかん", 5000, 50), Property("こうしゃ", 10000, 100)]]
]
