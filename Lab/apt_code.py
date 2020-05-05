import pymysql


def create_apt_table(apt_code):



	db = pymysql.connect(host='127.0.0.1', user='suk', passwd='1234', db='K_apt', charset='utf8')
	
	cursor = db.cursor()

	
	sql = '''
            CREATE TABLE {0} (
		date varchar(100) NOT NULL,
		공용관리비 int(100),
		일반관리비 int(100),
		인건비 int(100),
		급여 int(100),
		제수당 int(100),
		상여금 int(100),
		퇴직금 int(100),
		산재보험료 int(100),
		고용보험료 int(100),
		국민연금 int(100),
		건강보험료 int(100),
		식대_등_복리후생비 int(100),
		제사무비 int(100),
		일반사무용품비 int(100),
		도서인쇄비 int(100),
		여비교통비 int(100),
		제세공과금 int(100),
		통신료 int(100),
		우편료 int(100),
		제세공과금_등 int(100),
		피복비 int(100),
		교육훈련비 int(100),
		차량유지비 int(100),
		연료비 int(100),
		수리비 int(100),
		보험료 int(100),
		기타차량유지비 int(100),
		그밖의부대비용 int(100),
		관리용품구입비 int(100),
		전문가자문비_등 int(100),
		잡비 int(100),
		청소비 int(100),
		경비비 int(100),
		소독비 int(100),
		승강기유지비 int(100),
		지능형홈네트워크설비유지비 int(100),
		수선유지비 int(100),
		수선비 int(100),
		시설유지비 int(100),
		안전점검비 int(100),
		재해예방비 int(100),
		위탁관리수수료 int(100),
		개별사용료 int(100),
		난방비 int(100),
		난방_공용 int(100),
		난방_전용 int(100),
		급탕비 int(100),
		급탕_공용 int(100),
		급탕_전용 int(100),
		가스사용료 int(100),
		가스_공용 int(100),
		가스_전용 int(100),
		전기료 int(100),
		전기_공용 int(100),
		전기_전용 int(100),
		수도료 int(100),
		수도_공용 int(100),
		수도_전용 int(100),
		정화조오물수수료 int(100),
		생활폐기물수수료 int(100),
		입주자대표회의_운영비 int(100),
		건물보험료 int(100),
		선거관리위원회_운영비 int(100),
		장기수선충당금_월부가액 int(100),
		월사용액 int(100),
		충당금잔액 int(100),
		적립요율 int(100)
            );
        '''.format(apt_code)

	cursor.execute(sql)
	db.commit()
	db.close()




if __name__ == "__main__" :
	create_apt_table("A111112")
