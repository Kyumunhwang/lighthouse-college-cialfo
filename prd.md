# 차세대 글로벌 AI 대학 진학·진로(CCR) 및 국경 초월 원서 접수 플랫폼 제품 요구사항 정의서 (PRD)

* **문서 버전**: v3.0 (Enterprise Full-Lifecycle & Global Direct Apply Specification)
* **작성 기준일**: 2026년 10월 21일
* **벤치마킹 레퍼런스**: [Cialfo 공식 플랫폼(cialfo.co)](https://www.cialfo.co/), [Explore by Cialfo 대학 파트너 플랫폼](https://www.cialfo.co/universities), [Cialfo Direct Apply](https://www.cialfo.co/direct-apply) 및 글로벌 국제학교·고등학교 12개 실무·웨비나·튜토리얼 영상 데이터셋
* **대상 독자**: 프로덕트 매니저(PM), 시스템 아키텍트, UI/UX 디자이너, 프론트엔드·백엔드·AI 엔지니어링 팀
* **핵심 설계 범위**: 학생(Student)·학부모(Guardian), 교사(Teacher/Recommender), 카운슬러(Counselor), 학교·교육그룹 관리자(School/Group Admin) 및 대학 입학사정관(University Rep)을 아우르는 5대 역할별 상세 기능 명세, 다국가 입시 데이터 파이프라인, 상태 머신(State Machine), 그리고 현행 Cialfo 사용 현장의 12대 UX 페인포인트를 해결하는 차세대 UI/UX 디자인 아키텍처

## Part 1. 12대 Cialfo 실무·튜토리얼 영상 기반 시스템 사용성 및 워크플로우 심층 분석

본 섹션은 필리핀 마닐라 중국국제학교(CISM), 싱가포르 아메리칸 스쿨(SAS), 인도 뭄바이 Children's Academy Group of Schools(CAGS), 튀르키예 이스탄불 히사르 스쿨(Hisar School), 미국 일리노이 펜턴 고등학교(Fenton High School) 등 전 세계 고등학교 현장과 [Cialfo](https://www.cialfo.co/) 본사 제품·클라이언트 경험 팀이 제작한 12개의 영상을 전수 분석하여, 현행 시스템의 실제 조작 방식과 현장에서 드러난 구조적 UI/UX 병목(Pain Points)을 도출한 결과이다.

### 1.1 분석 대상 12대 유튜브 영상 요약 매트릭스

| 번호 | 영상 제목 및 링크 | 제작 채널 (발표 기관·연사) | 주요 타겟 역할 | 핵심 설명 모듈 및 시연 워크플로우 요약 |
| :--- | :--- | :--- | :--- | :--- |
| **영상 1** | [Why are high school counselors using Cialfo's Direct apply? \|\| Counselor Testimonial](https://www.youtube.com/watch?v=c9q20-5LodM) | Cialfo (필리핀 마닐라 중국국제학교 CISM 카운슬러) | 카운슬러, 학생, 학부모 | **Direct Apply(DA)** 5단계 통합 지원(영국 UCAS·호주 등), 전형료 면제 및 Cialfo 장학금, **전담 Cialfo Education Counselor(비자 신청까지 동행 및 누락 서류 독촉)**, `cDocs` 및 `Application Results` 자동 집계, 일반 UCAS 센터와 달리 **영국 조건부 합격(Conditional Offer)의 전체 상세 조건(Full Conditions) 열람**, 긴급 인앱 채팅(1분 내 응답) |
| **영상 2** | [College Counseling: Introduction to Cialfo: December 6, 2018](https://www.youtube.com/watch?v=5EUZ9qsdAqY) | Singapore American School (싱가포르 아메리칸 스쿨 카운슬러 팀) | 학생, 학부모, 카운슬러 | 대형 국제학교의 Cialfo 초기 도입 오리엔테이션(55분), 학생·학부모 프로필 셋업, 글로벌 대학 검색 및 교내 최근 합격자 데이터 기반 스캐터그램(Scattergram) 해석, 카운슬러-학생-학부모 3자 간 입시 타임라인 및 지원 리스트 동기화 |
| **영상 3** | [Cialfo Session \| Live Stream](https://www.youtube.com/watch?v=xlQXfAKiCbQ) | Children's Academy Group of Schools, Mumbai (Amandeep Kaur, Debapriya, Ayush) | 8~10학년 학생, 학부모 | 이메일 초대 기반 비밀번호 설정, 3대 진단(`Personality`, `Intelligences`, `Learning & Productivity` 35~40분), 프로필 기반 소셜 알고리즘형 대학·전공 팝업 추천, **사자 캐릭터 AI 챗봇 `Saige`**(심야 10시 진로·전공·복수전공 즉시 응답), **`Hubs` 개인 클라우드 드라이브**(수료증·캠퍼스 투어 전단지 사진·유튜브 링크 폴더별 보관), `Courses`(예: 축구, 음악 5,039개 과정, 항공 조종사, 게임 디자인, STEAM 복수전공) 및 `Discovery Center` 국가별 가이드(일본 등), **Direct Apply 파트너 대학 무료 `Cialfo Guide` 상담(교육론·숙소·Flywire 송금·비자 100% 성공·항공권) vs 유료 `Premium Counseling`**, 모바일 앱 대비 데스크톱 웹 권장 한계 |
| **영상 4** | [CAGS x CIALFO Onboarding Session](https://www.youtube.com/watch?v=cm11i6gquEU) | Children's Academy Group of Schools (Amandeep, Paul, Janvi Ruparel) | 9~10학년 학생, 학부모 | 초기 가입 링크 이메일(`notification@cialfo`)의 스팸/프로모션함 유입 주의, 섹션별 필수 저장(`Save Information`), 프로필 구성(`Personal Info` 사진·시민권, `Application Details`, `Preference Fit` 예산·국내외, `Tests` **플랫폼 내 IELTS/TOEFL/SAT 시험 접수 바로가기**, `Contacts` 부모 2명 등록, `Extracurricular Activities` 9학년+ 활동·증빙 업로드), **원클릭 `Resume Builder`**(스킬 숙련도·2~5개 언어 실시간 미리보기 및 PDF/DOC 다운로드), `Longlist`→`Shortlist`→`Applying` 3단계 리스트 및 `Uni-Fit`, `Events` 라이브 웨비나 등록 및 **과거 세션 녹화본(`Past Recordings`) 아카이브**, Google Keep 스타일 `Notes`, 3색 상태(`Done` 초록/`In Progress` 주황/`Not Started` 회색) `Tasks`(자체 생성 `Self Tasks` 포함), 24/7 `Chat with Cialfo` |
| **영상 5** | [EDUtech Asia Cialfo Intro](https://www.youtube.com/watch?v=hutEMUK3odM) | Cialfo (Rachel Partnerships Manager) | 카운슬러, 학교 리더십 | 지역·장학금·환경·입학요건(표준화 시험 및 **영국 대학용 IB 점수 필터**) 및 **카운슬러 커스텀 필터** 기반 대학 검색, UCAS 직연동 영국 전공 요건, 미국 대학(NYU 등) 프로필 내 가상 투어·에세이 프롬프트·Common App 표시·최근 업데이트 일자·재정보조 및 **교내 익명 데이터/Cialfo 네트워크 스캐터그램**, 지원 리스트 승인 시 **국가/대학별 맞춤형 `Tasks` 자동 생성**(일반 체크리스트 vs **에세이 버전/초안 이력 관리 `Essay Tasks`**), 클릭 시 전체 화면이 동적 필터링되는 인터랙티브 `Reports`(장학금·지원·예치금·등록 추적), 전 세계 카운슬러 전용 소셜 네트워크 **`Cialfo Community`** |
| **영상 6** | [How Cialfo Simplifies the College Application Process for Counselors?](https://www.youtube.com/watch?v=-BTHVO7-d9U) | Cialfo Client Experience | 카운슬러 | 상담 중 작성한 **`Notes`의 실시간 학생 공유**(몇 분 내 학생이 지난달·작년 상담 기록과 미완료 과제를 즉시 열람), **학년별(9학년 vs 12학년) 맞춤형 학생 테이블 컬럼 뷰 설정**, 녹화된 대학 이벤트 영상 다시보기 및 인앱 상시 채팅, `Cialfo Community` 내 NACAC/카운슬러 전문 강좌 및 피어 네트워크 |
| **영상 7** | [How to Make the Most Out of Cialfo’s Explore Platform](https://www.youtube.com/watch?v=M_-K-RdCAQQ) | Cialfo (Rachel Miller, Meera Sadri, Dominique, Jason) | 대학 입학사정관 (`Explore` 플랫폼) | 대학 로고·미디어·어학 요건 설정, Google 캘린더 동기화 및 팀 권한(`Admin`, 방문 예약용 `Member`, Direct Apply 심사용 `Admission Officer`), **4단계 입시 퍼널 대시보드**(`Connections` 리드: 국내/해외·학생/카운슬러/학부모·2024 vs 2025 YoY 비교·리스트 추가/이벤트/프로필 방문/오프라인 투어 QR 스캔 출처 분석 → `Shortlisted/Applying` → `Applicants` → `Offers`), **Technolutions Slate CRM 자동 푸시**, 관심 급증 지역 기반 **AI 추천 방문 고등학교(예: 대만 관심 급증 감지)**, 고교 방문 예약(`Book Now` 즉시 확정 vs `Request Visit` 승인 요청, 정문 대신 Gate D 출입 등 보안 지침 확인, 가상/대면 선택 — 한국 달튼 외국인학교 시연), 미응답 학교 독촉(`Gentle Nudge`) 및 일정표 다운로드, 고교를 4개 지표로 평가하는 **`Visit Rating` 시스템**, 연 2회 인도·중국·동남아 **Cialfo 고교 투어 & `Counselor Connect`** |
| **영상 8** | [The Student-Counselor Experience on Cialfo](https://www.youtube.com/watch?v=jr0DD4WAV2I) | Cialfo (Ryan Fleming, Kath Wong, 튀르키예 Hisar School Michelle Duang) | 카운슬러, 학생, 대학 사정관 | 여름방학 완료율 88%를 기록한 게이미피케이션 설문 **`University Quest` 및 진화형 동물 페르소나**(`Curious Capybara` → `Exploring Elephant` → `List-Building Leopard` → 우주복 입은 12학년 `Applying Alpaca`, `Focus Area`/`What to Embrace`/`What to Avoid` 제시 및 **학급 친구간 `Kudos`(칭찬 좋아요) 소셜 기능**), 대학 페이지 내 맥락 인지형 **`Saige AI`**(예: *"SUNY Buffalo State가 튀르키예 졸업장을 인정하나요?"* 즉시 답변), **카운슬러 커스텀 `Cialfo Groups`**(지원 국가·조기지원·시민권·비공개 IELTS 응시 그룹별 필터링 및 `Broadcast` 단체 이메일/SMS 발송), **비영어권 교사를 위한 카운슬러 대리 추천서(`cDocs`) 번역·업로드 워크플로우**, `Applying List` 내 `My School GPA/SAT` vs `본교 최근 5년 합격자 평균 GPA/SAT` 비교 및 **Excel 내보내기**, 대학 담당자 이메일 **`Do Not Share`(카운슬러 전용 열람) 토글**, 스캐터그램 내 **카운슬러 전용 `최근 지원자 실명 및 재학 동문(Alumni) 조회`**(재학생-동문 멘토링 연결), 유연한 대학 방문 등록 마감 시간 설정 및 참석자 명단 사후 반출, **`Cialfo Connections`(`Get Connected` 버튼 및 리스트 추가 기반 옵트인 리드)** |
| **영상 9** | [The Cialfo Story: An Exclusive Interview With Rohan Pasari](https://www.youtube.com/watch?v=Cr8s1mxeNhk) | Cialfo (Rohan Pasari 공동창업자 겸 CEO) | 학교 리더십, 전 이해관계자 | Cialfo 학생 **1인당 평균 3개 국가(3개 대학이 아닌 3개국!) 동시 지원** 통계, 전 세계 대학 입시의 공통원서("Common App of the world")를 지향하는 `Direct Apply`, 고등학교 대상 **평생 무료 버전(Free Version: 핵심 대학 검색·학생 관리·원서 지원 포함)** 제공 철학, 팬데믹 이후 학생들의 3대 핵심 고려 요소(장학금·안전 및 웰빙·졸업 후 취업 비자 및 고용 기회) |
| **영상 10** | [Cialfo 2023 – Discover, Apply, Succeed](https://www.youtube.com/watch?v=aloNKgqehqc) | Cialfo Product Team | 학생, 카운슬러 | **2023 대규모 UI/UX 개편**: 미니멀 좌측 메뉴(`Home`, `Universities`, `Bookmarks`, `Applications`, `Discovery Center`, `Careers`), 단계 달성 시 대학 일러스트가 진화하는 인터랙티브 **`My University Roadmap`**(`Profile`→`Discovery`→`Apply`→`Enroll`), 상단 유틸리티 메뉴 통합(`Inbox`+`Notes` → **`Inbox`** 통합; `Tasks`+`Assessments`+`Visits`+`Surveys` → **`To-Do's`** 통합), 카운슬러 내비게이션(`Students`, `Universities`, `cDocs` 전면 배치 + `More` 탭 하위 정리), 플랫폼 전역 검색 **`Universal Search`**, `Bookmarks` 내 **카운슬러의 합격 가능성(`Likelihood`) 수동 오버라이드 및 `Cialfo Likelihood` 참조**, 240개국 140개 통화 현지 결제 및 실시간 추적을 지원하는 **`Flywire` 등록금 결제 내장**, 대학 방문 요청 카드에서 **즉시 새로운 시간 역제안(`Propose a new time`)** 및 **우리 도시/인근 고교를 방문하는 대학을 탐색해 선제적으로 방문 초청(`Invite to Visit`)**하는 기능 |
| **영상 11** | [Cialfo Part 1: College Search and Lists](https://www.youtube.com/watch?v=J7BvZhzzJCI) | Rachel Georgakis (미국 일리노이 Fenton High School 카운슬러) | 12학년 학생 (Naviance → Cialfo 전환) | 크롬북(Chromebook)에서 개인 Gmail과 학교 Gmail 동시 로그인 시 발생하는 2단계 Google SSO 프롬프트 주의(`fenton.cialfo.com`), 대학 검색 시 **상단 토글이 `All`이 아닌 `Applying`에 고정되어 검색 결과 0건이 나오는 UX 함정**, 검색 결과 테이블 컬럼 커스터마이징(`Likelihood`, `Portals` **파란 물결=Common App / 트리플 C=Coalition App 아이콘**, `Majors`, `State`, `Acceptance %`, `Average ACT/SAT`, `Fenton Accepted Avg GPA/SAT`, `First Deadline`), 검색 스크롤 위치를 잃지 않고 우측에서 슬라이드 오버되는 **`Overview` 미니 드로어** |
| **영상 12** | [Cialfo Part 2: Letters of Recommendation](https://www.youtube.com/watch?v=GdbN9Q-8rYI) | Rachel Georgakis (미국 일리노이 Fenton High School 카운슬러) | 12학년 학생, 교사, 카운슬러 | 5대 핵심 교과(외국어·영어·사회·과학·수학, 예체능 전공 지원 시 예외) 11학년 교사 추천서 요청 가이드 및 학교별 최대 추천인 수 제한(예: 2명 캡), `Recommendations` → `Request Letter of Recommendation` → `Add Recommender` 진입 시 **화면 상단 고정 텍스트로 적힌 설문 질문을 학생이 마우스로 드래그·복사(Copy)하여 하단 입력창에 붙여넣기(Paste)한 뒤 답변해야 하는 심각한 UX 페인포인트**, 여러 교사에게 요청 시 공통 질문(나를 표현하는 형용사 3개 등)과 과목별 질문을 수동으로 복사·편집해야 하는 번거로움, `Surveys` 탭 내 별도 `Counselor Letter of Recommendation Survey`(방과 후 동생 돌봄, 주 30시간 아르바이트, 가업 지원 등 입력 및 `Save Draft`/`Submit`) |

### 1.2 영상별 시스템 조작 메커니즘 및 실무 디테일 해부

#### (1) 국경 초월 원서 접수(`Direct Apply`) 및 사후 등록·결제·비자 동행 메커니즘 ([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 9](https://www.youtube.com/watch?v=Cr8s1mxeNhk), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))

* **1인당 평균 3개국 동시 지원과 '글로벌 공통원서' 아키텍처**:
  * CEO 로한 파사리(Rohan Pasari)가 밝혔듯 Cialfo 플랫폼을 사용하는 학생들은 평균 **3개의 서로 다른 국가(예: 미국 + 영국 + 호주/캐나다/싱가포르)**에 동시 지원한다([영상 9](https://www.youtube.com/watch?v=Cr8s1mxeNhk)).
  * `Direct Apply (DA)`는 외부 대학 포털이나 유학원을 거치지 않고 Cialfo 내부에서 5단계(5-Step Process)만으로 영국(UCAS 전 대학 포함), 호주, 미국, 유럽, 아시아 파트너 대학 및 파운데이션/패스웨이 과정(INTO, Navitas, Kaplan 등)에 직접 원서를 제출하는 기능이다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
  * 대학당 평균 $200~$300에 달하는 전형료 면제(Fee Waivers)와 Cialfo 전용 장학금 혜택이 제공되어, 10개 대학 지원 시 학부모에게 수천 달러의 비용 절감 효과를 제공한다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
* **영국 조건부 합격(Conditional Offer) 상세 조건 전체 열람 및 `cDocs` 자동 집계**:
  * 일반 고등학교가 영국 UCAS 등록 센터(Registered Center)로만 운영할 경우 UCAS 시스템에서는 학생이 받은 조건부 합격의 요약본(Summary)만 볼 수 있어 구체적인 성적 조건을 파악하기 어렵다. 반면 Cialfo `Direct Apply`를 통해 지원하면 **조건부 합격의 전체 상세 조건(Full Conditions of a Conditional Offer)이 투명하게 표시**되고, 합격·불합격 결과가 `cDocs`와 `Application Results` 패널에 자동으로 집계(Auto-tally)된다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM)).
* **전담 입학 어드바이저(`UEA` / `Cialfo Guide`) 및 `Flywire` 등록금 결제·비자 100% 지원**:
  * Direct Apply 파트너 대학 지원 시 무료로 배정되는 전담 Cialfo 교육 카운슬러(University Enrollment Advisor)가 마감일 전 누락 서류 독촉부터 SOP/추천서 점검, 오퍼 수락, 학자금 대출, 기숙사 신청, **플랫폼 내 내장된 `Flywire`를 통한 240개국 140개 이상 현지 통화 등록금 결제 및 실시간 추적**([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)), 그리고 **학생 비자(Visa) 신청(비자 발급 성공률 100%) 및 출국 전 항공편 안내**까지 전 과정을 셰퍼드(Shepherd) 방식으로 밀착 지원하여 고가의 외부 유학원(Education Agent) 의존을 완전히 대체한다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).

#### (2) 게이미피케이션 기반 온보딩(`University Quest`), `Saige AI` 및 개인 클라우드 `Hubs` ([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))

* **`University Quest`와 4단계 진화형 동물 페르소나(Animal Personas)**:
  * 여름방학 중에도 **88%의 설문 완료율**을 기록한 인터랙티브 퀘스트로, 시민권, 학제(IB/AP/A-Level/국가 교육과정), 성적, 갭이어 계획, 관심 유학 국가 순위("Realms of interest"), 장학금 필요 여부를 질문한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * 응답 및 플랫폼 활동 수준에 따라 학생에게 귀여운 동물 페르소나 레벨이 부여되며 진화한다: ① 1단계 **`Curious Capybara` (호기심 많은 카피바라)** → ② 2단계 **`Exploring Elephant` (탐험하는 코끼리)** → ③ 3단계 **`List-Building Leopard` (리스트를 구축하는 표범)** → ④ 4단계 **`Applying Alpaca` (우주복을 입은 지원 단계 알파카)**([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)). 각 페르소나는 현재 집중할 영역(`Focus Area`), 권장 행동(`What to Embrace`), 피해야 할 행동(`What to Avoid`)을 알려주며, 같은 반 친구들의 동물 레벨을 보고 **`Kudos`(칭찬 하트)**를 보내는 소셜 기능이 결합되어 있다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
* **단계별 대학 일러스트가 변하는 `My University Roadmap`**:
  * 학생 홈(`Home`) 화면 중앙에는 `Profile` → `Discovery` → `Apply` → `Enroll` 4단계 시각적 로드맵이 배치되어, 각 단계의 체크리스트를 달성할 때마다 배경의 대학 캠퍼스 일러스트가 점진적으로 완성된다([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
* **맥락 인지형 AI 어시스턴트 `Saige`(Cialfo의 암사자 마스코트)**:
  * 밤 10시 학원 수업이 끝난 뒤 학교 카운슬러에게 연락할 수 없을 때 학생과 학부모가 질문할 수 있는 24/7 AI 챗봇이다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
  * ① **진로·전공 탐색 모드**: *"수학(Maths)을 좋아하는데 어떤 진로가 있어?"* 또는 *"음악과 과학 복수전공(Dual degree in music and science)이 가능한 대학은?"*이라고 물으면 순수수학 vs 응용수학 경로, 고교 권장 이수 과목, 입학시험 준비법, 복수전공 제공 대학을 즉시 답변하고 `Cialfo Guide` 상담 예약 버튼을 함께 띄운다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
  * ② **대학 프로필 내장 맥락 모드**: 특정 대학(예: SUNY Buffalo State) 상세 페이지 우측에 떠 있는 `Saige`에게 *"이 대학은 튀르키예 고교 졸업장(Turkish diploma)을 인정하나요?"*처럼 국제 학제 인정 여부나 유학생 지원 제도를 물으면 해당 대학 웹사이트와 Cialfo DB를 실시간 합성하여 정확한 답변을 제공한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
* **학생 개인용 멀티미디어 클라우드 드라이브 `Hubs` 및 `Resume Builder`**:
  * 학생들이 각종 수상 수료증(Certificates)이나 대학 캠퍼스 방문 시 받은 종이 브로슈어·전단지(Flyers)를 자주 분실한다는 피드백을 반영해 출시된 **`Hubs`** 기능은, 학생이 직접 `Certificates`, `Australia`, `UK`, `USA`, `Engineering` 등의 폴더를 만들고 전단지 사진을 찍어 올리거나 유튜브·소셜 미디어 아티클 링크를 붙여넣어 한곳에 아카이빙할 수 있게 한다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
  * 프로필에 입력한 학력·과외활동·수상 내역은 **`Resume Builder`**에서 원클릭(`Create Resume`)으로 불러와지며, 보유 스킬의 숙련도 슬라이더와 구사 언어(2~5개 국어)를 추가하면 우측 실시간 미리보기에 즉시 반영되고 PDF 또는 Word(DOC) 포맷으로 다운로드된다([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)). 또한 `Tests` 섹션에서는 IELTS, TOEFL, SAT 시험 일정을 조회하고 플랫폼에서 바로 외부 공식 시험 예약 페이지로 이동해 접수할 수 있다([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)).

#### (3) 카운슬러의 그룹 관리(`Cialfo Groups`), 에세이 버전 트래킹, 대리 추천서 및 동문 연결 ([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))

* **국가·대학별 자동 과제 생성(`Auto-Generated Tasks`) 및 에세이 초안 버전 관리(`Essay Tasks`)**:
  * 학생의 `Applying List`에 대학이 추가되고 카운슬러·학생·학부모 간 승인이 완료되면, **해당 대학의 국가 및 전형 특성에 맞는 필수 과제들이 자동으로 생성**된다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
  * 과제는 단순 완료형(`Done / Not Done`)과 **중요 입시 에세이(영국 UCAS Personal Statement, 미국 Common App Essay 등)의 수정 버전(Draft History)을 순차 추적하는 `Essay Tasks`**로 나뉜다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
* **비영어권 교사를 위한 카운슬러 대리 추천서(`cDocs Proxy LOR`) 워크플로우**:
  * 튀르키예 Hisar School 등 비영어권 국가의 국제/민족학교에서는 모든 교과 교사가 영어로 추천서를 작성하기 어렵다. Cialfo는 학생이 11학년 때 플랫폼에서 교사 추천서를 요청하면, 카운슬러 오피스가 교사를 대신해 번역·검수된 추천서를 `cDocs`에 대리 업로드하고 학생은 본인 대시보드에서 실시간 완료 상태만 투명하게 추적하는 유연한 대리(Proxy) 워크플로우를 지원한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
* **스캐터그램 내 카운슬러 전용 '실명 지원자·재학 동문(Alumni)' 조회 및 사정관 연락처 보호**:
  * 학생과 학부모가 보는 스캐터그램은 최근 5년간 본교 지원자의 익명화된 합격/불합격 분포와 평균 GPA/SAT만 표시하지만, 카운슬러 계정으로 스캐터그램을 클릭하면 **해당 대학에 최근 지원했거나 현재 재학 중인 본교 졸업생(Alumni)의 실명 리스트**를 즉시 조회하여 후배 재학생과 선배 동문을 멘토로 연결해 줄 수 있다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * 또한 대학 상세 페이지에 본교 담당 입학사정관 연락처를 등록할 때, 사정관이 학생들의 직접 이메일 폭주를 원치 않으면 카운슬러가 **`Do Not Share` 체크박스**를 켜서 오직 카운슬러들에게만 연락처가 보이도록 제어할 수 있다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

#### (4) 대학 입학사정관용 `Explore by Cialfo` 및 양방향 고교 방문(`Visits`) 생태계 ([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))

* **4단계 입시 퍼널(`Connections` → `Shortlisted` → `Applicants` → `Offers`) 및 AI 방문 고교 추천**:
  * 대학 입학처는 `Explore` 대시보드에서 자교를 리스트(`Longlist`/`Shortlist`/`Applying`)에 담았거나 프로필에서 `Get Connected` 버튼을 누른 옵트인 학생(`Cialfo Connections`)의 유입 추이를 2024년 대비 2025년 YoY 그래프, 유입 경로(리스트 추가, 이벤트 등록, 프로필 방문, 오프라인 박람회 QR 코드 스캔)별로 분석하고 이를 **Technolutions Slate CRM**으로 자동 푸시한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * 특히 AI가 **예상치 못한 지역별 관심 급증(예: 대만 소재 고등학교들의 자교 프로필 조회 급증)**을 감지하여 다음 출장 시 방문해야 할 고등학교를 대시보드에서 선제적으로 추천한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)).
* **양방향 방문 스케줄링, 인근 방문 대학 탐색 초청 및 `Visit Rating` 평가제**:
  * **대학 → 고교 예약**: 대학 사정관은 국가별로 고교를 검색(예: 태국 Bangkok Patana, 한국 달튼 외국인학교 등)하여 학교가 설정한 출입 보안 지침(예: *"정문이 아닌 Gate D로 출입하세요"*)을 확인하고, 대면(`In-person`) 또는 가상(`Virtual`) 방문을 선택해 시간표 연동 학교는 파란색 `Book Now`로 즉시 확정하고 수동 승인 학교는 흰색 `Request Visit`으로 요청한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)). 방문 종료 후에는 대학이 해당 고등학교를 4가지 항목(`Overall Experience`, `Student Engagement`, `Event Organization`, `Event Facilities`)으로 별점 평가(`Visit Rating`)한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)).
  * **고교 → 대학 역초청(`Discover Nearby Visiting Universities`)**: 고교 카운슬러는 방문 요청 카드에서 바로 새로운 시간을 역제안(`Propose a new time`)할 수 있을 뿐 아니라, **현재 우리 도시나 인근 다른 고등학교를 방문할 예정인 대학 사정관 목록을 조회하여 우리 학교에도 들러달라고 선제적 방문 초청(`Send Visit Invitation`)**을 보낼 수 있다([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).

### 1.3 12개 영상에서 발굴된 12대 핵심 UX 페인포인트(Pain Points) 및 차세대 시스템 해결 설계

12개 영상에서 카운슬러, 학생, 학부모, Cialfo 매니저들이 실제로 시연하며 겪은 불편사항과 수동 우회(Workaround) 사례를 분석하여, 우리가 개발할 차세대 시스템(`Next-Gen Global CCR Platform`)에서 반드시 해결해야 할 12대 과제로 정의하였다.

| 식별 코드 | 발견된 현행 Cialfo 시스템 UX 페인포인트 및 엣지 케이스 (출처 영상) | 차세대 시스템(PRD)의 아키텍처 및 UI/UX 해결 설계 |
| :--- | :--- | :--- |
| **PP-01** | **교사 추천서 요청 시 '설문 질문 드래그·복사·붙여넣기' 수기 노가다** ([영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI)): 학생이 교사에게 추천서를 요청할 때 학교가 설정한 사전 질문들이 입력창 위쪽에 단순 정적 텍스트로만 떠 있어서, 카운슬러가 학생들에게 *"질문들을 마우스로 드래그해 복사(Copy)한 뒤 아래 빈 메모 박스에 붙여넣고(Paste) 그 사이에 답을 타이핑하라"*고 교육해야 함. 심지어 2명의 교사에게 요청할 때 공통 질문(나를 묘사하는 형용사 3개 등)과 과목별 질문을 일일이 다시 복사·편집해야 함. | **구조화된 2계층 동적 폼 빌더(`Two-Tier Structured LOR Questionnaire`)**: 정적 텍스트 복사·붙여넣기를 전면 폐지. ① `Section A: 공통 자기성찰 질문`(한 번 입력하면 모든 추천인에게 자동 동기화 저장)과 ② `Section B: 해당 교사 과목별 질문`(선택한 교사의 담당 과목명이 자동 치환되는 개별 입력 필드)으로 분리된 인터랙티브 폼으로 렌더링하고 문항별 자동 임시저장 지원. |
| **PP-02** | **대학 검색 시 상단 `'Applying' vs 'All'` 스티키 탭 함정으로 인한 '0건 결과' 혼란** ([영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)): 학생이 `Schools` 검색창에 "Illinois State"를 입력했는데 결과가 0건으로 나와 당황함. 원인은 상단 서브 탭이 전체 대학(`All`)이 아니라 본인이 이미 지원 중인 리스트(`Applying`)에 고정(Sticky)되어 있었기 때문이며, `All`을 눌러야 비로소 33개 대학이 나타남. | **통합 검색 스코프 자동 전환(Smart Scope Switching & Zero-Result Fallback)**: 검색창에 키워드 입력 시 기본 스코프를 항상 `All Universities (Global DB)`로 자동 전환하되, 만약 내 북마크/지원 리스트 필터가 켜진 상태에서 결과가 0건이면 즉시 하단에 *"내 지원 리스트에는 'Illinois State'가 없습니다. 전체 대학 DB에서 검색된 33개 결과를 바로 표시할까요? [전체 결과 보기]"* 원클릭 폴백 제공. |
| **PP-03** | **모바일 앱의 기능 제약으로 인한 '데스크톱 전용 사용' 권고 한계** ([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)): 학부모가 스마트폰 앱으로 사용해도 되는지 질문하자 Cialfo 담당자가 직접 *"모바일 앱은 이동 중 단순 대학 검색용으로만 쓰고, 리스트 생성·노트 작성·원서 접수는 모바일에서 어려우므로 반드시 노트북이나 데스크톱 웹을 사용하라"*고 답변함. 모바일 퍼스트 세대인 Z세대 학생과 학부모의 접근성을 크게 떨어뜨림. | **반응형 모바일 퍼스트 PWA & 바텀 시트(Bottom-Sheet) 액션 아키텍처**: 무거운 멀티 컬럼 테이블과 우측 슬라이드 드로어를 모바일 뷰포트에서는 스와이프 가능한 카드 스택(Swipeable Cards), 스티키 하단 액션 바(Sticky Bottom Action Bar), 음성-텍스트 변환(Voice-to-Note) 노트 입력, 모바일 최적화된 단계별 스텝퍼(Step-by-step Mobile Wizard)로 100% 동등하게 구현. |
| **PP-04** | **프로필 입력 시 섹션별 수동 `'Save Information'` 미클릭으로 인한 데이터 증발** ([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)): 온보딩 세션에서 매니저가 *"각 프로필 섹션을 채울 때마다 반드시 아래쪽 `Save Information` 버튼을 눌러야 하며, 누르지 않고 탭을 이동하면 입력한 데이터가 모두 사라진다"*고 반복 경고함. | **실시간 디바운스 자동 저장(Optimistic Debounced Auto-Save) & 변경 상태 배지**: 모든 프로필·설문·이력서 입력 필드에 500ms 디바운스 기반 실시간 자동 저장(`☁️ 모든 변경사항이 자동 저장됨`)을 적용하고, 필수(`*`) 항목 미입력 상태로 페이지 이탈 시에만 인라인 하이라이트 안내 제공. |
| **PP-05** | **초기 계정 활성화 이메일(`notification@cialfo`)의 스팸/프로모션함 유입 및 로그인 실패** ([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)): 학교가 학생·학부모를 초대했을 때 발송되는 `"Get Started with Cialfo"` 이메일이 Gmail 프로모션 탭이나 스팸함으로 빠져 수많은 학생·학부모가 라이브 세션 당일까지 로그인을 못하는 사태 발생. | **다중 채널 온보딩(SSO + 교실 QR 코드 + WhatsApp/SMS OTP 초대) & 전달 상태 트래커**: 이메일 단일 의존을 탈피하여 ① 학교 Google/Microsoft/Clever/ClassLink SSO 원클릭 자동 프로비저닝, ② 교실 칠판에 띄우는 학급별 온보딩 QR 코드 + 학생 학번/생년월일 인증, ③ 학부모 휴대폰 SMS/WhatsApp 알림톡 매직 링크 발송을 지원하고, 카운슬러 화면에 이메일 `열람/스팸반송/미접속` 상태를 실시간 표시. |
| **PP-06** | **크롬북(Chromebook)에서 개인 Gmail과 학교 Gmail 이중 로그인 충돌** ([영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)): 학교 크롬북에서 학생이 개인 이메일과 학교 이메일에 동시에 로그인해 있을 때 서브도메인(`fenton.cialfo.com`) 접속 시 Google 인증창이 두 번 중복해서 뜨거나 잘못된 계정으로 진입해 로그인이 꼬이는 현상 발생. | **도메인 힌트 강제 바인딩(`login_hint` & `hd` Parameter Enforcement) 및 계정 전환 가드레일**: 학교 전용 서브도메인 접속 시 OAuth 요청에 해당 학교 도메인 파라미터(`hd=fenton.edu`)를 자동 주입하여 개인 Gmail 선택 실수를 원천 차단하고, 잘못된 도메인 선택 시 *"학교 공식 계정(@fenton.edu)으로 자동 전환합니다"* 원클릭 리다이렉트 제공. |
| **PP-07** | **35~40분 소요 심리·진로 진단(`Assessments`)의 중도 이탈 시 재시작 혼선** ([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)): 3대 진단(`Personality`, `Intelligences`, `Learning & Productivity`)이 각각 15~40분 걸리는데, 발표자가 *"한 번에 끝내지 않고(`at one go`) 중간에 멈추면 정확한 진단에 방해가 된다"*고 설명하며, `To-Do` 알림이 57개씩 쌓여 어디서 진단을 이어서 해야 할지 찾기 어려움([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)). | **마이크로 모듈형 진단 분할(bite-sized 5-Min Checkpoints) & 상단 고정 진행 바**: 40분짜리 진단을 5분 단위의 미니 챕터(Part 1~4)로 모듈화하여 수업 시간 자투리나 모바일에서도 끊김 없이 이어할 수 있게 하고, 57개 알림 속에 묻히지 않도록 미완료 진단을 `To-Do's` 최상단 고정 카드(Pinned Progress Card)로 분리. |
| **PP-08** | **비영어권 교사 추천서의 수동 번역·대리 업로드 관리 부담** ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)): 튀르키예 Hisar School처럼 비영어권 국가 학교에서는 교사들이 자국어로 추천서를 작성하면 카운슬러 오피스가 이를 수동으로 번역해 `cDocs`에 대리 업로드하느라 막대한 행정 시간이 소요됨. | **다국어 AI 추천서 번역·교정 브릿지(`Multilingual Teacher LOR Studio` + Counselor Review Gate)**: 교사가 본인의 모국어(튀르키예어, 한국어, 중국어, 스페인어 등)로 학생의 구체적 에피소드와 평가를 작성하면, 입시 전문 AI가 영미권 대학 입학사정관 표준 어조(Academic English LOR Style)로 정밀 번역·초안화하고, 카운슬러가 좌우 대조 화면(원문 vs 영문 번역본)에서 최종 감수·승인(`Approve to cDocs`)하는 하이브리드 파이프라인 구축. |
| **PP-09** | **학교별 고교 방문(`Visits`) 운영 방식의 양극화(전면 자동 예약 vs 전면 이메일 수기 조율)** ([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)): Hisar School 카운슬러는 *"일부 학교와 달리 우리는 수업 중 학생 외출이 유연해서 Cialfo 자동 방문 예약 슬롯을 쓰지 않고 대학들과 직접 이메일을 주고받아 일정을 잡는다"*고 밝힘([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)). 그 결과 수동 이메일로 잡은 일정은 다시 카운슬러가 플랫폼에 수기로 타이핑해 등록해야 하는 이중 작업 발생. | **3모드 하이브리드 방문 스케줄러(`Instant Book` / `Flexible Window Request` / `Email-to-Event AI Parser`)**: ① 고정 슬롯 즉시 예약(`Book Now`), ② 시간대 제한 없이 대학이 희망 일시를 제안하면 카운슬러가 원클릭 수락/시간 역제안하는 유연 요청 모드, ③ 이메일로 주고받은 방문 확정 내역을 포워딩하면 AI가 일시·대학·담당자·장소를 파싱해 캘린더에 자동 등록하는 파서 제공. |
| **PP-10** | **대학 방문 현장 출석 체크의 사후 수기 입력 번거로움** ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)): 대학 입학사정관이 현장에 QR 코드나 참석자 명부를 가져오지 않은 경우, 행사가 끝난 뒤 카운슬러가 다시 시스템에 들어가 누가 실제로 참석했는지 일일이 수기로 출석을 업데이트(`update the attendees`)해야 함. | **인앱 원탭 모바일 체크인 & 자동 QR 패스(`Dynamic Event QR & Geofence Check-in`)**: 모든 고교 방문 이벤트 생성 시 카운슬러 화면과 교실 프로젝터용 동적 QR 코드가 자동 생성되어 학생이 스마트폰으로 스캔 시 즉시 출석(`Attended`) 처리되며, 사전 등록 학생 명단을 대학 사정관의 `Explore` 앱과 실시간 공유. |
| **PP-11** | **지원 리스트(`Applying List`) 공유를 위한 수동 Excel 다운로드 및 버전 파편화** ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)): 학생과 카운슬러가 마감일, 본교 합격자 평균 GPA/SAT 비교 데이터를 학부모와 공유하기 위해 Excel 스프레드시트로 내려받아(`export as an Excel spreadsheet`) 전달하다 보니, 이후 마감일이나 지망 대학이 바뀌면 엑셀 파일과 실시간 시스템 데이터가 불일치함. | **실시간 인터랙티브 패밀리 공유 뷰 & 원클릭 PDF/웹 브리핑 링크(`Live Family Comparison Link`)**: 엑셀 반출 기능은 유지하되, 학부모 카카오톡/WhatsApp/이메일로 로그인 없이도(보안 PIN 인증) 자녀의 실시간 `Longlist/Shortlist/Applying` 비교표와 마감일 타임라인을 볼 수 있는 라이브 브리핑 뷰 및 깔끔한 인쇄용 PDF 리포트 제공. |
| **PP-12** | **다국가 지원 시 국가별 입학 요건(미국 GPA/SAT vs 영국 IB/A-Level 조건부 오퍼 vs 인도/튀르키예 내신) 비교 기준의 파편화** ([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 9](https://www.youtube.com/watch?v=Cr8s1mxeNhk)): 한 학생이 평균 3개국(미국·영국·호주/캐나다 등)을 동시에 지원하는데, 미국 대학은 100점 만점/4.0 GPA와 SAT를 보고, 영국 대학은 IB 예상 점수(예: 38점, HL 666)와 조건부 오퍼 상세 조건을 보며, 호주/유럽은 파운데이션/패스웨이 여부를 보므로 단일 테이블에서 합격 가능성을 비교하기 까다로움. | **다중 학제 자동 환산 엔진(`Multi-Curriculum Credential Equivalency Engine`) & 국가별 적응형 컬럼 뷰**: 학생 프로필에 등록된 원점수(100점제 내신, 4.0 GPA, IB Predicted/Final, A-Level, CBSE/ICSE, 튀르키예/한국 내신 등)를 지원 대상 대학의 국가 표준(미국 GPA/SAT 기준선 vs 영국 UCAS Tariff/IB HL 컷오프 vs 호주 ATAR 환산치)에 맞춰 자동 매핑·시각화하고, 영국 조건부 오퍼(`Conditional Offer`)의 과목별 달성률을 신호등 게이지로 추적. |

## Part 2. 차세대 글로벌 CCR 플랫폼 아키텍처, 데이터 파이프라인 및 상태 머신 설계

본 파트는 앞서 수행한 [Cialfo 솔루션 심층 분석](https://www.cialfo.co/)의 핵심 모듈(`Explore`, `Direct Apply`, `cDocs`, `Saige AI`, `University Quest`, `Hubs`, `Flywire`, `Cialfo Community`)과 12개 실무 영상의 요구사항을 완벽히 통합하고 12대 페인포인트를 해결하는 엔터프라이즈 시스템 아키텍처를 정의한다.

### 2.1 멀티 테넌트(Multi-Tenant) 계층 및 6대 역할 기반 접근 제어 (RBAC)

시스템은 글로벌 학교 그룹/교육청(School Group / District, 예: 인도 CAGS 그룹, 국제학교 네트워크) → 개별 캠퍼스(School Building) → 코호트/커스텀 그룹(`Cialfo Groups`, [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)) → 사용자(User)로 이어지는 4단계 멀티 테넌시를 지원하며, 6대 핵심 역할을 정의한다.

| 역할(Role) 식별자 | 역할 명칭 | 인증(Auth) 및 온보딩 방식 (PP-05·PP-06 해결) | 데이터 접근 범위 (Scope) 및 핵심 권한 요약 |
| :--- | :--- | :--- | :--- |
| `ROLE_STUDENT` | 학생 (8~12학년 & 졸업 동문) | 학교 도메인 강제 바인딩(`hd` 파라미터) Google/Microsoft/Clever SSO, 교실 온보딩 QR 코드 + 학번 인증, 이메일·SMS 매직 링크 | `University Quest` 동물 페르소나 진단, 3대 심리·진로 진단, 프로필·`Resume Builder`·개인 클라우드 `Hubs` 관리, `Longlist/Shortlist/Applying` 구축, `Saige AI` 질문, `Essay Tasks` 초안 버전 업로드, 추천서·성적표 요청, `Direct Apply` 원서 접수, `Flywire` 등록금 결제, `Get Connected` 대학 옵트인 제어 |
| `ROLE_GUARDIAN` | 학부모 / 보호자 (최대 2명 기본 + 확장 지원) | 학생/학교가 `Contacts`에 등록 시 SMS/WhatsApp/이메일로 즉시 활성화 링크 발송, 자녀 전환 스위처 지원 | 자녀의 프로필, 진단 리포트(PDF/웹), `Longlist/Shortlist/Applying` 비교표, 스캐터그램, 마감일 및 `Tasks`, `cDocs` 발송 상태, 영국 조건부 오퍼 상세 조건 열람; `Courses`/`Scholarships` 직접 검색, `Saige AI` 질문, `Cialfo Guide` 상담 예약 및 `Flywire` 등록금 납부 실행 |
| `ROLE_TEACHER` | 교과 교사 / 추천인 (Recommender) | 학교 SSO 또는 매직 링크 인증 (다국어 인터페이스 지원) | 추천서를 요청한 학생의 구조화된 2계층 설문 답변(공통 질문 + 내 과목 질문), 활동 이력·성적 열람; 영문 직접 작성·PDF 업로드 또는 **모국어 작성 후 AI 영문 입시 추천서 변환(`Multilingual LOR Studio`)** 제출 |
| `ROLE_COUNSELOR` | 학교 진학 카운슬러 (School Counselor) | 학교 SSO + 2FA 보안 인증 | 담당 코호트 및 커스텀 `Cialfo Groups` 생성·필터링, `Broadcast` 단체 이메일/SMS 발송, 상담 `Notes` 실시간 공유, 학생 `Likelihood`(합격 가능성) 수동 오버라이드, 국가/대학별 `Tasks` 및 `Essay Tasks` 배포·첨삭, `cDocs`(Common App/Parchment/UCAS/Direct Apply) 발송 및 비영어권 교사 대리 추천서 업로드, 스캐터그램 내 실명 지원자·동문(Alumni) 조회, 고교 방문(`Visits`) 승인·역제안·인근 방문 대학 초청, `Cialfo Community` 활동 |
| `ROLE_SCHOOL_ADMIN` | 학교 리더십 및 교육그룹 관리자 (Principal / Group Admin) | 학교 그룹 통합 SSO + 2FA | 단일 학교 또는 다수 캠퍼스(School Group)의 학년 중/연말 인터랙티브 `Reports`(국가별 지원·합격·장학금 총액·예치금·최종 등록률, School Profile 자동 갱신 데이터) 조회, 교사 최대 추천서 캡(Cap) 및 마감 리드타임 정책 설정, SIS/LMS 동기화 및 무료/프리미엄 티어 거버넌스 관리 |
| `ROLE_UNIV_REP` | 대학 입학사정관 (`Explore by Cialfo` 파트너) | 대학 공식 도메인 인증 (`Admin` / 방문 예약용 `Member` / Direct Apply 심사용 `Admission Officer` 세부 권한 분리 — [영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)) | 자교 프로필·브로슈어·영상·입학요건 관리, 4단계 입시 퍼널(`Connections`→`Shortlisted`→`Applicants`→`Offers`) 및 YoY 통계 분석, Slate CRM 연동, AI 추천 방문 고교 확인 및 대면/가상 고교 방문 예약(`Book Now`/`Request Visit`), 고교 `Visit Rating` 평가, `Direct Apply` 원서 심사 및 조건부/최종 오퍼 발급 |

### 2.2 글로벌 입시·문서·결제·비자 통합 데이터 파이프라인 명세

차세대 플랫폼은 평균 3개국 이상에 동시 지원하는 글로벌 학생들의 여정을 끊김 없이 연결하기 위해 7대 외부 생태계와 실시간 파이프라인을 구축한다.

1. **다국가 원서 및 문서 전송 네트워크 (`cDocs` + `Direct Apply` Engine)**:
   * **미국**: [The Common Application](https://www.cialfo.co/) 및 Coalition App(Scoir) 양방향 연동(대학 검색 테이블 내 파란 물결 아이콘 `Common App` 및 트리플 C 아이콘 `Coalition App` 자동 표시 — [영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)), [Parchment](https://www.cialfo.co/) 전자 성적표 네트워크 연동.
   * **영국**: **UCAS** 공식 코스 요건(A-Level, IB 총점 및 HL 과목별 기준 점수) 실시간 풀링([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)) 및 `Direct Apply`를 통한 UCAS 대학 원서 직접 제출, **조건부 합격(`Conditional Offer`)의 전체 상세 조건(Full Text Conditions) 원문 수신 및 `cDocs` 자동 집계**([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM)).
   * **호주·유럽·아시아·패스웨이**: 호주 주요 대학, 유럽(네덜란드·이탈리아 등), 인도·싱가포르·일본 국제학부 및 글로벌 패스웨이 기관(INTO, Navitas, Kaplan — Foundation/Bridge 및 Diploma-to-Degree 과정)과 `Direct Apply` API 직연동([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
2. **대학 입학처 CRM 파이프라인 (Technolutions Slate Integration)**:
   * 학생이 대학 프로필에서 `Get Connected`를 누르거나 `Longlist`/`Shortlist`/`Applying`에 추가하여 옵트인(`Cialfo Connections`)하면, 해당 리드 데이터와 출처(프로필 방문, 이벤트 등록, 오프라인 투어 QR 스캔)가 대학의 **Technolutions Slate CRM**으로 자동 푸시된다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
3. **글로벌 학비 결제 파이프라인 (`Flywire` Embedded Payment API)**:
   * 원서 합격 후 오퍼 수락 단계에서 플랫폼을 이탈하지 않고 **240개 이상 국가·지역의 140개 이상 현지 통화**로 예치금(Deposit)과 등록금(Tuition)을 안전하게 결제하고, 학생·학부모·대학·카운슬러가 실시간 송금 상태(`Initiated` → `Processing` → `Delivered to Institution`)를 추적한다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
4. **공인 시험 접수 및 교내 학사(SIS)·캘린더 연동**:
   * 프로필 `Tests` 탭에서 IELTS, TOEFL, SAT, ACT 공식 시험 접수 포털로 원클릭 연결하며([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)), 학교 SIS로부터 내신 성적(100점 만점, 4.0 스케일, IB 예상 점수 등)을 동기화하고 Google Calendar / Microsoft Outlook과 카운슬러 상담·대학 방문 일정을 양방향 동기화한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

### 2.3 핵심 비즈니스 로직 및 상태 머신(State Machine) 명세

#### (1) 3단계 대학 리스트 진화 및 자동 과제 생성 상태 머신 (`Longlist` → `Shortlist` → `Applying`)

1. `BOOKMARK_LONGLIST` (초기 관심 대학 광범위 수집) → **\[카운슬러·학부모 논의 및 `Compare` 비교\]** → `BOOKMARK_SHORTLIST` (압축된 후보 대학 리스트, [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
2. `BOOKMARK_SHORTLIST` → **\[학생·학부모·카운슬러 합의로 `Move to Applying` 승인\]** → `APPLYING_ACTIVE` 상태로 전이([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
3. **국가·대학별 워크플로우 자동 트리거 (`Auto-Task & Essay Spawner`, [영상 5](https://www.youtube.com/watch?v=hutEMUK3odM))**:
   * 대학이 `APPLYING_ACTIVE`로 진입하는 즉시, 해당 대학의 국가(`Country`), 지원 포털(`Common App` / `UCAS` / `Direct Apply` / `Coalition`), 마감일(`First Deadline`)에 맞춰 두 종류의 과제가 학생의 `To-Do's`에 자동 생성된다:
     * **Type A — `Checklist Tasks` (`Not Started [회색]` → `In Progress [주황]` → `Done [초록]`)**: 예: 여권 사본 `Hubs` 업로드, Common App 계정 매칭, IELTS 성적표 제출([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU), [영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
     * **Type B — `Essay Tasks` (`Draft v1` → `Counselor Feedback` → `Draft v2...` → `Final Approved`)**: 해당 대학의 당해 연도 보충 에세이 문항 및 국가별 공통 에세이(미국 Common App 인성 에세이, 영국 UCAS Personal Statement, Direct Apply SOP)에 대한 초안 버전 관리 스레드가 자동 생성된다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
4. **오퍼 수신 및 등록금·비자 종단 추적 (`Post-Application Shepherd Flow`, [영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ))**:
   * `SUBMITTED` → `OFFER_RECEIVED` (`Unconditional Offer` 또는 상세 조건이 명시된 `Conditional Offer`) → `OFFER_ACCEPTED` → `DEPOSIT_PAID_VIA_FLYWIRE` → `VISA_PROCESSING` (Direct Apply 전담 어드바이저 동행) → `ENROLLED` (학교 연말 리포트 및 차년도 School Profile 진학 통계에 자동 반영 — [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

## Part 3. 5대 핵심 역할별 상세 기능 명세 및 UI/UX 디자인 아키텍처

본 파트는 Cialfo의 2023~2025 최신 UI 패러다임([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))을 기반으로, 앞서 발굴한 12대 페인포인트를 해결한 학생·학부모, 교사, 카운슬러, 학교·그룹 관리자, 대학 입학사정관용 기능과 UI/UX를 상세히 정의한다.

### 3.1 [역할 1] 학생 및 학부모 포털 (Student & Guardian Experience)

#### 3.1.1 미니멀 글로벌 내비게이션(GNB) 및 모바일 퍼스트 반응형 아키텍처 (PP-03 해결)

* **좌측 6대 핵심 메뉴 (`Minimalist Left Sidebar`, [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc) 계승·확장)**:
  1. `🏠 Home (마이 로드맵 & 대시보드)`
  2. `🏛️ Universities & Courses (대학·전공·장학금 통합 탐색)`
  3. `🔖 Bookmarks (Longlist · Shortlist · Compare)`
  4. `🚀 Applications & Direct Apply (원서·에세이·추천서·Flywire·비자)`
  5. `🌍 Discovery Center & Events (국가별 가이드·아티클·웨비나 녹화본)`
  6. `🧭 Careers & Hubs (3대 진단·이력서 빌더·개인 클라우드 드라이브)`
* **상단 통합 유틸리티 바 (`Consolidated Top Bar`, [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))**:
  * **`🔍 Universal Search (전역 옴니박스 검색, 단축키 Cmd/Ctrl + K)`**: 화면 어디서나 몇 글자만 타이핑하면 대학, 전공 과정(`Courses`), 장학금, 진로 아티클, 도움말(`Help Center` 동영상·스크린샷 가이드)을 한 번에 찾아준다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
  * **`✅ To-Do's (통합 할 일 허브)`**: 카운슬러 과제(`Tasks`), 학생 자체 과제(`Self Tasks`), 미완료 심리 진단(`Assessments`), 신청한 대학 방문(`Visits`), 학교 설문(`Surveys`)을 단일 드롭다운과 배지로 통합 관리한다([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)). 이때 57개 알림 속에 중요한 진단이 묻히지 않도록([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)) **진행 중인 진단(`Continue Assessment`)과 D-7 임박 과제는 최상단 고정 카드(Pinned Card)로 분리**한다(PP-07 해결).
  * **`💬 Inbox (메시지 & 실시간 상담 노트 통합)`**: 카운슬러와의 채팅 메시지, 카운슬러가 상담 직후 공유한 미팅 기록(`Counselor Notes`), 개인 메모(`My Notes`), 그리고 **긴급 체크 시 1분 내 응답하는 `24/7 Chat with Cialfo` 및 `Cialfo Guide` 세션 예약**을 한곳에 통합한다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
  * **`🦁 Ask Saige AI (상시 플로팅 코파일럿)`**: 우측 하단 또는 상단에서 언제든 호출 가능한 사자 마스코트 AI 어시스턴트([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
* **모바일 퍼스트 반응형 웹/앱 동등성 보장 (PP-03 완벽 해결)**:
  * 스마트폰에서도 노트북과 100% 동일한 작업(리스트 이동, 추천서 요청, 노트 작성, Direct Apply 서류 업로드)이 가능하도록, 모바일 뷰포트에서는 다중 컬럼 표를 **좌우 스와이프 비교 카드(Swipeable Comparison Cards)**로 자동 변환하고, `Overview` 슬라이드 드로어를 **모바일 바텀 시트(Draggable Bottom Sheet)**로 렌더링한다.

#### 3.1.2 게이미피케이션 홈: `My University Roadmap` & `University Quest` 동물 페르소나 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))

* **인터랙티브 `My University Roadmap` 캔버스**:
  * 홈 화면 상단에 `Stage 1: Complete Profile` → `Stage 2: Discovery & Quest` → `Stage 3: Build Lists & Apply` → `Stage 4: Offer, Flywire & Enroll` 4단계 진행 바가 표시되며, 학생이 각 단계의 세부 마일스톤을 달성할 때마다 중앙의 대학 캠퍼스 일러스트가 활기차게 진화한다([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
* **`University Quest` & 4단계 진화형 동물 페르소나 위젯 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))**:
  * 5분 내 완료 가능한 게이미피케이션 온보딩 퀘스트(시민권, 학제, 성적, 갭이어 여부, 선호 유학 국가 순위 "Realms of interest", 장학금 필요도)를 수행하면 학생의 현재 준비 단계에 맞는 동물 아바타 카드를 부여한다:
    * **Lv.1 `Curious Capybara` (호기심 많은 카피바라)**: 탐색 시작 단계 — 진로 진단 및 국가 가이드 읽기 추천.
    * **Lv.2 `Exploring Elephant` (탐험하는 코끼리)**: 대학·전공 확장 단계 — `Longlist` 10개 이상 구축 및 캠퍼스 투어/웨비나 참여 추천.
    * **Lv.3 `List-Building Leopard` (리스트를 다듬는 표범)**: `Shortlist` 압축 단계 — 스캐터그램·입학 요건 대조 및 추천서 사전 요청 추천.
    * **Lv.4 `Applying Alpaca` (우주복 입은 지원 알파카)**: 12학년 실전 지원 단계 — 에세이 초안 완성, `Direct Apply`/Common App 제출 및 장학금 지원.
  * 카드 내부에는 맞춤형 행동 지침(`Focus Area`, `What to Embrace`, `What to Avoid`)이 제시되며, 우측의 **`Classmate Kudos` 피드**에서 반 친구들의 동물 레벨 진화 소식을 보고 응원 스티커(`👏 Kudos`)를 보낼 수 있다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

#### 3.1.3 자동 저장 프로필, 3대 진단(`Assessments`), `Resume Builder` 및 개인 클라우드 `Hubs` ([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU))

* **실시간 자동 저장 프로필 (`Auto-Save Profile` — PP-04 해결)**:
  * 기존처럼 `Save Information` 버튼을 누르지 않아 입력 데이터가 날아가는 사고([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU))를 막기 위해 모든 필드에 실시간 자동 저장을 적용한다.
  * 구성 섹션: ① `Personal Info`(카운슬러 식별용 프로필 사진, 타임존, 복수 시민권, 졸업 연도), ② `Application Details`(지원 과정: 학부 `Undergraduate` / 패스웨이 `Foundation·Diploma`, 입학 희망 연도, 관심 학문 분야), ③ `Preference Fit`(대학 랭킹 중요도, 국립 vs 사립, 국내 진학 vs 해외 유학, 연간 가용 예산, 기숙사·농구장·테니스장 등 캠퍼스 스포츠 시설 선호도 — [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)), ④ `Tests`(IELTS/TOEFL/SAT/ACT 점수 기록 및 **플랫폼 내 시험 접수 바로가기 버튼**), ⑤ `Guardians/Contacts`(부모님 최대 2명 이상 등록 시 즉시 학부모 계정 초대 링크 자동 발송), ⑥ `Extracurricular Activities`(9학년 이후 교내외 활동, 가업 돕기, 봉사활동, 직책, 주당 시간 및 수료증 첨부 무제한 등록).
  * **소셜 알고리즘형 실시간 추천 팝업**: 학생이 프로필 선호도나 관심 전공을 수정하는 즉시 소셜 미디어 알고리즘처럼 화면 우측에 맞춤형 추천 대학·전공·아티클 카드가 동적으로 갱신된다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
* **모듈형 3대 심리·진로·학습 진단 (`Assessments` — PP-07 해결)**:
  * 8~10학년 과목 선택(Subject Selection) 및 진로 설계를 위해 3대 핵심 진단을 제공한다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)):
    1. `Personality Assessment`: 내향/외향 등 성향 분석 및 적합 직무 환경 도출.
    2. `Learning & Productivity Assessment`: 시각(`Visual`)·청각(`Auditory`)·체감각(`Kinesthetic`) 학습 유형, 최적 집중 시간대(아침형 vs 야간형), 조명·소음 환경, 그룹 스터디 vs 단독 학습 선호도 분석([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)).
    3. `Multiple Intelligences Assessment`: 다중지능 강점 분석 및 추천 전공 계열(`STEM`, `STEAM`, `Business & Economics`, `Arts & Humanities`, `Health & Medicine` 등) 매핑.
  * 35~40분이 소요되는 전체 진단을 5~10분 단위의 4개 체크포인트로 분할 자동 저장하여 중도 이탈 시에도 정확도를 유지하며, 완료 즉시 **웹 인터랙티브 리포트와 학부모 공유용 PDF 리포트**를 동시 생성한다([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)).
* **원클릭 실시간 미리보기 `Resume Builder` 및 멀티미디어 드라이브 `Hubs`**:
  * `Resume Builder`에서 `Create Resume` 클릭 시 프로필과 활동 내역이 즉시 조합되며, 좌측 패널에서 스킬 숙련도 바(`Skills Proficiency`)와 구사 언어(2~5개 언어)를 조절하면 우측 이력서 프리뷰에 실시간 반영되고 PDF 또는 Word(`.docx`)로 즉시 다운로드된다([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)).
  * **`Hubs` (내 입시 클라우드 드라이브)**: 학생이 직접 `Certificates (수료증)`, `USA`, `UK`, `Australia`, `Engineering`, `Music Portfolio` 등 커스텀 폴더를 만들고, 대회 상장 PDF, 캠퍼스 방문 시 받은 대학 브로슈어 스마트폰 촬영 사진, 유튜브/소셜 미디어에서 찾은 유용한 입시 영상·아티클 URL을 한곳에 저장하고 카운슬러와 공유한다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).

#### 3.1.4 글로벌 대학·전공·장학금 검색(`Universities & Courses`) 및 3단계 리스트(`Bookmarks`) UI/UX (PP-02·PP-11·PP-12 해결)

* **통합 검색 탭(`All Universities` / `Courses` / `Scholarships`) 및 스티키 필터 함정 방지 (PP-02 해결)**:
  * 기존에 검색 스코프가 `Applying` 탭에 걸려 있어 전체 대학 검색 시 0건이 나오던 문제([영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI))를 해결하기 위해, 상단 검색창 입력 시 자동으로 전체 DB(`All`)를 검색하고 내 리스트에 이미 담긴 대학은 행 우측에 `🔖 In Shortlist` / `🚀 In Applying` 배지로 표시한다.
  * **전공·과정 직접 검색(`Courses Search`, [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ))**: 대학 이름을 몰라도 학부모나 학생이 `"Football"`, `"Music"`(5,039개 과정), `"Law"`, `"Game Design"`, `"Pilot / Aviation"`, `"Dual Degree in Music and Science (STEAM)"`처럼 관심 키워드를 입력하고 국가·주(State) 필터를 걸면, 해당 과정의 학업 기간(Duration), 연간 학비(Annual Fee), 제공 장학금, 패스웨이(Foundation/Diploma-to-Degree) 유무를 카드 형태로 즉시 비교한다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ)).
* **커스터마이징 가능한 검색 테이블 & 우측 슬라이드 오버 `Overview` 드로어 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI))**:
  * 학생과 카운슬러는 테이블 컬럼을 자유롭게 켜고 끌 수 있다: `Uni-Fit / Likelihood`, `Portals`(`🌊 Common App`, `CCC Coalition App`, `⚡ Direct Apply`, `🇬🇧 UCAS`), `Country/State`, `Acceptance %`, `First Deadline`, **`My School GPA vs. 본교 최근 5년 합격자 평균 GPA`**, **`My School SAT/IB vs. 본교 최근 5년 합격자 평균 점수`**([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)).
  * 행 우측의 `Overview` 버튼을 클릭하면 현재 검색 스크롤 위치를 잃지 않고 화면 오른쪽에서 슬라이드 오버 드로어(Slide-over Drawer)가 열려 대학 핵심 요약, 마감일, 스캐터그램 미니 뷰를 즉시 보여준다([영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)).
* **대학 상세 프로필(`University Profile`) + 맥락 인지형 `Saige AI` + `Get Connected` ([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))**:
  * 대학 프로필에는 캠퍼스 비디오/가상 투어, 브로슈어, 당해 연도 에세이 프롬프트, 재정보조(Institutional/Federal/State Aid), 최근 데이터 업데이트 일자(`Last Updated`), 카운슬러가 대학 방문 시 기록해 둔 공유 노트(`Visit Notes` — 방문을 놓친 학생도 열람 가능), 본교 담당 입학사정관 연락처(단, 카운슬러가 `Do Not Share` 설정 시 학생에게는 숨김)가 표시된다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * **맥락 인지형 `Saige AI` 사이드 패널**: 대학 페이지 우측에서 *"이 대학이 우리 국가 고교 졸업장(예: 튀르키예 디플로마, 한국 고교 내신, 인도 CBSE)을 인정하나요?"*, *"유학생 기숙사 보장 정책은?"*을 물으면 해당 대학 공식 웹 데이터와 Cialfo DB를 결합해 즉시 답변한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * **`Get Connected` 옵트인 버튼**: 학생이 관심 대학 페이지에서 `Get Connected`를 누르거나 리스트에 추가하면 해당 대학의 소식 업데이트와 인근 방문 알림을 받고 대학 입학처와 직접 연결된다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
* **`Bookmarks` (`Longlist` → `Shortlist` → `Applying`) & 다국가 비교 매트릭스 (PP-11·PP-12 해결)**:
  * 3단계 리스트 간 드래그 앤 드롭 이동과 사이드바이사이드 `Compare` 뷰를 제공한다([영상 4](https://www.youtube.com/watch?v=cm11i6gquEU), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * **`Cialfo Likelihood` + 카운슬러 수동 오버라이드(`Counselor Likelihood`)**: 알고리즘이 산출한 합격 가능성(`Likely` / `Target` / `Reach`) 옆에 담당 카운슬러가 학생의 에세이·포트폴리오·전공 경쟁률을 고려해 직접 판정한 `Counselor Likelihood` 배지를 나란히 표시한다([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
  * **실시간 패밀리 브리핑 링크 & Excel 내보내기**: `Export to Excel` 기능([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))과 함께 학부모 모바일에서도 실시간 업데이트되는 라이브 비교표 링크를 제공한다(PP-11 해결).

#### 3.1.5 구조화된 추천서 요청(`Recommendations`), 에세이 버전 관리 및 `Direct Apply` · `Flywire` 통합 센터 (PP-01 해결)

* **복사·붙여넣기 없는 '구조화된 2계층 추천서 요청 폼' (`Structured LOR Request Form` — PP-01 완벽 해결)**:
  * 기존처럼 학생이 화면 상단의 정적 설문 질문을 마우스로 드래그·복사해 아래 메모장에 붙여넣고 여러 교사에게 수동으로 복제해야 했던 치명적 불편([영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI))을 완전히 제거한다.
  * **학교 정책 가드레일**: 상단에 "11학년 핵심 5대 교과(영어·수학·과학·사회·외국어) 교사 우선 권장(예체능 전공 예외)" 안내와 학교가 설정한 최대 추천인 수 제한 게이지(예: `1 / 2 Recommenders Requested`)를 표시한다([영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI)).
  * **2계층 자동 동기화 입력 구조**:
    * **Tier 1 — `공통 자기성찰 답변 (Common Student Reflections — 1회 작성 시 모든 추천 교사에게 자동 적용)`**: *"나를 가장 잘 표현하는 형용사 3가지와 이유"*, *"교외 활동·가업 지원·가족 돌봄·아르바이트 등 배경 맥락"* 등 모든 교사에게 공통으로 필요한 문항은 한 번만 작성하면 두 번째 교사 추가 시 자동으로 채워진다([영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI)).
    * **Tier 2 — `과목별 맞춤 답변 (Course-Specific Reflections — 교사별 개별 입력창)`**: *"\[교사명\] 선생님의 \[과목명\] 수업에서 가장 기억에 남는 프로젝트와 성장한 역량은?"*, *"희망 전공과 이 과목의 연관성은?"* 등 교사별로 달라지는 질문은 각각의 독립된 텍스트 필드로 제공된다([영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI)).
* **`Direct Apply` 5단계 원클릭 제출 & 조건부 오퍼 상세 트래커 ([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))**:
  * `Applications` 탭에서 `Direct Apply` 대상 대학을 선택하면 이미 작성된 프로필·성적·`Hubs` 서류가 자동 프리필되어 5단계 스텝퍼로 원서가 제출되며, 전형료 면제 코드와 Cialfo 장학금 대상 여부가 자동 적용된다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM)).
  * 합격 발표 시 **영국 대학의 `Conditional Offer`(조건부 합격) 원문 전체 조건(예: *"IB 총점 38점 이상, HL 수학·물리 각각 6점 이상, IELTS 7.0 이상"*)을 항목별 체크리스트로 파싱**하여 학생·학부모·카운슬러가 조건 달성 여부를 한눈에 추적할 수 있게 한다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM)).
  * 오퍼 수락 후에는 동일 화면에서 **`Flywire` 현지 통화 등록금 결제 모듈**을 호출해 납부하고, 전담 `Cialfo Guide (UEA)`와 기숙사·학자금 대출·비자(Visa) 서류 준비 체크리스트를 완료한다([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).

### 3.2 [역할 2] 교사 포털 (Teacher & Multilingual Recommender Studio)

국제학교 및 비영어권 국가 고등학교 교사들의 업무 환경을 모두 아우르기 위해, 구조화된 학생 답변 뷰어와 다국어 AI 번역·초안 브릿지를 결합한 추천서 스튜디오를 설계한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI)).

#### 3.2.1 추천서 요청 대시보드 및 마감일 트래커

* **교사용 추천서 요청 큐**: 요청 학생 명단, 담당 과목 및 학기 성적, 가장 빠른 대학 원서 마감일(`First Deadline`), 추천서 제출 대상 포털(`Common App` / `UCAS` / `Direct Apply` / `cDocs`), 현재 상태를 한눈에 표시한다.
* **좌-우 분할 추천서 작성 스튜디오 (`Split-View LOR Studio`)**:
  * **좌측 패널**: 학생이 Tier 1(공통 질문)과 Tier 2(내 과목 맞춤 질문)에 작성한 답변이 깔끔한 문답 카드로 정리되어 표시되며([영상 12](https://www.youtube.com/watch?v=GdbN9Q-8rYI)), 학생의 `Resume`와 `Hubs` 내 관련 프로젝트 산출물을 탭 전환으로 열람할 수 있다.
  * **우측 패널 (다국어 AI 추천서 변환 스튜디오 — PP-08 해결)**:
    * **모드 1 — 영문 직접 작성 또는 공식 레터헤드 PDF 업로드**: 영어가 능통한 교사는 바로 작성하거나 PDF를 업로드하여 `cDocs`에 보관한다.
    * **모드 2 — 비영어권 교사용 모국어 입력 → AI 영문 추천서 변환 + 카운슬러 감수 요청 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I) 확장)**: 영문 추천서 작성이 부담스러운 교사가 모국어(튀르키예어, 한국어, 중국어 등)로 학생의 수업 태도와 일화를 입력하면, AI가 영미권 대학 입학사정관 표준 양식의 영문 추천서 초안으로 변환하고 이를 카운슬러 감수 큐(`Counselor cDocs Proxy Queue`)로 전달한다. 교사가 제출을 완료하면 학생 화면의 추천서 진행 바가 실시간으로 `Completed`로 변경된다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

### 3.3 [역할 3] 카운슬러 포털 (Counselor Command Center & cDocs Hub)

2023 UI 개편으로 도입된 카운슬러 좌측 핵심 내비게이션(`Students`, `Universities`, `cDocs` + `More` 탭 하위 `Broadcast`, `Tasks & Assessments`, `Surveys`, `Events`, `Reports`, `Visits`, `Direct Apply` — [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))을 기반으로, 대규모 학생 코호트 관리와 글로벌 문서 발송을 자동화한다.

#### 3.3.1 동적 컬럼 학생 테이블, `Cialfo Groups` 및 `Broadcast` 커뮤니케이션 ([영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))

* **학년별·목적별 동적 학생 테이블 뷰 (`Customizable Student Table`, [영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U))**:
  * 카운슬러가 9학년 진로 탐색 코호트를 볼 때(진단 완료 여부, 동물 페르소나 레벨, 관심 계열 컬럼)와 12학년 입시 코호트를 볼 때(지원 국가 수, `Applying` 대학 수, 가장 빠른 마감일, `cDocs` 발송 상태, 에세이 진행률 컬럼) 테이블 컬럼 프리셋을 1클릭으로 전환한다([영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U)).
* **커스텀 `Cialfo Groups` 및 타겟 `Broadcast` 발송 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))**:
  * 알파벳순 담당 배정 외에도 카운슬러가 원하는 조건(예: `영국 UCAS 지원자 그룹`, `미국 Early Decision/Restrictive EA 지원자 그룹`, `특정 시민권 보유자`, `교내 비공개 IELTS 응시 대상자`, `장학금 필수 희망자`)으로 커스텀 그룹(`Cialfo Groups`)을 무제한 생성한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * 특정 그룹을 선택해 **`Broadcast`**(단체 이메일, 인앱 메시지, 학부모 SMS/WhatsApp)를 발송하거나 맞춤형 `Tasks` 및 `Surveys`를 일괄 배포한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
* **실시간 상담 노트 동기화 (`Instant Meeting Notes Sync`, [영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U))**:
  * 1:1 상담 중 카운슬러가 타이핑한 미팅 노트와 액션 아이템은 저장 즉시(또는 공개 범위 설정에 따라) 학생·학부모의 `Inbox > Notes` 타임라인에 동기화되어, 다음 달이나 내년에 상담할 때도 종이 노트를 뒤적일 필요 없이 지난 대화 이력과 과제 수행 여부를 1초 만에 파악한다([영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U)).

#### 3.3.2 `cDocs` 통합 문서 발송 센터, 에세이 버전 리뷰 및 스캐터그램 동문(Alumni) 매칭 ([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))

* **`cDocs` 멀티 네트워크 발송 허브 (Common App · Parchment · UCAS · Direct Apply)**:
  * 학생별·대학별 필수 서류(School Profile, Counselor Recommendation, Initial/Mid-Year/Final Transcript, Teacher LORs, Predicted IB/A-Level Grades) 준비 상태를 단일 매트릭스에서 점검하고 원클릭으로 전송한다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
  * **비영어권 교사 대리 업로드(`Proxy LOR Upload`) 및 번역 감수**: 교사가 제출한 모국어/번역 추천서를 카운슬러가 최종 검토 후 해당 학생의 `cDocs` 슬롯에 대리 업로드한다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
  * **`Direct Apply` 전담 셰퍼드 연동 및 1분 긴급 채팅**: Direct Apply 지원 건은 Cialfo 전담 교육 카운슬러(UEA)의 서류 검수 상태와 영국 조건부 오퍼 상세 조건이 자동 집계되며, 급한 입시 문의 시 우측 하단 채팅에서 **`Urgent(긴급)` 플래그를 켜면 1분 이내에 Cialfo 지원팀과 실시간 연결**된다([영상 1](https://www.youtube.com/watch?v=c9q20-5LodM)).
* **`Essay Tasks` 초안 버전 비교 뷰어 ([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM))**:
  * 학생이 업로드한 에세이 초안(`Draft v1`, `v2`, `v3`)의 변경점(Diff)을 비교하며 인라인 코멘트를 남기고 승인 상태를 관리한다.
* **스캐터그램 내 카운슬러 전용 '실명 지원자 & 재학 동문(Alumni)' 브릿지 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))**:
  * 특정 대학(예: Northeastern University) 스캐터그램 조회 시, 학생/학부모에게는 익명 점만 보이지만 카운슬러 화면 하단에는 **최근 5년간 해당 대학에 지원한 본교 졸업생 실명, 세부 전형 결과, 현재 해당 대학에 재학 중인 동문(Alumni) 연락처**가 표시되어 후배 재학생과 선배 동문을 즉시 연결해 줄 수 있다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

#### 3.3.3 양방향 고교 방문(`Visits`) 매니저 및 전 세계 카운슬러 네트워크 `Cialfo Community` ([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc))

* **유연한 고교 방문 스케줄링 & 인근 방문 대학 선제 초청 (PP-09·PP-10 해결)**:
  * 대학 사정관이 보낸 방문 요청 카드에서 카운슬러는 `Accept`, `Decline`, 또는 **카드 내에서 즉시 새로운 시간 역제안(`Propose a new time`)**을 할 수 있다([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
  * **`Discover Universities Visiting Nearby`**: 현재 우리 도시(예: 서울, 이스탄불, 싱가포르, 뭄바이)나 인근 고등학교에 방문 일정이 잡힌 해외 대학 리스트를 레이더 뷰로 확인하고, 빈 시간대에 우리 학교도 방문해 달라고 **`Send Visit Invitation`(선제 초청)**을 보낸다([영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)).
  * 학생 사전 등록 마감 시간(예: 방문 24시간 전까지 등록 또는 무제한 자율 참석 — [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))을 유연하게 조절하고, 현장 QR 체크인 출석부를 사정관에게 원클릭 공유한다.
* **내장 전문가 소셜 네트워크 `Cialfo Community` ([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U))**:
  * 전 세계 수천 명의 진학 카운슬러들이 플랫폼 안에서 뉴스피드, Q&A, 토픽별 구독(진로 지도, 학생 웰빙, 학부모 소통법, 국가별 입시 변화), 웨비나, NACAC/전문 연수 코스를 수강하며 교류하는 전용 커뮤니티 탭을 제공한다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 6](https://www.youtube.com/watch?v=-BTHVO7-d9U)).

### 3.4 [역할 4] 학교 리더십 및 교육그룹 관리자 포털 (School & Group Leadership Console)

단일 고등학교 교장단부터 다수의 캠퍼스를 운영하는 교육그룹(예: 인도 CAGS 그룹, 글로벌 국제학교 재단) 본부까지 데이터 기반 의사결정과 School Profile 갱신을 자동화한다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I), [영상 9](https://www.youtube.com/watch?v=Cr8s1mxeNhk)).

* **클릭 반응형 인터랙티브 애널리틱스 (`Interactive In-Year & End-of-Year Reports`, [영상 5](https://www.youtube.com/watch?v=hutEMUK3odM), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))**:
  * 대시보드 내 어느 데이터 포인트(특정 국가, 대학, 전공 계열, 장학금 구간, 입학 결과)든 하나를 클릭하면 **페이지 전체의 모든 차트와 학생 명단이 실시간으로 연동 필터링(Cross-Filtering)**된다([영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
  * 주요 지표: ① 코호트별 평균 지원 국가 수(글로벌 평균 3개국 대비 본교 지표 — [영상 9](https://www.youtube.com/watch?v=Cr8s1mxeNhk)), ② 대학별 지원·합격·대기·불합격 및 예치금 납부(`Deposit`)·최종 등록(`Matriculation`) 전환율(예: *"올해 우리 학교에서 보스턴 대학교에 몇 명이 지원했고 몇 명이 합격했는가"* 1초 조회 — [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)), ③ 학년 전체 누적 장학금 수혜 총액 및 전형료 면제 절감액([영상 3](https://www.youtube.com/watch?v=xlQXfAKiCbQ), [영상 5](https://www.youtube.com/watch?v=hutEMUK3odM)).
* **차년도 `School Profile` 자동 생성 위자드 ([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I))**:
  * 매년 학기 초 이전 졸업생들의 최종 대학 합격 및 등록(`Matriculations & Acceptances`) 데이터를 확정하면, 대학 입학처에 발송할 공식 **학교 프로파일(`School Profile PDF`) 내 대학 진학 실적 표와 평균 GPA/SAT/IB 통계 섹션이 원클릭으로 자동 업데이트**된다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

### 3.5 [역할 5] 대학 입학사정관 포털 (`Explore by Cialfo` Partner Console)

글로벌 대학 입학처가 전 세계 고등학교 및 옵트인 학생들과 연결되는 전용 B2B 포털(`Explore`)의 UI/UX를 정의한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ), [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

* **4단계 입시 퍼널 대시보드 & YoY 비교 차트 ([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ))**:
  * 상단 4대 위젯: ① `Connections`(국내/해외, 학생/카운슬러/학부모 비중, 2024 vs 2025 YoY 월별 스파이크 차트, 유입 출처: `Longlist/Shortlist/Applying` 추가·이벤트 등록·프로필 방문·오프라인 투어 QR 스캔), ② `Shortlisted/Applying`, ③ `Applicants`, ④ `Offers`([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)).
  * **AI 기반 방문 추천 고등학교 (`Recommended High Schools to Visit`)**: 자교 프로필 조회수나 리스트 추가가 급증한 국가·도시(예: 대만, 한국, 태국 등)의 고등학교를 AI가 자동 감지해 출장 방문 우선순위로 추천한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)).
* **글로벌 고교 방문 예약(`School Visits`), 출장 일정표 반출 및 `Visit Rating` ([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ))**:
  * 국가별 고교 필터링 후 각 학교의 보안 출입 지침(예: *"Gate D로 출입"*), 대면(`In-person`) vs 가상(`Virtual`) 선호 여부를 확인하고, 즉시 확정(`Book Now` - 파란 버튼) 또는 승인 요청(`Request Visit` - 흰색 버튼)을 보낸다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)).
  * 미응답 학교에 대한 독촉 알림(`Send a gentle nudge`), 과거 방문 이력 토글(`Include past visits`), 출장 보고용 전체 일정표(`Itinerary CSV/PDF`) 다운로드, 그리고 방문 종료 후 고등학교를 4개 항목(`Overall Experience`, `Student Engagement`, `Event Organization`, `Event Facilities`)으로 채점하는 **`Visit Rating`** 기능을 제공한다([영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)).

## Part 4. UI/UX 디자인 시스템(Design System), 프라이버시 및 단계별 구축 로드맵

### 4.1 디자인 시스템 토큰 및 인터랙션 가이드라인

| 디자인 요소 | 세부 규격 및 컬러/컴포넌트 토큰 | 적용 화면 및 UX 설계 의도 |
| :--- | :--- | :--- |
| **브랜드 & 시맨틱 컬러** | Cialfo Royal Blue (`#2563EB`), Saige Lion Gold (`#F59E0B`), Direct Apply Emerald (`#10B981`), Warning Orange (`#F97316`), Danger Rose (`#E11D48`), Neutral Slate (`#F8FAFC`) | [영상 4](https://www.youtube.com/watch?v=cm11i6gquEU)의 과제 상태 3색(`Done` 초록 / `In Progress` 주황 / `Not Started` 회색) 및 [영상 7](https://www.youtube.com/watch?v=M_-K-RdCAQQ)의 방문 예약 버튼(`Book Now` 블루 / `Request Visit` 화이트) 시맨틱 일관성 유지 |
| **포털 식별 배지 아이콘** | `🌊 Blue Wave` (Common App), `CCC Triple-C` (Coalition App), `⚡ Lightning Badge` (Cialfo Direct Apply), `🇬🇧 UCAS Badge` | [영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)에서 호평받은 직관적 포털 아이콘 체계를 확장하여 다국가 원서 접수 경로를 텍스트 없이도 0.1초 만에 식별 |
| **동물 페르소나 & 로드맵 일러스트** | SVG/Lottie 벡터 애니메이션: `Curious Capybara` → `Exploring Elephant` → `List-Building Leopard` → `Applying Alpaca` 및 4단계 진화형 캠퍼스 일러스트 | [영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)의 여름방학 88% 설문 참여율을 견인한 친근한 캐릭터 UX와 [영상 10](https://www.youtube.com/watch?v=aloNKgqehqc)의 `My University Roadmap` 시각적 성취감 극대화 |
| **컨텍스트 보존형 오버레이** | 우측 슬라이드 오버 드로어(`Overview Drawer`, 데스크톱 폭 `480px`) 및 모바일 드래그형 바텀 시트(`Bottom Sheet`) | [영상 11](https://www.youtube.com/watch?v=J7BvZhzzJCI)의 대학 검색 스크롤 위치 보존 장점을 모바일(PP-03)까지 완벽히 확장 |

### 4.2 개인정보보호(GDPR / FERPA) 및 옵트인(`Cialfo Connections`) 보안 원칙

1. **명시적 학생 옵트인 기반 `Connections` 공유**: 대학 입학처(`Explore`)는 학생이 스스로 대학 프로필에서 `Get Connected`를 클릭하거나 관심 리스트(`Longlist`/`Shortlist`/`Applying`)에 추가하며 정보 공유에 동의한 경우에 한해서만 연결(Qualified Connection)을 수립할 수 있다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
2. **스캐터그램 실명 데이터의 역할별 엄격 분리**: 학생과 학부모 화면의 스캐터그램은 최근 5년 지원자의 익명 점과 합격/불합격 비율만 노출하며, 지원자 실명 및 재학 동문(Alumni) 리스트는 오직 소속 학교 카운슬러(`ROLE_COUNSELOR`) 권한에서만 열람 가능하다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).
3. **대학 담당자 연락처 보호 토글 (`Do Not Share`)**: 카운슬러가 등록한 대학 사정관의 직통 이메일은 `Do Not Share` 플래그 활성화 시 학생·학부모 화면에서 마스킹 처리되어 카운슬러 전용 내부 커뮤니케이션 채널로 보호된다([영상 8](https://www.youtube.com/watch?v=jr0DD4WAV2I)).

### 4.3 단계별 개발 로드맵 (Phased Implementation Roadmap) 및 핵심 성과 지표 (KPIs)

| 개발 단계 | 목표 기간 | 핵심 구축 모듈 및 딜리버러블 | 검증 핵심 성과 지표 (Target KPIs) |
| :--- | :--- | :--- | :--- |
| **Phase 1: Onboarding, Gamified Roadmap & Mobile-First Core** | M1 ~ M3 | 다중 채널 온보딩(SSO `hd` 바인딩 + 교실 QR + WhatsApp/SMS — PP-05·06 해결), 실시간 자동 저장 프로필(PP-04 해결), `My University Roadmap` & `University Quest` 4단계 동물 페르소나(`Kudos` 포함), 모듈형 3대 진단(PP-07 해결), `Resume Builder` & 개인 클라우드 `Hubs`, 모바일 퍼스트 PWA(PP-03 해결) | 초기 계정 활성화율 98% 이상(스팸함 누락 제로화), 방학 중 `University Quest` 완료율 88%+ 유지, 모바일 웹/앱 작업 완료율 90% 이상 |
| **Phase 2: Multi-Country Search, Bookmarks & Structured LOR** | M4 ~ M6 | 대학·전공(`Courses`)·장학금 통합 검색(스티키 탭 함정 제거 — PP-02 해결), 다중 학제 자동 환산 엔진(PP-12 해결), `Longlist/Shortlist/Applying` & 라이브 패밀리 공유 뷰(PP-11 해결), 스캐터그램(카운슬러 전용 동문 매칭 포함), **구조화된 2계층 추천서 요청 폼(복사·붙여넣기 제거 — PP-01 해결)** 및 다국어 AI 추천서 번역 스튜디오(PP-08 해결) | 검색 시 'Applying 탭 고정으로 인한 0건 오류' 0%, 학생 1인당 추천서 요청 설문 작성 시간 65% 단축, 비영어권 교사 추천서 처리 시간 70% 절감 |
| **Phase 3: cDocs, Direct Apply 2.0, Flywire & Saige AI** | M7 ~ M9 | 국가·대학별 자동 과제 & 에세이 버전 트래커(`Essay Tasks`), `cDocs` 통합 전송(Common App/Parchment/UCAS), **`Direct Apply` 5단계 원서 제출 및 영국 조건부 오퍼 상세 조건 파서**, `Flywire` 140개 통화 등록금 결제 내장, 24/7 맥락 인지형 **`Saige AI`** & 1분 응답 긴급 채팅 | 학생 1인당 평균 3개국 이상 다국가 지원 처리 무결성 99.9%, 조건부 오퍼 세부 요건 누락 사고 0건, 긴급 채팅 응답 SLA 60초 이내 달성 |
| **Phase 4: Explore Partner Network, Hybrid Visits & Analytics** | M10 ~ M12 | 대학용 `Explore` 4단계 퍼널 & Slate CRM 자동 연동, AI 방문 고교 추천, 3모드 하이브리드 고교 방문 스케줄러(인근 방문 대학 선제 초청 & QR 자동 출석 — PP-09·10 해결), `Visit Rating`, 클릭 반응형 인터랙티브 `Reports` & `School Profile` 자동 갱신, `Cialfo Community` | 고교 방문 현장 수기 출석 입력 90% 감소, 인근 방문 대학 역초청 성사율 40% 증가, 연말 진학 통계 및 School Profile 제작 시간 80% 단축 |
