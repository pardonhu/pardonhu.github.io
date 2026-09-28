# 内容来源与设计说明

核对日期：2026-09-28。

## 个人资料

GitHub 用户名 `pardonhu` 和邮箱 `facheng_hu@sjtu.edu.cn` 由主页所有者在本次更新中明确提供。站点地址为 `https://pardonhu.github.io/`；已部署基线为 `35037043115283c4ff84fe6e9fe5c93e08e94f4f`。

个人资料由所有者于 2026-09-28 确认：2017 年在上海交通大学（Shanghai Jiao Tong University）获得工学学士（Bachelor of Engineering）；2024 年在上海交通大学获得硕士学位，导师为朱弘恣教授（Prof. Hongzi Zhu）；2017–2019 年在广汽乘用车（GAC Motor）从事汽车电子电气相关工作（automotive electronics and electrical systems）。保留 IEEE 研究生会员、上海交通大学 Global College 博士在读、导师皮宜博教授（Prof. Yibo Pi）及人工智能赋能的网络和无线感知研究兴趣。ORCID 为 https://orcid.org/0000-0003-0448-8907 ，显示于公开社交链接及 JSON-LD sameAs。未提供的本科专业、院系、导师、起始年份以及工作职位、地点均不填写；博士入学年份也不推测。

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

此前的原创一句话概述已移除，改用经核验的完整英文摘要及完整中文译文；四篇摘要均已取得，逐篇证据见文末。论文的著作权属于相应权利人；本项目不打包转载原文 PDF。本站纳入所有者明确批准的四张论文配图，不使用装饰封面。

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
- 公众号“杂记遣怀”及笔名“发成”“何从”由所有者确认。当前已核验文章与完整性限制见下方“读书与随笔”记录；程序格式校验不能替代来源核验。

公开搜索结果及未收录候选的核验限制见下方“读书与随笔”记录。

## pages928-images 授权原图

所有者明确授权肖像及以下本人论文概览/引言图用于个人主页。未依据 arXiv 的通用说明推定 CC 许可；著作权仍归相应权利人。仅公开处理后的肖像与两张获批准的图，不打包全文。

- `assets/images/portrait.jpg`：所有者提供的照片，经方向归一化、自然裁切为 400×400，保留脸部、头发、抬起的手臂和上半身；RGB JPEG，移除 EXIF/GPS/XMP/IPTC/注释。未修饰、生成或替换背景。原文件只读且哈希核验不变；私人来源路径不公开。
- `assets/images/prism-overview.png`：Prism 作者稿 Figure 2，System architecture of Prism。完整原图，722×547；IMU 数据先检测非独立同分布特性，再划分用于训练。来源：https://arxiv.org/html/2501.01598v1#S2.F2 ，图片：https://arxiv.org/html/2501.01598v1/prism.png 。替代此前概念 SVG。
- `assets/images/saga-overview.png`：Saga 作者稿 Figure 2，Overview of Saga，包含 Multi-level Masking、Models Training、Low Cost Weight Searching。完整原图，实际解码尺寸为 1411×374。来源：https://arxiv.org/html/2504.11726v1#S2.F2 ，图片：https://arxiv.org/html/2504.11726v1/overview.png 。

两张图的公开衍生文件与已下载原图的解码像素和尺寸完全一致，移除附加元数据。页面保留双语替代文本、语义图注和本地全尺寸图片链接。按本次授权移除访客可见的作者稿、图 2 来源标签与按钮；原图图号和来源继续记录于本文件。

### 6cea710 之后的用户供图增量

2026-09-28，所有者直接提供并明确授权 FastSET 环境切换图和 DeepAoA+ 实验装置拼图用于个人主页。来源为用户供图，不推定公开许可；不公开私人来源路径。FastSET 保留原图内嵌的 Fig. 1 及完整英文图注；DeepAoA+ 保留全部照片与设备标签，不推断未提供的图号。两图均完整保留原始画幅与尺寸，无裁切、擦除、重绘或替代图。

公开 JPEG 使用 quality=95、4:4:4 色度采样及优化熵编码；重新构建纯 RGB 像素图以移除 EXIF/GPS/XMP/IPTC 和注释。此为有损 JPEG 保守重编码，未声称像素完全相同。双语替代文本、语义图注、本地完整图片链接沿用现有页面结构；不增加访客可见的来源或处理按钮。原文件保持不变。

- `assets/images/fastset-overview.jpg`：原图与公开图均为 788×528；原图 SHA-256 `bcc34d582646d4648d956dde5d9a1855727ec31186f21d8ae0e6905d69bb6a3c`；公开图 SHA-256 `f73bdcf81eb97366a3fefdf0bd0676b65f81ed4388a8bd963780eb5f233f36f8`；文件大小 110962 → 84129 字节。
- `assets/images/deepaoa-overview.jpg`：原图与公开图均为 776×348；原图 SHA-256 `c3b67dbf8eefaf7513791c915371e86ce763340bd581ba2cfd6240aff7d23696`；公开图 SHA-256 `b5f4ef432a82b78a45b94da73d4ac4c32df277e71c6998bab42d8e543c8fd681`；文件大小 230604 → 151287 字节。

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

## 读书与随笔：六篇选文及来源限制

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

## 公众号入口二维码

2026-09-28 所有者提供并授权公众号二维码，公开资源为 `assets/images/wechat-qr.png`。原 JPEG 无 EXIF，但图像结束标记后有未知附加数据，故从解码 RGB 像素构建无元数据 PNG；逐像素验证完整 430×430 画面与全部白边完全一致，无裁切、有损重压缩或重新生成。页面以 180×180、object-fit: contain 展示，点击打开本地全尺寸图，原文件未改动。
