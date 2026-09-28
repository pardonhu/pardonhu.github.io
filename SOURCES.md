# 内容来源与设计说明

核对日期：2026-09-28。

## 个人资料

GitHub 用户名 `pardonhu` 和邮箱 `facheng_hu@sjtu.edu.cn` 由主页所有者在本次更新中明确提供。站点地址为 `https://pardonhu.github.io/`；已部署基线为 `1d1e8bcf338a27f81382c734063c4cf77a5569cf`。

姓名、IEEE 研究生会员身份、2017 年理学学士学位、2024 年上海交通大学硕士学位（导师朱洪紫教授）、当前在上海交通大学 Global College 攻读博士（导师皮宜博教授），以及人工智能赋能的网络和无线感知研究兴趣，均依据所有者在 pages928-bio-abstracts 任务中的明确授权。未提供本科院校或博士入学年份，因此不填写。此次授权覆盖此前的博士入学年份表述。

公开成员资料也列出 Facheng Hu 及学校邮箱：
https://lion.sjtu.edu.cn/member/memberDetail?id=53

没有将资格考试信息、学号、私人通信或内部项目材料写入网页。默认写 `Ph.D. Student`，没有把 `Ph.D. Candidate` 资格作为已确认事实。

## 论文

### FastSET / IEEE SECON 2026（基线已收录）

- 论文集目录（第 4 个 PDF 页面）：https://www.proceedings.com/content/086/086473webtoc.pdf#page=4
- 目录确认：FastSET: Fast Sequential Retraining to Accelerate Real-Time Online Adaptation for Neural Receivers。
- 目录所列作者顺序：Facheng Hu、Yunzhe Li、Hongzi Zhu、Xudong Wang。
- 卷名：2026 22nd Annual IEEE International Conference on Sensing, Communication, and Networking (SECON 2026)。
- 基线核验记录已逐项查看目录页面；本次保留该记录。目录列出起始页 152；本次 IEEE 提交至 Crossref 的正式页码为 150–158，二者存在差异，本站采用正式记录，保留目录为历史证据。
- 正式 DOI：https://doi.org/10.1109/SECON68281.2026.11579146 。IEEE 发表记录：https://ieeexplore.ieee.org/document/11579146/ 。核验接口：https://api.crossref.org/works/10.1109/SECON68281.2026.11579146 （HTTP 200）；确认题目、四位作者、150–158 页及 2026 年 6 月 3–5 日 Pisa 会议。未取得公开全文。
- 此前的一句话简介已移除；完整摘要状态见文末逐篇证据。

### Prism / IEEE INFOCOM 2025

- 作者稿与正式出版记录关联：https://arxiv.org/abs/2501.01598
- 作者稿正文（共同贡献说明）：https://arxiv.org/html/2501.01598v1
- 正式 DOI：https://doi.org/10.1109/INFOCOM55648.2025.11044768

### Saga / IEEE ICDCS 2025

- 作者所在实验室记录：https://lion.sjtu.edu.cn/publication/publicationDetail?id=137
- 作者稿与正式出版记录关联：https://arxiv.org/abs/2504.11726
- 作者稿正文（共同贡献说明）：https://arxiv.org/html/2504.11726v1
- 正式 DOI：https://doi.org/10.1109/ICDCS63083.2025.00090

本版题目采用论文正文和实验室发表记录中的短题目，以 `IMU Data` 结尾。arXiv 摘要页的题目另带有 `for User Perception`，没有将这种差异忽略或虚构成另一篇论文。

### DeepAoA+ / IEEE Transactions on Vehicular Technology 2024

- 作者所在实验室记录（作者、卷期与页码）：https://lion.sjtu.edu.cn/publication/publicationDetail?id=128
- IEEE 页面：https://ieeexplore.ieee.org/document/10638788/
- 正式 DOI：https://doi.org/10.1109/TVT.2024.3445722

作者列表采用实验室正式条目中的六位作者，没有复制旧个人主页中不同的待发表作者列表。本版未推断其共同一作标记。

此前的原创一句话概述已移除，改用经核验的完整英文摘要及完整中文译文；四篇摘要均已取得，逐篇证据见文末。论文的著作权属于相应权利人；本项目不打包转载原文 PDF。本轮仅纳入所有者明确批准的两张作者稿原图；缺图论文不使用装饰封面。

## 设计参考

- 用户指定的参考站：https://haifengjia.github.io/
- 参考站页脚所指模板：https://github.com/luost26/academic-homepage

本版借鉴简介卡、动态、教育经历、论文条目等学术信息组织方式，以独立 HTML/CSS/JavaScript 重新实现。不是对原仓库的 fork，也没有复制 Haifeng Jia 的个人资料、照片、论文配图或统计脚本。

## GitHub Pages 官方部署依据

- 建站、仓库命名与公开可见性：
  https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- 分支发布设置：
  https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

仓库设置界面可能随 GitHub 更新发生变化；需要以实际页面为准。pages928-update 是从上述部署基线开始的已授权更新，本轮图片增量已通过本地构建、回归测试和启用 Chrome sandbox 的桌面/手机图片渲染及交互验收。实际发布版本以 https://github.com/pardonhu/pardonhu.github.io/actions 中对应提交的 Pages 成功记录及线上验收为准。维护流程为检查 diff、精确暂存、提交推送、等待对应提交的 Pages 部署、执行线上测试；详见 `README_CN.md`。

## pages928-update 核验补充

- IEEE 发表记录：https://ieeexplore.ieee.org/document/11044768/ 。本次以 IEEE 向 Crossref 提交的元数据核验，接口为 https://api.crossref.org/works/10.1109/INFOCOM55648.2025.11044768 。确认题目、八位作者顺序、页码 1–10、INFOCOM 2025，以及 2025-05-19 至 2025-05-22 在英国伦敦举行的会议信息。
- 日期须区分：作者稿 HTML v1 标注 2025-01-03；Crossref 的 published / published-print 为 2025-05-19。Crossref created / deposited 的 2025-09-12 是元数据登记时间，不替代论文发表日期。
- 阅读作者稿正文的 NID 检测、EM 域估计和在线推理部分及相关图注后，独立撰写中英文短简介。NID 基于预测不一致性；EM 联合优化任务相关域与模型；设备端按特征空间的最近域选择模型。没有将实验条件下的数值改写为普遍性能承诺。
- IEEE document 请求返回 202 空正文，abstract 入口和作者页返回 418；其他提取仅见公共页脚。未直接取得 IEEE 全文、作者简介或肖像。arXiv 摘要页关联正式 DOI；共同贡献依据作者稿 v1 的明确说明，而非 Crossref 作者排序。
- 所有者提供的 IEEE 作者主页：https://ieeexplore.ieee.org/author/996384661373839 。作为所有者提供的链接展示，不据此增加任何身份、研究兴趣或任职事实。SJTU 成员 id53 本次连接无正文；保留此前核验的资料，不声称本次重新取得正文。本轮头像使用所有者另行提供并授权的肖像。
- 读书笔记公众号名“杂记遣怀”由所有者明确确认。尚未核验具体公开文章身份及原始 URL，因此账号不带猜测链接，文章数组为空；不将同名搜索结果归属于该账号。后续仅收录经人工核验的原始 HTTPS 链接、准确标题、日期和原创双语短摘要。程序校验格式不能替代文章身份核验。

公开搜索补充：搜狗微信文章搜索出现同名账号下的候选《我怀念的 约翰 · 丹佛》，但未核验原始 URL、日期或与所有者的身份关联，未将其收录为文章。账号搜索未找到相关官方认证订阅号，不能据此断言账号不存在；Google 提取仅得搜索外壳，Bing 结果无身份佐证。已请求所有者提供公众号公开主页、原文链接或二维码，再核验归属、准确标题与日期。

## pages928-images 授权原图

所有者明确授权肖像及以下本人论文概览/引言图用于个人主页。未依据 arXiv 的通用说明推定 CC 许可；著作权仍归相应权利人。仅公开处理后的肖像与两张获批准的图，不打包全文。

- `assets/images/portrait.jpg`：所有者提供的照片，经方向归一化、自然裁切为 400×400，保留脸部、头发、抬起的手臂和上半身；RGB JPEG，移除 EXIF/GPS/XMP/IPTC/注释。未修饰、生成或替换背景。原文件只读且哈希核验不变；私人来源路径不公开。
- `assets/images/prism-overview.png`：Prism 作者稿 Figure 2，System architecture of Prism。完整原图，722×547；IMU 数据先检测非独立同分布特性，再划分用于训练。来源：https://arxiv.org/html/2501.01598v1#S2.F2 ，图片：https://arxiv.org/html/2501.01598v1/prism.png 。替代此前概念 SVG。
- `assets/images/saga-overview.png`：Saga 作者稿 Figure 2，Overview of Saga，包含 Multi-level Masking、Models Training、Low Cost Weight Searching。完整原图，实际解码尺寸为 1411×374。来源：https://arxiv.org/html/2504.11726v1#S2.F2 ，图片：https://arxiv.org/html/2504.11726v1/overview.png 。

两张图的公开衍生文件与已下载原图的解码像素和尺寸完全一致，移除附加元数据。页面保留双语替代文本、语义图注和本地全尺寸图片链接。按本次授权移除访客可见的作者稿、图 2 来源标签与按钮；原图图号和来源继续记录于本文件。

FastSET 与 DeepAoA+ 尚未取得实际原图。DeepAoA+ 实验室链接连接关闭，IEEE 10638788 提取无正文，arXiv 检索无匹配；FastSET arXiv 结果不匹配作者，IEEE 11579146 返回 202 空正文。未绕过访问控制或使用内部材料，保留纯文字卡片。已请求所有者提供原始 PDF 或图文件及图号、图注，待收到后补充。

## pages928-bio-abstracts 摘要证据（本地核验）

先阅读现有本地来源文档，再提取实际摘要。Prism 与 Saga 英文仅折叠 HTML 排版空白；DeepAoA+ 按索引位置重建，FastSET 仅作下述数值排版归一化；均不改写、删节或拼接正文；中文为对应完整译文，不是出版方提供的官方译文。作者及出版历史保持不变。

### FastSET

- 题目：FastSET: Fast Sequential Retraining to Accelerate Real-Time Online Adaptation for Neural Receivers
- 作者（原顺序）：Facheng Hu, Yunzhe Li, Hongzi Zhu, Xudong Wang
- 摘要核验 API（精确端点）：https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/SECON68281.2026.11579146?fields=title,authors,externalIds,abstract
- 版本：Semantic Scholar Graph API v1 third-party indexed abstract, paperId 5810e7106cf3c9189355dfa694ca5aac331109b9; public API retrieved 2026-09-28 (no abstract revision timestamp supplied).
- 证据：父任务于 2026-09-28 使用 curl 直接从公开 API 获取的原始 JSON `fastset-semanticscholar.json`，位于本地 `.local-audit/`；SHA-256：`62221391cbdd552be06eb2cd1b84292e0fcf66c99d3893d4dc2a6b7283aaa97d`。这是第三方索引摘要，未直接从出版方取得摘要。
- 逐项核对：DOI、题目一致，四位作者顺序一致；索引第二作者写作 `Yun-Zhe Li`，原论文列表为 `Yunzhe Li`。仅在此记录拼写变体，论文作者列表保持原样。
- 提取完整 `abstract` 字段；唯一显示归一化：`$\mathbf{5. 1}-\mathbf{5. 9} \times$` → `5.1–5.9 ×`，去掉数字粗体 LaTeX、数字内部空格，以可访问纯文本显示小数范围和乘号，含义不变。保留索引中的 `twostage` 等其他全部英文。中文完整保留 3GPP TDL、频域 OFDM、射线追踪场景、5.1–5.9 倍适应速度及相对基线 BER 退化不超过 3% 的主张。

### Prism

- 题目：Prism: Mining Task-aware Domains in Non-i.i.d. IMU Data for Flexible User Perception
- 作者（原顺序）：Yunzhe Li, Facheng Hu, Hongzi Zhu, Quan Liu, Xiaoke Zhao, Jiangang Shen, Shan Chang, Minyi Guo
- 摘要来源：https://arxiv.org/html/2501.01598v1#abstract1
- 版本：arXiv:2501.01598v1
- 证据：现有本地 `prism-author-manuscript.html` 的 `abstract1.1` 完整段落；全部英文及中文译文存于 `profile.json` 的 `abstract`，构建写入 HTML，原生展开控件无需 JavaScript 即可打开。

### Saga

- 题目：Saga: Capturing Multi-granularity Semantics from Massive Unlabelled IMU Data
- 作者（原顺序）：Yunzhe Li, Facheng Hu, Hongzi Zhu, Shifan Zhang, Liang Zhang, Shan Chang, Minyi Guo
- 摘要来源：https://arxiv.org/html/2504.11726v1#abstract1
- 版本：arXiv:2504.11726v1
- 证据：现有本地 `saga-author-manuscript.html` 的 `abstract1.1` 完整段落；全部英文及中文译文存于 `profile.json` 的 `abstract`，构建写入 HTML，原生展开控件无需 JavaScript 即可打开。

### DeepAoA+

- 题目：DeepAoA+: Online Cross-Domain Vehicular Relative Direction Estimation via Deep Learning
- 作者（原顺序）：Facheng Hu, Yunxiang Cai, Hongzi Zhu, Shan Chang, Xudong Wang, Minyi Guo
- 摘要核验 API（精确端点）：https://api.openalex.org/works/https://doi.org/10.1109/TVT.2024.3445722
- 版本：OpenAlex third-party indexed abstract, W4401692172; updated_date 2026-09-21T07:43:02.447757; public API retrieved 2026-09-28.
- 证据：父任务于 2026-09-28 使用 curl 直接从公开 API 获取的原始 JSON `deepaoa-openalex.json`，位于本地 `.local-audit/`；SHA-256：`f5e09d027a35c6ebaa998ffd4be0c153f99e307ab07947b689569d2267e4650c`。这是第三方索引摘要，未直接从出版方取得摘要。
- 逐项核对：题目及六位作者原顺序完全一致；API DOI 为 `10.1109/tvt.2024.3445722`，与 profile DOI 仅大小写不同。倒排索引共 239 个位置，覆盖 0–238，缺口 0、重复 0；按编号重建全部词与标点，不补写句子。保留索引中的 `non-i.i.d(independent` 等原始排版。

Saga 的 HTML v1 题目使用上述短题目，摘要页的题目另带 `for User Perception`，本次不改动论文题目历史。英文中“over 90% accuracy of the full-fledged model”译为达到该完整模型准确率的 90% 以上，不误写成绝对准确率超过 90%。
