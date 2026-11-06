# Onitama introduction maintenance / 介绍页维护

The EN introduction is https://songhaifan.github.io/frankie-onitama/; Chinese is `zh/`. The playable app is https://onitama-game-songhaifans-projects.vercel.app. The page builds independently of Next.js and never reads environment files.

英文默认，中文位于 `zh/`；介绍页独立构建，不需要构建应用或读取环境变量。

## Content and owning code / 文案与对应代码

| What changed / 变化 | Update / 更新 |
| --- | --- |
| Movement, exchange, captures, temples / 走棋、换牌与胜负 | Read `src/utils/gameManager.ts`; update both languages in `site/content.json`. |
| Pack names, counts, patterns / 卡包与走法 | `public/pack/onitama_cards_*.json` feeds counts and the diagram at build time. Update `content.json` if special rules change. |
| Wind deal or two-stage move / 风灵发牌与双阶段走棋 | Read `src/utils/dataLoader.ts`, `gameManager.ts`; the current app requires at least three wind cards. Do not replace this with a different tabletop setup description. |
| AI or restrictions / AI 与限制 | Read `src/utils/ai/aiFactory.ts`, `aiRestrictions.ts`, `gameController.ts`, `ai/winProbability.ts`; keep local-search and heuristic wording accurate. |
| Layout/controls / 布局与控件 | Read `GameHeader.tsx`, `GameBoard.tsx`, `MoveCards.tsx`, `MoveGrid.tsx`, `OnitamaLanding.tsx`; refresh screenshots below. |
| Palette/type/logo / 视觉风格 | `src/app/globals.css`, `public/Onitama_Logo.svg.png`; adapt `site/style.css`. The page intentionally keeps the app’s light scroll-paper theme. |

`site/cards.js` is a small, clearly labelled diagram adapted from `MoveGrid.tsx` and player-oriented coordinate logic. It reads real Ox/Crab/Tiger data, rotates for Blue, and stores nothing. It is not a full embedded game. If these cards are removed, update the selected IDs in `site/build.py`; a missing record fails the build rather than inventing data.

移动示意使用真实标准包数据，切换红蓝视角；不保存数据，也不冒充完整游戏。卡牌删除时，需要同步更新构建器里的示例 ID。

## Exact assets / 替换哪些素材

| Asset | Capture / 采集方式 |
| --- | --- |
| `site/assets/board-current.png` | Standard only → Begin → settled starting board. / 只选标准包，开始后等待棋盘稳定。 |
| `site/assets/move-current.png` | Select a current-player piece and card; capture the legal destination highlight before moving. / 选中当前玩家棋子与卡牌，采集高亮合法目标格。 |
| `site/assets/packs-current.png` | Landing page with all pack buttons loaded, EN or Chinese intentionally chosen. / 首页卡包按钮全部加载后采集。 |
| `site/assets/wind-current.png` | Select Wind + Standard, Begin; capture neutral spirit and separate patterns after animation settles. / 风灵与标准包混合，开始后采集风灵与双图案。 |
| `docs/readme/banner.png` | Approved banner reused for Open Graph; regenerate through `docs/readme/build.py` only if banner source UI/icon changes. / 分享图继续复用已确认 banner。 |
| `public/Onitama_Logo.svg.png`, `docs/readme/assets/frankie.svg` | Real project logo and approved signature, copied unchanged. / 真实标志与系列签名，直接复用。 |

Use real UI with no private content. Capture around 1468×1247 or update dimensions in `build.py`. Wait for fonts/images and movement transitions before screenshotting. The hero applies a CSS crop of the original screenshot; inspect the crop on phones. Update `project.json` capture revision/date and both captions in `content.json`. The original wide images remain available in the gallery. If adding a GIF, record a real interaction, provide an informative resting frame, and offer playback through an explicit control.

使用真实稳定界面；采集后同步素材版本、双语图注与尺寸，检查手机裁切。GIF 必须来自真实操作，并提供明确播放入口。

## Preview and publish / 预览与发布

```sh
python3 site/build.py --out _site
python3 -m http.server 8080 --directory _site --bind 127.0.0.1
```

Check `/` and `/zh/` on desktop and 390px phones: readable screenshots, no broken images, no overflow, all three sample cards and both perspectives. Intro controls must not modify a real game. Check `#use` and `#start`, source links and the app link. No app rebuild or model request is needed.

Push reviewed `site/` changes to `main`; `.github/workflows/pages.yml` publishes only `_site/`. It also watches real pack JSON, logo and banner inputs. Keep app behavior, dependencies, env files and unrelated changes out of the documentation commit.

检查两种语言、桌面与手机、三张示例卡和红蓝视角；只提交介绍页相关改动。工作流会监听示例数据、标志与 banner 更新。

## Rules and attribution / 规则与出处

Basic movement, exchange and two win conditions are grounded in the [Arcane Wonders Onitama page](https://www.arcanewonders.com/eu/product/onitama/). The [publisher’s Way of the Wind rulebook](https://www.arcanewonders.com/eu/wp-content/uploads/sites/6/2024/06/Onitama_Way_of_the_Wind.pdf) is linked for the physical expansion. Explain this app’s variant behavior from its owning code; do not imply every pack implements every publisher rule exactly. See `site/AUDIT.md` for inspected flows and code evidence.
