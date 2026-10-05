# 온톨로지 따라하기 — 공개 웹판 보관본

- 원제: 온톨로지 따라하기 (RAG 다음의 설계: PostgreSQL로 시작하는 실전 온톨로지)
- 저자: **이창근**
- 출처: https://wikidocs.net/book/21274
- 저작권/라이선스: **CC BY-NC-ND 4.0** (https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ko)
- 수집 시각(UTC): `2026-10-05T05:50:33.068402+00:00`

## 포함 범위와 제한

공개 목차 **60개 페이지 전체**, 책 소개 및 본문 이미지/직접 연결된 정적 첨부파일 **5개**를 저장했습니다.
**10장과 11장은 공개 미리보기만 포함합니다. 유료 전자책 본문은 포함하지 않습니다.**
외부 참고 사이트와 별도 예제 코드 GitHub 저장소는 복제하지 않았습니다.

원문 저작권은 저자에게 있습니다. 출처·저자·라이선스를 유지하고 **비영리**로 이용해야 합니다.
원문을 변경한 2차 저작물의 배포는 이 라이선스에서 허용하지 않습니다.
이 보관본은 원저자의 공식 배포판이나 보증을 의미하지 않습니다.
저장소의 다른 코드에 적용되는 라이선스가 있더라도 이 자료에는 자동 적용되지 않습니다.

## 열람

`index.html`을 브라우저로 열면 전체 목차를 볼 수 있습니다.

**[온톨로지 따라하기_요약정리.html](온톨로지%20따라하기_요약정리.html)**: 공개 웹판 기반의 독립적인 비공식 학습 메모입니다. 장별 개념, 구현 흐름, 원문 보고 실험값과 한계, 적용 체크리스트 및 60개 페이지 출처를 담았습니다. 원본 보관 파일은 수정하지 않았으며, 예제 벤치마크는 재실행하지 않았습니다. 단일 HTML로 열람하고 브라우저 인쇄에서 PDF로 저장할 수 있습니다.

GitHub에서는 아래 원문 링크 또는 다운로드한 HTML을 이용하세요.

- `originals/`: HTTP로 받은 원본 HTML 바이트 그대로 보존
- `pages/`: 본문 텍스트를 변경하지 않은 오프라인 열람용 HTML. 화면 틀과 링크 경로만 조정
- `assets/`: 본문 이미지, 정적 첨부파일, 책 표지와 라이선스 표시 이미지
- `manifest.json`: 페이지 목록, 원문 URL, 수집 시각, SHA-256 체크섬, 공개 미리보기 여부

원본 사이트의 광고·댓글·로그인 기능은 오프라인 열람본에서 제공하지 않습니다.
외부 링크는 인터넷 연결이 필요합니다. 코드의 실행 가능성이나 책 내용의 정확성은 별도로 검증하지 않았습니다.

## 목차

1. [00. 들어가며](https://wikidocs.net/426475) — [로컬 HTML](pages/426475.html)
2. [01. 문서를 다 넣었는데 AI는 왜 틀릴까?](https://wikidocs.net/426476) — [로컬 HTML](pages/426476.html)
3. [01-1. RAG가 틀린 답변 10개 해부하기](https://wikidocs.net/426477) — [로컬 HTML](pages/426477.html)
4. [01-2. 오류를 네 가지로 구분하기: 검색·데이터·의미·규칙](https://wikidocs.net/426478) — [로컬 HTML](pages/426478.html)
5. [01-3. 이 책의 가상 기업과 업무 질문 30개](https://wikidocs.net/426479) — [로컬 HTML](pages/426479.html)
6. [01-4. 실습: 기본 RAG로 업무 질문 30개 채점하기](https://wikidocs.net/426480) — [로컬 HTML](pages/426480.html)
7. [02. 이 오류에 온톨로지가 필요한가?](https://wikidocs.net/426481) — [로컬 HTML](pages/426481.html)
8. [02-1. 온톨로지란 무엇인가: 개념·관계·제약·공유된 정의](https://wikidocs.net/426482) — [로컬 HTML](pages/426482.html)
9. [02-2. DB 스키마와 온톨로지는 무엇이 다른가?](https://wikidocs.net/426483) — [로컬 HTML](pages/426483.html)
10. [02-3. DB를 잘 설계하면 온톨로지는 필요 없을까?](https://wikidocs.net/426484) — [로컬 HTML](pages/426484.html)
11. [02-4. RAG·GraphRAG·지식 그래프·온톨로지는 어디에서 만나는가?](https://wikidocs.net/426485) — [로컬 HTML](pages/426485.html)
12. [02-5. 팔란티어 Ontology에서 배울 점과 가져오지 않을 점](https://wikidocs.net/426486) — [로컬 HTML](pages/426486.html)
13. [03. 실습 환경 준비](https://wikidocs.net/426487) — [로컬 HTML](pages/426487.html)
14. [03-1. PostgreSQL + pgvector 설치 (Docker Compose)](https://wikidocs.net/426488) — [로컬 HTML](pages/426488.html)
15. [03-2. Python 환경과 LLM API 설정](https://wikidocs.net/426489) — [로컬 HTML](pages/426489.html)
16. [03-3. 예제 코드 저장소 구조와 실행 방법](https://wikidocs.net/426490) — [로컬 HTML](pages/426490.html)
17. [03-4. 평가 도구: 같은 질문 세트로 여러 구성을 채점하는 방법](https://wikidocs.net/426491) — [로컬 HTML](pages/426491.html)
18. [04. 업무 질문에서 개념 뽑아내기](https://wikidocs.net/426492) — [로컬 HTML](pages/426492.html)
19. [04-1. 업무 질문 30개에서 개념·관계 후보 추출하기](https://wikidocs.net/426493) — [로컬 HTML](pages/426493.html)
20. [04-2. 용어 사전 만들기: 같은 말, 다른 뜻 구분하기](https://wikidocs.net/426494) — [로컬 HTML](pages/426494.html)
21. [04-3. 개념 계층과 관계 정의하기](https://wikidocs.net/426495) — [로컬 HTML](pages/426495.html)
22. [04-4. LLM으로 초안을 만들고 사람이 다듬기](https://wikidocs.net/426496) — [로컬 HTML](pages/426496.html)
23. [04-5. 실습: 고객·계약·환불 도메인의 최소 의미 모델](https://wikidocs.net/426497) — [로컬 HTML](pages/426497.html)
24. [05. 조건·예외·시점·근거 설계하기](https://wikidocs.net/426498) — [로컬 HTML](pages/426498.html)
25. [05-1. 원칙과 예외를 함께 표현하기](https://wikidocs.net/426499) — [로컬 HTML](pages/426499.html)
26. [05-2. 시점: 계약 당시 규정과 현재 규정 중 무엇을 적용하는가](https://wikidocs.net/426500) — [로컬 HTML](pages/426500.html)
27. [05-3. 근거 연결: 어떤 문서의 어느 조항이 답을 뒷받침하는가](https://wikidocs.net/426501) — [로컬 HTML](pages/426501.html)
28. [05-4. 정보가 부족할 때: 판단 보류와 추가 질문](https://wikidocs.net/426502) — [로컬 HTML](pages/426502.html)
29. [05-5. 경계 나누기: 의미 정의·업무 규칙·데이터 검증·에이전트 제어](https://wikidocs.net/426503) — [로컬 HTML](pages/426503.html)
30. [06. PostgreSQL로 의미 모델 구현하기](https://wikidocs.net/426504) — [로컬 HTML](pages/426504.html)
31. [06-1. 개념·관계를 테이블로: 설계 선택지 비교](https://wikidocs.net/426505) — [로컬 HTML](pages/426505.html)
32. [06-2. 시점(유효기간) 모델링과 이력 테이블](https://wikidocs.net/426506) — [로컬 HTML](pages/426506.html)
33. [06-3. 근거 문서·조항과 의미 모델 연결하기 (pgvector 결합)](https://wikidocs.net/426507) — [로컬 HTML](pages/426507.html)
34. [06-4. 의미 모델을 API로 노출하기](https://wikidocs.net/426508) — [로컬 HTML](pages/426508.html)
35. [06-5. 실습: 스키마 구축과 데이터 적재](https://wikidocs.net/426509) — [로컬 HTML](pages/426509.html)
36. [07. 검색·SQL·규칙을 연결해 답변 만들기](https://wikidocs.net/426510) — [로컬 HTML](pages/426510.html)
37. [07-1. 질문 분석: 어떤 개념과 조건이 필요한가](https://wikidocs.net/426511) — [로컬 HTML](pages/426511.html)
38. [07-2. 검색 + SQL 조회 + 규칙 평가 파이프라인](https://wikidocs.net/426512) — [로컬 HTML](pages/426512.html)
39. [07-3. LLM에 의미 모델을 전달하는 방법: 컨텍스트 설계](https://wikidocs.net/426513) — [로컬 HTML](pages/426513.html)
40. [07-4. 답변에 근거와 적용 조건 붙이기](https://wikidocs.net/426514) — [로컬 HTML](pages/426514.html)
41. [07-5. 실습: 작은 업무 답변 서비스 완성](https://wikidocs.net/426515) — [로컬 HTML](pages/426515.html)
42. [08. 온톨로지 도입 실험실: 추가 전후 비교하기](https://wikidocs.net/426516) — [로컬 HTML](pages/426516.html)
43. [08-1. 실험 설계: 같은 모델·문서·질문, 구성 요소만 바꾼다](https://wikidocs.net/426517) — [로컬 HTML](pages/426517.html)
44. [08-2. 구성 1·2: 기본 RAG vs 검색·메타데이터 개선 RAG](https://wikidocs.net/426518) — [로컬 HTML](pages/426518.html)
45. [08-3. 구성 3: SQL 조회·규칙 처리를 결합한 RAG](https://wikidocs.net/426519) — [로컬 HTML](pages/426519.html)
46. [08-4. 구성 4: 명시적 의미 모델을 추가한 구성](https://wikidocs.net/426520) — [로컬 HTML](pages/426520.html)
47. [08-5. 결과 해석: 무엇이 온톨로지의 효과이고 무엇이 아닌가](https://wikidocs.net/426521) — [로컬 HTML](pages/426521.html)
48. [08-6. 정확도 외의 비교: 비용·응답 시간·관리 부담](https://wikidocs.net/426522) — [로컬 HTML](pages/426522.html)
49. [09. 그래프 DB로 옮길 때와 PostgreSQL에 남을 때](https://wikidocs.net/426523) — [로컬 HTML](pages/426523.html)
50. [09-1. 그래프 탐색이 유리한 질문 유형](https://wikidocs.net/426524) — [로컬 HTML](pages/426524.html)
51. [09-2. PostgreSQL 안에서 그래프 다루기: 재귀 CTE와 Apache AGE](https://wikidocs.net/426525) — [로컬 HTML](pages/426525.html)
52. [09-3. 구성 5: 필요한 일부를 그래프 탐색으로 구현하기](https://wikidocs.net/426526) — [로컬 HTML](pages/426526.html)
53. [09-4. RDF·OWL·SPARQL 표준은 언제 필요한가](https://wikidocs.net/426527) — [로컬 HTML](pages/426527.html)
54. [09-5. 판단 체크리스트: 유지·이전·혼합](https://wikidocs.net/426528) — [로컬 HTML](pages/426528.html)
55. [10장 전자책 미리보기: 전문 업무로 확장 — 세무 상담 사례](https://wikidocs.net/427390) — [로컬 HTML](pages/427390.html)
56. [11장 전자책 미리보기: 운영 — 모델을 살아 있게 유지하기](https://wikidocs.net/427391) — [로컬 HTML](pages/427391.html)
57. [부록A. 실습 질문 세트 30개 전체와 정답·근거](https://wikidocs.net/426540) — [로컬 HTML](pages/426540.html)
58. [부록B. 다섯 가지 구성 비교 결과표](https://wikidocs.net/426541) — [로컬 HTML](pages/426541.html)
59. [부록C. 용어 정리](https://wikidocs.net/426542) — [로컬 HTML](pages/426542.html)
60. [부록D. 참고 자료와 심화 학습 경로](https://wikidocs.net/426543) — [로컬 HTML](pages/426543.html)
