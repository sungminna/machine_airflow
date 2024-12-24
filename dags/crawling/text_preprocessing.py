import re

class TextPreprocessor:

    def preprocess_paragraph_names(self, paragraph_names):
        res = []
        for name in paragraph_names:
            # 숫자, 점, 공백을 제거하고 실제 내용만 추출
            content = name.split('. ')[-1].strip()
            res.append(content)
        return res

    def preprocess(self, text):
        text = re.sub(r'<img.*?>', '', text)

        # HTML 속성 제거
        text = re.sub(r'data-v-[a-zA-Z0-9]+', '', text)

        # 특수문자 제거(한글, 영문, 숫자, 공백, 마침표, 쉼표만 남김)
        text = re.sub(r'[^가-힣a-zA-Z0-9\s\.,]', ' ', text)

        # 중복 공백 제거
        text = re.sub(r'\s+', ' ', text)

        # 앞뒤 공백 제거
        text = text.strip()

        return text

    def chunk(self, text):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return sentences

if __name__ == '__main__':
    text='''모든 삼성 반도체 해외공장에서 사용하는 에너지는 100% 재생에너지를 사용하며, 대한민국에서의 재생에너지 사용 비중도 늘리고 있다. 삼성 반도체의 국내외 모든 생산공장은 폐기물 제로 인증을 받았으며 반도체 업계 중 최초로 친환경 우수상을 영국의 비영리단체에서 받았다.
생산 공정에서 발생하는 유리 조각과 같은 산업폐기물을 최소화해 토양 오염을 예방하고, 폐유나 페인트 등은 연료로 재활용하고 있다. 삼성전자 광주 사업장의 경우, 산업폐기물 재활용률을 2019년 93%에서 2021년 98%까지 확대한 바 있으며, 2024년까지 100% 수준으로 높일 계획이다.
현재 삼성전자가 직접 배출하는 탄소는 주로 반도체 제조공정에서 발생하는 공정가스와 LNG 등 연료 사용에 따른 것이다. 삼성전자는 2030년까지 공정가스 처리효율을 대폭 개선할 신기술을 개발하고 처리시설을 라인에 확충할 계획이다. 또 LNG 보일러 사용을 줄이기 위해 폐열 활용을 확대하고 전기열원 도입 등도 검토한다.
삼성전자는 2027년까지 모든 해외사업장에서 재생에너지 목표 달성을 추진한다. 서남아와 베트남은 2022년, 중남미 2025년, 동남아∙CIS∙아프리카는 2027년까지 재생에너지 목표 달성을 완료한다. 이미 재생에너지 목표를 달성한 미국, 중국, 유럽의 경우 재생에너지 발전사업자와 직접 체결하는 재생에너지공급계약(PPA)을 확대해 나가기로 했다. DX 부문은 국내외 모두 2027년까지 재생에너지 목표 달성을 추진한다.
삼성전자는 2027년까지 모든 업무용 차량(1,500여 대)을 100% 무공해차(전기∙수소차)로 전환한다. 향후 기타 간접배출(Scope3) 중장기 감축 목표를 설정하고 공급망, 자원순환, 물류 등에서 다양한 감축과제를 지속 발굴할 예정이다.
협력사를 대상으로 온실가스 감축 목표 수립, 이행 등을 체계적으로 지원한다.
삼성전자는 삼성EHS전략연구소가 준비한 탄소 감축성과 인증체제에 참여해 성과를 정확히 측정하며, 외부 전문가가 포함된 ‘탄소감축 인증 위원회‘를 구성해 객관적인 점검을 받기로 했다.
삼성전자는 원료부터 폐기∙재활용까지 전자제품의 모든 주기에 걸쳐 자원순환성을 높이는 프로젝트에 돌입한다. 재활용 소재로 전자제품을 만들고 다 쓴 제품을 수거해 자원을 추출한 뒤 다시 이를 제품의 재료로 사용하는 ‘자원 순환 체제‘를 만드는 것이 목표다.
삼성전자는 자원순환 극대화를 위해 소재 재활용 기술과 제품 적용을 연구하는 조직인 ‘순환경제연구소‘를 설립했다. 이 연구소는 재활용 소재 개발, 폐기물 자원 추출 연구 등을 통해 궁극적으로 제품의 모든 소재를 재활용 소재로 대체하는 것을 추진하는 조직이다.
폐배터리의 경우 2030년까지 삼성전자가 수거한 모든 폐배터리에서 광물을 추출해 재활용하는 체제를 구축할 계획이다.
사업장의 자원순환성 강화를 위해 수자원 순환 활용 극대화에 나선다. 반도체 국내 사업장에서는 물 취수량 증가 제로화를 추진한다. 반도체 라인 증설로 반도체 사업장의 하루 취수 필요량은 2030년 현재의 2배 이상으로 늘어난다. 이를 삼성전자는 용수 재이용을 최대한 늘려 이를 2021년 수준으로 동결하기로 했다.
DX부문은 수처리 시설 고도화로 용수 재이용을 확대하는 한편 2030년까지 글로벌 수자원 발굴 프로젝트와 수질 개선, 하천 복원사업 등을 통해 물을 쓴 만큼 100% 사회에 다시 돌려줄 예정이다.
삼성전자 DS부문은 배출하는 대기와 수질의 오염물질을 최소화한다. 반도체를 생산하는 과정에서 배출되는 대기 및 수질 오염물질을 제거하는 신기술을 적용해 2040년부터는 환경에 미치는 영향이 거의 없는 ‘자연상태‘로 처리해 배출하는 것을 목표로 정했다.
삼성전자는 새로운 처리기술 개발과 적용을 통해 방류수는 하천 상류 수준의 깨끗한 물로, 배출 대기는 국가 목표 수준의 깨끗한 공기로 처리해 배출할 계획이다. 또 글로벌 환경안전 인증 기관인 UL(Underwriters Laboratories)이 발급하는 폐기물 매립 제로 플래티넘 인증 획득(자원순환율 99.5% 이상)을 2025년 모든 글로벌 사업장으로 확대해 나갈 계획이다.
삼성전자는 반도체 산업현장에서 배출되는 탄소를 저장하고 이를 자원으로 재활용하는 탄소 포집·활용 기술을 개발·상용화하기 위해 2021년 9월에 종합기술원 내 탄소포집연구소를 반도체 업계 최초로 설립했다. 삼성전자는 탄소포집 기술을 2030년 이후 반도체 제조시설에 적용한 뒤 전사와 협력사까지 확대 적용할 방침이다. 탄소 포집·활용 기술개발이 결실을 맺게 된다면 반도체 업계 공통의 탄소 배출 문제를 원천적으로 해결하고 반도체 산업의 친환경성을 제고할 수 있을 것으로 전망된다.
삼성전자는 대기를 오염시키는 미세먼지 저감 기술 개발에도 적극 나서 2030년부터 지역사회에 이를 활용할 계획이다. 삼성전자는 2019년 1월 미세먼지연구소를 설립했으며, 미세먼지 감지, 분석, 제거를 위한 다양한 신개념필터와 공기정화시스템 원천 기술 개발에 매진하고 있다. 세척해 다시 사용할 수 있고 미세입자와 가스까지 동시에 제거할 수 있는 세라믹촉매필터를 개발하고, 이를 협력사, 버스터미널, 어린이집 등 지역사회에 적용할 예정이다. 삼성전자는 유망 친환경 기술을 발굴하고 그 분야의 스타트업을 육성, 지원하기 위한 투자도 진행한다. 기술혁신 커뮤니티와 함께 혁신기술 상용화 및 보급을 지원함으로써 글로벌 환경난제 해결에 협력할 예정이다. 사내외 벤처 육성 프로그램인 삼성전자 C-Lab에서도 친환경 관련 과제를 적극 발굴해 지원한다.
'''
    res = TextPreprocessor().preprocess(text)
    TextPreprocessor().chunk(res)
    print(res)