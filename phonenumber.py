def phonenumber_to_region(phonenumber):
    region_number = phonenumber[:phonenumber.find("-")]
    region = {'02':'서울', '051':'부산', '053':'대구', '032':'인천', '062':'광주',
              '042':'대전', '052':'울산', '044':'세종', '031':'경기', '033':'강원',
              '043':'충북', '041':'충남', '063':'전북', '061':'전남', '054':'경북',
              '055':'경남', '064':'제주', '010':'휴대폰', '070':'인터넷전화'}
    return region[region_number]

r1 = phonenumber_to_region("02-872-4071")
print(r1)