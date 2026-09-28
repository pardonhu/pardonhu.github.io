# 胡发成 / Facheng Hu — 个人学术主页

这是一份已经生成好的静态网站。直接打开 `index.html` 即可预览，不需要安装 Node.js、Ruby、Jekyll 或任何第三方包。本次 pages928-update 从已部署基线 `1d1e8bcf338a27f81382c734063c4cf77a5569cf` 开始，属于已授权的增量图片更新，已完成本地构建、回归测试及原生浏览器图片与交互验收。实际发布版本以[仓库 Pages 部署记录](https://github.com/pardonhu/pardonhu.github.io/actions)中对应提交的成功结果及线上验收为准。

## 1. 本版内容

- 姓名：Facheng Hu / 胡发成。
- 身份：上海交通大学 Global College 博士研究生；导师：皮宜博老师（Yibo Pi）。
- 联系邮箱：`facheng_hu@sjtu.edu.cn`。
- GitHub：`pardonhu`；个人站点地址：`https://pardonhu.github.io/`。
- 教育经历：2017 年理学学士、2024 年上海交通大学硕士（导师朱洪紫教授），现为 Global College 博士研究生（导师皮宜博教授）；不填写未提供的本科院校和博士入学年份。
- 代表性论文：FastSET（SECON 2026）、Prism、Saga、DeepAoA+。FastSET 已置于首位，并加入 2026 年动态和年份筛选。已有论文链接与 BibTeX 保留。
- 研究兴趣：人工智能赋能的网络和无线感知；IEEE 研究生会员身份及完整双语简介由所有者明确提供。
- 没有填写未经提供的奖项、访问经历、简历或学术账号。
- 头像为所有者授权的自然摄影裁切；Prism 与 Saga 使用获授权的作者稿图 2，保留双语语义图注及本地全尺寸图片链接，图号与来源保存在 `SOURCES.md`。FastSET 和 DeepAoA+ 保持纯文字卡片。

默认英文，右上角可切换中文。论文正式标题与作者姓名在两种语言下均保留英文。页面适配手机和电脑；可以按年份筛选论文、展开及复制引用。页面没有访客跟踪、统计脚本、外部字体、第三方 JavaScript 或登录功能。出版页面、学校和导师链接只在访客点击时打开。

## 2. 后续可维护的资料

| 字段 | 在哪里修改 | 说明 |
| --- | --- | --- |
| GitHub 用户名 | `profile.json` → `github_username` | 已填 `pardonhu`。不要填密码、Token、验证码或完整网址。留空时不显示 GitHub 按钮。 |
| 个人照片 | 将图片放入 `assets/images/`，设置 `portrait` | 例如 `assets/images/profile.jpg`。留空时保留 FH 标识。 |
| Google Scholar | `google_scholar` | 填自己的完整主页链接；留空时不显示。 |
| ORCID | `orcid` | 可选；填自己的完整链接。 |
| 简历 PDF | `cv_url` | 放入网站目录后填写相对路径；也可以填写外部网址。留空时不显示。 |
| 完整简介 | `bio` → `en` / `zh` | 按所有者确认的双语全文维护；不推断本科院校或博士入学年份。 |
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

`awards` 和 `experience` 默认为空数组，不渲染空白栏目。每条记录的格式如下；仅用你的真实信息替换示例：

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

## 6. 读书笔记与来源维护

`profile.json` 是数据源。`ieee_author_profile` 是所有者提供的作者主页链接；访问限制见 `SOURCES.md`，不据此推断个人资料。
Prism 的 `publication_record` 是 IEEE 发表记录，`pages` 为 Crossref 核验的 1–10 页；`thumbnail_alt` 与 `thumbnail_caption` 维护配图说明。

公开搜索曾在搜狗微信结果中发现同名账号下的候选《我怀念的 约翰 · 丹佛》，但原始 URL、日期与所有者身份关联尚未核验，因此未收录。已请求所有者提供公众号公开主页、原文链接或二维码，收到后再核验归属与文章信息。

`reading_notes` 包含 `account_name`（目前为“杂记遣怀”）与 `articles`（目前为空）。空数组只显示真实账号与尚无核验链接的状态，不生成占位文章。核验文章身份后，每条须包含：

- `url`：真实文章的原始绝对 HTTPS URL，不含账户凭证或片段；不填猜测链接。
- `title`：原文准确标题，不要求虚构译名。
- `date`：原文日期，格式 `YYYY-MM-DD`，必须为有效日历日期。
- `summary`：原创 `en` 和 `zh` 短摘要，分别最多 320 和 160 个字符，均不得为空。

构建拒绝缺项、错误格式和过长摘要，并转义渲染内容。程序只能检查格式；原始链接归属、准确标题和日期仍须人工核验。测试用例中的合成样本仅在临时目录渲染，不写入生产网站数据；测试源码本身可能随公开仓库发布。

## 7. 构建、验证与发布交接

```sh
python3 build.py
python3 -m unittest discover -s tests -v
```

回归测试覆盖构建确定性、生成文件同步、已核验来源字段、空及非空读书笔记、双语内容、HTML 转义以及非法 URL、日期、缺项和摘要长度。测试仅依赖 Python 标准库。新增摘要来源对照测试还需本地已核验原始证据 `.local-audit/deepaoa-openalex.json` 与 `.local-audit/fastset-semanticscholar.json`，缺失时测试失败，不跳过核验。
本轮图片更新已通过启用 Chrome sandbox 的本地原生浏览器验收，包括肖像完整显示、两张论文图保持原比例以及点击打开全尺寸原图，同时复验：桌面 1440×1000、手机 390×844 的双语切换、所有年份筛选、导航、引用展开/关闭及剪贴板复制、图片与资源加载、无横向溢出、无 JavaScript 错误，以及禁用 JavaScript 后的内容可读性。已查看英文桌面与中文手机截图；截图在复制提示消失后采集。后续更新应重复这些检查，并在 Pages 部署完成后执行线上验收。

本地预览可在项目根目录执行 `python3 -m http.server 8000 --bind 127.0.0.1` 后打开本机地址。仅本机使用，避免暴露审计文件。
沿用现有 Pages 配置，检查已存在的仓库与部署设置，无需重复创建仓库。发布前审阅准确的文件清单、工作区与暂存 diff，按第 3 节完成发布和实际部署确认。
本地审计目录、工具元数据、凭证和私人路径不属于发布内容。推送或构建成功不等于线上验收通过。

## 8. 授权图片维护

所有者明确授权自己的肖像及 Prism、Saga 的作者稿图 2 用于本人主页。肖像经过 EXIF 方向归一化后自然裁切为 400×400，再保存为无私人元数据的 RGB JPEG；没有生成式修改、修饰或背景替换。原始文件保持不变，私人路径与哈希证据仅存于忽略的本地审计目录。

论文图保留完整画面与原始解码像素，仅移除附加元数据；点击图片打开本地全尺寸文件，图下仅显示语义说明，作者稿来源与图号保存在 `SOURCES.md`，授权不等同于声明 arXiv 通用许可为 CC。FastSET 与 DeepAoA+ 尚缺原始 PDF 或图文件、图号及图注，收到所有者资料后再补。仅发布肖像与两张批准的论文图，不发布全文。构建和主 unittest 仍仅使用标准库；Pillow 仅用于本地图片处理及忽略目录内的离线审计脚本。

## 9. pages928-bio-abstracts 交接

本次更新完整双语简介、教育与搜索元数据，移除不受支持的博士入学年份。Prism 与 Saga 使用本地 arXiv v1 的完整实际摘要及完整中文译文。FastSET 与 DeepAoA+ 分别使用已核验 Semantic Scholar 完整摘要字段及 OpenAlex 无缺口、无重复位置的完整倒排索引摘要，并附完整中文译文。四篇实际摘要均已具备；第三方索引版本、API 端点和唯一的数值排版归一化见 `SOURCES.md`。

摘要使用原生 `details` / `summary`，支持键盘展开和语言切换，全文存在 HTML 中，不截断。论文作者、共同贡献、出版年份和 BibTeX 不变；肖像与原图资源不变。

运行 `python3 build.py` 和 `python3 -m unittest discover -s tests -v`。本次原生浏览器脚本仅存于忽略目录 `.local-audit/pages928-bio-abstracts-verify_browser.py`，可在本机预览服务或 https://pardonhu.github.io 上执行只读验证，Chromium sandbox 必须保持开启；本次任务不提交、推送或部署。
