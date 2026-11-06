from html import escape

import streamlit as st


st.set_page_config(
    page_title="나를 소개합니다",
    page_icon="✳️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 이 내용만 내 정보로 바꾸면 페이지가 함께 바뀝니다.
PROFILE = {
    "name": "이지아",
    "intro": "호기심을 따라 배우고, 좋아하는 일에 꾸준히 도전하는 사람입니다.",
    "school": "청주교육대학교",
    "study": "컴퓨터교육과",
    "dream": "초등학교에서 아이들과 함께 성장하는 교사가 되는 것",
    "foods": ["밀크티", "치아바타", "마카롱"],
    "interests": ["피아노 연주하기", "음악 듣기", "영화 보기", "산책 하기"],
}

name = escape(PROFILE["name"])
intro = escape(PROFILE["intro"])
school = escape(PROFILE["school"])
study = escape(PROFILE["study"])
dream = escape(PROFILE["dream"])
foods = "".join(f'<span class="food-tag">{escape(food)}</span>' for food in PROFILE["foods"])
interests = "".join(
    f'<li><span class="interest-dot"></span>{escape(interest)}</li>'
    for interest in PROFILE["interests"]
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #202a28;
        --muted: #68736f;
        --paper: #f7f8f5;
        --white: #ffffff;
        --teal: #bce6dd;
        --coral: #ff806b;
        --yellow: #f4cd68;
        --blue: #a9c5f5;
        --green: #b9d995;
        --pink: #f2b5cb;
    }

    html { scroll-behavior: smooth; }
    [data-testid="stAppViewContainer"] { background: var(--paper); }
    [data-testid="stHeader"], #MainMenu, footer { visibility: hidden; }
    .block-container { max-width: 1120px; padding: 28px 42px 72px; }
    .stMarkdown, p, h1, h2, h3, a, li, span, div {
        font-family: 'DM Sans', 'Noto Sans KR', sans-serif;
    }

    .site-nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 4px 0 34px;
    }
    .brand {
        color: var(--ink);
        font-size: 15px;
        font-weight: 800;
        text-decoration: none;
        letter-spacing: 0;
    }
    .brand-mark {
        display: inline-grid;
        place-items: center;
        width: 30px;
        height: 30px;
        margin-right: 8px;
        border-radius: 9px;
        background: var(--coral);
        color: var(--ink);
    }
    .nav-links { display: flex; gap: 27px; }
    .nav-links a {
        color: var(--muted);
        font-size: 13px;
        font-weight: 600;
        text-decoration: none;
    }
    .nav-links a:hover { color: var(--ink); }

    .hero {
        display: grid;
        grid-template-columns: 1.12fr .88fr;
        align-items: center;
        gap: 68px;
        min-height: 490px;
        padding: 22px 0 66px;
    }
    .eyebrow, .section-kicker {
        color: #438d81;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.4px;
    }
    .hero h1 {
        margin: 20px 0 18px;
        color: var(--ink);
        font-size: 58px;
        font-weight: 800;
        line-height: 1.2;
        letter-spacing: 0;
        word-break: keep-all;
    }
    .hero h1 .name-highlight {
        position: relative;
        z-index: 0;
        white-space: normal;
    }
    .hero h1 .name-highlight::after {
        position: absolute;
        z-index: -1;
        right: -5px;
        bottom: 1px;
        left: -5px;
        height: 18px;
        border-radius: 3px;
        background: var(--yellow);
        content: '';
    }
    .hero-copy {
        max-width: 460px;
        color: var(--muted);
        font-size: 16px;
        line-height: 1.9;
        word-break: keep-all;
    }
    .hero-note {
        display: inline-flex;
        align-items: center;
        gap: 9px;
        margin-top: 24px;
        color: var(--ink);
        font-size: 13px;
        font-weight: 700;
    }
    .note-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--coral); }
    .portrait-wrap {
        position: relative;
        width: min(100%, 370px);
        justify-self: end;
        padding: 14px 14px 0 0;
    }
    .portrait-wrap::before {
        position: absolute;
        z-index: 0;
        top: 0;
        right: 0;
        width: 67%;
        height: 72%;
        border-radius: 12px;
        background: var(--teal);
        content: '';
    }
    .portrait {
        position: relative;
        z-index: 1;
        display: block;
        width: 100%;
        aspect-ratio: 4 / 4.7;
        border-radius: 10px;
        overflow: hidden;
        background: #fff5d8;
    }
    .photo-caption {
        position: absolute;
        z-index: 2;
        right: -18px;
        bottom: 23px;
        padding: 13px 17px;
        border-radius: 8px;
        background: var(--yellow);
        color: var(--ink);
        font-size: 12px;
        font-weight: 800;
        transform: rotate(3deg);
    }

    .about-strip {
        display: grid;
        grid-template-columns: 180px 1fr;
        gap: 34px;
        align-items: start;
        padding: 29px 32px;
        border-radius: 10px;
        background: var(--teal);
    }
    .about-strip p {
        margin: 0;
        color: var(--ink);
        font-size: 18px;
        font-weight: 600;
        line-height: 1.75;
        word-break: keep-all;
    }
    .section { padding-top: 82px; scroll-margin-top: 24px; }
    .section-heading {
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 24px;
    }
    .section-heading h2 {
        margin: 7px 0 0;
        color: var(--ink);
        font-size: 30px;
        font-weight: 800;
        letter-spacing: 0;
    }
    .section-index { color: #9aa39f; font-size: 12px; font-weight: 700; }
    .info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .info-card {
        min-height: 210px;
        padding: 26px;
        border-radius: 9px;
    }
    .school-card { background: var(--blue); }
    .dream-card { background: var(--pink); }
    .card-label { color: rgba(32, 42, 40, .68); font-size: 12px; font-weight: 700; }
    .info-card h3 {
        margin: 38px 0 9px;
        color: var(--ink);
        font-size: 24px;
        font-weight: 800;
        line-height: 1.4;
        word-break: keep-all;
    }
    .info-card p { margin: 0; color: rgba(32, 42, 40, .75); font-size: 14px; line-height: 1.7; }
    .food-layout { display: grid; grid-template-columns: 1.15fr .85fr; gap: 16px; }
    .food-panel, .interest-panel { padding: 28px; border-radius: 9px; background: var(--white); }
    .food-panel { min-height: 210px; }
    .food-panel h3, .interest-panel h3 {
        margin: 0 0 20px;
        color: var(--ink);
        font-size: 18px;
        font-weight: 800;
    }
    .food-tags { display: flex; flex-wrap: wrap; gap: 10px; }
    .food-tag { padding: 10px 15px; border-radius: 6px; color: var(--ink); font-size: 14px; font-weight: 700; }
    .food-tag:nth-child(4n + 1) { background: var(--yellow); }
    .food-tag:nth-child(4n + 2) { background: var(--green); }
    .food-tag:nth-child(4n + 3) { background: var(--coral); }
    .food-tag:nth-child(4n + 4) { background: var(--blue); }
    .interest-panel { background: var(--green); }
    .interest-panel ul { display: grid; gap: 13px; margin: 0; padding: 0; list-style: none; }
    .interest-panel li { display: flex; align-items: center; gap: 10px; color: var(--ink); font-size: 14px; font-weight: 600; }
    .interest-dot { width: 8px; height: 8px; flex: 0 0 8px; border-radius: 50%; background: var(--coral); }
    .site-footer {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin-top: 86px;
        padding-top: 20px;
        border-top: 1px solid #dfe4df;
        color: var(--muted);
        font-size: 12px;
    }

    @media (max-width: 760px) {
        .block-container { padding: 20px 22px 50px; }
        .site-nav { padding-bottom: 14px; }
        .nav-links { gap: 13px; }
        .nav-links a { font-size: 11px; }
        .hero { grid-template-columns: 1fr; gap: 34px; padding: 35px 0 48px; }
        .hero h1 { font-size: 44px; }
        .portrait-wrap { width: min(80%, 340px); justify-self: center; }
        .about-strip { grid-template-columns: 1fr; gap: 14px; padding: 24px; }
        .about-strip p { font-size: 16px; }
        .section { padding-top: 62px; }
        .section-heading h2 { font-size: 26px; }
        .info-grid, .food-layout { grid-template-columns: 1fr; }
        .info-card { min-height: 180px; }
        .info-card h3 { margin-top: 28px; }
        .site-footer { margin-top: 62px; }
    }
    @media (max-width: 420px) {
        .nav-links { gap: 9px; }
        .nav-links a { font-size: 10px; }
        .hero h1 { font-size: 38px; }
        .section-index { display: none; }
        .site-footer { flex-direction: column; gap: 6px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <nav class="site-nav">
        <a class="brand" href="#top"><span class="brand-mark">✳</span>MY PAGE</a>
        <div class="nav-links">
            <a href="#about">소개</a>
            <a href="#journey">학교와 꿈</a>
            <a href="#favorites">좋아하는 것</a>
        </div>
    </nav>

    <section class="hero" id="top">
        <div>
            <div class="eyebrow">A LITTLE PAGE ABOUT ME</div>
            <h1>안녕하세요,<br /><span class="name-highlight">{name}</span>입니다.</h1>
            <div class="hero-copy">{intro}</div>
            <div class="hero-note"><span class="note-dot"></span>오늘보다 조금 더 나은 내일을 향해</div>
        </div>
        <div class="portrait-wrap">
            <svg class="portrait" viewBox="0 0 400 470" role="img" aria-labelledby="drawing-title">
                <title id="drawing-title">해님 아래 꽃과 함께 서 있는 사람의 손그림</title>
                <rect width="400" height="470" rx="16" fill="#fff5d8" />
                <path d="M24 355 Q112 325 205 355 T380 347 L400 470 L0 470 Z" fill="#b9d995" />
                <path d="M0 390 Q105 365 195 395 T400 382 L400 470 L0 470 Z" fill="#bce6dd" />

                <g stroke="#202a28" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M316 67 L316 42 M350 82 L370 67 M354 112 L380 118 M285 81 L267 65 M278 111 L254 119" fill="none" />
                    <circle cx="316" cy="97" r="34" fill="#f4cd68" />
                    <path d="M305 97 Q308 93 311 97 M321 97 Q324 93 327 97 M307 109 Q316 117 325 108" fill="none" />

                    <path d="M147 190 Q148 148 196 146 Q244 148 246 194 L237 219 L155 218 Z" fill="#202a28" />
                    <circle cx="197" cy="202" r="47" fill="#ffd2a6" />
                    <path d="M151 191 Q156 151 194 155 Q222 153 240 180 Q216 172 202 174 Q181 177 151 191 Z" fill="#202a28" />
                    <path d="M181 203 L181 204 M211 203 L211 204 M187 220 Q197 230 208 219" fill="none" />

                    <path d="M166 255 Q197 242 228 255 L240 327 Q196 341 153 326 Z" fill="#ff806b" />
                    <path d="M161 265 Q140 284 130 315 M231 264 Q251 282 265 307" fill="none" />
                    <path d="M173 330 L166 376 M218 330 L226 376" fill="none" />
                    <path d="M151 381 Q168 373 181 381 M215 381 Q233 373 246 381" fill="none" />
                </g>

                <g stroke="#438d81" stroke-width="6" stroke-linecap="round" fill="none">
                    <path d="M74 382 L77 335 M77 366 L55 348 M77 357 L97 339" />
                    <path d="M326 384 L326 340 M326 365 L307 350 M326 359 L346 343" />
                </g>
                <g stroke="#202a28" stroke-width="5" stroke-linejoin="round">
                    <path d="M77 327 C61 312 48 327 61 339 C46 351 62 364 77 351 C91 365 107 351 93 339 C107 324 91 312 77 327 Z" fill="#f2b5cb" />
                    <circle cx="77" cy="340" r="7" fill="#f4cd68" />
                    <path d="M326 333 C312 319 299 334 313 346 C298 359 314 372 326 358 C340 372 356 358 341 346 C355 331 340 319 326 333 Z" fill="#ff806b" />
                    <circle cx="326" cy="347" r="7" fill="#f4cd68" />
                </g>
                <path d="M35 420 Q48 410 62 420 M277 425 Q291 415 305 425 M350 414 Q362 406 374 414" stroke="#438d81" stroke-width="5" stroke-linecap="round" fill="none" />
            </svg>
            <div class="photo-caption">내가 그린 작은 그림</div>
        </div>
    </section>

    <section class="about-strip" id="about">
        <div class="section-kicker">01 / ABOUT ME</div>
        <p>{intro}</p>
    </section>

    <section class="section" id="journey">
        <div class="section-heading">
            <div><div class="section-kicker">02 / MY JOURNEY</div><h2>배우고, 꿈꾸고</h2></div>
            <div class="section-index">조금씩 채워가는 나의 이야기</div>
        </div>
        <div class="info-grid">
            <article class="info-card school-card">
                <div class="card-label">지금 배우는 곳</div>
                <h3>{school}</h3>
                <p>{study}</p>
            </article>
            <article class="info-card dream-card">
                <div class="card-label">앞으로 이루고 싶은 것</div>
                <h3>{dream}</h3>
                <p>나만의 속도로 한 걸음씩 나아가는 중</p>
            </article>
        </div>
    </section>

    <section class="section" id="favorites">
        <div class="section-heading">
            <div><div class="section-kicker">03 / LITTLE JOYS</div><h2>내가 좋아하는 것</h2></div>
            <div class="section-index">나를 웃게 하는 작은 취향들</div>
        </div>
        <div class="food-layout">
            <article class="food-panel">
                <h3>좋아하는 음식</h3>
                <div class="food-tags">{foods}</div>
            </article>
            <article class="interest-panel">
                <h3>요즘 관심사</h3>
                <ul>{interests}</ul>
            </article>
        </div>
    </section>

    <footer class="site-footer">
        <span>{name}의 작은 페이지</span>
        <span>천천히, 나답게.</span>
    </footer>
    """,
    unsafe_allow_html=True,
)
