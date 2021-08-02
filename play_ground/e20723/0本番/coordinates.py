groundDict = {
    "青": (0, 0),
    "赤": (0, 1),
    "黄": (0, 2),
    "駅": (0, 4),
    "目駅": (0, 5),
    "縦": (0, 6),
    "横": (0, 7),
    "緑": (0, 8),
    "草": (1, 8),
    "木": (0, 9),
    "水": (1, 9)
}

unitsDict = {
    "0k": (0, 0),
    "0h": (1, 0),
    "0j": (2, 0),
    "0l": (3, 0),

    "1k": (0, 1),
    "1h": (1, 1),
    "1j": (2, 1),
    "1l": (3, 1),

    "2k": (0, 2),
    "2h": (1, 2),
    "2j": (2, 2),
    "2l": (3, 2),

    "3k": (0, 2),
    "3h": (1, 2),
    "3j": (2, 2),
    "3l": (3, 2),
}

arrowDict = {
    0: (0, 0),
    1: (1, 0),
    2: (2, 0),
    3: (3, 0)
}

backGroundDict = {
    "黒": (0, 0),
    "オレンジ": (1, 0)
}

letterDict = {
    "0": (0, 0),
    "1": (1, 0),
    "2": (2, 0),
    "3": (3, 0),
    "4": (4, 0),

    "5": (0, 1),
    "6": (1, 1),
    "7": (2, 1),
    "8": (3, 1),
    "9": (4, 1),

    "A": (0, 2),
    "B": (1, 2),
    "C": (2, 2),
    "D": (3, 2),
    "E": (4, 2),

    "F": (0, 3),
    "G": (1, 3),
    "H": (2, 3),
    "I": (3, 3),
    "J": (4, 3),

    "K": (0, 4),
    "L": (1, 4),
    "M": (2, 4),
    "N": (3, 4),
    "O": (4, 4),

    "P": (0, 5),
    "Q": (1, 5),
    "R": (2, 5),
    "S": (3, 5),
    "T": (4, 5),

    "U": (0, 6),
    "V": (1, 6),
    "W": (2, 6),
    "X": (3, 6),
    "Y": (3, 6),

    "Z": (0, 7),

    "あ": (0, 8),
    "い": (1, 8),
    "う": (2, 8),
    "え": (3, 8),
    "お": (4, 8),

    "か": (0, 9),
    "き": (1, 9),
    "く": (2, 9),
    "け": (3, 9),
    "こ": (4, 9),

    "さ": (0, 10),
    "し": (1, 10),
    "す": (2, 10),
    "せ": (3, 10),
    "そ": (4, 10),

    "た": (0, 11),
    "ち": (1, 11),
    "つ": (2, 11),
    "て": (3, 11),
    "と": (4, 11),

    "な": (0, 12),
    "に": (1, 12),
    "ぬ": (2, 12),
    "ね": (3, 12),
    "の": (4, 12),

    "は": (0, 13),
    "ひ": (1, 13),
    "ふ": (2, 13),
    "へ": (3, 13),
    "ほ": (4, 13),

    "ま": (0, 14),
    "み": (1, 14),
    "む": (2, 14),
    "め": (3, 14),
    "も": (4, 14),

    "や": (0, 15),
    "ゆ": (2, 15),
    "よ": (4, 15),

    "ら": (0, 16),
    "り": (1, 16),
    "る": (2, 16),
    "れ": (3, 16),
    "ろ": (4, 16),

    "":(1, 17),

    "わ": (0, 17),
    "を": (2, 17),
    "ん": (4, 17),

    "ア": (0, 18),
    "イ": (1, 18),
    "ウ": (2, 18),
    "エ": (3, 18),
    "オ": (4, 18),

    "カ": (0, 19),
    "キ": (1, 19),
    "ク": (2, 19),
    "ケ": (3, 19),
    "コ": (4, 19),

    "サ": (0, 20),
    "シ": (1, 20),
    "ス": (2, 20),
    "セ": (3, 20),
    "ソ": (4, 20),

    "タ": (0, 21),
    "チ": (1, 21),
    "ツ": (2, 21),
    "テ": (3, 21),
    "ト": (4, 21),

    "ナ": (0, 22),
    "ニ": (1, 22),
    "ヌ": (2, 22),
    "ネ": (3, 22),
    "ノ": (4, 22),

    "ハ": (0, 23),
    "ヒ": (1, 23),
    "フ": (2, 23),
    "ヘ": (3, 23),
    "ホ": (4, 23),

    "マ": (0, 24),
    "ミ": (1, 24),
    "ム": (2, 24),
    "メ": (3, 24),
    "モ": (4, 24),

    "ヤ": (0, 25),
    "ユ": (2, 25),
    "ヨ": (4, 25),

    "ラ": (0, 26),
    "リ": (1, 26),
    "ル": (2, 26),
    "レ": (3, 26),
    "ロ": (4, 26),

    "ワ": (0, 27),
    "ヲ": (2, 27),
    "ン": (4, 27),

    "!": (0, 28),
    "?": (1, 28),
    "円": (2, 28),

    "っ": (0, 29),

    "ゃ": (1, 29),
    "ゅ": (2, 29),
    "ょ": (3, 29),

    "ッ": (4, 29),

    "ャ": (0, 30),
    "ュ": (1, 30),
    "ョ": (2, 30),

    "兆": (3, 30),
    "億": (4, 30),
    "万": (0, 31),

    "。": (1, 31),
    "、": (2, 31),


    "年": (3, 31),
    "目": (4, 31),
    "月": (0, 32),

    "が": (1, 32),
    "ぎ": (2, 32),
    "ぐ": (3, 32),
    "げ": (4, 32),
    "ご": (0, 33),

    "だ": (1, 33),
    "ぢ": (2, 33),
    "づ": (3, 33),
    "で": (4, 33),
    "ど": (0, 34),

    "ば": (1, 34),
    "び": (2, 34),
    "ぶ": (3, 34),
    "べ": (4, 34),
    "ぼ": (0, 35),

    "ぱ": (1, 35),
    "ぴ": (2, 35),
    "ぷ": (3, 35),
    "ぺ": (4, 35),
    "ぽ": (0, 36),

    "ガ": (1, 36),
    "ギ": (2, 36),
    "グ": (3, 36),
    "ゲ": (4, 36),
    "ゴ": (0, 37),

    "ダ": (1, 37),
    "ヂ": (2, 37),
    "ヅ": (3, 37),
    "デ": (4, 37),
    "ド": (0, 38),

    "バ": (1, 38),
    "ビ": (2, 38),
    "ブ": (3, 38),
    "ベ": (4, 38),
    "ボ": (0, 39),

    "パ": (1, 39),
    "ピ": (2, 39),
    "プ": (3, 39),
    "ペ": (4, 39),
    "ポ": (0, 40),

    "ー": (1, 40)
}
