# 内容来源与设计说明

核对日期：2026-09-28。

## 个人资料

GitHub 用户名 `pardonhu` 和邮箱 `facheng_hu@sjtu.edu.cn` 由主页所有者在本次更新中明确提供。站点地址为 `https://pardonhu.github.io/`；已部署基线为 `1bc00e60510ae91feec1b172e334a94ae337628e`。

中文姓名、英文姓名、当前博士身份、2024 年春季入学、Global College、导师皮宜博和带下划线的联系邮箱，根据主页所有者此前明确提供的资料填写。

公开成员资料也列出 Facheng Hu 及学校邮箱：
https://lion.sjtu.edu.cn/member/memberDetail?id=53

没有将用户尚未确定的研究方向、资格考试信息、学号、私人通信或内部项目材料写入网页。默认写 `Ph.D. Student`，没有把 `Ph.D. Candidate` 资格作为已确认事实。

## 论文

### FastSET / IEEE SECON 2026（基线已收录）

- 论文集目录（第 4 个 PDF 页面）：https://www.proceedings.com/content/086/086473webtoc.pdf#page=4
- 目录确认：FastSET: Fast Sequential Retraining to Accelerate Real-Time Online Adaptation for Neural Receivers。
- 目录所列作者顺序：Facheng Hu、Yunzhe Li、Hongzi Zhu、Xudong Wang。
- 卷名：2026 22nd Annual IEEE International Conference on Sensing, Communication, and Networking (SECON 2026)。
- 基线核验记录已逐项查看目录页面；本次保留该记录。目录列出起始页 152；没有根据下一篇文章的起始页自行推断本篇完整页码，因此不填页码范围。
- 尚未核实正式 DOI 或全文入口。页面提供明确标注的“论文集目录”，不将它标为全文 PDF，也不编造 DOI。
- 一句话简介据标题与主页所有者提供的工作说明重新撰写，不含未经核验的速度或误码率数值。

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

各论文简介为重新撰写的一句话概述，不是论文完整摘要。论文的著作权属于相应权利人；本项目不打包转载原文 PDF。网页中的装饰封面不是论文原图，也不表示实测数据。

## 设计参考

- 用户指定的参考站：https://haifengjia.github.io/
- 参考站页脚所指模板：https://github.com/luost26/academic-homepage

本版借鉴简介卡、动态、教育经历、论文条目等学术信息组织方式，以独立 HTML/CSS/JavaScript 重新实现。不是对原仓库的 fork，也没有复制 Haifeng Jia 的个人资料、照片、论文配图或统计脚本。

## GitHub Pages 官方部署依据

- 建站、仓库命名与公开可见性：
  https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- 分支发布设置：
  https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

仓库设置界面可能随 GitHub 更新发生变化；需要以实际页面为准。pages928-update 是从上述部署基线开始的已授权更新，已通过本地构建、回归测试和启用 Chrome sandbox 的桌面/手机原生浏览器验收。实际发布版本以 https://github.com/pardonhu/pardonhu.github.io/actions 中对应提交的 Pages 成功记录及线上验收为准。维护流程为检查 diff、精确暂存、提交推送、等待对应提交的 Pages 部署、执行线上测试；详见 `README_CN.md`。

## pages928-update 核验补充

- IEEE 发表记录：https://ieeexplore.ieee.org/document/11044768/ 。本次以 IEEE 向 Crossref 提交的元数据核验，接口为 https://api.crossref.org/works/10.1109/INFOCOM55648.2025.11044768 。确认题目、八位作者顺序、页码 1–10、INFOCOM 2025，以及 2025-05-19 至 2025-05-22 在英国伦敦举行的会议信息。
- 日期须区分：作者稿 HTML v1 标注 2025-01-03；Crossref 的 published / published-print 为 2025-05-19。Crossref created / deposited 的 2025-09-12 是元数据登记时间，不替代论文发表日期。
- 阅读作者稿正文的 NID 检测、EM 域估计和在线推理部分及相关图注后，独立撰写中英文短简介。NID 基于预测不一致性；EM 联合优化任务相关域与模型；设备端按特征空间的最近域选择模型。没有将实验条件下的数值改写为普遍性能承诺。
- IEEE document 请求返回 202 空正文，abstract 入口和作者页返回 418；其他提取仅见公共页脚。未直接取得 IEEE 全文、作者简介或肖像。arXiv 摘要页关联正式 DOI；共同贡献依据作者稿 v1 的明确说明，而非 Crossref 作者排序。
- 所有者提供的 IEEE 作者主页：https://ieeexplore.ieee.org/author/996384661373839 。作为所有者提供的链接展示，不据此增加任何身份、研究兴趣或任职事实。SJTU 成员 id53 本次连接无正文；保留此前核验的资料，不声称本次重新取得正文。头像继续使用 FH 字母标识。
- `assets/images/prism-concept.svg` 为本次独立创作的 SVG 概念流程图，仅据方法理解绘制。没有复制或描摹论文图、出版商标志、照片或实测图表；图中形状不表示实验数据。原创 SVG 代码随本站源码维护，其原创表达与论文权利分开；论文及其原图版权仍归各自权利人。本次没有将论文正文或原图纳入发布文件。页面提供双语原创图注与描述性替代文本。
- 读书笔记公众号名“杂记遣怀”由所有者明确确认。尚未核验具体公开文章身份及原始 URL，因此账号不带猜测链接，文章数组为空；不将同名搜索结果归属于该账号。后续仅收录经人工核验的原始 HTTPS 链接、准确标题、日期和原创双语短摘要。程序校验格式不能替代文章身份核验。

公开搜索补充：搜狗微信文章搜索出现同名账号下的候选《我怀念的 约翰 · 丹佛》，但未核验原始 URL、日期或与所有者的身份关联，未将其收录为文章。账号搜索未找到相关官方认证订阅号，不能据此断言账号不存在；Google 提取仅得搜索外壳，Bing 结果无身份佐证。已请求所有者提供公众号公开主页、原文链接或二维码，再核验归属、准确标题与日期。
