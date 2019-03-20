cd /Users/mac/TestiCore/FakeFRS
python FakeFRSHttpServer.py -f './FRS_Normal.txt' -p 8001 > FRS_normal.log
python FakeFRSHttpServer.py -f './FRS_Unknown.txt' -p 8002 > FRS_unknown.log
python FakeFRSHttpServer.py -f './FRS_Malicious.txt' -p 8003 > FRS_malicious.log
