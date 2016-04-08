# Learn_Python

Common parameters present in every configuration
________________________________________________
TURN_RADIO_ON - valid values are ["1" or "0"]
PROTOCOL      - valid values are ["802.11b/bg/ng" or "802.11a/na"]
SSID_NAME     - any string
WIRELESSMODE  - valid values are depends on the PROTOCOL vlaues (params are defined in below section)
BROADCAST     - valid values are ["1" or "0"]

Configuration Parameters for protocol "802.11b/bg/ng"
_____________________________________________________
WIRELESSMODE  - valid values are ["11b", "11bg" and "11ng" ]

Configuration Parameters for protocol "802.11a/an"
__________________________________________________
WIRELESSMODE  - valid values are ["11a" and "11na" ]

Parameters for "11ng"
_____________________
CHANNEL =	"Auto"
			"1/2.412GHz""
			"2/2.417GHz"
			"3/2.422GHz"
			"4/2.427GHz"
			"5/2.432GHz"
			"6/2.437GHz"
			"7/2.442GHz"
			"8/2.447GHz"
			"9/2.452GHz"
			"10/2.457GHz"
			"11/2.462GHz"

MSCRATE =	"Best"
			"0 / 7.2 Mbps"
			"1 / 14.4 Mbps"
			"2 / 21.7 Mbps"
			"3 / 28.9 Mbps"
			"4 / 43.3 Mbps"
			"5 / 57.8 Mbps"
			"6 / 65 Mbps"
			"7 / 72.2 Mbps"
			"8 / 14.44 Mbps"
			"9 / 28.88 Mbps"
			"10 / 43.33 Mbps"
			"11 / 57.77 Mbps"
			"12 / 86.66 Mbps"
			"13 / 115.56 Mbps"
			"14 / 130 Mbps"
			"15 / 144.44 Mbps"

CHANNELWIDHT =	"Dynamic 20/40 MHz"
				"20 MHz"
				"40 MHz"

GUARDINTERVAL =	"Long - 800 ns"
				"Auto"

TXPOWER =	"Quarter"
			"Half"
			"Full"
			"Eighth"
			"Minimum"


Parameters for "11na"
_____________________
CHANNEL =	"Auto"
			"36/5.180GHz"
			"40/5.200GHz"
			"44/5.220GHz"
			"48/5.240GHz"
			"149/5.745GHz"
			"153/5.765GHz"
			"157/5.785GHz"
			"161/5.805GHz"

MSCRATE =	"Best"
			"0 / 15 Mbps"
			"1 / 30 Mbps"
			"2 / 45 Mbps"
			"3 / 60 Mbps"
			"4 / 90 Mbps"
			"5 / 120 Mbps"
			"6 / 135 Mbps"
			"7 / 150 Mbps"
			"8 / 30 Mbps"
			"9 / 60 Mbps"
			"10 / 90 Mbps"
			"11 / 120 Mbps"
			"12 / 180 Mbps"
			"13 / 240 Mbps"
			"14 / 270 Mbps"
			"15 / 300 Mbps"

CHANNELWIDHT =	"Dynamic 20/40 MHz"
				"20 MHz"
				"40 MHz"

GUARDINTERVAL =	"Long - 800 ns"
				"Auto"

TXPOWER =	"Quarter"
			"Half"
			"Full"
			"Eighth"
			"Minimum"

Parameters for "11a"
_____________________
CHANNEL =	"Auto"
			"36/5.180GHz"
			"40/5.200GHz"
			"44/5.220GHz"
			"48/5.240GHz"
			"149/5.745GHz"
			"153/5.765GHz"
			"157/5.785GHz"
			"161/5.805GHz"
			"165/5.825GHz"

DATARATE =	"Best"
			"6 Mbps"
			"9 Mbps"
			"12 Mbps"
			"18 Mbps"
			"24 Mbps"
			"36 Mbps"
			"48 Mbps"
			"54 Mbps"

TXPOWER =	"Quarter"
			"Half"
			"Full"
			"Eighth"
			"Minimum"

Parameters for "11bg"
_____________________
CHANNEL =	"Auto"
			"1/2.412GHz"
			"2/2.417GHz"
			"3/2.422GHz"
			"4/2.427GHz"
			"5/2.432GHz"
			"6/2.437GHz"
			"7/2.442GHz"
			"8/2.447GHz"
			"9/2.452GHz"
			"10/2.457GHz"
			"11/2.462GHz"

DATARATE =	"Best"
			"1 Mbps"
			"2 Mbps"
			"5.5 Mbps"
			"6 Mbps"
			"9 Mbps"
			"11 Mbps"
			"12 Mbps"
			"18 Mbps"
			"24 Mbps"
			"36 Mbps"
			"48 Mbps"
			"54 Mbps"

TXPOWER =	"Quarter"
			"Half"
			"Full"
			"Eighth"
			"Minimum"

Parameters for "11b"
_____________________
CHANNEL =	"Auto"
			"1/2.412GHz"
			"2/2.417GHz"
			"3/2.422GHz"
			"4/2.427GHz"
			"5/2.432GHz"
			"6/2.437GHz"
			"7/2.442GHz"
			"8/2.447GHz"
			"9/2.452GHz"
			"10/2.457GHz"
			"11/2.462GHz"

DATARATE =	"Best"
			"1 Mbps"
			"2 Mbps"
			"5.5 Mbps"
			"11 Mbps"

TXPOWER =	"Quarter"
			"Half"
			"Full"
			"Eighth"
			"Minimum"
