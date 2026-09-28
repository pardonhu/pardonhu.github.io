# 胡发成 / Facheng Hu — 个人学术主页

这是一份已经生成好的静态网站。直接打开 `index.html` 即可预览，不需要安装 Node.js、Ruby、Jekyll 或任何第三方包。它目前只是本地交付文件，**尚未发布到互联网，也没有创建或修改任何 GitHub 仓库**。

## 1. 本版内容

- 姓名：Facheng Hu / 胡发成。
- 身份：上海交通大学 Global College 博士研究生；导师：皮宜博老师（Yibo Pi）。
- 联系邮箱：`facheng_hu@sjtu.edu.cn`。
- GitHub：`pardonhu`；预配置的个人站点地址：`https://pardonhu.github.io/`（本文件包不代表已上线）。
- 教育经历：2024 年春季起的博士阶段；未臆造此前学历。
- 代表性论文：FastSET（SECON 2026）、Prism、Saga、DeepAoA+。FastSET 已置于首位，并加入 2026 年动态和年份筛选。已有论文链接与 BibTeX 保留。
- 没有预设新的科研方向；`research_interests` 默认留空。
- 没有填写未经提供的奖项、访问经历、简历或学术账号。
- 当前头像为 FH 字母标识，不是合成的人物照片；论文封面是文字装饰卡，不是论文实验图。

默认英文，右上角可切换中文。论文正式标题与作者姓名在两种语言下均保留英文。页面适配手机和电脑；可以按年份筛选论文、展开及复制引用。页面没有访客跟踪、统计脚本、外部字体、第三方 JavaScript 或登录功能。出版页面、学校和导师链接只在访客点击时打开。

## 2. 后续可维护的资料

| 字段 | 在哪里修改 | 说明 |
| --- | --- | --- |
| GitHub 用户名 | `profile.json` → `github_username` | 已填 `pardonhu`。不要填密码、Token、验证码或完整网址。留空时不显示 GitHub 按钮。 |
| 个人照片 | 将图片放入 `assets/images/`，设置 `portrait` | 例如 `assets/images/profile.jpg`。留空时保留 FH 标识。 |
| Google Scholar | `google_scholar` | 填自己的完整主页链接；留空时不显示。 |
| ORCID | `orcid` | 可选；填自己的完整链接。 |
| 简历 PDF | `cv_url` | 放入网站目录后填写相对路径；也可以填写外部网址。留空时不显示。 |
| 研究兴趣 | `research_interests` | 等正式确定后再填写；不会根据导师论文自动推测。 |
| 其他论文 | `publications` | 在核对最终题目、作者、发表状态和链接后添加。 |

只填 GitHub 用户名并不会授予别人操作账号的权限。发布需要你自己登录 GitHub，或在可信的连接工具中另行授权；不要在聊天中发送密码、验证码或访问令牌。

## 3. 部署到 GitHub Pages

以下为 GitHub 官方当前文档对应的分支发布方式，资料来源见 `SOURCES.md`。

1. 登录你的 GitHub，创建名为 **`pardonhu.github.io`** 的仓库。GitHub Free 使用公开（Public）仓库。若同名主页仓库已经存在，先备份并检查现有内容，不要直接覆盖。
2. 将本文件夹中的文件上传到仓库根目录。最重要的是 `index.html`、`assets/` 和 `.nojekyll`；也可将 `profile.json`、`build.py`、`templates/` 一起保存，便于维护。**不要再套一层 `pardonhu.github.io/` 文件夹**，否则根路径可能找不到首页。
3. 打开仓库 **Settings → Pages → Build and deployment**，将 **Source** 设为 **Deploy from a branch**，选择 **main** 分支和 **/(root)**，点击 **Save**。
4. 等待部署完成，在 Pages 页面点击 **Visit site**。个人站点通常位于 `https://pardonhu.github.io/`。首次或后续发布可能需要数分钟，不以本地预览成功代替线上部署核验。

用户名包含大写字母时，个人主页仓库名采用小写。所有上传到公开仓库的源码、配置和文件均可被公开访问，部署前请检查整个文件夹；不要加入学号、证件、私人通信、内部项目材料或任何凭证。`.nojekyll` 是空文件，用于静态分支部署时跳过 Jekyll 处理；部分文件管理器可能将它隐藏。

### FastSET 出版信息

本版作者顺序采用 2026-09-28 核验的公开 IEEE SECON 2026 论文集目录：Facheng Hu、Yunzhe Li、Hongzi Zhu、Xudong Wang。
本次未取得可核验的 DOI 或全文入口，因此没有编造这两项：该条目的标题与“论文集目录”按钮链接到目录第 4 页，而不是冒充论文全文 PDF。BibTeX 保留已核对的标题、作者、会议和年份，没有推测页码范围或 DOI。
后续拿到正式 DOI 后，填入 `profile.json` 中该条目的 `doi`，执行 `python build.py`，页面会自动使用 DOI 并显示出版页面按钮；拿到可公开分享的论文版本后再补 PDF。

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

构建脚本仅使用 Python 标准库。它会重新生成 `index.html` 和 `publications.bib`；无需安装任何 Python 包。之后重新打开或刷新 `index.html`，再上传修改后的文件。**不要只改 `profile.json` 而不重新构建**，因为线上页面读取的是生成后的 `index.html`。

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
- `thumbnail`：可选，放入有权使用的论文配图后设置相对路径；否则使用文字装饰封面。
- `description`：中英文各写一句对工作内容的准确概括，不要添加未证实的提升数字或排名。

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

## 6. 原始文件包所记录的验证范围（本阶段未复验）

本次使用 Chromium 直接载入完整预览 HTML，检查桌面和手机排版、中英文切换、2026 年份筛选、FastSET 引用展开，以及关闭 JavaScript 后的正文可读性。320、375、390、768、1024、1440 像素视口的两种语言及展开的引用框均未发现横向溢出，未出现 JavaScript 错误。另对部署版 index.html 核对了邮箱、GitHub、canonical 地址、本地资源和页内链接。

本环境的浏览器策略阻止直接访问 file:// 本地地址，因此没有声称完成本地 URL 导航测试；截图与交互检查使用内嵌同一 CSS、JavaScript 和页面正文的独立预览版。

没有创建或修改 GitHub 仓库，没有进行线上部署，也没有冒充已完成线上测试。部署后仍需在 Settings → Pages 确认成功，并打开实际网址核验。外部站点的可用性及系统剪贴板权限可能随网络和浏览器变化。

## 7. 本地检查与后续维护

本阶段已将压缩包外层目录展开至项目根目录，目录结构见第 5 节。
现有静态发布入口为根目录 `index.html` 与 `.nojekyll`，无需另建部署工作流。
执行 `python3 build.py` 成功，生成的首页和 BibTeX 与原文件包逐字节一致。
个人资料、论文作者顺序和发表状态、导师及研究兴趣字段保持原样。

预览：在项目根目录执行 `python3 -m http.server 8000 --bind 127.0.0.1`，
浏览器打开 `http://127.0.0.1:8000/`。该命令会暴露工作目录中的文件，只在本机使用。
发布前检查：构建成功、本地资源无缺失、中英文切换、各年份筛选、引用展开，
以及桌面和手机宽度下无横向溢出；检查 Git diff 和待提交文件的公开适宜性。
本阶段仅完成构建及静态资源检查：环境拒绝 socket 操作，本地 HTTP 服务、
浏览器启动和 GitHub API 请求受阻，因此没有完成 HTTP、桌面/手机交互或远端验收。
第 6 节是原始文件包的历史记录，不代表本阶段已复验。

后续发布必须获得明确授权才可提交或推送。先确认 GitHub 登录账号为 `pardonhu`，
只读核对远端历史、内容和 Pages 配置；已有部署方式优先复用。
远端不存在时才创建公开仓库；不能仅根据未认证请求的 404 判断不存在。
安全合并后检查暂存 diff，仅逐项添加必要网站文件和维护源文件，禁止使用未经审查的全目录添加。
`.local-audit/`、工具元数据、运行日志、检查脚本、内部规则及个人路径不得发布。
推送后跟踪实际 Pages build/deploy，再核验线上首页、资源和交互；推送成功不等于上线完成。

回退：确认有明确推送授权后，用 `git revert <需撤销的提交>` 创建新提交，
检查变更、重新本地验证后推送，再跟踪部署和线上结果。
禁止强推或改写历史；不要删除未知远端文件。
