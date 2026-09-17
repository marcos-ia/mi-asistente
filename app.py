import os

from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai


app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(
    os.environ.get("GEMINI_MODEL", "gemini-1.5-flash"),
    system_instruction=(
        "Responde mensajes de WhatsApp de forma natural, clara y breve en español. "
        "Responde como un asistente personal útil."
    ),
)


@app.post("/whatsapp")
def whatsapp():
    mensaje = request.form.get("Body", "")

    resultado = model.generate_content(mensaje)
    respuesta = resultado.text.strip()

    twiml = MessagingResponse()
    twiml.message(respuesta)

    return Response(str(twiml), mimetype="application/xml")


@app.get("/")
def inicio():
    return "Asistente de WhatsApp funcionando"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
    )                initial-value: -32px;
            }

            html,
            body,
            #root {
                min-height: 100%;
                margin: 0;
            }

            #enter-static-bootstrap-loading {
                --enter-static-brand-yellow: #ffc157;
                --enter-static-brand-orange: #ff8400;
                --enter-static-brand-pink: #ff8ee5;
                --enter-static-brand-purple: #d559ff;
                --enter-static-loading-text-color: #737373;

                position: fixed;
                inset: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 16px;
                background: #ffffff;
            }

            .dark #enter-static-bootstrap-loading {
                --enter-static-brand-yellow: #ffe073;
                --enter-static-brand-orange: #ffa13d;
                --enter-static-brand-pink: #ff98e7;
                --enter-static-brand-purple: #d96bff;
                --enter-static-loading-text-color: #a1a1aa;

                background: #09090b;
            }

            #enter-static-bootstrap-loading-mark {
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 64px;
                height: 64px;
                flex-shrink: 0;
            }

            .enter-static-brand-door {
                position: relative;
                display: block;
                width: 13.6px;
                height: 16px;
                flex-shrink: 0;
                overflow: hidden;
                border-radius: 50% 50% 1.45% 1.45% / 42.5% 42.5% 1.23% 1.23%;
                background: radial-gradient(
                    ellipse at 5% 100%,
                    var(--enter-static-brand-yellow) 6.84%,
                    var(--enter-static-brand-orange) 48.64%,
                    var(--enter-static-brand-pink) 77.15%,
                    var(--enter-static-brand-purple) 100%
                );
                contain: paint;
                isolation: isolate;
                transform: scale(4);
            }

            .enter-static-brand-door-layer {
                --enter-static-brand-door-phase: -32px;

                position: absolute;
                inset: 0;
                display: block;
                border-radius: inherit;
                pointer-events: none;
                background: repeating-radial-gradient(
                    ellipse at 0% 100%,
                    var(--enter-static-brand-yellow) calc(var(--enter-static-brand-door-phase) + 0px),
                    var(--enter-static-brand-orange) calc(var(--enter-static-brand-door-phase) + 10.67px),
                    var(--enter-static-brand-pink) calc(var(--enter-static-brand-door-phase) + 20px),
                    var(--enter-static-brand-purple) calc(var(--enter-static-brand-door-phase) + 25.33px),
                    var(--enter-static-brand-yellow) calc(var(--enter-static-brand-door-phase) + 32px)
                );
                animation: enter-static-brand-door-loop 2400ms linear infinite;
            }

            @keyframes enter-static-brand-door-loop {
                from {
                    --enter-static-brand-door-phase: -32px;
                }

                to {
                    --enter-static-brand-door-phase: 0px;
                }
            }

            #enter-static-bootstrap-loading-text {
                display: inline-flex;
                align-items: baseline;
                white-space: pre;
                font-family: Inter, 'Instrument Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
                font-size: 14px;
                line-height: 20px;
                color: var(--enter-static-loading-text-color);
            }

            .enter-static-bootstrap-loading-letter,
            .enter-static-bootstrap-loading-letter-glyph {
                display: inline-block;
            }

            .enter-static-bootstrap-loading-letter-glyph {
                animation: enter-static-bootstrap-loading-letter-hop 2400ms
                    cubic-bezier(0.65, 0, 0.35, 1) infinite;
                animation-delay: calc(
                    var(--enter-static-bootstrap-loading-letter-delay) + 420ms
                );
            }

            @keyframes enter-static-bootstrap-loading-letter-hop {
                0%,
                24%,
                100% {
                    transform: translate3d(0, 0, 0);
                }

                12% {
                    transform: translate3d(0, -0.08em, 0);
                }
            }

            @media (prefers-reduced-motion: reduce) {
                .enter-static-brand-door-layer,
                .enter-static-bootstrap-loading-letter-glyph {
                    animation: none;
                }
            }
        </style>
        <script id="enter-static-bootstrap-loading-i18n">
        // 静态首帧的微型 i18n：与 @workspace/i18n 同一解析链 cookie(enter-language) -> navigator -> 'en'，
        // 文案镜像 business-components/locales/*.json 的 common.pageLoading.entering。
        (function () {
            'use strict';

            var TEXTS = {
            "ar-SA": "Enterالدخول إلى العالم السحري...",
            "de-DE": "Magische Welt wird betreten...",
            "en": "Entering the magic realm...",
            "es-ES": "Entering el reino mágico...",
            "fr-FR": "Entering dans le royaume magique...",
            "id-ID": "Enterdi alam ajaib...",
            "it-IT": "Enterentro nel regno magico...",
            "ja-JP": "Enter魔法の領域へ...",
            "ko-KR": "Enter마법의 영역을 탐험 중...",
            "pt-BR": "Enter entrando no reino mágico...",
            "ru-RU": "Enterв волшебном мире...",
            "tr-TR": "Entersihirli alemde...",
            "zh-CN": "正在进入魔法世界...",
            "zh-TW": "正在進入魔法世界..."
        };
            var SUPPORTED = ["en","zh-CN","zh-TW","de-DE","pt-BR","es-ES","fr-FR","id-ID","it-IT","ja-JP","ko-KR","ru-RU","ar-SA","tr-TR"];
            var PREFIX_FALLBACKS = [["zh-Hant","zh-TW"],["zh-TW","zh-TW"],["zh-HK","zh-TW"],["zh-MO","zh-TW"],["en","en"],["zh","zh-CN"],["de","de-DE"],["pt","pt-BR"],["es","es-ES"],["fr","fr-FR"],["id","id-ID"],["it","it-IT"],["ja","ja-JP"],["ko","ko-KR"],["ru","ru-RU"],["ar","ar-SA"],["tr","tr-TR"]];

            function normalize(value) {
                if (!value) return null;
                var trimmed = String(value).trim();
                if (!trimmed) return null;
                var lower = trimmed.toLowerCase();
                var i;
                for (i = 0; i < SUPPORTED.length; i++) {
                    if (SUPPORTED[i] === trimmed) return SUPPORTED[i];
                }
                for (i = 0; i < SUPPORTED.length; i++) {
                    if (SUPPORTED[i].toLowerCase() === lower) return SUPPORTED[i];
                }
                for (i = 0; i < PREFIX_FALLBACKS.length; i++) {
                    var prefix = PREFIX_FALLBACKS[i][0].toLowerCase();
                    if (lower === prefix || lower.indexOf(prefix + '-') === 0) {
                        return PREFIX_FALLBACKS[i][1];
                    }
                }
                return null;
            }

            function resolveLanguage() {
                var items = document.cookie ? document.cookie.split(';') : [];
                for (var i = 0; i < items.length; i++) {
                    var item = items[i].trim();
                    if (item.indexOf('enter-language=') === 0) {
                        var fromCookie = normalize(
                            decodeURIComponent(item.slice('enter-language='.length))
                        );
                        if (fromCookie) return fromCookie;
                        break;
                    }
                }
                var languages = navigator.languages || [];
                for (var j = 0; j < languages.length; j++) {
                    var normalized = normalize(languages[j]);
                    if (normalized) return normalized;
                }
                return normalize(navigator.language) || 'en';
            }

            function fill(holder, text) {
                holder.setAttribute('aria-label', text);
                var delay = 0;
                Array.from(text).forEach(function (character) {
                    var letter = document.createElement('span');
                    letter.className = 'enter-static-bootstrap-loading-letter';
                    letter.setAttribute('aria-hidden', 'true');
                    letter.style.setProperty(
                        '--enter-static-bootstrap-loading-letter-delay',
                        delay + 'ms'
                    );
                    var glyph = document.createElement('span');
                    glyph.className = 'enter-static-bootstrap-loading-letter-glyph';
                    glyph.textContent = character;
                    letter.appendChild(glyph);
                    holder.appendChild(letter);
                    delay += 42;
                });
            }

            try {
                var language = resolveLanguage();
                var text = TEXTS[language] || TEXTS.en;
                if (!text) return;
                document.documentElement.lang = language;
                // 本脚本位于 head（外部样式表之前），body 中的文案节点由观察器就位后填充，
                // 避免被首屏大体积 CSS 阻塞执行。
                var observer = new MutationObserver(function () {
                    var holder = document.getElementById('enter-static-bootstrap-loading-text');
                    if (holder) {
                        observer.disconnect();
                        fill(holder, text);
                    }
                });
                observer.observe(document.documentElement, { childList: true, subtree: true });
            } catch (error) {
                // 文案失败时保留无文字的品牌门 Loading，不阻断启动。
            }
        })();
        </script>

        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link rel="preconnect" href="https://api.enter.pro" />
        <link
            rel="stylesheet"
            href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,400..600&family=Instrument+Sans:wght@400;500;600&display=swap"
            media="print"
            onload="this.media='all'"
        />
        <noscript>
            <link
                rel="stylesheet"
                href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,400..600&family=Instrument+Sans:wght@400;500;600&display=swap"
            />
        </noscript>
        <title>Enter</title>
      <script type="module" crossorigin src="/_enter_web/assets/main-NRS9PPfY.js"></script>
      <link rel="modulepreload" crossorigin href="/_enter_web/assets/session-client-D6zTj-Oh.js">
      <link rel="modulepreload" crossorigin href="/_enter_web/assets/react-vendor-CSGD7AD7.js">
      <link rel="stylesheet" crossorigin href="/_enter_web/assets/session-client-DYgwkIEk.css">
    <link rel="preload" href="/_enter_web/assets/sandbox-62091bd9.js" as="fetch" crossorigin fetchpriority="low" id="sandbox-preload">
</head>

    <body>
        <div id="root">
            <div
    id="enter-static-bootstrap-loading"
    role="status"
    aria-busy="true"
    aria-label="Loading"
    data-testid="static-bootstrap-loading"
>
    <span id="enter-static-bootstrap-loading-mark" aria-hidden="true">
        <span class="enter-static-brand-door">
            <span class="enter-static-brand-door-layer"></span>
        </span>
    </span>
    <span id="enter-static-bootstrap-loading-text"></span>
</div>
        </div>
    <script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/v31edd6df95cf4e85bb4c19e7a9bdbcba1788362987495" integrity="sha512-iIg7k2xntmwu6/uSb5tpc/hySgZc4eoL31yB29W6tJFo2akwjPWcEqnCEdJvGexCL0KEQwVYv5BlowfhVz26hg==" data-cf-beacon='{"version":"2024.11.0","token":"a9ffd0acd2974817b4c2b30148231e3b","spa":2}' crossorigin="anonymous"></script>
</body>
</html>
