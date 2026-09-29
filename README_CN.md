# 胡发成 / Facheng Hu — 个人学术主页

这是一份已生成的静态网站，直接打开 `index.html` 即可预览。本版合并个人资料、公众号二维码与六篇阅读选文。实际发布版本以[仓库 Pages 部署记录](https://github.com/pardonhu/pardonhu.github.io/actions)中对应提交的成功结果及线上验收为准。

## 1. 本版内容

- 姓名：Facheng Hu / 胡发成。
- 身份：上海交通大学 Global College 博士研究生；导师：皮宜博老师（Yibo Pi）。
- 联系邮箱：`facheng_hu@sjtu.edu.cn`。
- GitHub：`pardonhu`；个人站点地址：`https://pardonhu.github.io/`。
- 个人资料由所有者于 2026-09-28 确认：2017 年在上海交通大学（Shanghai Jiao Tong University）获得工学学士（Bachelor of Engineering）；2024 年在上海交通大学获得硕士学位，导师为朱弘恣教授（Prof. Hongzi Zhu）；2017–2019 年在广汽乘用车（GAC Motor）从事汽车电子电气相关工作（automotive electronics and electrical systems）。保留 IEEE 研究生会员、上海交通大学 Global College 博士在读、导师皮宜博教授（Prof. Yibo Pi）及人工智能赋能的网络和无线感知研究兴趣。ORCID 为 https://orcid.org/0000-0003-0448-8907 ，显示于公开社交链接及 JSON-LD sameAs。所有者于 2026-09-29 补充确认本科 2013–2017、硕士 2021–2024、博士 2024–至今；履历保留广汽 2017–2019，并按时间排序。所有者同日确认：本科为机械与动力工程学院、机械工程（试点班）；硕士为计算机专业；博士为信息与通信工程。未提供的硕士院系、专业代码、本科导师、工作职位和地点不填写，2019–2021 不补造经历。ORCID 已有链接保留，并在首页简介附近以完整号码和文字链接突出展示。
- 论文：FastSET（SECON 2026）、Prism、Saga、DeepAoA+。FastSET 已置于首位，并加入 2026 年动态和年份筛选。已有论文链接与 BibTeX 保留。
- 研究兴趣：人工智能赋能的网络和无线感知；IEEE 研究生会员身份及完整双语简介由所有者明确提供。
- 没有填写未经提供的奖项、访问经历、简历或学术账号。
- 头像为所有者授权的自然摄影裁切；Prism 与 Saga 使用获授权的作者稿图 2，保留双语语义图注及本地全尺寸图片链接，图号与来源保存在 `SOURCES.md`。FastSET 和 DeepAoA+ 使用所有者授权的真实论文配图；四篇均有完整双语摘要。

默认英文，右上角可切换中文。论文正式标题与作者姓名在两种语言下均保留英文。页面适配手机和电脑；可以按年份筛选论文、展开及复制引用。页面没有访客跟踪、统计脚本、外部字体、第三方 JavaScript 或登录功能。出版页面、学校和导师链接只在访客点击时打开。

## 2. 后续可维护的资料

| 字段 | 在哪里修改 | 说明 |
| --- | --- | --- |
| GitHub 用户名 | `profile.json` → `github_username` | 已填 `pardonhu`。不要填密码、Token、验证码或完整网址。留空时不显示 GitHub 按钮。 |
| 个人照片 | 将图片放入 `assets/images/`，设置 `portrait` | 例如 `assets/images/profile.jpg`。留空时保留 FH 标识。 |
| Google Scholar | `google_scholar` | 填自己的完整主页链接；留空时不显示。 |
| ORCID | `orcid` | 已填所有者确认的 ORCID，公开链接与 JSON-LD sameAs 同步。 |
| 简历 PDF | `cv_url` | 放入网站目录后填写相对路径；也可以填写外部网址。留空时不显示。 |
| 完整简介 | `bio` → `en` / `zh` | 按所有者确认的双语全文维护；不推断未提供的专业、院系、导师或入学年份。 |
| 研究兴趣 | `research_interests` | 已由所有者确认；不会根据导师论文自动推测。 |
| 其他论文 | `publications` | 在核对最终题目、作者、发表状态和链接后添加。 |

只填 GitHub 用户名并不会授予别人操作账号的权限。发布需要你自己登录 GitHub，或在可信的连接工具中另行授权；不要在聊天中发送密码、验证码或访问令牌。

## 3. 部署到 GitHub Pages

本站使用现有仓库与 Pages 配置，维护时无需重新创建仓库。官方配置依据见 `SOURCES.md`。

1. 检查当前分支、工作区 diff 和 Pages 发布源，沿用现有分支与根目录配置。
2. 构建并完成本地验证后，按准确文件清单逐项暂存；检查暂存 diff，确认包含生成文件及所需资源。
3. 提交并推送到已配置的发布分支，等待对应提交的 Pages 部署完成。
4. 打开 `https://pardonhu.github.io/`，确认实际部署版本，执行线上交互与资源测试；推送成功或本地预览通过不能代替部署确认。

公开仓库中的源码、测试和配置均可能被访问。发布前检查文件清单；`.local-audit/` 仅保存本地审计材料，不纳入暂存或发布。`.nojekyll` 用于静态分支部署时跳过 Jekyll 处理。

### FastSET 出版信息

本版采用 IEEE 提交至 Crossref 的正式记录，确认四位作者 Facheng Hu、Yunzhe Li、Hongzi Zhu、Xudong Wang，DOI `10.1109/SECON68281.2026.11579146`，页码 150–158，会议于 2026 年 6 月 3–5 日在 Pisa 举行。页面及 BibTeX 已同步。历史论文集目录的起始页为 152，与正式记录不同，保留为历史证据，详见 `SOURCES.md`。未取得公开全文或 FastSET 原图，不猜测 PDF 入口。

## 4. 修改内容

资料集中保存在 `profile.json`。修改后，在这个文件夹中执行：

```sh
python build.py
```

Windows 也可使用：

```powershell
py build.py
```

Linux / macOS 也可使用：

```sh
python3 build.py
```

构建脚本仅使用 Python 标准库。它会重新生成 `index.html` 和 `publications.bib`；无需安装任何 Python 包。之后重新打开或刷新 `index.html`，再按发布流程提交修改后的文件。**不要只改 `profile.json` 而不重新构建**，因为线上页面读取的是生成后的 `index.html`。

直接编辑 `index.html` 也能修改页面，但下次执行 `build.py` 会覆盖这些手动修改。布局在 `templates/page.html`，样式在 `assets/style.css`，交互在 `assets/main.js`。

初次交付的独立预览 HTML 是当前版本的快照，不会随 `profile.json` 自动更新；长期维护请以本目录中的 `index.html` 为准。

### 研究兴趣与附加简介

```json
"research_interests": [
  {"en": "A research area you have confirmed", "zh": "你已确定的研究方向"}
],
"extra_bio": {"en": "An additional biography paragraph.", "zh": "补充的个人简介。"}
```

### 奖项 / 经历

教育与工作记录在“个人履历 / Background”中按本科→广汽→硕士→博士顺序合并展示，导航指向 `#background`。`education` 与 `experience` 保留各自数据结构；英文硕士学位显示为 `Master’s degree`。工作记录只填写已确认的单位、活动和年份，不要求职位或地点。`awards` 为空时不渲染栏目。每条记录的格式如下；仅用你的真实信息替换示例：

```json
{
  "title": {"en": "Title", "zh": "名称"},
  "detail": {"en": "Institution or description", "zh": "机构或说明"},
  "period": {"en": "Year or date range", "zh": "年份或时间段"}
}
```

### 新论文

复制一个已有的 `publications` 条目并更新：

- `id`：独一无二的小写英文或数字标识，可包含连字符。
- `title` / `authors` / `year` / `venue`：以正式出版版本或经你核实的记录为准。
- `type`：期刊用 `article`，会议用 `inproceedings`。
- `equal_contributors`：只有确证共同贡献的作者才填入；不会自动根据作者顺序判断。
- `doi` / `arxiv`：分别只填 DOI 或 arXiv 编号，脚本会生成链接。
- `code_url` / `project_url` / `paper_url`：可选，留空不会产生失效按钮。
- `thumbnail`：可选，放入有权使用的论文配图后设置相对路径；留空则显示纯文字卡片。原图同时填写 `thumbnail_width`、`thumbnail_height`、双语 `thumbnail_alt` / `thumbnail_caption`、`figure_number` 和带图号锚点的 `figure_source`。
- `abstract`：完整实际英文摘要及忠实完整中文译文（`en` / `zh`），不得填入原创概述。`abstract_evidence` 必须记录 `status`、`source`、`version`、题目和作者；未取得原文时设 `abstract: null`、`status: "missing"` 并说明原因，页面明确显示待核验。来源及版本差异同时记录在 `SOURCES.md`。

## 5. 文件说明

```text
index.html              已生成的首页，可直接打开或部署
profile.json            集中维护的个人资料与论文数据
build.py                无第三方依赖的构建脚本
publications.bib        已列论文的 BibTeX
.nojekyll               GitHub Pages 静态分支发布标记
assets/style.css        样式与响应式布局
assets/main.js          语言切换、年份筛选、复制功能
assets/favicon.svg      FH 网站图标
assets/images/          放入你的照片或论文配图
templates/page.html     HTML 模板
README_CN.md            本说明
SOURCES.md              信息核对来源与设计说明
```

## 6. 读书与随笔及来源维护

当前为所有者选定、经核验或所有者确认的六篇文章，**并非公众号完整目录**。账号为“杂记遣怀”；保留原两篇摘要。清单如下：

- [猎户星座](https://mp.weixin.qq.com/s/xrk3NmYKp0TA-j-8uzsUAA)，署名发成。
- [深宫修罗场——北魏子贵母死制度的黑色幽默](https://mp.weixin.qq.com/s/wZiHg6oNw5ok62wXAi2_vA)，署名何从。
- [魏晋外貌协会大赏——侃《世说新语·容止》](https://mp.weixin.qq.com/s/xRUlN4Pcs_biWIcqLU_5BQ)，署名发成。
- [“闻鸡起舞”少年们的升华人生](https://mp.weixin.qq.com/s/K9kZ77K7tmjc5PLO8gU52w)，署名发成。
- [英雄迟暮《敕勒歌》](https://mp.weixin.qq.com/s/cilRgAzcsfic_dd--5oJGw)，署名发成。
- [我怀念的 约翰 · 丹佛](https://mp.weixin.qq.com/s/qr12cl9yo03XHMPerka75g)，署名未知，省略。

2026-09-28 为核验/确认日期，不是发表日期；六篇均无可靠发表日期，全部省略。前三篇新增历史/文学文章的标题、署名、账号及正文节选已由原生读取核验；原两篇也已有同等范围的核验，响应长度限制不等于取得全文。

约翰·丹佛一篇的准确标题和原始链接由所有者提供，已解决此前缺少原始 URL 的问题。已有搜狗公开正文节选及同名账号/标题支持非常短的摘要：喜欢约翰·丹佛，受父亲影响接触其歌曲。原文提取失败，随后一次普通 curl 请求遇微信验证页后停止；未取得原文正文、署名或日期，不声称已核验这些字段。未再请求来源、绕过验证码或检索全部账号文章。

只展示原文链接和忠实双语短摘要，不翻译或转载全文，不使用封面、视频或嵌入资源。原文弹窗测试以精确 URL 的本地响应验证交互，不能证明微信线上可访问。原始抓取及审计材料不公开。

2026-09-28 所有者提供并授权公众号二维码，公开资源为 `assets/images/wechat-qr.png`。原 JPEG 无 EXIF，但图像结束标记后有未知附加数据，故从解码 RGB 像素构建无元数据 PNG；逐像素验证完整 430×430 画面与全部白边完全一致，无裁切、有损重压缩或重新生成。页面以 180×180、object-fit: contain 展示，点击打开本地全尺寸图，原文件未改动。

每条 `articles` 数据包含：

- `url`：已核验的原始绝对 HTTPS 链接，不含凭证或片段，不重复。
- `title`：准确中文标题，标记中文语言，不虚构译名。
- `author`：可选；仅在署名已核验时提供，存在时必须为非空字符串。未知时删除字段，不显示署名行。
- `category`：简短 `en` / `zh` 编辑分类，均不超过 60 字符。
- `summary`：依据已核验正文或所有者证据撰写的忠实双语短摘要，英文最多 320 字符、中文最多 160 字符。
- `date`：可选，仅在发表日期已核验时填写有效 `YYYY-MM-DD`；不确定则删除该字段。

栏目及导航为 Reading & Essays / 读书与随笔，保留 `#reading-notes`。英文按钮 Read in Chinese，中文按钮 阅读原文。只链接原文，不转载或翻译全文，不嵌入视频、不热链图片或跟踪资源。构建检查双语字段、日期、重复及安全 URL，并转义内容；来源身份须另行核验。空数组继续提供真实空状态。

## 7. 构建、验证与发布交接

```sh
python3 build.py
python3 -m unittest discover -s tests -v
```

回归测试覆盖构建确定性、生成文件同步、已核验来源字段、空及非空读书笔记、双语内容、HTML 转义以及非法 URL、日期、缺项和摘要长度。构建仅依赖 Python 标准库；图片回归测试另需 Pillow。新增摘要来源对照测试还需本地已核验原始证据 `.local-audit/deepaoa-openalex.json` 与 `.local-audit/fastset-semanticscholar.json`，缺失时测试失败，不跳过核验。
本次合并的原生浏览器检查由父端运行，保持 chromium_sandbox=True，覆盖桌面 1440×1000、手机 390×844 双语资料、六卡片、二维码及既有摘要、引用、筛选与图片交互。浏览器脚本和交付脚本保存在忽略的本地审计目录；本地构建和测试不代表线上验收通过。

本地预览可在项目根目录执行 `python3 -m http.server 8000 --bind 127.0.0.1` 后打开本机地址。仅本机使用，避免暴露审计文件。
沿用现有 Pages 配置，检查已存在的仓库与部署设置，无需重复创建仓库。发布前审阅准确的文件清单、工作区与暂存 diff，按第 3 节完成发布和实际部署确认。
本地审计目录、工具元数据、凭证和私人路径不属于发布内容。推送或构建成功不等于线上验收通过。

## 8. 授权图片维护

所有者明确授权自己的肖像及 Prism、Saga 的作者稿图 2 用于本人主页。肖像经过 EXIF 方向归一化后自然裁切为 400×400，再保存为无私人元数据的 RGB JPEG；没有生成式修改、修饰或背景替换。原始文件保持不变，私人路径与哈希证据仅存于忽略的本地审计目录。

Prism 与 Saga 论文图保留完整画面与原始解码像素，仅移除附加元数据；点击图片打开本地全尺寸文件，图下仅显示语义说明，作者稿来源与图号保存在 `SOURCES.md`，授权不等同于声明 arXiv 通用许可为 CC。FastSET 与 DeepAoA+ 已使用所有者提供的完整画幅 JPEG，历史处理为有损重编码，不声明像素完全相同；详情见 SOURCES.md。四张论文图、肖像和 BibTeX 在本次合并中保持基线字节不变。新二维码使用逐像素一致的无元数据 PNG。构建使用标准库，图片测试使用 Pillow。

## 9. pages928-bio-abstracts 交接

本次更新完整双语简介、教育与搜索元数据，博士入学年份现采用所有者于 2026-09-29 确认的 2024 年。Prism 与 Saga 使用本地 arXiv v1 的完整实际摘要及完整中文译文。FastSET 与 DeepAoA+ 分别使用已核验 Semantic Scholar 完整摘要字段及 OpenAlex 无缺口、无重复位置的完整倒排索引摘要，并附完整中文译文。四篇实际摘要均已具备；第三方索引版本、API 端点和唯一的数值排版归一化见 `SOURCES.md`。

摘要使用原生 `details` / `summary`，支持键盘展开和语言切换，全文存在 HTML 中，不截断。论文作者、共同贡献、出版年份和 BibTeX 不变；肖像与原图资源不变。

运行 `python3 build.py` 和 `python3 -m unittest discover -s tests -v`。本次原生浏览器脚本仅存于忽略目录 `.local-audit/pages928-bio-abstracts-verify_browser.py`，可在本机预览服务或 https://pardonhu.github.io 上执行只读验证，Chromium sandbox 必须保持开启；本次任务不提交、推送或部署。

本科院系和专业英文分别采用忠实译法 “School of Mechanical Engineering and Power Engineering” 与 “Mechanical Engineering (Pilot Class)”；硕士“计算机专业”译为 “Computer Science”，博士“信息与通信工程”译为 “Information and Communication Engineering”。这些是本站编辑译文，不声称为校方官方英文项目名。

页面顶部采用独立静态星空装饰带：CSS 星点和内联 SVG 星座线条，不覆盖正文、图片或二维码，不捕获交互；无动画、外部素材或新增依赖，保留浅色学术版式和减少动态效果支持。
