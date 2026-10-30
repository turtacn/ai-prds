import os

pages_data = {}

# Section 06: User Experience
pages_data["06-user-experience/user-journey.html"] = ("用户旅程地图", "06 用户体验", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-route"></i> 用户旅程地图 (User Journey Map)</h1>
    <p class="page-subtitle">定义安全工程师与 DPO 在高危漏洞突发时的典型协同旅程</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-map-signs"></i> 典型场景：发现 0-Day/High CVE 漏洞暴露 GDPR 数据的全旅程</h3></div>
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-date">Phase 1: 实时感知与预警</div>
                <p><strong>行为：</strong> SGCS 增量扫描引擎自动捕获最新 CVE，匹配到某台保存有 50 万欧洲用户 PII 的数据库服务器。<br>
                <strong>体验：</strong> 系统通过 Slack/Teams 和邮件向 SecOps 与 DPO 同时发送分级预警。</p>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-date">Phase 2: 风险评估与协同决策</div>
                <p><strong>行为：</strong> CISO 和 DPO 登录控制台查看“隐私风险暴露值 (PRE: 94)”。系统显示补丁尚不可用，但可启用虚拟补丁规则。<br>
                <strong>体验：</strong> 一键点击“应用 WAF 虚拟防护”，系统自动部署规则过滤恶意流量，将风险降低 80%。</p>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-date">Phase 3: 补丁修复与合规举证</div>
                <p><strong>行为：</strong> 运维团队打上正式系统补丁，SGCS 自动复测关闭 Jira 工单，并自动生成 GDPR 72小时免责证据包送交 DPO 归档。</p>
            </div>
        </div>
    </div>
</div>
''')

pages_data["06-user-experience/dashboard-mockup.html"] = ("控制台界面原型", "06 用户体验", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-desktop"></i> 控制台界面原型 (Dashboard Mockup)</h1>
    <p class="page-subtitle">包含 CVE 风险分布、GDPR 合规评分、待修复趋势图与资产分类饼图的统一看板</p>
</div>

<div class="grid-4">
    <div class="stat-card">
        <div class="stat-icon critical"><i class="fas fa-exclamation-circle"></i></div>
        <div><div class="stat-value">38</div><div class="stat-label">Critical 级漏洞 (待修复)</div></div>
    </div>
    <div class="stat-card">
        <div class="stat-icon success"><i class="fas fa-check-circle"></i></div>
        <div><div class="stat-value">94.2</div><div class="stat-label">GDPR 合规健康分</div></div>
    </div>
    <div class="stat-card">
        <div class="stat-icon high"><i class="fas fa-bolt"></i></div>
        <div><div class="stat-value">12</div><div class="stat-label">CISA KEV 在野利用</div></div>
    </div>
    <div class="stat-card">
        <div class="stat-icon primary"><i class="fas fa-server"></i></div>
        <div><div class="stat-value">1,250</div><div class="stat-label">已监控企业资产数</div></div>
    </div>
</div>

<div class="grid-2" style="margin-top:20px;">
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-chart-bar"></i> 资产类型与 PII 分布</h3></div>
        <div class="table-responsive">
            <table class="data-table">
                <thead><tr><th>资产分类</th><th>总数</th><th>关联 PII 敏感数据</th><th>安全合规状态</th></tr></thead>
                <tbody>
                    <tr><td>云数据库 (RDS/Postgres)</td><td>120</td><td>98 (高敏感)</td><td><span class="badge badge-success">正常</span></td>
                    <tr><td>Kubernetes Pods</td><td>450</td><td>150</td><td><span class="badge badge-high">警告 (3 CVE)</span></td>
                    <tr><td>Linux 生产服务器</td><td>380</td><td>85</td><td><span class="badge badge-critical">需关注</span></td>
                    <tr><td>S3 存储桶</td><td>300</td><td>210</td><td><span class="badge badge-success">正常</span></td>
                </tbody>
            </table>
        </div>
    </div>
    <div class="card">
        <div class="card-header"><h3 class="card-title"><i class="fas fa-history"></i> 最近扫描与事件日志</h3></div>
        <ul style="font-size:0.9rem; list-style:none;">
            <li style="margin-bottom:12px;"><i class="fas fa-sync fa-spin" style="color:var(--primary-color)"></i> 10分钟前：对 <code>prod-eu-west-1</code> 完成全量 CVE 增量扫描</li>
            <li style="margin-bottom:12px;"><i class="fas fa-shield-alt" style="color:var(--success-color)"></i> 25分钟前：针对 <code>CVE-2023-38606</code> 自动下发 WAF 虚拟防护规则</li>
            <li style="margin-bottom:12px;"><i class="fas fa-file-download" style="color:var(--secondary-color)"></i> 1小时前：DPO 导出 <code>2024-Q2-GDPR-Audit-Package.pdf</code></li>
        </ul>
    </div>
</div>
''')

pages_data["06-user-experience/workflow-scenarios.html"] = ("典型工作流场景", "06 用户体验", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-tasks"></i> 典型工作流场景 (Workflow Scenarios)</h1>
    <p class="page-subtitle">涵盖漏洞扫描、DSAR 自动化响应与 DPIA 评估的三大标准工作流</p>
</div>

<div class="accordion">
    <div class="accordion-item active">
        <button class="accordion-header">场景一：漏洞从扫描到闭环排查工流 <i class="fas fa-chevron-down"></i></button>
        <div class="accordion-content">
            <p>1. 扫描引擎触发周期/增量扫描 -> 2. 漏洞关联引擎评估 PII 影响并打分 -> 3. PRE >= 85 自动在 Jira 创建 High-Priority 工单 -> 4. 工程师部署补丁或开启虚拟防护 -> 5. 系统自动复测并闭环工单。</p>
        </div>
    </div>
    <div class="accordion-item">
        <button class="accordion-header">场景二：用户提交 DSAR 数据的自动化处理流程 <i class="fas fa-chevron-down"></i></button>
        <div class="accordion-content">
            <p>1. 用户在合规门户提交删除申请 -> 2. DPO 在 SGCS 控制台审核通过 -> 3. 系统向包含该用户 PII 的所有数据库/S3 下发清除 API -> 4. 确认清除后自动生成审计凭证报告。</p>
        </div>
    </div>
</div>
''')

# Section 07: Implementation Roadmap
pages_data["07-implementation-roadmap/phase1-mvp.html"] = ("Phase 1: MVP", "07 实施路线图", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-rocket"></i> Phase 1: MVP 功能 (Q1 2024)</h1>
    <p class="page-subtitle">交付核心 CVE 扫描、基础 PII 识别与最基本合规报告</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-check-square"></i> MVP 关键交付项列表</h3></div>
    <ul>
        <li><strong>核心漏洞扫描：</strong> 支持 Linux/Windows Agentless 扫描与 NVD/CISA KEV 基础库对接。</li>
        <li><strong>基础 PII 资产地图：</strong> 支持 MySQL / PostgreSQL 数据库内常见 PII 数据列自动识别。</li>
        <li><strong>基础风险排序：</strong> 实现简单的 CVSS + PII 权重叠加打分机制。</li>
        <li><strong>单体导出报告：</strong> 支持导出 PDF 格式的 CVE 漏洞与 GDPR 基础合规清单。</li>
    </ul>
</div>
''')

pages_data["07-implementation-roadmap/phase2-expansion.html"] = ("Phase 2: 功能扩展", "07 实施路线图", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-expand-arrows-alt"></i> Phase 2: 功能扩展 (Q2-Q3 2024)</h1>
    <p class="page-subtitle">推出无补丁虚拟防护、高级 API 集成与完整 DSAR 工作流</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-cubes"></i> Expansion 阶段交付目标</h3></div>
    <ul>
        <li><strong>无补丁虚拟防护：</strong> 对接 AWS WAF / Nginx，实现 CVE 防护规则一键自动下发。</li>
        <li><strong>完整 DSAR 门户：</strong> 提供面向数据主体的端到端申请与自动化数据擦除管道。</li>
        <li><strong>生态集成：</strong> 交付与 Jira Cloud, ServiceNow, Splunk SIEM 的开箱即用插件。</li>
    </ul>
</div>
''')

pages_data["07-implementation-roadmap/phase3-ai-automation.html"] = ("Phase 3: AI自动化", "07 实施路线图", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-robot"></i> Phase 3: AI 自动化与全球化 (Q4 2024)</h1>
    <p class="page-subtitle">引入 AI 风险预测算法与全球多数据中心部署</p>
</div>

<div class="card">
    <div class="card-header"><h3 class="card-title"><i class="fas fa-brain"></i> AI 智能与全球路线图</h3></div>
    <div style="text-align: center; padding: 10px 0;">
        <img src="../assets/images/roadmap_gantt.png" alt="SGCS 产品路线图 (Roadmap 2024)" style="max-width: 100%; height: auto; border: 1px solid var(--border-color); border-radius: 8px;">
    </div>
</div>
''')

# Section 08: Compliance Framework
pages_data["08-compliance-framework/gdpr-mapping.html"] = ("GDPR条款映射", "08 合规框架映射", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-scale-balanced"></i> GDPR 条款映射表 (GDPR Mapping)</h1>
    <p class="page-subtitle">SGCS 功能模块对 GDPR 法案核心条款的精确覆盖</p>
</div>

<div class="card">
    <div class="table-responsive">
        <table class="data-table">
            <thead>
                <tr><th>GDPR 条款编号</th><th>条款要求概要</th><th>SGCS 对应解决方案功能</th><th>合规证明产出物</th></tr>
            </thead>
            <tbody>
                <tr><td>Art. 32 (1)(b)</td><td>确保处理系统的持续安全性与可用性</td><td>CVE 漏洞双模扫描与无补丁防护</td><td>实时漏洞修复与 SLA 履约报告</td></tr>
                <tr><td>Art. 32 (1)(d)</td><td>定期测试与评估安全措施有效性</td><td>自动化二次扫描与闭环验证 Engine</td><td>自动化评估日志与防篡改凭证包</td></tr>
                <tr><td>Art. 33</td><td>向监管机构通知个人数据泄露 (72小时)</td><td>CVE + PII 风险预警与 72h 报告生成器</td><td>带时间戳的违规事件通知草案</td></tr>
                <tr><td>Art. 17</td><td>数据主体被遗忘权 (Right to erasure)</td><td>DSAR 自动化请求处理流水线</td><td>数据彻底擦除合规日志证明</td></tr>
            </tbody>
        </table>
    </div>
</div>
''')

pages_data["08-compliance-framework/iso27001-alignment.html"] = ("ISO 27001对齐", "08 合规框架映射", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-certificate"></i> ISO 27001 对齐 (ISO 27001 Alignment)</h1>
    <p class="page-subtitle">SGCS 对 ISO/IEC 27001:2022 附录 A 控制项的支撑</p>
</div>

<div class="card">
    <ul>
        <li><strong>A.8.8 技术漏洞管理 (Technical Vulnerability Management)：</strong> 通过 CVE 扫描、NVD 同步与补丁闭环提供完整支持。</li>
        <li><strong>A.8.12 数据泄漏预防 (Data Leakage Prevention)：</strong> 通过 PII 数据发现与隐私风险暴露值 (PRE) 计算防止敏感数据经由漏洞泄漏。</li>
    </ul>
</div>
''')

pages_data["08-compliance-framework/cisa-kev-integration.html"] = ("CISA KEV集成", "08 合规框架映射", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-shield-cat"></i> CISA KEV 集成 (CISA Known Exploited Vulnerabilities)</h1>
    <p class="page-subtitle">对接美国网络安全和基础设施安全局 (CISA) 在野利用漏洞库</p>
</div>

<div class="card">
    <p>SGCS 保持与 CISA KEV 数据库的毫秒级同步。当扫描检测到资产包含 CISA KEV 列表中的漏洞时，自动分配 <strong>1.5x 风险权重加成</strong>，并强制设定最高等级修复 SLA。</p>
</div>
''')

# Section 09: Pricing Licensing
pages_data["09-pricing-licensing/pricing-model.html"] = ("定价与授权模式", "09 商业与定价", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-tags"></i> 定价与授权模式 (Pricing & Licensing)</h1>
    <p class="page-subtitle">透明、灵活且基于资产规模的企业级 SaaS / 订阅制定价</p>
</div>

<div class="grid-3">
    <div class="card">
        <h3>Standard 标准版</h3>
        <p style="font-size:1.5rem; font-weight:bold; color:var(--primary-color);">$15,000 <span style="font-size:0.8rem; font-weight:normal;">/年</span></p>
        <ul style="font-size:0.88rem; margin:16px 0; line-height:1.8;">
            <li>最多 250 节点资产</li>
            <li>标准 CVE 漏洞扫描</li>
            <li>基础 GDPR 报告导出</li>
            <li>邮件技术支持</li>
        </ul>
    </div>
    <div class="card" style="border: 2px solid var(--secondary-color);">
        <div class="badge badge-info" style="float:right;">最受欢迎</div>
        <h3>Enterprise 企业版</h3>
        <p style="font-size:1.5rem; font-weight:bold; color:var(--primary-color);">$48,000 <span style="font-size:0.8rem; font-weight:normal;">/年</span></p>
        <ul style="font-size:0.88rem; margin:16px 0; line-height:1.8;">
            <li>最多 1,000 节点资产</li>
            <li>智能风险关联引擎 (PRE)</li>
            <li>无补丁虚拟防护 (Patchless)</li>
            <li>Jira / ServiceNow 集成</li>
            <li>72 小时 SLA 原厂支持</li>
        </ul>
    </div>
    <div class="card">
        <h3>Ultimate 旗舰版</h3>
        <p style="font-size:1.5rem; font-weight:bold; color:var(--primary-color);">$98,000+ <span style="font-size:0.8rem; font-weight:normal;">/年</span></p>
        <ul style="font-size:0.88rem; margin:16px 0; line-height:1.8;">
            <li>无限节点与多租户</li>
            <li>混合云 / K8s 私有部署</li>
            <li>专属数据保护官 (DPO) 顾问支持</li>
            <li>定制化 API 与 1V1 专享服务</li>
        </ul>
    </div>
</div>
''')

# Section 10: Appendix
pages_data["10-appendix/glossary.html"] = ("术语表", "10 附录", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-book"></i> 术语表 (Glossary)</h1>
    <p class="page-subtitle">SGCS PRD 文档涉及的核心专业术语定义</p>
</div>

<div class="card">
    <div class="table-responsive">
        <table class="data-table">
            <thead><tr><th>术语首字母/缩写</th><th>全称</th><th>中文定义与解释</th></tr></thead>
            <tbody>
                <tr><td><strong>CVE</strong></td><td>Common Vulnerabilities and Exposures</td><td>通用漏洞披露，系统公开已知的网络安全漏洞标准名称。</td></tr>
                <tr><td><strong>GDPR</strong></td><td>General Data Protection Regulation</td><td>欧盟《通用数据保护条例》，全球最严厉的数据隐私保护法规。</td></tr>
                <tr><td><strong>DSAR</strong></td><td>Data Subject Access Request</td><td>数据主体访问请求，赋予个人查询、导出或擦除自己数据的权利。</td></tr>
                <tr><td><strong>PII</strong></td><td>Personally Identifiable Information</td><td>个人身份标识信息，包含姓名、身份证、信用卡、邮箱等。</td></tr>
                <tr><td><strong>EPSS</strong></td><td>Exploit Prediction Scoring System</td><td>漏洞利用预测评分系统，估计 CVE 在未来 30 天内被利用的概率。</td></tr>
                <tr><td><strong>PRE</strong></td><td>Privacy Risk Exposure</td><td>隐私风险暴露值，SGCS 独创的“漏洞严重度 x PII 敏感度”综合风险评分。</td></tr>
            </tbody>
        </table>
    </div>
</div>
''')

pages_data["10-appendix/references.html"] = ("参考资料与来源", "10 附录", '''
<div class="page-header">
    <h1 class="page-title"><i class="fas fa-link"></i> 参考资料与数据来源 (References)</h1>
    <p class="page-subtitle">编写本 PRD 涉及的权威标准与行业报告</p>
</div>

<div class="card">
    <ul>
        <li><a href="https://nvd.nist.gov/" target="_blank">NIST National Vulnerability Database (NVD)</a></li>
        <li><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog" target="_blank">CISA Known Exploited Vulnerabilities Catalog</a></li>
        <li><a href="https://gdpr-info.eu/" target="_blank">General Data Protection Regulation (GDPR) Official Text</a></li>
        <li><a href="https://www.first.org/epss/" target="_blank">FIRST Exploit Prediction Scoring System (EPSS) Standard</a></li>
        <li>Gartner Market Guide for Vulnerability Assessment & Data Privacy Management 2023-2024</li>
    </ul>
</div>
''')

print("Part 3 updated with static PNG image tags.")
